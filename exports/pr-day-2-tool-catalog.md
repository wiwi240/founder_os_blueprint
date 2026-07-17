# PR Day 2 Tool Catalog

## Title

`Day 2 - add tool catalog and structured outputs`

## Body

```md
## Summary

This PR adds the day-2 Founder OS deliverables to make the agents more actionable.

## Added

- `docs/tool-catalog.md`
- `docs/structured-outputs.md`
- `evidence/tool-tests.md`
- `exports/pr-day-2-tool-catalog.md`

## Updated

- `docs/permissions-policy.md`

## Covered

- minimum catalog of six actions with permissions, risks and stack
- structured output schemas for lead qualification, email draft, mock quote and memory search
- evidence file with four tool tests and verdicts
- stricter permission rules for drafts, mock quotes, permanent notes and paid APIs

## Known limits

- `qualify_lead` and `search_knowledge_base` exist as real local scripts today
- other actions are documented contracts, not production integrations
- no remote PR was opened from this environment
```
