# 🛠 Linux Administration & Networking Lab (Ubuntu)

Essential commands for system administration, troubleshooting, and maintenance.

## 🌐 IP & Networking
* **Check IP addresses:** `ip a`
* **Remove temporary IP:** `sudo ip addr del [IP/CIDR] dev [INTERFACE]`
* **Check open ports:** `sudo ss -tulpn`

## 🔄 Maintenance & Updates
* **Update summary:** `/usr/lib/update-notifier/apt-check --human-readable`
* **Update workflow:** `sudo apt update && sudo apt upgrade -y`
* **Clean unused packages:** `sudo apt autoremove`

## 📊 System Resources
* **Disk usage:** `df -h`
* **Folder size summary:** `du -sh *`
* **Real-time processes:** `top` (or `htop`)

## ⚙️ Service Management (systemd)
* **Check service status:** `sudo systemctl status [service]`
* **Restart service:** `sudo systemctl restart [service]`
* **View real-time logs:** `sudo journalctl -f`
