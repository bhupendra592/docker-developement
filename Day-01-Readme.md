
# Docker Basics Guide By Bhupendra Created for PGDIoT Students, ACTS, Pune

This README provides a step-by-step guide to basic Docker commands for managing images, containers, and their operations.

---

## 1. Pull an Image
Download an official image of Ubuntu:
```bash
sudo docker pull ubuntu
```

---

## 2. List Docker Images
View all Docker images present locally:
```bash
sudo docker images
```

Example output:
```bash
REPOSITORY                 TAG             IMAGE ID       CREATED         SIZE
ubuntu                     latest          fec8bfd95b54   5 weeks ago     78.1MB
```

---

## 3. Run a Container
Start a container from the Ubuntu image and access the bash shell:
```bash
sudo docker run -it ubuntu:latest bash
```

---

## 4. List Containers

### List Running Containers:
```bash
sudo docker container ls
```

Example output:
```bash
CONTAINER ID   IMAGE            COMMAND        CREATED         STATUS         PORTS     NAMES
68854c219f15   ubuntu:latest    "bash"         4 minutes ago   Up 4 minutes             magical_tu
```

### List All Containers (Running and Stopped):
```bash
sudo docker ps -a
```

Example output:
```bash
CONTAINER ID   IMAGE            COMMAND        CREATED          STATUS                     PORTS     NAMES
c795c1e79cfb   ubuntu:latest    "bash"         2 minutes ago    Exited (0) 5 seconds ago             laughing_hertz
68854c219f15   ubuntu:latest    "bash"         24 minutes ago   Exited (0) 2 minutes ago             magical_tu
```

---

## 5. Start an Existing Container
Start a previously stopped container:
```bash
sudo docker start <container_id>
```

Example:
```bash
sudo docker start 68854c219f15
```

---

## 6. Login to a Running Container
Access a running container interactively:
```bash
sudo docker exec -it <container_id> bash
```

Example:
```bash
sudo docker exec -it 68854c219f15 bash
```

---

## 7. Execute a Command in a Running Container
Run a command inside a container without logging into it:
```bash
sudo docker exec -it <container_id> <command>
```

Example:
```bash
sudo docker exec -it 68854c219f15 bash
```

---

## 8. Attach to a Running Container
Attach your terminal to the standard input/output of a running container:
```bash
sudo docker attach <container_id>
```

---

## 9. Run a Container with a Custom Name
Start a container with a specific name:
```bash
sudo docker run --name <custom_name> -it ubuntu:latest bash
```

Example:
```bash
sudo docker run --name vamsi -it ubuntu:latest bash
```

---

## Quick Commands Summary
| **Command**                               | **Description**                                             |
|-------------------------------------------|-------------------------------------------------------------|
| `docker pull <image>`                     | Pull an image from Docker Hub.                             |
| `docker images`                           | List all images.                                           |
| `docker run -it <image>:<tag> bash`       | Start a container and access the bash shell.              |
| `docker container ls`                     | List running containers.                                   |
| `docker ps -a`                            | List all containers.                                       |
| `docker start <container_id>`             | Start a stopped container.                                 |
| `docker exec -it <container_id> bash`     | Login to a running container.                              |
| `docker exec -it <container_id> <cmd>`    | Execute a command in a running container.                 |
| `docker attach <container_id>`            | Attach to a running container’s stdin/stdout.             |
| `docker run --name <name> -it <image>`    | Run a container with a custom name.                       |

---

Connect : @bhupendra.jmd@gmail.com