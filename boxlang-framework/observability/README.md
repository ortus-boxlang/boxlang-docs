---
description: >-
  How to see what your BoxLang applications, servers and AI agents are doing,
  with BxLens, BxMCP, logging and the debugger.
icon: eye
---

# Observability

Observability answers one question: **what is my application doing right now, and why?** BoxLang gives you several tools for it. Some are built into the runtime, and some are modules you add. This section helps you pick the right one and shows how to get started.

{% embed url="https://www.youtube.com/watch?v=m0MAC_JetTk" %}

## 🧭 Pick your tool

| I want to... | Use | Cost |
| --- | --- | --- |
| See what one request did, step by step | [BxLens](bxlens.md) debug bar | Free |
| Find slow queries, repeated queries and slow outgoing calls | [BxLens](bxlens.md) bar and console | Free, with limits |
| Work failures as issues: group, resolve, ignore, add notes | [BxLens](bxlens.md) Errors page | Free in memory, saved to disk with BoxLang+ |
| Watch the JVM, threads, disks, caches and scheduled tasks of a server | [BxLens](bxlens.md) console | Free for one server |
| Be alerted by email, Slack, Teams or Telegram | [BxLens](bxlens.md) alerts and reports | BoxLang+ |
| Watch many servers from one place | [BxLens](bxlens.md) fleet view | BoxLang+ |
| See what your AI agents do and what they cost | [AI and MCP observability](ai-and-mcp.md) | BoxLang+ |
| Keep an audit trail of an agent you build | [BoxLang AI governance](../../boxlang-ai/governance-and-security.md) middleware | Included with BoxLang AI |
| Let an AI assistant inspect and operate a live runtime | [BxMCP](../modularity/bx-mcp/README.md) | Free, needs `bx-ai` |
| Write application and runtime logs | [Logging](../logging.md) | Core |
| Step through code | [BoxLang Debugger](../../getting-started/ide-tooling/boxlang-debugger/README.md) | Core |
| Time a block of code | [Timer component](../../boxlang-language/reference/components/debug/Timer.md) | Core |

## 🔭 What you can observe

{% columns %}
{% column %}

### Your application

* Every request, with a waterfall of templates, queries and HTTP calls
* Errors grouped into issues that you can work through
* Slow and repeated queries, including ORM SQL
* Outgoing HTTP calls by host and endpoint
* Mail your application builds and sends
* ColdBox events, views, modules and schedulers

{% endcolumn %}

{% column %}

### Your servers and agents

* The JVM: heap, garbage collection, threads and deadlocks
* Executors, scheduled tasks, datasources and caches
* Disks, CPU and memory, with the share that belongs to BoxLang
* Every server that shares a store folder
* AI agent runs, model calls, tool calls and MCP servers, with cost

{% endcolumn %}
{% endcolumns %}

## 🚀 Get started

{% stepper %}
{% step %}

### Install BxLens

```bash
# BoxLang binary
install-bx-module bx-lens

# CommandBox
box install bx-lens
```

{% endstep %}

{% step %}

### Turn on the bar and the console

BxLens ships with everything off. Enable each surface in `boxlang.json`. The [BxLens page](bxlens.md) shows the settings.

{% endstep %}

{% step %}

### Open your app

Load a page from the same machine to see the bar. Open `/~bxlens/index.bxm` for the console.

{% endstep %}

{% step %}

### Add the agents

If you build with BoxLang AI, turn on the AI page of the console. If you want an AI assistant to inspect the runtime, install [BxMCP](../modularity/bx-mcp/README.md). See [AI and MCP observability](ai-and-mcp.md).

{% endstep %}
{% endstepper %}

## 📚 In this section

{% content-ref url="bxlens.md" %}
[bxlens.md](bxlens.md)
{% endcontent-ref %}

{% content-ref url="ai-and-mcp.md" %}
[ai-and-mcp.md](ai-and-mcp.md)
{% endcontent-ref %}

{% content-ref url="gallery.md" %}
[gallery.md](gallery.md)
{% endcontent-ref %}

## 🔗 Related

{% content-ref url="../logging.md" %}
[logging.md](../logging.md)
{% endcontent-ref %}

{% content-ref url="../modularity/bx-mcp/README.md" %}
[README.md](../modularity/bx-mcp/README.md)
{% endcontent-ref %}
