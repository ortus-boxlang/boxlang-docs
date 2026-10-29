---
icon: magnifying-glass-chart
description: >-
  BxLens is the debug bar and ops console for BoxLang. Trace requests, errors,
  queries, HTTP calls, mail and AI agents, and watch every server.
---

# BxLens

{% hint style="info" %}
BxLens is **freeware with limits**. The debug bar and the basics of the console are free for one server, in production too. [BoxLang+](../../README.md) lifts the limits and adds history, alerts, many servers and AI. It needs BoxLang 1.19 or newer and Java 21.
{% endhint %}

**BxLens** shows what your BoxLang application and servers are doing. It has two surfaces:

* **The bar** is a strip docked on every HTML page. It shows what that one request did: templates, queries, HTTP calls, exceptions, timers and scopes.
* **The console** is a password protected page for a server: live requests, errors grouped into issues, queries, datasources, caches, logs, tasks, the JVM and threads. With BoxLang+ it also reads every server in a store folder and sends alerts by email, Slack, Teams or Telegram.

Both surfaces are off until you turn them on. An assistant named **Lensy** answers questions about the server in plain words and asks for approval before it changes anything.

{% embed url="https://www.youtube.com/watch?v=m0MAC_JetTk" %}

## 📦 Installation

```bash
# BoxLang binary
install-bx-module bx-lens

# CommandBox
box install bx-lens
```

Then follow [Getting started](getting-started.md) to enable the bar and the console.

## ✨ Features

* A waterfall of templates, functions, queries and HTTP calls for every request
* Slow query and N+1 detection, including ORM SQL
* Errors grouped into issues that you resolve, ignore and annotate, with a stable reference
* Outgoing HTTP by host, with latency and failures
* The JVM: heap, garbage collection, threads and deadlocks
* Executors, scheduled tasks, datasources, caches and file watchers
* Mail viewer for `bx-mail`
* ColdBox events, views, modules and schedulers
* AI observability for BoxLang AI agents, models and MCP servers
* Alerts and reports, and a fleet view of many servers (BoxLang+)
* No external requests from the console, so it works on air gapped networks

## 📚 In these docs

| Page | What it covers |
| --- | --- |
| [Getting started](getting-started.md) | Install, enable and open BxLens |
| [Licensing and registration](licensing-and-registration.md) | What is free, what needs BoxLang+, and the registration trial |
| [Built-in functions](built-in-functions.md) | The `lens*` functions for your own code |
| [Observability](../../../observability/README.md) | How BxLens, BxMCP and the other tools fit together |

The complete BxLens documentation is at **[bxlens.boxlang.io](https://bxlens.boxlang.io)**.

{% content-ref url="../../../observability/bxlens.md" %}
[bxlens.md](../../../observability/bxlens.md)
{% endcontent-ref %}
