# Telegram Bot Webhook

POC for implementing webhooks in telegram bot. 

## Set up python environment

```bash
python -m venv venv
python main.py
```
## Requirements for webhooks

Public IP/Domain:

```bash
snap install ngrok
```

## Run 

In different processes

Ubuntu 22

```
uvicorn main:asgi_application --ssl-keyfile=private.key --ssl-certfile=cert.pem --reload

ngrok http https://localhost:8000
```

## TODO:

 - Dockerfile