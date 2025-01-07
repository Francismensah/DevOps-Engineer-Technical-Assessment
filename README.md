# DevOps Engineer Technical Assessment

## Overview
This repository contains my solutions for the DevOps Engineer technical assessment. Each section is organized in separate directories with detailed documentation and implementation.

## Table of Contents
1. [General Technical Knowledge](docs/solutions/technical-questions.md)
2. [Coding Challenges](src)
3. [Behavioral Challenges](monitoring/behavioural.md)
4. [Monitoring and Troubleshooting](monitoring/troubleshooting.md)
5. [System Design](docs/architecture/gitops-cicd.md)

## Repository Structure
```
.
├── docs/
│   ├── architecture/
│   │   └── gitops-cicd.md
│   └── solutions/
│       └── technical-questions.md 
|       └── postgre-checker.md
├── src/
│   ├── prometheus-exporter/
│   │   ├── Dockerfile
│   │   └── exporter.py
|   |   └── requirements.txt
│   ├── laravel-monitor/
│   │   └── cpu-monitor.sh
│   └── laravel-docker/
│       └── Dockerfile
├── monitoring/
│   └── behaviourial.md
│   └── troubleshooting.md
└── README.md
```

## Getting Started

### Prerequisites
- Docker 24.x
- Python 3.10+
- Kubernetes 1.28+
- RabbitMQ 3.12+
- Access to a PostgreSQL database

### Installation
1. Clone the repository:
```bash
git clone https://github.com/Francismensah/DevOps-Engineer-Technical-Assessment.git
cd DevOps-Engineer-Technical-Assessment
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Build containers:
```bash
docker-compose build
```

## Solutions Overview

### 1. General Technical Knowledge
- Detailed answers to technical questions are in [docs/solutions/technical-questions.md](docs/solutions/technical-questions.md)
- Architecture diagrams can be found in [docs/architecture/](docs/architecture/)

### 2. Coding Challenges

#### RabbitMQ Prometheus Exporter
- Implementation: [src/prometheus-exporter/](src/prometheus-exporter/)
- Setup instructions:
  ```bash
  cd src/prometheus-exporter
  docker build -t rabbitmq-exporter .
  docker run -d \
    -e RABBITMQ_HOST=your-host \
    -e RABBITMQ_USER=your-user \
    -e RABBITMQ_PASSWORD=your-password \
    rabbitmq-exporter
  ```

#### Laravel CPU Monitor
- Script location: [src/laravel-monitor/cpu-monitor.sh](src/laravel-monitor/cpu-monitor.sh)
- Usage:
  ```bash
  chmod +x cpu-monitor.sh
  ./cpu-monitor.sh
  ```

#### Laravel Dockerfile
- Location: [src/laravel-docker/Dockerfile](src/laravel-docker/Dockerfile)
- Build and run:
  ```bash
  docker build -t laravel-app .
  docker run -d -p 8000:80 laravel-app
  ```

### 3. Monitoring and Troubleshooting
- API monitoring setup: [monitoring/configs/](monitoring/configs/)
- Performance debugging guidelines: [docs/solutions/troubleshooting.md](docs/solutions/troubleshooting.md)

### 4. System Design
- GitOps CI/CD architecture: [docs/architecture/gitops-cicd.md](docs/architecture/gitops-cicd.md)


## Security Considerations
- All secrets are managed through environment variables
- Container images are scanned for vulnerabilities
- Network policies are implemented for K8s deployments
- RBAC is properly configured

