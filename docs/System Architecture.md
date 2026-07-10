# System Architecture

The engine has four modules, all operating on one shared data schema. Modules 3 and 4 require no new AI processing — they re-render or template data that Modules 1 and 2 already produced.

---

## Module 1 — Regulatory Extraction Engine

**Input:** A SEBI circular (PDF/text)

**Process:** An LLM-based extraction pipeline reads the circular and converts each obligation-bearing sentence into structured fields.

**Example:**

| Legal Text | Structured Output |
|---|---|
| "Every stock broker shall submit the monthly compliance report within T+1 working day." | Obligation: Submit Monthly Compliance Report • Owner category: Compliance Department • Deadline: T+1 • Evidence required: Monthly report • Priority: High • Applicable to: Stockbrokers • Source clause: [citation] |

**Output:** A structured, machine-readable obligation record for every obligation-bearing clause, each tagged with its exact source citation.

---

## Module 2 — Obligation Reconciliation Engine ("Zombie") — Core Differentiator

**Input:** Structured obligations from Module 1, for two versions of related circulars.

**Process:** Compares the new obligation set against the previous one and classifies each as:

- **NEW** — didn't exist before
- **MODIFIED** — terms changed (e.g., deadline shifted from T+3 to T+1)
- **SUPERSEDED / OBSOLETE** — replaced by a later clause
- **UNCHANGED** — carried forward with no modification

Every classification is backed by the exact clause citation. The system never asserts an obligation is dead without pointing to the specific proving text — every output is a **flagged candidate for human review**, never an automated deletion.

**Output:** A reconciled obligation ledger.

---

## Module 3 — Patch Generator

**Input:** The reconciled obligation ledger (no new AI processing required).

**Process:** Re-renders the reconciliation data as a GitHub-commit-style changelog.
NEW       Monthly cyber-audit now mandatory (Clause 9.1)
UPDATED   Reporting deadline changed: T+3 → T+1 (Clause 4.1 → 7.2)
REMOVED   Quarterly declaration requirement withdrawn (Clause 12.4)
IMPACTED  Compliance · IT · Risk · Operations

---

## Module 4 — Recommended Compliance Actions

**Input:** The classified obligation ledger.

**Process:** Templated translation from classification → categorical recommended action.

| Classification | Recommended Action (Categorical) |
|---|---|
| SUPERSEDED | Retire the SOP governing this obligation; archive related checklists |
| MODIFIED (deadline) | Update your internal compliance calendar to reflect the new deadline |
| NEW | Establish an SOP and evidence-collection process for this obligation |

Deliberately categorical — never invents specific internal document IDs (e.g., never "Update SOP-14"), since no real organization's SOP registry is connected.

---

## Data Model

**Obligation record (Module 1 output):**
```json
{
  "obligation_id": "",
  "obligation_text": "",
  "owner_category": "",
  "deadline": "",
  "evidence_required": "",
  "applicable_to": "",
  "source_clause": "",
  "circular_version": ""
}
```

**Reconciliation record (Module 2 output):**
```json
{
  "obligation_id_old": "",
  "obligation_id_new": "",
  "classification": "NEW | MODIFIED | SUPERSEDED | UNCHANGED",
  "reasoning": "",
  "citation_old": "",
  "citation_new": "",
  "confidence": "HIGH | MEDIUM | LOW"
}
```

Modules 3 and 4 read directly from these two structures — no separate schema needed.

---

## Confidence & Human Review

| Confidence | System Behavior |
|---|---|
| **High** | Auto-classified, shown directly with citation |
| **Medium** | Shown, but visually flagged "needs review" |
| **Low** | Not auto-classified — surfaced as a question to the officer, never asserted as fact |

---

## AI Responsibilities & Boundaries

**The LLM IS responsible for:**
- Extracting obligations into the structured schema
- Producing structured JSON output, not free-text summaries
- Semantic comparison between old and new obligations to detect overlap, modification, or contradiction

**The LLM is explicitly NOT responsible for:**
- Making final compliance decisions on behalf of the organization
- Deleting or discarding obligations outright — it only flags candidates for human review
- Legal interpretation beyond textual comparison

---

## Technology Stack

| Layer | Approach |
|---|---|
| Extraction / reconciliation reasoning | LLM-based extraction with structured-output/JSON schema prompting; RAG-grounded against source text |
| Data source | Public SEBI Master Circulars (PDFs) |
| Obligation storage | Structured JSON per obligation; lightweight DB (SQLite/Postgres) |
| Reconciliation logic | Semantic similarity matching + explicit contradiction/reference detection |
| Frontend / demo UI | Upload circular(s) → obligation view → changelog view → recommended actions view |
| Citation grounding | Every output field points back to the exact source sentence/clause |