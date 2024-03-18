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
&
ngrok http https://localhost:8000
```

## TODO:

 - Dockerfile


*Notice: 

 The limitation mentioned in the documentation is that Telegram only supports four ports for webhooks: 443, 80, 88, and 8443. This means you can only run a maximum of four bots on one domain/IP address with the integrated server, as each bot would need to listen on a different port. 

