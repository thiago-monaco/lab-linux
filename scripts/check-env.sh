#!/bin/bash
echo "🔍 Checking Laboratory Environment..."

# Verifica Docker
if command -v docker >/dev/null 2>&1; then
    echo "✅ Docker is installed ($(docker --version))"
else
    echo "❌ Docker is NOT installed"
fi

# Verifica Docker Compose
if docker compose version >/dev/null 2>&1; then
    echo "✅ Docker Compose is available"
else
    echo "❌ Docker Compose is NOT available"
fi

# Verifica permissões do usuário
if groups $USER | grep &>/dev/null '\bdocker\b'; then
    echo "✅ User is in docker group"
else
    echo "⚠️ User is NOT in docker group (run: sudo usermod -aG docker \$USER)"
fi
