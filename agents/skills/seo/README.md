# SEO Extraction Bus

This folder stores mined and normalized SEO skill assets extracted from external repositories.

## Control Modules

- `stega-safe-metadata-gate.md`
- `seo-drift-telemetry-loop.md`
- `geo-crawler-policy-matrix.md`
- `rank-tracking-evidence-loop.md`

## Prompt Templates

- `templates/metadata_gate_prompt.md`
- `templates/drift_triage_prompt.md`

## Tooling

- `tools/rank_tracking_rollup.py`

## Source Repositories Used

- https://github.com/AgriciDaniel/claude-seo
- https://github.com/every-app/open-seo
- https://github.com/sanity-io/agent-toolkit
- https://github.com/VoltAgent/awesome-agent-skills
- https://github.com/modelcontextprotocol/servers
- https://github.com/crewAIInc/crewAI
- https://github.com/langchain-ai/langgraph
- https://github.com/simular-ai/agent-s

## Ingestion Notes

- `AgriciDaniel/AEO-Agent-Crew` was unavailable at clone time.
- `anthropics/frontend-design` was unavailable at clone time.
- `Significant-Gravitas/Auto-GPT` cloned with Windows long-path checkout warnings. SEO signal extraction still proceeded from available repositories.
