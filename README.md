Papa John’s Product Service

Servicio serverless desarrollado con AWS Lambda y Serverless Framework para realizar scraping del catálogo de productos de Papa John’s y exponer la información mediante una API.

Tecnologías

* AWS Lambda
* API Gateway
* DynamoDB
* Amazon S3
* Python 3.11
* Serverless Framework
* Docker

Requisitos

* Node.js
* Python 3.11
* Docker
* AWS CLI con credenciales válidas
* Serverless Framework

Instalación

Clonar el repositorio:

git clone <URL_DEL_REPOSITORIO>
cd papajohns-productos

Instalar dependencias:

npm install

Configuración de Docker (Amazon Linux)

sudo dnf install docker -y
sudo systemctl start docker
sudo usermod -aG docker ec2-user
newgrp docker

Verificar que Docker esté ejecutándose:

docker ps

Configurar credenciales de AWS

Verificar que las credenciales sean válidas:

aws sts get-caller-identity

Si las credenciales expiraron (por ejemplo, en AWS Academy Learner Lab), actualice el archivo:

~/.aws/credentials

Despliegue

sls deploy

Al finalizar el despliegue, Serverless mostrará los endpoints creados por API Gateway.

API

La especificación de los endpoints, parámetros y respuestas se encuentra en el archivo API_CONTRACT.md.
