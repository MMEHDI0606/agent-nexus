# AI Agent Foundation Template

A production-ready, extensible **AI agent foundation** with 60+ skills, organized tooling, automated bootstrap, and persistent context management. Built by synthesizing best practices from leading AI agent frameworks and skill libraries.

## Features

✨ **60+ Pre-installed Skills** — comprehensive skill library covering:
- API design, backend patterns, database patterns
- Python, Java, Go, C++, Swift, Django, Spring Boot
- Frontend design, testing, DevOps, security, performance
- Advanced topics: MCP servers, LLM pipelines, continuous learning

🛠️ **Organized Tooling** — utilities and runtime tools:
- Browser automation (`browser-use`)
- Memory management (`claude-mem`)
- Context orchestration (`ccpm`)

📋 **Persistent Planning** — built-in planning layer:
- `.planning/current.md` — active tasks
- `.planning/backlog.md` — queued work
- `.planning/README.md` — planning protocol

🧠 **Context Preservation** — systematic memory layers:
- `claude.md` — project DNA and architecture
- `.clauderules` — agent behavior contract
- `.claude/config.md` — sub-agent role definitions
  
🚀 **Bootstrap Automation** — self-healing setup:
- Windows: `scripts/bootstrap-agent-foundation.ps1`
- WSL/Ubuntu: `.bootstrap.sh`
- Canonical installs with resilient fallbacks

## Quick Start

### 1. Clone This Template

```bash
git clone https://github.com/MMEHDI0606/ai-agent-foundation-template.git my-agent-project
cd my-agent-project
```

### 2. Run Bootstrap (Choose Your OS)

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy Bypass -File ./scripts/bootstrap-agent-foundation.ps1
```

**WSL/Ubuntu:**
```bash
bash ./.bootstrap.sh
```

### 3. Verify Installation

```powershell
# Check skills are discoverable
Get-ChildItem .agents/skills -Directory

# Verify tools are available
Get-ChildItem .tools -Directory

# List all skills
gsd --help  # or npx -y skills
```

### 4. Start Using

Edit `.planning/current.md` to add your first task:
```yaml
## In Progress
- [ ] My first AI agent task
  - Outcome: ...
  - Status: in-progress
```

## Directory Structure

```
.agents/skills/              ← 60+ installed skills ready to use
  ├── frontend-design
  ├── python-patterns
  ├── springboot-*           (5 Spring Boot pattern skills)
  ├── django-*               (4 Django pattern skills)  
  ├── swift-*                (4 Swift pattern skills)
  └── ...                    (48 total skills)

.tools/                      ← Runtime utilities
  ├── browser-use            (browser automation)
  └── claude-mem             (memory management)

.vendor/                     ← Infrastructure
  ├── ccpm                   (context + task mgmt)
  └── everything-claude-code (extended skills source)

.planning/                   ← Work organization
  ├── current.md             (active tasks)
  ├── backlog.md             (queued tasks)
  └── README.md              (planning protocol)

.claude/                     ← Claude Code config
  ├── config.md              (sub-agent roles)
  └── skills/                (copied skills for IDE)

.github/                     ← GitHub integration
  └── copilot-instructions.md (Copilot Agent bridge)

scripts/                     ← Setup automation
  ├── bootstrap-agent-foundation.ps1 (Windows)
  └── install-antigravity.ps1         (skills pack)

