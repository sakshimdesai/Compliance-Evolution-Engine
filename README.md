# Compliance Evolution Engine

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61dafb)
![License](https://img.shields.io/badge/License-MIT-yellow)

> **Transforming SEBI regulations into executable, auditable compliance workflows.**

Compliance Evolution Engine is an AI-powered regulatory intelligence platform that converts SEBI circulars into structured, machine-actionable compliance obligations. Instead of simply summarizing regulatory documents, the platform identifies regulatory changes, reconciles evolving obligations, and generates explainable compliance patches with complete audit traceability.

---

# Problem

Financial intermediaries regularly receive lengthy SEBI circulars containing new, modified, and superseded compliance obligations. Today, compliance teams must manually:

- Read lengthy regulatory documents
- Compare amendments with previous circulars
- Identify affected obligations
- Update internal SOPs and policies
- Coordinate implementation across departments
- Maintain evidence for regulatory audits

This process is time-consuming, error-prone, difficult to audit, and slows regulatory response.

---

# Our Solution

Compliance Evolution Engine transforms regulatory text into structured operational intelligence through four core stages:

1. Regulatory Obligation Extraction
2. Obligation Reconciliation
3. Compliance Patch Generation
4. Explainable Audit Trail

Rather than acting as a chatbot, the platform enables compliance teams to understand exactly **what changed, why it changed, and what operational action should be taken.**

---

# System Architecture

![Architecture](design/Architecture%20Diagram.png)

---

# Workflow

![Workflow](design/Workflow%20Diagram.png)

---

# Prototype UI

![UI](design/UI%20Mockups.png)

---

# Core Features

- AI-powered obligation extraction from SEBI circulars
- Structured compliance knowledge representation
- Obligation reconciliation across circular versions
- Automatic identification of **New**, **Modified**, **Superseded**, and **Unchanged** obligations
- Compliance Patch generation
- Clause-level citation and explainability
- Human review workflow
- Audit-ready compliance history

---

# Repository Highlights

- Modular FastAPI backend scaffold
- React frontend scaffold
- Shared JSON compliance schemas
- Sample SEBI circulars for demonstration
- System architecture documentation
- Workflow documentation
- UI mockups
- Technical design documents

---

# Repository Structure

```text
compliance-evolution-engine/

├── backend/
│   ├── app/
│   ├── requirements.txt
│   └── main.py
│
├── frontend/
│
├── docs/
│   ├── Problem Statement.md
│   ├── Solution Overview.md
│   ├── System Architecture.md
│   └── Prototype Scope.md
│
├── design/
│   ├── Architecture Diagram.png
│   ├── Workflow Diagram.png
│   └── UI Mockups.png
│
├── sample_data/
│   ├── old_circular.pdf
│   └── amended_circular.pdf
│
├── schemas/
│   ├── obligation_schema.json
│   └── patch_schema.json
│
├── LICENSE
├── README.md
└── .gitignore
```

---

# Planned Backend Routes

| Method | Route | Purpose |
|---------|-------|---------|
| POST | `/upload` | Upload SEBI circular |
| POST | `/extract` | Extract structured obligations |
| POST | `/reconcile` | Compare obligation versions |
| POST | `/patch` | Generate compliance patch |
| GET | `/health` | Service health check |

> These routes currently represent the planned API structure for the prototype backend.

---

# Technology Stack

## Backend

- Python
- FastAPI

## AI / NLP

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Structured Information Extraction

## Frontend

- React

## Data Layer

- JSON-based compliance schemas

---

# Current Status

This repository contains the **prototype design and technical foundation** developed for the **SEBI Securities Market TechSprint 2026**.

### Completed

- Repository structure
- Backend scaffold
- Frontend scaffold
- System architecture
- Workflow design
- UI mockups
- Compliance schemas
- Sample SEBI circulars
- Technical documentation

### Planned

- LLM-powered obligation extraction
- Obligation reconciliation engine
- Compliance Patch generation
- Interactive dashboard
- End-to-end workflow integration

---

# License

This project is licensed under the **MIT License**.
