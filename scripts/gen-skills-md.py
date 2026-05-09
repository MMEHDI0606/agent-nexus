import os

skills_file = r'c:\Users\hkals\agent-nexus\skills-list.tmp.txt'
output_file = r'c:\Users\hkals\agent-nexus\skills.md'

with open(skills_file, 'r', encoding='utf-8-sig') as f:
    skills = [s.strip() for s in f.readlines() if s.strip()]

count = len(skills)

lines = [
    '# Skills Registry',
    '',
    f'**Status:** {count} skills installed',
    '',
    '## Folder Structure',
    f'- `.agents/skills/` \u2014 **{count} installed skills**',
    '- `.tools/` \u2014 Runtime tools and utilities',
    '- `.vendor/reference/` \u2014 Template references',
    '- `.vendor/` \u2014 Infrastructure dependencies',
    '',
    '## Local Skill Loader',
    '- Script: `skills.sh`',
    '- Bootstrap Windows: `scripts/bootstrap-agent-foundation.ps1`',
    '- Runtime: `npx skills@latest`',
    '- Command: `bash ./skills.sh`',
    '',
    f'## Installed Skills (`.agents/skills/`) \u2014 {count} total',
    '',
]

for s in skills:
    lines.append(f'- {s}')

lines += [
    '',
    '## Installed Tools (`.tools/`)',
    '- `browser-use` \u2014 Browser automation and interaction toolkit',
    '- `claude-mem` \u2014 Claude memory management utility',
    '',
    '## Infrastructure (`.vendor/`)',
    '- `ccpm` \u2014 Context/task management',
    '- `everything-claude-code` \u2014 Source repository',
    '',
    '## Action Contract',
    '- Discover skills: `Get-ChildItem .agents/skills -Directory`',
    '- Add skills to `.agents/skills/` via `git clone` or `npx skillkit`',
    '- Keep this file synchronized with skill inventory changes',
]

with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')

print(f'Done. {count} skills, {len(lines)} lines written.')