claude.md                    ← Project DNA & architecture
.clauderules                 ← Agent behavior contract
skills.md                    ← Skills inventory + metadata
skills.sh                    ← Skills loader script
.bootstrap.sh                ← WSL/Ubuntu bootstrap
```

## Skill Categories

### Design & Development (7 skills)
`frontend-design`, `web-design-guidelines`, `ui-ux-pro-max-skill`, `mcp-builder`, `article-writing`, `content-engine`, `investor-materials`

### Python Ecosystem (7 skills)
`python-patterns`, `python-testing`, `cost-aware-llm-pipeline`, `django-patterns`, `django-security`, `django-tdd`, `django-verification`

### Java/Spring Boot (9 skills)
`java-coding-standards`, `jpa-patterns`, `springboot-patterns`, `springboot-security`, `springboot-tdd`, `springboot-verification`, `database-migrations`, `postgres-patterns`

### Go (2 skills)
`golang-patterns`, `golang-testing`

### C++ (2 skills)
`cpp-coding-standards`, `cpp-testing`

### Swift/iOS (4 skills)
`swift-actor-persistence`, `swift-concurrency-6-2`, `swift-protocol-di-testing`, `swiftui-patterns`, `liquid-glass-design`

### Testing & Quality (8 skills)
`e2e-testing`, `tdd-workflow`, `security-scan`, `security-review`, `verification-loop`, `eval-harness`, `skill-stocktake`, `search-first`

### DevOps & Infrastructure (5 skills)
`deployment-patterns`, `docker-patterns`, `database-migrations`, `clickhouse-io`

### Advanced Topics (9+ skills)
`foundation-models-on-device`, `iterative-retrieval`, `search-first`, `continuous-learning`, `continuous-learning-v2`, `mcp-builder`, `regex-vs-llm-structured-text`, `strategic-compact`, `market-research`, and more

## Key Files Explained

### `claude.md` — Project DNA
Defines:
- Mission context
- Architecture directives
- Core runtime layers (ingest, detect, reason, alert, audit)
- Execution discipline and decision records

**When to use:** Document architectural changes, record decisions.

### `.clauderules` — Agent Behavior Contract
Governs how Claude Code operates in your project:
- Mandatory pre-execution checks
- Execution rules
- Memory continuity expectations

**When to use:** Customize this for your team's workflow.

### `.planning/current.md` — Active Work
Standard format:
```yaml
## In Progress
- [ ] Feature Name
  - Outcome: What success looks like
  - Command: How to verify
  - Status: blocked/in-progress/complete

## Blockers
- Issue description
```

**When to use:** Daily stand-ups, progress tracking, task handoffs.

### `skills.md` — Skills Inventory
Comprehensive registry of:
- Installed skills (60+)
- Tools available
- Installation sources
- Usage patterns

**When to use:** Reference before implementing features. Run `Get-ChildItem .agents/skills -Directory` to discover skills.

## Installation Details

### Tools & Commands Installed

| Tool | Use | Status |
|------|-----|--------|
| `gsd` / `gsd-cli` | Get shit done CLI | Installed |
| `ccpm` | Context + task management | Installed (`.vendor/ccpm`) |
| `npx skills` | Skill discovery | Available |
| `memclaude` | Memory utility | Probe-based |

### Skill Sources & Attribution

**Installed From (60+ total skills):**

1. **Everything Claude Code** (56 skills)
   - Source: https://github.com/affaan-m/everything-claude-code
   - License: Refer to repository
   - Includes: Python, Django, Java, Spring Boot, Go, C++, Swift, DevOps, testing patterns

2. **Anthropic Skills** (3 skills + sub-packages)
   - `frontend-design` — https://github.com/anthropics/skills (Design & UI)
   - `mcp-builder` — MCP server building
   - Included in everything-claude-code distribution

3. **Vercel Labs**
   - `web-design-guidelines` — https://github.com/vercel-labs/agent-skills
   - Web interface best practices

4. **UI/UX Pro Max**
   - `ui-ux-pro-max-skill` — https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
   - Professional UI/UX patterns and systems

5. **Marketing Skills**
   - `marketingskills` — @coreyhaines31/marketingskills
   - Marketing automation patterns

6. **Antigravity Awesome Skills**
   - https://github.com/sickn33/antigravity-awesome-skills
   - Community curated skills pack

7. **Impeccable**
  - https://github.com/pbakaus/impeccable
  - Frontend quality vocabulary, commands, and anti-pattern guidance

### Tools Attribution

- **browser-use** — https://github.com/browser-use/browser-use
  - Browser automation and interaction
  - License: See repository

- **claude-mem** — https://github.com/thedotmack/claude-mem
  - Claude memory management utility
  - License: See repository

- **ccpm** — Context and task project management
  - Included in `.vendor/ccpm`

- **everything-claude-code** — https://github.com/affaan-m/everything-claude-code
  - Comprehensive Claude Code extensions, skills, and commands
  - License: Refer to repository

### Framework Attribution

This template is built on the **ai-agent-foundation** principle originated by:
- **MMEHDI0606** — Base template structure: https://github.com/MMEHDI0606/ai-agent-foundation-template
- **Curated & Enhanced** with 60+ skills and organized tooling

## Customization

### Add New Skills

**Option 1: Clone from GitHub**
```powershell
cd .agents/skills
git clone https://github.com/user/skill-name.git
```

**Option 2: Use skillkit**
```powershell
npx -y skillkit install user/skill-name
```

**Option 3: Install from everything-claude-code**
Reference `.vendor/everything-claude-code/skills` and copy desired skills.

### Add New Tools

```powershell
cd .tools
git clone https://github.com/user/tool-repo.git
```

### Configure Sub-Agents

Edit `.claude/config.md` to define sub-agent roles (Architect, Reviewer, Coder):
```yaml
## Architect
- Role: Design decisions, pattern selection
- Constraints: No implementation, only design review
- Invocation: `/architect` or automatic on large features

