```markdown
## ☸️ Kubernetes & OpenShift Manifests
This folder contains base templates for deploying scalable applications.

### 📜 Deployment & Service Example
A standard way to deploy an app with 3 replicas and expose it via a LoadBalancer.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ocr-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ocr-service
  template:
    metadata:
      labels:
        app: ocr-service
    spec:
      containers:
      - name: ocr-container
        image: ocr-service:latest
        ports:
        - containerPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: ocr-service
spec:
  selector:
    app: ocr-service
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
  type: LoadBalancer

🔧 Useful Kubernetes Commands
Get all resources: kubectl get all

Describe a pod (troubleshooting): kubectl describe pod <pod_name>

View pod logs: kubectl logs -f <pod_name>

Apply changes: kubectl apply -f deployment.yaml
