# Infrastructure

> **Status:** Not yet implemented.

This directory will contain all Terraform infrastructure-as-code for Payflow's AWS deployment.

## Planned AWS Services

| Service | Purpose |
|---------|---------|
| Amazon RDS PostgreSQL | Managed relational database |
| Amazon ECR | Docker image registry |
| Amazon ECS Fargate | Serverless container compute |
| Application Load Balancer | HTTP routing and TLS termination |
| IAM | Roles and least-privilege policies |
| VPC | Networking — subnets, security groups, routing |
| CloudWatch | Logs, metrics, and alarms |

## Planned Structure

```
infrastructure/
├── modules/
│   ├── networking/   # VPC, subnets, security groups
│   ├── rds/          # PostgreSQL RDS instance
│   ├── ecr/          # Container registry
│   ├── ecs/          # ECS cluster, task definitions, services
│   ├── alb/          # Application Load Balancer
│   └── iam/          # Roles and policies
├── environments/
│   ├── dev/
│   └── prod/
├── main.tf
├── variables.tf
├── outputs.tf
└── backend.tf        # Remote state configuration
```

## Implementation

Infrastructure will be defined in Terraform and implemented manually during Phase 1.

No Terraform code exists yet.
