## 🐳 Docker Best Practices
Example of a high-performance, secure, and small-footprint Dockerfile using **Multi-Stage Builds**.

### 🛠️ The "Perfect" Dockerfile (Conceptual)
Using multi-stage builds allows us to use a heavy image for compiling/building and a very light one for production.

```dockerfile
# Stage 1: Build
FROM python:3.10-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Production (Final Image)
FROM python:3.10-slim
WORKDIR /app
# Copy only the installed packages from the builder stage
COPY --from=builder /root/.local /root/.local
COPY ./app .

ENV PATH=/root/.local/bin:$PATH
CMD ["python", "main.py"]

🔧 Useful Docker Commands
Clean up unused images/volumes: docker system prune -a --volumes

Real-time resource stats: docker stats

Check IP address: docker inspect <id> | grep "IPAddress"

Check logs (last 100 lines): docker logs --tail 100 -f <container_name>
