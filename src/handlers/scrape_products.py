import json
import boto3
import requests
from bs4 import BeautifulSoup
import os
from decimal import Decimal

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["PRODUCTS_TABLE"])

URL = "https://www.papajohns.com.pe/menu/promociones"
headers = {"User-Agent": "Mozilla/5.0"}

def scrape_products():
    html = requests.get(URL, headers=headers, timeout=10).text
    soup = BeautifulSoup(html, "html.parser")

    products = []

    for i, product in enumerate(soup.select("li.product.product-item"), start=1):

        name_tag = product.select_one("a.product-item-link")
        if not name_tag:
            continue

        img = product.select_one("img.product-image-photo")
        price_tag = product.select_one("[data-price-amount]")

        # precio seguro para DynamoDB (Decimal obligatorio)
        price = None
        if price_tag and price_tag.get("data-price-amount"):
            price = Decimal(str(price_tag["data-price-amount"]))

        products.append({
            "tenantId": "SURCO-01",
            "productId": f"P{i:03}",
            "name": name_tag.get_text(strip=True),
            "price": price,
            "imageUrl": img["src"] if img else None,
            "link": name_tag["href"]
        })

    return products


def lambda_handler(event, context):
    try:
        products = scrape_products()

        with table.batch_writer() as batch:
            for p in products:
                batch.put_item(Item=p)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Scraping exitoso",
                "count": len(products)
            })
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Error en scraping",
                "error": str(e)
            })
        }
