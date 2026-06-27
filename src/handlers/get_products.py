import os
import json
import boto3
from boto3.dynamodb.conditions import Key
from src.utils import response

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["PRODUCTS_TABLE"])

def lambda_handler(event, context):
    try:
        tenant_id = event["pathParameters"]["tenantId"]

        query_params = event.get("queryStringParameters") or {}

        limit = int(query_params.get("limit", 10))

        last_key = query_params.get("lastKey")

        query = {
            "KeyConditionExpression": Key("tenantId").eq(tenant_id),
            "Limit": limit
        }

        if last_key:
            query["ExclusiveStartKey"] = json.loads(last_key)

        result = table.query(**query)

        products = result.get("Items", [])

        bucket = os.environ["PRODUCT_IMAGES_BUCKET"]

        for product in products:
            if "imageKey" in product:
                product["imageUrl"] = (
                    f"https://{bucket}.s3.amazonaws.com/{product['imageKey']}"
                )

        return response(200, {
            "products": products,
            "lastKey": result.get("LastEvaluatedKey")
        })

    except Exception as e:
        return response(500, {
            "message": "Error obteniendo productos",
            "error": str(e)
        })
