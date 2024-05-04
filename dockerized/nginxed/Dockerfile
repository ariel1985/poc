# Use the Nginx image from Docker Hub
FROM nginx:latest

# Copy the static HTML files to the Nginx container
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# No need since nginx image already has this command
# CMD ["nginx", "-g", "daemon off;"]