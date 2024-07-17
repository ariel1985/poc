# POC Microservices

This project demonstrates a simple "Hello World" API using Node.js and FastAPI, deployed with Docker Compose.

## Project Structure

```
poc-microservices/
├── docker-compose.yml
├── node-service/
│   ├── Dockerfile
│   ├── package.json
│   └── index.js
└── fastapi-service/
    ├── Dockerfile
    ├── main.py
    └── requirements.txt
```

## How to Run

1. Navigate to the project directory:

   ```sh
   cd ms-fastapi-node-angular-mongo
   ```

2. Build and run the services using Docker Compose:

   ```sh
   docker-compose up --build
   ```

   Or use docker: 

   ```sh
   docker build -t angular-service:latest .
   docker run -d -p 4200:80 angular-service


docker build -t angular-service .
docker run -p 4200:80 angular-service

docker rmi $(docker images -a -q)
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```


3. Access the APIs:
   - Node.js service: [http://localhost:3000](http://localhost:3000)
   - FastAPI service: [http://localhost:8000](http://localhost:8000)



## Installations: 

Using Angular CLI to create the angular-service on the root folder:

```sh
npm install -g @angular/cli
ng new angular-service
ng build --configuration production
```

*** To upgrade node on Linux: 
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
# download and install Node.js (you may need to restart the terminal)
nvm install 20
# verifies the right Node.js version is in the environment
node -v # should print `v20.15.1`
# verifies the right NPM version is in the environment
npm -v # should print `10.7.0`
```

