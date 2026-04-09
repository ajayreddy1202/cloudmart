# CloudMart — Cloud Native E-Commerce Platform

A production-grade microservices e-commerce platform built with Django, Docker, Kubernetes, and AWS.

## 🌐 Live Demo
| Service | URL |
|---|---|
| User Service | http://13.205.186.22:8000/api/users/register/ |
| Product Service | http://13.205.186.22:8001/api/products/ |
| Order Service | http://13.205.186.22:8002/api/orders/ |
| Notification Service | http://13.205.186.22:8003/api/notifications/ |

## 🛠️ Tech Stack
- **Backend:** Python, Django, Django REST Framework
- **Database:** MySQL
- **Containerization:** Docker, Docker Compose
- **Orchestration:** Kubernetes (AWS EKS)
- **Cloud:** AWS EC2, ECR, EKS, IAM, VPC
- **CI/CD:** GitHub Actions

## ✅ Features
- 4 Production-grade Microservices
- JWT Authentication
- REST APIs for all services
- LoadBalancer for high availability
- Zero downtime deployment

## 🏗️ Architecture
- User Service → Port 8000
- Product Service → Port 8001
- Order Service → Port 8002
- Notification Service → Port 8003

## 🚀 Deployment
- Containerized with Docker
- Images pushed to AWS ECR
- Deployed on AWS EKS with 8 pods across 2 worker nodes
- Automated CI/CD via GitHub Actions
- Deployment time reduced by 80%

## 📦 Run Locally
```bash
git clone https://github.com/ajayreddy1202/cloudmart.git
cd cloudmart
docker compose up -d
```

## 👨‍💻 Author
Ajay Kumar Bhumana
- GitHub: github.com/ajayreddy1202
- LinkedIn: linkedin.com/in/Bhumana-Ajay-Kumar
