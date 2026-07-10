# Solution Overview

## One-Line Pitch

Software engineers use Git to instantly see what changed between two versions of code. Compliance officers deserve the same capability for regulation.

**Compliance Evolution Engine** shows exactly what changed in a new SEBI circular, what became obsolete, and what operational action is required — with a citation for every claim.

---

## Core Philosophy

Most compliance-AI tools answer:
> "What does this regulation mean?"

This engine answers a harder, rarer question:
> "What should my organization do now?"

---

## How It Works, At a Glance
SEBI Circular (PDF)
↓
Module 1 — Regulatory Extraction Engine
↓ (structured obligations)
Module 2 — Obligation Reconciliation Engine ("Zombie")
↓ (new / modified / superseded / removed — with citations)
Module 3 — Patch Generator
↓ (GitHub-style changelog view)
Module 4 — Recommended Compliance Actions
↓
Compliance officer sees: what changed, why, and what to do next.

Every module operates on the same underlying extracted data — this is **one engine with three output lenses**, not four separate systems.

---

## Why It's Different

| Competing Approach | Its Limit | Our Answer |
|---|---|---|
| Generic RAG / chatbot over circulars | Only answers when asked; doesn't proactively flag changes | Proactive reconciliation across versions, citation-backed |
| Extraction-only tools | Treats each circular in isolation; obligations never retire | Explicitly tracks supersession — our core differentiator |
| Full enterprise workflow platforms | Needs fictional org data (owners, SOPs); high build risk | Categorical recommendations only, no faked org data |

---

## Business Model

- **Compliance teams** at regulated intermediaries — SaaS subscription
- **RegTech vendors** — licensing of the underlying engine
- **SEBI itself** — reference tool within its Innovation Sandbox, or to assess consistency of interpretation across intermediaries

---

## Why Organizations Would Adopt It

- Directly reduces hours spent per circular cycle on manual comparison and interpretation
- Reduces audit risk with a citation-backed record of exactly why an obligation was retired or changed
- Reduces divergent interpretation across similarly situated intermediaries — the exact inconsistency problem SEBI's brief names