#!/bin/bash
# Cria um backup das configurações do Prometheus e do JSON do Grafana
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="lab_backup_$TIMESTAMP.tar.gz"

echo "💾 Backing up configurations to $BACKUP_NAME..."

# Compacta os arquivos importantes
tar -czf $BACKUP_NAME ../monitoring/prometheus/*.yml ../monitoring/grafana/*.json

echo "✅ Backup completed successfully!"
