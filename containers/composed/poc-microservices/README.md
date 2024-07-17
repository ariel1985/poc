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
   cd poc-microservices
   ```

2. Build and run the services using Docker Compose:

   ```sh
   docker-compose up --build
   ```

3. Access the APIs:
   - Node.js service: [http://localhost:3000](http://localhost:3000)
   - FastAPI service: [http://localhost:8000](http://localhost:8000)
