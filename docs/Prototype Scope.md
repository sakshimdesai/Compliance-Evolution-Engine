# Prototype Scope

This document defines exactly what we are building for the prototype round, what we are deliberately excluding, and how we'll know it's done. Re-read the "Out of Scope" section before every build decision — it exists specifically to stop scope creep under time pressure.

---

## Frozen Demo Dataset

> To be filled in and frozen by the team — do not change once set.

| Field | Value |
|---|---|
| **Source** | SEBI Master Circular for Stockbrokers *(exact circular number/date: ____________)* |
| **Chapter/topic selected** | ____________ *(e.g., cyber security / reporting obligations)* |
| **"Old" circular version** | ____________ *(exact date/number, download link)* |
| **"New"/amending circular version** | ____________ *(exact date/number, download link)* |
| **Obligations expected to be flagged** | ____________ *(write these down in advance to verify the system finds them)* |
| **Backup chapter/topic** | ____________ *(in case the primary one has extraction issues)* |

Once filled in, this becomes the only dataset used for every future build, screenshot, and demo rehearsal — **no substitutions.**

---

## Explicitly Out of Scope for the Prototype

| Excluded Feature | Why |
|---|---|
| Task management / owner assignment | Requires fictional organizational structure that doesn't exist in a public-data demo |
| Audit dashboard with department-level tracking | Same problem — no real org data to visualize against |
| Workflow engine / approval flows | Enterprise-software scope, not hackathon-buildable |
| Notifications / integrations with external systems | No real system to integrate with in a prototype |
| Multi-regulator support (RBI, IRDAI, etc.) | Roadmap item only (see Section 13 of master doc) — never built or demoed |
| Fine-tuned / local models | Phase 2+ roadmap item — prototype uses a general-purpose LLM |

These are legitimate, valuable future features — mention them verbally in the pitch as **"Phase 2 roadmap"** — but they must never appear on screen as if they are working. A judge who catches a faked or scripted-looking feature does more damage to credibility than a narrower, fully-real demo would have avoided entirely.

---

## Success Metrics — Prototype Checklist

- [ ] Correctly extracts obligations from the frozen SEBI chapter into the Data Model schema
- [ ] Correctly classifies each obligation as NEW / MODIFIED / SUPERSEDED / UNCHANGED against the prior circular version
- [ ] Shows a clause-level citation for **every single classification** — no exceptions
- [ ] Assigns a confidence tier (High/Medium/Low) to each classification and visibly handles Low-confidence cases as a question, not an assertion
- [ ] Generates the patch/changelog view (Module 3) directly from the reconciliation output
- [ ] Generates a categorical recommended action (Module 4) for every flagged obligation
- [ ] Full pipeline runs live, end-to-end, on the frozen dataset, in under the 3-minute demo window — no manual intervention or pre-recorded shortcuts

If any item on this list isn't true yet, that is the next thing to build — not a new feature, not a nicer UI.

---

## Honest Risks & Limitations

- Extraction and reconciliation accuracy on dense legal language is a genuinely hard, still-open problem in NLP research — we do not claim a specific accuracy number we cannot defend live.
- The system is built and positioned as a **decision-support tool** for human compliance reviewers, not an autonomous compliance-decision system — this is a deliberate design choice, not a limitation to hide.
- Prototype scope is intentionally narrow (one chapter, two frozen circular versions) — broader real-world deployment would require a larger, curated corpus and real-world validation.
- Recommended actions are categorical, not integrated with any real organization's actual SOP registry — this is correctly scoped, not a gap to apologize for.
- Data residency/confidentiality: a real-world deployment sending circulars to a third-party LLM API may concern regulated intermediaries — addressed on the roadmap via local/on-premise inference, not in the prototype.