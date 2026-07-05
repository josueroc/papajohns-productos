import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.papajohns.com.pe/menu/promociones"

headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(URL, headers=headers).text
soup = BeautifulSoup(html, "html.parser")

products = []

for i, product in enumerate(soup.select("li.product.product-item"), start=1):

    # Nombre
    name_tag = product.select_one("a.product-item-link")
    name = name_tag.get_text(strip=True)

    # Link
    link = name_tag["href"]

    # Imagen
    img = product.select_one("img.product-image-photo")
    image = img["src"] if img else None

    # Precio
    price_tag = product.select_one("[data-price-amount]")
    price = float(price_tag["data-price-amount"]) if price_tag else None

    products.append({
        "tenantId": "SURCO-01",
        "productId": f"P{i:03}",
        "name": name,
        "price": price,
        "imageUrl": image,
        "link": link
    })

print(json.dumps(products, indent=2, ensure_ascii=False))
