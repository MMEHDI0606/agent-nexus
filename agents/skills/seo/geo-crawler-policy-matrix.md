# GEO Crawler Policy Matrix

## Intent

Control AI answer-surface discoverability while preserving classical SEO crawl health.

## Derived Logic

- Maintain explicit policy matrix for search crawlers and AI crawlers.
- Separate crawl allowance from content reuse policy.
- Version policies and keep an audit trail.
- Validate `robots.txt`, `llms.txt`, and major domain-level directives as a synchronized set.

## Policy Axes

- Crawl: allow, throttle, deny.
- Snippet reuse: allow summary, allow citation only, deny.
- Asset access: html only, include media, deny media.
- Locale coverage: global, regional, market-specific.

## Procedure

1. Build crawler inventory with agent signatures.
2. Generate candidate policy profile per market.
3. Validate for conflicts across `robots.txt`, `sitemap.xml`, and `llms.txt`.
4. Deploy policy bundle with change ticket reference.
5. Monitor answer-surface citation rate and crawl diagnostics.

## Operational Checks

- Robots directives do not block canonical URLs.
- Sitemap URLs are indexable under active policies.
- llms policy file references canonical host and language scope.
- Policy changes trigger recrawl schedule.
