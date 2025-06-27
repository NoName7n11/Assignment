# DevOps Assignment: Multi-Service Docker Setup Guide

## Project Structure

```
SourceCodeForDevopsAssignment/
│   docker-compose.yml
│
├── service_1/
│     main.go
│     Dockerfile
│
├── service_2/
│     app.py
│     Dockerfile
│
└── nginx/
      default.conf
      Dockerfile
```

---

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- [Git](https://git-scm.com/) (optional, for cloning repo)
- [VS Code](https://code.visualstudio.com/) (optional, for editing/viewing code)

---

## Setup Steps

### 1. Clone or Download the Project

```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```
Or download and extract the ZIP, then open the folder in VS Code.

---

### 2. Build and Start the Services

Open a terminal in the project root and run:

```sh
docker compose up --build
```

This will:
- Build images for `service_1`, `service_2`, and `nginx`
- Start all containers with health checks

---

### 3. Check Service Health

Wait until you see logs indicating all services are healthy and Nginx is running without errors.

---

### 4. Test the Endpoints

Open your browser and visit:

- [http://localhost:8081/service1/ping](http://localhost:8081/service1/ping)
- [http://localhost:8081/service2/ping](http://localhost:8081/service2/ping)

You should see JSON responses.

---

### 5. View Logs (Optional)

To see logs for each service:

```sh
docker compose logs service1
docker compose logs service2
docker compose logs nginx
```

---

### 6. Stop the Services

Press `Ctrl+C` in the terminal, then run:

```sh
docker compose down
```

---

## docker-compose.yml Example

```yaml
version: '3.8'

services:
  service1:
    build: ./service_1
    container_name: service1
    expose:
      - "8001"
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:8001/ping"]
      interval: 10s
      retries: 3

  service2:
    build: ./service_2
    container_name: service2
    expose:
      - "8002"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8002/ping"]
      interval: 10s
      retries: 3

  nginx:
    build: ./nginx
    ports:
      - "8081:80"
    depends_on:
      service1:
        condition: service_healthy
      service2:
        condition: service_healthy
```

---