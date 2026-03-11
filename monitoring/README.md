# 📊 Monitoring Projects

This section contains infrastructure monitoring tools, metrics collectors, and visualization dashboards.

## 🚀 Projects

* **[Uptime Kuma](./uptime-kuma/):** Real-time service availability dashboard and alerting.
* **[Prometheus](./prometheus/):** Time-series database for metrics collection with custom scraping configurations.
* **[Grafana](./grafana/):** Advanced data visualization and analytics for infrastructure health.

---

### 🛠️ Modular Implementation Note
The projects in this folder are organized as **independent modules** for educational purposes. 

To run them in a production environment:
1. Ensure all services are on the same **Docker Network**.
2. Adjust **Volume Mappings** in the `.yml` files to point to your local configuration paths.
3. Check the `prometheus.config.yml` to define your specific scrape targets.
