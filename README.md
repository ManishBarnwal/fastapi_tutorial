Once you have cloned the repository, check if you have docker installed by typing `docker version`. If you don't have it installed, see this -- https://www.docker.com/products/docker-desktop/.

## Refresher on docker (optional)
If you want a quick refreshed on docker, please read the `README.Docker.md`.

## Build the image
Let's start by building the image and running the containers.

- `docker compose up --build`
    The command  is used to build and start a Docker container with the services defined in a Docker Compose file. The `--build` flag tells Docker Compose to build any images that are not yet built or have changed. This means that Docker Compose will look for a Dockerfile in the directory specified for each service and use it to build a Docker image. 
    
    The `docker-compose up` command starts the container, and the `--build` flag specifies that the image should be rebuilt before starting the container. Overall, the command `docker-compose up --build` is useful when you have made changes to your Dockerfile or any other files and you want to ensure that those changes are reflected in the running container

## Check if the build is successful
Once the images are built and the containers are up, check if:
    - the image is installed by typing `docker images`
    - containers are running by typing `docker ps`. 

You can now access the `ml-model-server` app at `http://0.0.0.0:8000/`. 