## Reviewer
- Role: Code review, quality gates
- Constraints: Read-only, feedback-only
- Invocation: `/review before merge
```

### Customize Planning Template

Edit `.planning/README.md` to align with your workflow:
- Daily stand-ups
- Sprint structure
- Decision records
- Dependency tracking

## Bootstrap Troubleshooting

### Command Not Found: `gsd`

Windows PATH may not be updated. Verify:
```powershell
Get-Command gsd-cli
```

If found, alias it:
```powershell
Set-Alias -Name gsd -Value gsd-cli -Scope CurrentUser
```

### Skills Not Discoverable

Verify skills folder exists:
```powershell
Test-Path .agents/skills
Get-ChildItem .agents/skills -Directory
```

Install manually if needed:
```powershell
npx -y antigravity-awesome-skills --path .agents/skills
```

### Mono-repo Support

For multi-project setups:
```powershell
# Sync from template into new repo
powershell -ExecutionPolicy Bypass -File scripts/sync-from-nexus.ps1 -TargetPath C:\path\to\new-repo
```

## Workflow Example

### Initialize New Agent Project

```powershell
# 1. Clone template
git clone <this-repo> my-agent
cd my-agent

# 2. Bootstrap
./scripts/bootstrap-agent-foundation.ps1

# 3. Plan your first task
# Edit .planning/current.md and add your task

# 4. Reference skills
# Browse .agents/skills to find relevant patterns
Get-ChildItem .agents/skills -Directory | Select-Object Name

# 5. Use skills in implementation
# Load them in Claude Code via `/skills python-patterns` or similar

# 6. Track progress
# Update .planning/current.md as work progresses
```

## Architecture Layers

This template organizes AI agents into discrete layers:

1. **Ingest** — Camera/video/frame adapters
2. **Detect** — Object + behavior inference
3. **Reason** — Policy thresholds and confidence gating
4. **Alert** — Escalation rules and notification fan-out
5. **Audit** — Event timeline, explainability, retention controls

See `claude.md` for full architecture directives.

## License & Attribution

**Template & Organization:** Built on `ai-agent-foundation-template` by MMEHDI0606

**Skills & Tools:** Licensed under respective repositories (see links above)
- Everything Claude Code: https://github.com/affaan-m/everything-claude-code
- Anthropic Skills: https://github.com/anthropics/skills
- Vercel Labs: https://github.com/vercel-labs/agent-skills
- And others listed in [Installation Details](#installation-details)

**Use & Modification:** Freely use for personal and commercial projects. Respect individual repository licenses.

## Contributing

To contribute improvements:
1. Fork this template
2. Make enhancements (new skills, docs, automation)
3. Submit a pull request
4. Ensure `.planning/current.md` documents your changes

## Support

- **Issue Tracker:** GitHub Issues ([report here](../../issues))
- **Documentation:** See `.planning/README.md` and `claude.md`
- **Skills Help:** Check individual skill `SKILL.md` files in `.agents/skills/`

## Next Steps

1. ✅ Clone template
2. ✅ Run bootstrap
3. ⬜ Edit `.planning/current.md` with your first task
4. ⬜ Browse `.agents/skills/` for relevant patterns
5. ⬜ Start implementing with skill guidance
6. ⬜ Document decisions in `claude.md`

---

**Built with 60+ curated skills • Organized for team collaboration • Ready for production**
