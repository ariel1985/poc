#!/bin/bash

# already in a container:
# # Start Nginx
# service nginx start
# # Obtain SSL certificates
# certbot certonly --nginx --non-interactive --agree-tos -m your-email@example.com -d your-domain.com

# Start Gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000
