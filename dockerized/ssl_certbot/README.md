# Docker Compose

## Build and run:

- Build an image

```bash
docker-compose build --no-cache
```

- Run a container

```bash
docker-compose up --build

```

# Dockers

## Build and run

- Build an image

```bash
docker build -t myimg .
```

- Run a container

```bash
docker run -p 80:80 myimg
```


### Docker Images

- List all images

```bash
docker images
```

- Remove an image

```bash
docker rmi <image_id>

docker rmi $(docker images -q)

docker rmi $(docker images -q) -f

# stop all containers
docker stop $(docker ps -a -q)
```
