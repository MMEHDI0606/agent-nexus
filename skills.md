# Skills Registry

**Status:** 60+ skills installed ✓

## Folder Structure
- `.agents/skills/` — **60 installed skills** (AI/ML enhancement packages)
- `.tools/` — Runtime tools and utilities (automation, browser, memory)
- `.vendor/reference/` — Template references for agent setup
- `.vendor/` — Infrastructure dependencies (build, orchestration)

## Local Skill Loader
- Script: `skills.sh`
- Bootstrap (WSL/Ubuntu): `.bootstrap.sh`
- Bootstrap (Windows): `scripts/bootstrap-agent-foundation.ps1`
- Runtime: `npx skills@latest`
- Command: `bash ./skills.sh`

## Installed Skills (`.agents/skills/`) — 60 total

**Core Design & Development:**
- `frontend-design`, `web-design-guidelines`, `ui-ux-pro-max-skill`
- `mcp-builder` — Model Context Protocol building
- `article-writing`, `content-engine`, `investor-materials`

**Language-Specific Patterns:**
- Python: `python-patterns`, `python-testing`
- Java: `java-coding-standards`, `jpa-patterns`, `springboot-*` (5 variants)
- Django: `django-patterns`, `django-security`, `django-tdd`, `django-verification`
- Go: `golang-patterns`, `golang-testing`
- C++: `cpp-coding-standards`, `cpp-testing`
- Swift: `swift-actor-persistence`, `swift-concurrency-6-2`, `swift-protocol-di-testing`, `swiftui-patterns`
- Backend: `backend-patterns`, `docker-patterns`, `database-migrations`

**Testing & Quality:**
- `e2e-testing`, `tdd-workflow`, `security-scan`, `security-review`, `verification-loop`
- Code standards, deployment patterns, cost-aware LLM pipelines

**Advanced Topics:**
- `foundation-models-on-device`, `iterative-retrieval`, `search-first`
- `continuous-learning`, `continuous-learning-v2`
- Specialized: `clickhouse-io`, `postgres-patterns`, `liquid-glass-design`

**Sources:**
- 4 initially installed skills (frontend-design, mcp-builder, web-design-guidelines, ui-ux-pro-max-skill)
- 56 skills from `everything-claude-code/skills`
- Includes: marketingskills (coreyhaines31), antigravity-awesome-skills

## Installed Tools (`.tools/`)
- `browser-use` — Browser automation and interaction toolkit (30+ MB, 477 files)
- `claude-mem` — Claude memory management utility

## References (`.vendor/reference/`)
- `ai-agent-foundation-template` — Agent setup reference

## Infrastructure (`.vendor/`)
- `ccpm` — Context/task management
- `everything-claude-code` — Source repository (cleaned of docs/tests/examples)

## Cleanup Status ✓
- ✓ Removed duplicate folders (`.agent`, `.kiro`)
- ✓ Removed .git folders from cloned repos
- ✓ Removed unnecessary docs/tests/examples from vendor
- ✓ Consolidated all skills into single `.agents/skills/` folder
- ✓ Extracted 56 skills from everything-claude-code

## Action Contract
- Discover available skills: `Get-ChildItem .agents/skills -Directory`
- Add new skills to `.agents/skills/` via`git clone` or `npx skillkit`
- Add tools to `.tools/` folder
- Keep this file synchronized with skill inventory changes
