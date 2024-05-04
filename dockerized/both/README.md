# Docker Compose

Remove all images and containers

```bash
docker-compose down
docker rmi $(docker images -q) -f
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

docker-compose build --no-cache
docker-compose up --build
```

## Build and run:

Build an image

```bash
docker-compose build --no-cache
docker-compose up --build
```


# Dockers

## Build and run

```bash
docker build -t myapp .
docker run -p 8000:8000 myapp
```


### Docker Images

List all images

```bash
docker images
```

Remove an image

```bash
docker-compose down
docker rmi $(docker images -q) -f
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```
