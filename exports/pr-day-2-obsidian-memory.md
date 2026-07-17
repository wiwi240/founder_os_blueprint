# PR Day 2 Obsidian Memory

## Title

`Day 2 - add local vault memory and Coach agent`

## Body

```md
## Summary

This PR adds the day-2 memory layer for Founder OS with a local markdown vault and a Coach agent that can answer from notes with citations.

## Added

- `vault/` structured local memory
- `scripts/coach_memory_agent.py`
- `docs/memory-setup.md`
- `evidence/runs/day-2-coach-memory.md`
- `exports/pr-day-2-obsidian-memory.md`

## Covered

- at least 10 founder memory notes across business, clients, offer, SEO, sales, admin, learning and journal areas
- local-first memory path with zero cloud dependency
- Coach agent CLI that reads notes and cites the sources it used
- evidence run for the weekly learning question

## Known limits

- retrieval is lexical, not semantic
- no automatic embeddings or vector store yet
- no remote PR was opened from this environment
```
