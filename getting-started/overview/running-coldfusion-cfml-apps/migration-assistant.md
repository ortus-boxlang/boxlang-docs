---
description: A free desktop app that checks, audits and runs your Adobe ColdFusion or Lucee app on BoxLang, then builds your migration plan.
icon: wand-magic-sparkles
---

# BoxLang Migration Assistant

The **BoxLang Migration Assistant** is the easy button for moving an Adobe ColdFusion or Lucee application to BoxLang. Point it at your app folder and it walks you through every step: a compile check, a compatibility audit, server settings, the files to run on BoxLang, a test run with CommandBox, and a migration plan your team can import into Jira or GitHub.

Everything runs on your machine. Your code is never uploaded, and nothing is committed for you.

{% embed url="https://www.youtube.com/watch?v=TiwY0SmuKIA" %}
BoxLang Migration Assistant
{% endembed %}

## 📦 Download

Get it for macOS (Apple Silicon), Windows (x64 and ARM) and Linux (x64 and ARM: `.deb`, `.rpm` and AppImage):

{% embed url="https://downloads.ortussolutions.com/#/ortussolutions/boxlang-migration-assistant/" %}

The app ships with its own Java runtime and BoxLang server. You do not need Java or BoxLang installed.

| You need | Why |
|---|---|
| [CommandBox](https://www.ortussolutions.com/products/commandbox#download) | To start your app on BoxLang in the Test app step. The assistant shows you how to install it. |
| Git (optional) | To write the generated files to a new branch. |
| A CFConfig export (recommended) | So your datasources, mail servers and mappings come along. The assistant shows you how to export it. |

## 🚀 The Steps

{% stepper %}
{% step %}
### Choose your app

Pick your app folder. The assistant detects the engine from `server.json` (for example `adobe@2023` or `lucee@5`), counts your source files, and finds git, `box.json` and any CFConfig file.
{% endstep %}

{% step %}
### Compile check

Every `.cfm` and `.cfc` file is parsed with the real BoxLang compiler, the same check as [`boxlang check`](../../ide-tooling/boxlang-syntax-check.md). Files that do not compile are listed with the line, the code around it, and a fix prompt for your own LLM.
{% endstep %}

{% step %}
### Compatibility audit

The [CFML Feature Audit](../../ide-tooling/cfml-feature-audit.md) runs across your whole app. You get a compatibility score, the modules your app needs (BoxLang+ modules are marked), and every feature with no BoxLang equivalent, with its files and lines.
{% endstep %}

{% step %}
### Server settings

If your app has a CFConfig file, the assistant points CommandBox at it. If not, it shows how to export one from your current server, or offers a starter `.boxlang.json`.
{% endstep %}

{% step %}
### Generate files

Preview, then write, the files to run on BoxLang: `server.json` with the right modules, `box.json`, `MIGRATION.md`, `AGENTS.md` and the BoxLang migration [skills](../../agentic-development/skills-and-guidelines.md) for your AI coding agent. Write them to a new git branch, your app folder or a separate copy. Existing files are merged and backed up.
{% endstep %}

{% step %}
### CommandBox check and test

The assistant checks that CommandBox is installed, starts your app on BoxLang with one click, and tells you when it answers. The server is stopped when you are done or close the app.
{% endstep %}

{% step %}
### Your migration plan

The report turns the results into work:

* A **migration checklist** with a status, steps, acceptance criteria and an effort size for every item.
* **Tickets**: a Jira CSV (one Epic, one Task per open item) and GitHub issues, with an optional `gh` script.
* **One AI prompt** that has your LLM read `AGENTS.md` and the skills, then fix the open items in order.
* A **management report** you can save as a PDF. It leaves out file paths by default.
{% endstep %}
{% endstepper %}

## 💡 Licensing

The report also shows what it takes to run your app on BoxLang. The BoxLang core is free and open source (Apache 2.0). BoxLang+ is not priced by CPU cores, RAM, nodes or traffic, dev machines never count, and every BoxLang+ module includes a 60 day free trial. Estimate your cost with the [BoxLang calculator](https://calculator.boxlang.io) and see the [plans](https://www.boxlang.io/plans).

{% hint style="info" %}
Prefer the command line? The assistant uses the same tools you can run yourself: [`boxlang check`](../../ide-tooling/boxlang-syntax-check.md), the [CFML Feature Audit](../../ide-tooling/cfml-feature-audit.md) and the [CFML Transpiler](../../ide-tooling/cfml-to-boxlang-transpiler.md) (the assistant runs the first two; the transpiler is for when you want to convert code to BoxLang syntax). The rest of [Running ColdFusion/CFML Apps](README.md) walks through them by hand.
{% endhint %}
