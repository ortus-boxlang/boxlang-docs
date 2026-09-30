---
description: >-
  Browse skills.boxlang.io and install BoxLang agent skills for core
  development, modules, CommandBox, and more so your AI agent writes idiomatic
  code.
icon: book-sparkles
---

# Skills & Guidelines

**Skills** are step-by-step playbooks stored in a `SKILL.md` file. An agent sees a catalog of skill names and descriptions and reads a skill only when the task calls for it. This keeps the agent's base context small while deep knowledge stays one file read away.

**Guidelines** describe your project's conventions, such as architecture, style, and commands. They usually live in `AGENTS.md`. See [AI Setup](ai-setup.md).

## 🌐 skills.boxlang.io

{% embed url="https://skills.boxlang.io" %}

**[skills.boxlang.io](https://skills.boxlang.io)** is the BoxLang Skills Hub, the online directory of skills for BoxLang, ColdBox, TestBox, CommandBox, and the wider Ortus ecosystem. Browse and search it to find the skill your agent needs, then install it with one command.

The directory is built from the skill repositories we maintain:

| Repository | Contents |
| --- | --- |
| [`ortus-boxlang/skills`](https://github.com/ortus-boxlang/skills) | BoxLang developer skills, core development skills, module skills, and CommandBox skills |
| [`ortus-solutions/skills`](https://github.com/Ortus-Solutions/skills) | Ortus standards and engineering skills such as code review, documentation, and Java |

## ⚡ Get Started in One Command

Install **every BoxLang skill** into your project:

```bash
npx skills add ortus-boxlang/skills
```

For most application developers, we recommend starting with the complete **BoxLang developer** set:

```bash
npx skills add ortus-boxlang/skills/boxlang-developer
```

This gives your agent skills for language fundamentals, classes and OOP, functional programming, `Application.bx`, web development, database access, caching, async, scheduled tasks, file handling, Java integration, testing, security, configuration, deployment and runtime targets, CFML migration, and syntax checking.

{% hint style="info" %}
The `skills` CLI runs through `npx`, so you only need [Node.js](https://nodejs.org). It detects the agents you use, such as Claude Code, Cursor, and GitHub Copilot, and places the skills where each agent expects them.
{% endhint %}

## 🗂️ Categories

| Category | Best for | Install |
| --- | --- | --- |
| **BoxLang Developer** | Building applications with BoxLang | `npx skills add ortus-boxlang/skills/boxlang-developer` |
| **BoxLang Core Development** | Extending the runtime: BIFs, components, interceptors, modules | `npx skills add ortus-boxlang/skills/boxlang-core-development` |
| **BoxLang Modules** | Using specific modules such as `bx-ai`, `bx-pdf`, `bx-orm`, and `bx-compat-cfml` | `npx skills add ortus-boxlang/skills/boxlang-modules` |
| **CommandBox** | The CLI, package manager, embedded server, and task runners | `npx skills add ortus-boxlang/skills/commandbox` |

### BoxLang Developer

Skills for writing BoxLang applications, including:

* Language: fundamentals, classes and OOP, functional programming, best practices
* Web: web development, templating, `Application.bx`, security
* Data: database access, caching, file handling, zip
* Async: async programming, scheduled tasks, file watchers
* Platform: Java integration, configuration, modules and packages, testing
* Deployment: runtime skills for MiniServer, CommandBox, Docker, AWS Lambda, Azure Functions, Google Cloud Functions, Spring Boot, and more
* Migration: CFML to BoxLang
* Validation: `boxlang check` syntax checking, see [Validate Your Code](validate-your-code.md)

### BoxLang Core Development

Skills for extending BoxLang itself: async tasks, BIF development, component development, interceptors, logging, module development, and runtime architecture.

```bash
npx skills add ortus-boxlang/skills/boxlang-core-development
```

### BoxLang Modules

Module-specific skills teach your agent how to use a module correctly. Install only the ones your application uses. Larger modules, such as `bx-ai` and `bx-orm`, ship several focused skills.

```bash
npx skills add ortus-boxlang/skills/boxlang-modules/bx-ai
npx skills add ortus-boxlang/skills/boxlang-modules/bx-orm
npx skills add ortus-boxlang/skills/boxlang-modules/bx-compat-cfml
```

Available module skills include `bx-ai`, `bx-charts`, `bx-compat-cfml`, `bx-csrf`, `bx-docbox`, `bx-esapi`, `bx-ftp`, `bx-image`, `bx-ini`, `bx-jdbc`, `bx-jsoup`, `bx-jython`, `bx-mail`, `bx-markdown`, `bx-orm`, `bx-oshi`, `bx-password-encrypt`, `bx-pdf`, `bx-rss`, `bx-ui-forms`, `bx-unsafe-evaluate`, `bx-web-support`, and `bx-yaml`. Browse [skills.boxlang.io](https://skills.boxlang.io) for the current list.

### CommandBox

Skills for setup, usage, package management, the embedded server, task runners, developing commands, configuration, deploying, and testing with CommandBox.

```bash
npx skills add ortus-boxlang/skills/commandbox
npx skills add ortus-boxlang/skills/commandbox/commandbox-embedded-server
```

## 🎯 Install Individual Skills

Add a single skill by its path:

```bash
# BoxLang developer
npx skills add ortus-boxlang/skills/boxlang-developer/language-fundamentals
npx skills add ortus-boxlang/skills/boxlang-developer/web-development
npx skills add ortus-boxlang/skills/boxlang-developer/database-access
npx skills add ortus-boxlang/skills/boxlang-developer/testing
npx skills add ortus-boxlang/skills/boxlang-developer/syntax-check

# Core development
npx skills add ortus-boxlang/skills/boxlang-core-development/module-development
npx skills add ortus-boxlang/skills/boxlang-core-development/bif-development

# CommandBox
npx skills add ortus-boxlang/skills/commandbox/commandbox-package-management
```

## 🔧 Manage Skills

```bash
npx skills list              # list installed skills
npx skills find boxlang      # search for skills
npx skills update            # update to the latest versions
npx skills remove <name>     # remove a skill
```

## 🔌 Plugin and Marketplace Installs

**Claude Code plugin:**

```bash
/plugin marketplace add ortus-boxlang/skills
/plugin install boxlang-agent-skills@boxlang-agent-skills
```

**Cursor:** add `ortus-boxlang/skills` from Cursor's Marketplace settings. The repository ships a Cursor plugin manifest.

## 🧱 Install With the ColdBox CLI

Building a ColdBox application? The ColdBox CLI reads your `box.json`, installs skills based on your stack, and manages them for you:

```bash
box install coldbox-cli
coldbox ai install
coldbox ai skills list
coldbox ai skills add <owner>/skills/<skill-name>
```

Skills are installed to `.agents/skills/` in your project. See the [ColdBox Skills & Guidelines](https://coldbox.ortusbooks.com/getting-started/agentic-development/skills-and-guidelines) documentation.

## 🧭 Make the Agent Use Them

Installing a skill is not enough. Tell the agent when to read them in your `AGENTS.md`:

```markdown
## Skills

Before working in an area, read the matching skill in `.agents/skills/`.
Always read the best practices skill before writing new code.
After every edit, validate syntax with `boxlang check`.
```

## ✍️ Write Your Own

Capture your team's conventions as a skill:

```bash
npx skills init my-team-conventions
```

Edit the generated `SKILL.md`, then share it from a repository. Contributions to `ortus-boxlang/skills` are welcome.

{% hint style="info" %}
The [BoxLang AI](https://ai.ortusbooks.com) module also has its own skill support for agents that run inside your application. That is different from the coding-agent skills on this page.
{% endhint %}

{% hint style="warning" %}
Skills are instructions your agent will follow. Review a skill before installing it, especially from sources you do not know.
{% endhint %}
