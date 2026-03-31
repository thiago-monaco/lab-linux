# ☁️ OCI Cloud & Cloud-Native Lab: Rancher + Istio + K3s

Este repositório documenta o provisionamento e a arquitetura de uma infraestrutura de microserviços de nível enterprise, utilizando os recursos **Always Free** da Oracle Cloud Infrastructure (OCI). 

O projeto foca na construção de um ecossistema completo de Kubernetes, do hardware à malha de serviços (Service Mesh).

---

## 🎯 Visão Geral e Objetivos
O intuito deste laboratório é realizar o deploy "End-to-End" de uma plataforma de containers robusta, aplicando conceitos de **SRE (Site Reliability Engineering)** e **Infrastructure as Code**:

1. **Cloud Foundation:** Provisionamento de rede, instâncias e segurança na OCI.
2. **Orquestração:** Setup de cluster Kubernetes utilizando **K3s** (Lightweight K8s).
3. **Management:** Gestão centralizada de clusters via **Rancher Manager**.
4. **Service Mesh:** Controle de tráfego, segurança mTLS e observabilidade com **Istio**.

---

## 🏗️ Arquitetura de Software (The Stack)

Para suportar aplicações modernas, a stack foi desenhada com foco em performance e visibilidade:

- **Rancher Manager:** Nosso "Cockpit" para gerenciamento de workloads e monitoramento de saúde do cluster.
- **Istio Service Mesh:** Implementação de políticas de **mTLS**, **Circuit Breaking**, **Fault Injection** e deploys do tipo **Canary/Blue-Green**.
- **Kiali & Jaeger:** (Planejado) Para visualização da malha de serviços e rastreamento distribuído.
- **K3s:** Escolha estratégica pelo baixo consumo de recursos, ideal para ambientes de nuvem otimizados.

---

## 🗺️ Topologia de Infraestrutura (Rede)

```text
[ Internet ] 
      |
[ Internet Gateway ] <--- (Ingress: 80, 443, 6443)
      |
[ VCN-LAB-INFRA ] 
      |
      +--- [ Public Subnet ]
                |
                +-- [ srv-rancher-manager ] (Ubuntu 22.04 | Shape ARM)
                |      (Rancher + K3s Control Plane)
                |
                +-- [ Worker Nodes / Istio Ingress ]

```

---
## 🚀 Diário de Bordo & Desafios Superados

### 1. Networking & Connectivity (Bypass de Restrições)
Um diferencial técnico deste projeto foi superar barreiras de redes corporativas restritivas:

* **O Problema:** Bloqueio de porta 22 (SSH) via Netskope/EDR.
* **A Solução:** Implementação de acesso via OCI Cloud Shell e Serial Console Connection.

### 2. Provisionamento de Compute
* [x] **VCN & Security:** Setup de tabelas de roteamento e Security Lists.
* [x] **Instância de Validação:** Provisionamento de VM Standard.E2.1.Micro (AMD).
* [ ] **High Performance Shape:** Em processo de upgrade para Ampere (A1.Flex - 12GB RAM).

---

### 🛠️ Como Reproduzir
1. Gerar par de chaves RSA via PowerShell.
2. Criar VCN e Subnet na OCI.
3. Injetar chave pública no Cloud Shell para acesso seguro.
4. Executar o check-up de recursos: `free -h` e `df -h /`.

---

### 📈 Roadmap do Projeto
* [x] Design de Rede e Provisionamento de VCN.
* [x] Bypass de Firewall corporativo e primeiro acesso SSH.
* [ ] Instalação do Docker Engine e K3s Runtime.
* [ ] Deploy do Rancher Manager.
* [ ] Instalação do Istio e configuração da Malha de Serviços.



**Responsável:** [Thiago Monaco](https://github.com/thiago-monaco)
