# Stega-Safe Metadata Gate

## Intent

Prevent SEO-visible head tags from receiving editor trace payloads or instrumentation noise.

## Derived Logic

- Execute metadata fetches in an isolated read mode.
- Disable editorial overlays and Stega decoration for metadata queries.
- Build deterministic fallback chain: `seo.title -> page.title -> site.defaultTitle` and `seo.description -> excerpt -> site.defaultDescription`.
- Enforce canonical URL normalization and locale-aware alternates.
- Fail closed if metadata response contains zero-width or non-printable artifacts.

## Procedure

1. Resolve route payload and locale.
2. Fetch content with tracing disabled for head-surface fields.
3. Materialize title, description, canonical, Open Graph, and Twitter fields.
4. Validate length windows and character hygiene.
5. Emit telemetry event `metadata_gate_pass` or `metadata_gate_fail`.

## Validation Gates

- Title length: 20 to 65 chars.
- Description length: 120 to 160 chars.
- Canonical must be absolute HTTPS.
- No control characters in title, description, or URL fields.

## Output Contract

```json
{
  "title": "string",
  "description": "string",
  "canonical": "https://...",
  "openGraph": {"title": "string", "description": "string", "images": ["https://..."]},
  "twitter": {"card": "summary_large_image", "title": "string", "description": "string"},
  "status": "pass|fail",
  "reasons": ["..."]
}
```
