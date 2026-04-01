# 📊 Monitoring & Observability 360º

Este diretório contém a stack completa de observabilidade do laboratório, integrando métricas de infraestruturas híbridas e ambientes conteinerizados.


## 🎯 Escopo do Monitoramento
Diferente de um setup básico, este projeto integra dados de três ecossistemas distintos:

1. **💻 Infraestrutura Windows:** Monitoramento de performance (CPU, RAM, Disk) de servidores remotos via `Windows Exporter`.
2. **🐧 Host Linux (Ubuntu):** Visibilidade total das métricas do sistema operacional base via `Node Exporter`.
3. **📦 Docker Infrastructure:** Monitoramento granular de containers individuais (Vaultwarden, Guacamole, Nginx) utilizando `cAdvisor`.

---

## 🚀 Componentes da Stack

* **[📊 Grafana](./grafana/):** Dashboards avançados. Inclui o **JSON model** customizado para monitoramento de frotas Windows.
* **[🔥 Prometheus](./prometheus/):** Time-series database configurado com targets específicos para cada exportador.
* **[⏱️ Uptime Kuma](./uptime-kuma/):** Painel de disponibilidade em tempo real com sistemas de alerta.

---

### 🛠️ Notas de Implementação (SRE Approach)
Os projetos estão organizados de forma modular, permitindo a escalabilidade da stack:

1. **Service Discovery:** Os targets do Prometheus são definidos no `prometheus.config.yml`.
2. **Persistence:** Todos os dados de métricas e dashboards utilizam **Docker Volumes** para garantir a persistência em caso de restart.
3. **Networking:** Recomendado o uso de uma rede Docker dedicada (`monitoring-network`) para comunicação interna entre os exportadores e o Prometheus.

---
**SRE Responsável:** [Thiago Monaco](https://github.com/thiago-monaco) 🚀
