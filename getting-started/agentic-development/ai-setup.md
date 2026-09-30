---
description: >-
  Set up a BoxLang project for AI coding agents with AGENTS.md, skills, and
  documentation MCP servers.
icon: wand-magic-sparkles
---

# AI Setup

Three pieces make a BoxLang project agent-ready: a project guide, skills, and documentation MCP servers.

## 📄 Project Guide: AGENTS.md

`AGENTS.md` is a plain markdown file at the root of your project that tells an agent how your project works. Many agents read it automatically. Some tools use their own file name, such as `CLAUDE.md`, which can simply reference `AGENTS.md`.

Keep it short and specific. Good things to include:

* What the project is and how to run it
* How to run tests
* Code style rules, for example semicolon usage and spacing
* Where to find skills, and when the agent must read them

Example:

```markdown
# Project Guide

## Overview

An orders API built on BoxLang and ColdBox.

## Commands

- Start the server: `box server start`
- Validate syntax: `boxlang check --source ./src`
- Run tests: `./testbox/run --directory=tests/specs`

## Code Standards

- BoxLang only. Use `.bx` files.
- No semicolons on normal statements.
- Spaces inside parentheses: `foo( bar )`.

## Skills

Before working in an area, read the matching skill in `.agents/skills/`.
```

## 🧠 Skills

Skills live in `.agents/skills/<skill-name>/SKILL.md`. Agents that only look in tool-specific folders can read a symlink, for example `.claude/skills` pointing at `.agents/skills`.

```bash
cd .claude/skills
ln -s ../../.agents/skills/<skill-name> <skill-name>
```

Browse [skills.boxlang.io](https://skills.boxlang.io) and install the BoxLang developer set with:

```bash
npx skills add ortus-boxlang/skills/boxlang-developer
```

See [Skills & Guidelines](skills-and-guidelines.md) for categories and individual skills.

## 📚 Docs MCP Servers

Every Ortus documentation site is published as a Model Context Protocol server. Add the ones you use to your agent's MCP configuration so it can search and read current documentation.

| Server | URL |
| --- | --- |
| BoxLang | `https://boxlang.ortusbooks.com/~gitbook/mcp` |
| BoxLang AI | `https://ai.ortusbooks.com/~gitbook/mcp` |
| ColdBox | `https://coldbox.ortusbooks.com/~gitbook/mcp` |
| TestBox | `https://testbox.ortusbooks.com/~gitbook/mcp` |
| WireBox | `https://wirebox.ortusbooks.com/~gitbook/mcp` |
| CacheBox | `https://cachebox.ortusbooks.com/~gitbook/mcp` |
| LogBox | `https://logbox.ortusbooks.com/~gitbook/mcp` |
| CommandBox | `https://commandbox.ortusbooks.com/~gitbook/mcp` |

Example `.mcp.json` for an agent that supports HTTP MCP servers:

```json
{
  "mcpServers": {
    "boxlang-docs": {
      "type": "http",
      "url": "https://boxlang.ortusbooks.com/~gitbook/mcp"
    },
    "boxlang-ai-docs": {
      "type": "http",
      "url": "https://ai.ortusbooks.com/~gitbook/mcp"
    }
  }
}
```

{% hint style="info" %}
The configuration file name and shape differ between agents. Check your agent's documentation for where MCP servers are declared.
{% endhint %}

## 🧱 Building a Web App With ColdBox

If you are building a ColdBox application, the ColdBox CLI can generate all of the above for you, including guidelines, skills, agent files, and MCP servers:

```bash
coldbox ai install
```

See the [ColdBox agentic documentation](https://coldbox.ortusbooks.com/getting-started/agentic-development) for details.

## ✅ Verify

Ask your agent: "Which BoxLang skills are available in this project, and how do I run the tests?" It should answer from `AGENTS.md` and the skills catalog, not guess.
