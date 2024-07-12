# Stage 1: Build the Angular app
FROM node:latest AS builder

# Set the working directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy the source code
COPY . .

# Build the Angular app
RUN npm run build

# Stage 2: Serve the Angular app with a lightweight HTTP server
FROM nginx:alpine

# Copy the built Angular app from the builder stage
COPY --from=builder /app/dist/angular-service/browser /usr/share/nginx/html

# Expose port 80 to the outside world
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]



# # build and run
# docker build -t angular-service .
# docker run -p 4200:80 angular-service

# docker rmi $(docker images -a -q)
# docker stop $(docker ps -a -q)
# docker rm $(docker ps -a -q)