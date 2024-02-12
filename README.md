There are a few Docker terms that I keep forgetting so I will start with the common terms related to Docker. Below are a few in sequential order.

## Docker
A docker is a platform that enables you to run an application that may have multiple containers running in isolation. An example of an application could be a web app and to run this application, we would need many software and packages like fastapi, a database like MySQL, a queue like Redis. All of these software would have different package needs and they might conflict with each. To avoid these packages conflict, these software are run in the form of containers. Docker is just one platform for developing applications; there are many other platforms that does the same -- for example Podman, Cloud Foundry. 


## Containers
A container is a lightweight, standalone, executable package. 
    - **Lightweight** because each container has only a specific package/software in it. For example, if you want a database (eg. MySQL) in your docker application, then there will be a container only for the MySQL database. 
    - **Standalone* because each container contains only a single software. 
    - **Executable** because each container can run/execute on its own. 

A docker container is an isolated service that is created using a Docker image. A docker image is a blueprint of what all will be installed when the image is built. For example, you can create a MySQL docker container by downloading the MySQL docker image from the docker hub -- https://hub.docker.com/_/mysql.

## Image 
An image is a blue-print of information needed to create a container. The image contains information about the software, os, and packages needed to create the container. So in a way, we can say that a container is an instance of an image. These images are generally available in the docker hub. For example, if we want to use MySQL in our docker application, we can access the latest image of MySQL from this URL of the docker hub - https://hub.docker.com/_/mysql

Let's see how to get started once you have cloned the repository. Make sure you do not have the containers that are defined in this repository running. Below are some useful commands on containers.

## Dockerfile


## docker-compose.yaml

- `docker version` - to check if docker is installed in your local and its corresponding version. If you don't have it installed, see this -- https://www.docker.com/products/docker-desktop/

## Docker container commands
- `docker ps` : Lists all the running containers
- `docker ps -a`: Lists all the containers - running as well as the stopped ones
- `docker ps -a |grep Exit`: Lists only the stopped containers

- `docker stop <container_id or container_name>`: Stops a running container. Even if you stop the running container, the container is still available in the background. If you want to completely get rid of the container, you need to delete it by using the below command.
- `docker rm <container_id or container_name>`: Permanently delete the corresponding container


- `docker compose up --build`
    The command  is used to build and start a Docker container with the services defined in a Docker Compose file. The `--build` flag tells Docker Compose to build any images that are not yet built or have changed. This means that Docker Compose will look for a Dockerfile in the directory specified for each service and use it to build a Docker image. 
    
    The `docker-compose up` command starts the container, and the `--build` flag specifies that the image should be rebuilt before starting the container. Overall, the command `docker-compose up --build` is useful when you have made changes to your Dockerfile or any other files and you want to ensure that those changes are reflected in the running container

Once the images are built and the containers are up, check if your containers are running by typing `docker ps`. 

You can now access the `ml-model-server` app at `http://0.0.0.0:8000/`. 









