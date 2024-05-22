# Docker Compose Guide for Gunicorn, Nginx, and Certbot

This guide will show you how to set up a Docker Compose project with Gunicorn, Nginx, and Certbot. This project will allow you to run a web server with SSL support.

## Prerequisites

- docker
- docker compose
- git

## Certbot Setup

1. Register a domain name and point it to your server's IP address.
2. Install Certbot on your server.

    ```bash
    sudo apt-get update
    sudo apt-get install certbot
    ```

3. Run Certbot to generate SSL certificates.

    ```bash
    sudo certbot certonly --standalone -d example.com -d www.example.com
    ```

This is done once on the server itself, not in the Docker container or in the Docker Compose file because Certbot needs to bind to port 80 to verify the domain ownership.

## Docker Compose Setup

For local:

```bash
docker-compose -f docker-compose.local.yml up -d
```



