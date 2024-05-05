# Use the Nginx image from Docker Hub
FROM nginx:latest

# Copy the static HTML files to the Nginx container
COPY . /usr/share/nginx/html

# Copy the SSL certificate and key to the Nginx container
COPY localhost.crt /etc/nginx/ssl/
COPY localhost.key /etc/nginx/ssl/

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports 80 and 443
EXPOSE 80 443