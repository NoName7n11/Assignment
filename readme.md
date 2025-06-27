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
git clone https://github.com/shivam/SourceCodeForDevopsAssignment.git
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
# Output

Below are screenshots showing the successful output of the project:

![Service 1 Ping Output](output/Screenshot%20(130).png)
![Service 2 Ping Output](output/Screenshot%20(131).png)

## How These Outputs Are Received

When you open your browser and visit `http://localhost:8081/service1/ping` or `http://localhost:8081/service2/ping`, here’s what happens:

1. **Browser Request:**  
   You enter the URL in your browser. The request goes to your local machine on port `8081`, where the Nginx container is listening.

2. **Nginx Reverse Proxy:**  
   Nginx receives the request. Based on its configuration, it checks the path:
   - If the path starts with `/service1/`, Nginx forwards the request to the `service1` container on port `8001`.
   - If the path starts with `/service2/`, Nginx forwards the request to the `service2` container on port `8002`.

3. **Service Response:**  
   Each service has a `/ping` endpoint:
   - `service1` (Go) responds with `{"status":"ok","service":"1"}`.
   - `service2` (Python Flask) responds with `{"status":"ok","service":"2"}`.

4. **Nginx Returns the Response:**  
   Nginx receives the JSON response from the service and sends it back to your browser.

5. **Browser Displays Output:**  
   The browser displays the JSON output, as shown in the screenshots.

**This process confirms that:**
- Nginx is running in a Docker container and correctly routing requests.
- Both backend services are healthy and responding.
- The full Dockerized stack is working as