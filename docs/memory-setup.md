# Memory Setup

## Decision

The memory stack is local-first:

- storage: `vault/` markdown notes
- access mode: local file read
- agent path: `scripts/coach_memory_agent.py`
- cloud dependency: none

## Why This Choice

This is the most defendable MVP for day 2.

- it is real and runnable in this repo
- it keeps business notes out of external services
- it is easy to inspect, version and audit
- it avoids inventing an untested integration

## Tradeoffs

Benefits:

- zero API cost
- zero cloud exposure by default
- simple citations because note paths are stable

Limits:

- retrieval is local and section-aware, but still lexical rather than embedding-based
- no embeddings, vector index or automated chunking
- no multi-user sync workflow is configured here

## Vault Structure

```text
vault/
  00-index.md
  10-business/
  20-clients/
  30-offers/
  40-seo-market/
  50-sales-mail/
  60-admin/
  70-learning/
  90-agent-runs/
```

## Coach Agent

Question target:

```text
A partir de mes notes, que dois-je apprendre cette semaine pour mieux lancer mon offre ?
```

Execution:

```bash
python3 scripts/coach_memory_agent.py --json "A partir de mes notes, que dois-je apprendre cette semaine pour mieux lancer mon offre ?"
```

Behavior:

- read local notes from `vault/`
- score relevant notes by folder weight and section relevance
- generate a short weekly learning priority
- cite the notes used with short excerpts and line numbers
- avoid claims unsupported by the vault

## Why Not Cloud Or No-Code Here

Open WebUI, Flowise, Langflow and hosted knowledge bases are valid later options, but they are weaker for this task today because:

- no existing verified integration is already present in the repo
- they would add setup work without improving day-2 auditability enough
- the requested proof can be delivered locally with lower risk

## Possible Next Step

If a stronger retrieval layer is needed, the next pragmatic step is a local semantic index over `vault/` rather than a cloud migration first.
