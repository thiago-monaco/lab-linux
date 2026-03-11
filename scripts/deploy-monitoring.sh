#!/bin/bash
echo "🚀 Starting Monitoring Stack..."

# 1. Criar rede se não existir (para os containers se comunicarem)
docker network inspect monitoring-network >/dev/null 2>&1 || \
    docker network create monitoring-network

# 2. Subir Prometheus (ajuste o caminho se necessário)
echo "📦 Starting Prometheus..."
docker compose -f ../monitoring/prometheus/prometheus.yml up -d

# 3. Subir Grafana (ajuste o caminho se necessário)
echo "📦 Starting Grafana..."
docker compose -f ../monitoring/grafana/grafana.yml up -d

echo "✅ Stack is up! Check Grafana at http://localhost:3000"
