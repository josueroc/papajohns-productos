# 🍕 Papa John's Product Service

Este proyecto implementa un servicio **serverless** en AWS que realiza el scraping del catálogo de productos de Papa John's y expone la información a través de una API REST.

## Tecnologías utilizadas

- Python 3.11
- AWS Lambda
- API Gateway
- Amazon DynamoDB
- Amazon S3
- Serverless Framework
- Docker

## Requisitos

Antes de comenzar, asegúrate de tener instalado:

- Node.js
- Python 3.11
- Docker
- AWS CLI con credenciales configuradas
- Serverless Framework

## Instalación

1. Clona el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd papajohns-productos
```

2. Instala las dependencias:

```bash
npm install
```

## Configurar Docker (Amazon Linux)

Si estás utilizando Amazon Linux:

```bash
sudo dnf install docker -y
sudo systemctl start docker
sudo usermod -aG docker ec2-user
newgrp docker
```

Puedes verificar que Docker esté funcionando con:

```bash
docker ps
```

## Configurar AWS

Verifica que tus credenciales sean válidas ejecutando:

```bash
aws sts get-caller-identity
```

Si utilizas **AWS Academy Learner Lab**, recuerda que las credenciales expiran periódicamente y deberás actualizarlas en:

```text
~/.aws/credentials
```

## Desplegar el servicio

Una vez configurado el entorno, despliega el proyecto con:

```bash
sls deploy
```

Al finalizar, Serverless mostrará las URLs de los endpoints creados en API Gateway.

## Documentación de la API

La especificación de los endpoints, parámetros, respuestas y códigos de error se encuentra en **API_CONTRACT.md**.
