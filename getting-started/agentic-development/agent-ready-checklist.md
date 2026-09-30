---
description: >-
  A checklist and prompt recipes for making a BoxLang project productive for AI
  agents.
icon: list-check
---

# Agent-Ready Checklist

Use this checklist to get a BoxLang project ready for an AI agent, then use the recipes to put it to work.

## ✅ Project Checklist

* [ ] `AGENTS.md` describes the project, commands, and code standards. See [AI Setup](ai-setup.md).
* [ ] Skills are installed in `.agents/skills/` and `AGENTS.md` says when to read them. See [Skills & Guidelines](skills-and-guidelines.md).
* [ ] Documentation MCP servers are configured in your agent. See [AI Setup](ai-setup.md#docs-mcp-servers).
* [ ] Tests run from one command and the command is in `AGENTS.md`.
* [ ] Configuration lives in `boxlang.json` and secrets come from environment variables, not source files.
* [ ] The [BoxLang IDE](boxlang-ide.md) is installed for language intelligence and debugging.
* [ ] For running servers, `bx-mcp` is installed with a read-only security profile. See [BoxLang MCP](boxlang-mcp.md).

## 💬 Prompt Recipes

Replace the bracketed parts with your own details.

**Build a feature**

```text
Read AGENTS.md and the boxlang-best-practices skill. Add [feature] to this project.
Write the tests first, then the implementation, then run the tests.
```

**Understand unfamiliar code**

```text
Explain how [file or feature] works. Use the BoxLang docs MCP server to check
any built-in functions or components you are not sure about.
```

**Modernize CFML**

```text
Read the boxlang-cfml-migration skill. Audit [directory] for CFML features that
need changes to run on BoxLang, list them, then propose a migration plan
before changing any code.
```

**Diagnose a slow server** (requires BoxLang+ `bx-mcp`)

```text
Use the BoxLang MCP server with the read-only profile. Check cache health,
datasource pools, and slow requests, then summarize the likely causes.
```

**Add AI to your application**

```text
Read the BoxLang AI docs via the MCP server. Add a chat endpoint that uses
[provider] and streams responses. Do not hard-code API keys.
```

## 🧪 Keep Agents Honest

* Ask for tests and run them. Do not accept "it should work".
* Have the agent cite the documentation page or skill it relied on.
* Review generated code the way you review a teammate's pull request.
* Use least privilege for anything an agent can reach, especially live runtime tools.
