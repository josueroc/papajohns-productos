🍕 API Contract - Papa John’s Product Service

Este documento define la interfaz de comunicación entre las aplicaciones Frontend y el Backend Serverless encargado de consultar el catálogo de productos.

Configuración Base

* Base URL (Desarrollo): https://{api-id}.execute-api.us-east-1.amazonaws.com/dev
* Content-Type: application/json
* Multi-tenancy: Todas las rutas incluyen un {tenantId} que representa la sucursal de Papa John’s (Ejemplo: SURCO-01, MIRAFLORES-02).

⸻

1. Obtener Productos

Obtiene la lista de productos disponibles para una sucursal.

* Método: GET
* Ruta: /tenants/{tenantId}/products
* Autorización: Ninguna (Público)

Path Parameters

Parámetro	Tipo	Descripción
tenantId	string	Identificador de la sucursal.

Query Parameters

Parámetro	Tipo	Obligatorio	Descripción
limit	integer	No	Cantidad máxima de productos por página. Valor por defecto: 10.
lastKey	string	No	Token devuelto por la consulta anterior para obtener la siguiente página de resultados.

Request Body

Ninguno.

Response: 200 OK

{
  "products": [
    {
      "tenantId": "SURCO-01",
      "productId": "P001",
      "name": "Pizza Pepperoni Familiar",
      "description": "Pizza familiar con pepperoni",
      "category": "Pizzas",
      "price": 35.90,
      "imageUrl": "https://papajohns-product-service-images-dev.s3.amazonaws.com/p001.jpg"
    },
    {
      "tenantId": "SURCO-01",
      "productId": "P002",
      "name": "Coca Cola 1.5L",
      "description": "Bebida gaseosa",
      "category": "Bebidas",
      "price": 8.00,
      "imageUrl": "https://papajohns-product-service-images-dev.s3.amazonaws.com/p002.jpg"
    }
  ],
  "lastKey": {
    "tenantId": "SURCO-01",
    "productId": "P002"
  }
}

Nota: Cuando lastKey sea null, significa que no existen más productos para consultar.

Errores Posibles

* 400 Bad Request: El valor de limit no es válido.
* 500 Internal Server Error: Error al consultar DynamoDB o procesar la respuesta.
