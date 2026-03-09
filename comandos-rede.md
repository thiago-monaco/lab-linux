# 🛠 Lab de Redes e Manutenção - Linux (Ubuntu)

Repositório para registar comandos úteis de troubleshooting e configuração.

## 🌐 Gerenciamento de IP
* **Ver IPs da máquina:** `ip a` ou `ip addr show eth0`
* **Remover um IP secundário (temporário):** `sudo ip addr del [IP/CIDR] dev [INTERFACE]`
  *Exemplo: `sudo ip addr del 10.10.10.121/24 dev eth0`*

## 🔄 Manutenção e Atualizações
* **Procurar atualizações (resumo):** `/usr/lib/update-notifier/apt-check --human-readable`
* **Ver lista de pacotes a atualizar:** `apt list --upgradable`
* **Fluxo padrão de atualização:** `sudo apt update && sudo apt upgrade -y`
