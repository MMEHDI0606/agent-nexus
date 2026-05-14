# Rank Tracking Evidence Loop

## Intent

Create a stable feedback loop from rank movements to deploy actions with evidence-grade artifacts.

## Derived Logic

- Track target query sets by intent and page cluster.
- Pair rank snapshots with SERP feature context.
- Attach metadata diffs and content diffs to each movement event.
- Convert movement events into prioritized response tasks.

## Event Model

- `keyword`
- `page`
- `device`
- `location`
- `rank_previous`
- `rank_current`
- `delta`
- `serp_features`
- `change_window`
- `probable_causes`

## Procedure

1. Ingest rank snapshots from provider or exported CSV.
2. Normalize entity keys for keyword, page, market, and device.
3. Compute deltas and classify into gain, loss, flat, volatile.
4. Join with release notes, metadata changes, and drift scan outcomes.
5. Emit action queue with confidence score.

## Response Protocol

- Loss with high confidence technical cause -> route to engineering.
- Loss with high confidence content cause -> route to content ops.
- Volatile signal without corroboration -> hold and monitor.
- Gain with schema correlation -> replicate pattern across similar templates.
