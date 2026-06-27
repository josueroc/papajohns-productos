import os
import boto3
from boto3.dynamodb.conditions import Key
from src.utils import response

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["PRODUCTS_TABLE"])

def lambda_handler(event, context):
    try:
        tenant_id = event["pathParameters"]["tenantId"]

        result = table.query(
            KeyConditionExpression=Key("tenantId").eq(tenant_id)
        )

        products = result.get("Items", [])

        bucket = os.environ["PRODUCT_IMAGES_BUCKET"]

        for product in products:
            if "imageKey" in product:
                product["imageUrl"] = (
                    f"https://{bucket}.s3.amazonaws.com/{product['imageKey']}"
                )

        return response(200, products)

    except Exception as e:
        return response(500, {
            "message": "Error obteniendo productos",
            "error": str(e)
        })
