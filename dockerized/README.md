
# Certbot + Nginx with Docker Compose

This project provides a setup for automatically obtaining and renewing SSL certificates from Let's Encrypt, using Certbot, and serving a secure web server with Nginx. The setup employs Docker Compose to orchestrate the services.

## Project Structure

- **certbot/**: Contains the folders needed for Certbot certificate storage and web challenges.
  - `conf/`: Where Let's Encrypt certificates are stored after issuance.
  - `www/`: Web root for ACME challenges.

- **nginx/**: Holds the Nginx configuration files and Dockerfile.
  - `conf/default.conf`: Nginx server block configuration file.
  - `Dockerfile`: Dockerfile to build the custom Nginx image.

- **docker-compose.yml**: Docker Compose configuration file.

## How to Use

1. **Clone the Project**:  
   Clone or download this repository to your local machine.

2. **Edit Nginx Configuration**:  
   Update `nginx/conf/default.conf` with your domain name.

3. **Obtain SSL Certificates**:  
   Run the following command to obtain your SSL certificates:

   ```bash
   docker-compose run --rm certbot certonly --webroot --webroot-path=/var/www/certbot --email your-email@example.com --agree-tos --no-eff-email -d your-domain.com
   ```

   Replace `your-email@example.com` and `your-domain.com` with your email and domain.

4. **Update Nginx to Use SSL**:  
   Edit `nginx/conf/default.conf` to use the certificates provided by Let's Encrypt.

   ```nginx
   server {
     listen 443 ssl;
     server_name your-domain.com;

     ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
     ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;

     location / {
       # Your web application settings
     }
   }
   ```

5. **Start the Services**:  
   Run the following command to build the custom Nginx image and start the services:

   ```bash
   docker-compose up -d nginx
   ```

6. **Automate Certificate Renewal**:  
   Add a Certbot renewal service to `docker-compose.yml`:

   ```yaml
   certbot-renewal:
     image: certbot/certbot
     volumes:
       - ./certbot/conf:/etc/letsencrypt
       - ./certbot/www:/var/www/certbot
     entrypoint: "/bin/sh -c 'trap exit TERM; while :; do certbot renew --webroot --webroot-path=/var/www/certbot; sleep 12h & wait $${!}; done;'"
   ```

   This will automatically renew your certificates every 12 hours.

7. **Verify Renewal**:  
   Check the certificate expiration date with:

   ```bash
   docker-compose run --rm certbot certificates
   ```

   Ensure that certificates are renewed successfully and that Nginx is using the latest certificates.
