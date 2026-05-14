# SEO Drift Telemetry Loop

## Intent

Track on-page SEO regressions over time using repeatable baseline snapshots and severity scoring.

## Derived Logic

- Capture baseline at known-good deployment.
- Compare current state against baseline with rule packs.
- Compute weighted impact score for critical SEO surfaces.
- Persist drift history to local artifact store.
- Produce triage queue for engineering and content teams.

## Drift Rule Pack

- `title_changed`
- `description_changed`
- `canonical_changed`
- `robots_directive_changed`
- `schema_block_missing`
- `hreflang_cluster_incomplete`
- `heading_hierarchy_broken`
- `internal_link_drop`

## Severity Matrix

- Critical: Canonical, robots, indexability loss.
- High: Title, description, structured data disappearance.
- Medium: Hreflang, heading hierarchy, internal linking density.
- Low: Minor copy shifts within tolerance windows.

## Procedure

1. Collect HTML and extracted SEO facts for baseline and candidate.
2. Evaluate rule pack and mark each delta as pass, warn, or fail.
3. Aggregate severity score and emit release gate recommendation.
4. Store evidence bundle with timestamp.

## Output Contract

```json
{
  "url": "https://...",
  "baselineId": "string",
  "currentId": "string",
  "score": 0,
  "status": "pass|warn|fail",
  "criticalFindings": ["..."],
  "allFindings": [{"rule": "title_changed", "severity": "high", "delta": "..."}]
}
```
