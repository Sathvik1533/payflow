# Architecture Overview

> **Status:** Planned. Not yet implemented.

This document describes the intended architecture of Payflow.
It will be updated as implementation decisions are made and validated.

---

## System Layers

```
┌─────────────────────────────────────────────┐
│                   Frontend                  │
│                    (React)                  │
└────────────────────┬────────────────────────┘
                     │ HTTP / REST
┌────────────────────▼────────────────────────┐
│                   Backend                   │
│                  (FastAPI)                  │
└────────────────────┬────────────────────────┘
                     │ SQLAlchemy ORM
┌────────────────────▼────────────────────────┐
│                  Database                   │
│          (Amazon RDS PostgreSQL)            │
└─────────────────────────────────────────────┘
```

---

## Deployment Architecture

```
┌──────────────────────────────────────────────────┐
│                      AWS                         │
│                                                  │
│   ┌──────────────────────────────────────────┐   │
│   │                   VPC                    │   │
│   │                                          │   │
│   │  ┌───────────────────────────────────┐   │   │
│   │  │     Application Load Balancer     │   │   │
│   │  └──────────────────┬────────────────┘   │   │
│   │                     │                    │   │
│   │  ┌──────────────────▼────────────────┐   │   │
│   │  │         ECS Fargate               │   │   │
│   │  │    (FastAPI Docker container)     │   │   │
│   │  └──────────────────┬────────────────┘   │   │
│   │                     │                    │   │
│   │  ┌──────────────────▼────────────────┐   │   │
│   │  │       Amazon RDS PostgreSQL       │   │   │
│   │  └───────────────────────────────────┘   │   │
│   │                                          │   │
│   └──────────────────────────────────────────┘   │
│                                                  │
│   Amazon ECR  ──►  ECS (image source)            │
│   CloudWatch  ──►  Logs, metrics, alarms         │
│   IAM         ──►  Roles and policies            │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## Infrastructure as Code

All AWS resources will be defined in Terraform.
State will be managed remotely (S3 backend with DynamoDB locking — TBD).

---

## Data Flow — Payment Ingestion (Planned)

```
External source (API call / upload)
         │
         ▼
    FastAPI endpoint
         │
         ▼
    Validation (Pydantic)
         │
         ▼
    Persistence (SQLAlchemy → RDS PostgreSQL)
         │
         ▼
    Response (HTTP 201 Created)
```

---

## Design Decisions

Architecture Decision Records are located in `docs/decisions/`.

No decisions have been recorded yet. ADRs will be added as implementation progresses.
