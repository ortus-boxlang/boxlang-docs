---
description: >-
  Install BoxLang agent skills so your AI agent follows idiomatic BoxLang
  patterns for the task at hand.
icon: book-sparkles
---

# Skills & Guidelines

**Skills** are step-by-step playbooks stored in a `SKILL.md` file. An agent sees a catalog of skill names and descriptions and reads a skill only when the task calls for it. This keeps the agent's base context small while deep knowledge stays one file read away.

**Guidelines** describe your project's conventions, such as architecture, style, and commands. They usually live in `AGENTS.md`.

## 📦 Where Skills Come From

BoxLang skills are maintained in these GitHub repositories:

| Repository | Contents |
| --- | --- |
| `ortus-boxlang/skills` | BoxLang language, runtime, deployment, and core development skills |
| `ortus-solutions/skills` | Ortus standards and general engineering skills such as code review, documentation, and Java |

Examples from `ortus-boxlang/skills`:

| Area | Example skills |
| --- | --- |
| Language | `boxlang-language-fundamentals`, `boxlang-classes-and-oop`, `boxlang-functional-programming`, `boxlang-best-practices` |
| Data and files | `boxlang-database-access`, `boxlang-file-handling`, `boxlang-caching`, `boxlang-zip` |
| Web | `boxlang-web-development`, `boxlang-templating`, `boxlang-application-descriptor`, `boxlang-security` |
| Async and scheduling | `boxlang-async-programming`, `boxlang-scheduled-tasks`, `boxlang-file-watchers` |
| Runtimes | `boxlang-runtime-miniserver`, `boxlang-runtime-docker`, `boxlang-runtime-aws-lambda`, `boxlang-runtime-commandbox` |
| Migration | `boxlang-cfml-migration` |
| Testing | `boxlang-testing` |
| Extending BoxLang | `boxlang-core-dev-bif-development`, `boxlang-core-dev-module-development`, `boxlang-core-dev-interceptors` |

## ⬇️ Install Skills

Skills are installed with the `skills` CLI from npm. List what a repository offers, then install what you need:

```bash
npx skills add ortus-boxlang/skills --list
npx skills add ortus-boxlang/skills --skill boxlang-testing
```

Install globally for all projects with `-g`:

```bash
npx skills add ortus-boxlang/skills -g
```

The BoxLang runtime repository tracks its skills in a `skills-lock.json` file and installs them all with one command:

```bash
npx skills experimental_install
```

Check the `skills` CLI help for lock file support in your version.

## 🧭 Make the Agent Use Them

Installing a skill is not enough. Tell the agent when to read it in your `AGENTS.md`:

```markdown
## Skills

Before working in an area, read the matching skill in `.agents/skills/`.
Always read `boxlang-best-practices` before writing new code.
```

## ✍️ Write Your Own

Capture your team's conventions as a skill:

```bash
npx skills init my-team-conventions
```

Edit the generated `SKILL.md`, then share it from a repository.

{% hint style="info" %}
The [BoxLang AI](https://ai.ortusbooks.com) module also has its own skill support for agents that run inside your application. That is different from the coding-agent skills on this page.
{% endhint %}

## 🧱 ColdBox Projects

ColdBox has its own skill and guideline manager built into `coldbox-cli`. See the [ColdBox Skills & Guidelines](https://coldbox.ortusbooks.com/getting-started/agentic-development/skills-and-guidelines) documentation.
