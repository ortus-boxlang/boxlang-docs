---
description: >-
  Two ways to build a web application on BoxLang - a raw MiniServer app, or a
  full framework starter built for building with an AI agent.
icon: window
---

# Web Applications

The BoxLang core runtime doesn't know anything about HTTP - "web" is a layer on top, provided by the [MiniServer](miniserver.md) or a servlet server like [CommandBox](commandbox.md). What you put on top of *that* layer is up to you, and it depends on what you're building.

## 🧭 Which path should I take?

<table><thead><tr><th width="220">You're building...</th><th>Use</th></tr></thead><tbody>
<tr><td>A single page, a small API, a prototype, or an embedded UI</td><td>Raw BoxLang (<code>.bxm</code>/<code>.bx</code>) on the <a href="miniserver.md">MiniServer</a> - no framework, nothing to learn first</td></tr>
<tr><td>A real application - routing, auth, an ORM, an admin panel, a team behind it</td><td><a href="https://coldbox.ortusbooks.com">ColdBox</a>, BoxLang's flagship HMVC framework, started from <a href="https://cbgenesis.coldbox.org">cbGenesis</a></td></tr>
</tbody></table>

## 🪶 Path 1: Raw BoxLang on the MiniServer

For something small, you don't need a framework at all. Drop an `index.bxm` in a folder and start the [MiniServer](miniserver.md):

```bash
cd mySite
boxlang-miniserver
```

Enable [URL rewrites](miniserver.md#url-rewrites) if you want clean URLs, and route requests yourself out of `index.bxm`. That's the whole framework. It's the right amount of structure for a script, a webhook receiver, or a page that will never grow past a few routes.

## 🏗️ Path 2: ColdBox, started from cbGenesis

Once an app has more than a couple of routes, its own auth, or more than one person working on it, hand-rolling routing and conventions stops paying off. [ColdBox](https://coldbox.ortusbooks.com) is BoxLang's HMVC framework for that case - handlers, routing, dependency injection, interceptors, and a convention for where everything lives.

You *can* start a ColdBox app from a bare skeleton. The fastest way, though - especially with an AI agent doing some of the building - is [**cbGenesis**](https://cbgenesis.coldbox.org), a production-ready ColdBox starter template that ships a working app, not a blank one:

* Session auth, SSO, and WebAuthn passkeys
* A `resource:action` role-based permission model enforced via `@secured` handler annotations
* CSRF protection that's deny-by-default on every state-changing request
* An admin panel (users, roles, permissions, audit log, settings) built on Alpine.js + Bootstrap
* A real TestBox suite and a Docker Compose stack for local dev

```bash
install-bx-module bx-cli

coldbox create app skeleton=cbgenesis
box install
box migrate up
box migrate seed run
box server start
```

Ten minutes later you have a login screen, not a to-do list of security features you still need to build.

{% hint style="success" %}
**This is the fastest way to build a BoxLang web application with an AI agent at hand.** cbGenesis ships an `AGENTS.md`, the full [BoxLang skills](../agentic-development/skills-and-guidelines.md) ecosystem, and six project-specific skills describing its own permission model, CSRF contract, and CRUD conventions - so an agent builds on real patterns from its first prompt instead of exploring a mostly-empty repo. In one measured run, an agent using those skills needed 42% fewer tool calls and 34% less time than one given the same task with no skills to read. See [Agentic Development](../agentic-development/README.md) for what makes a BoxLang project agent-ready in general, and [cbGenesis's own docs](https://cbgenesis.coldbox.org/ai-native) for the full methodology behind that number.
{% endhint %}

## Where to go next

{% content-ref url="miniserver.md" %}
[miniserver.md](miniserver.md)
{% endcontent-ref %}

{% content-ref url="commandbox.md" %}
[commandbox.md](commandbox.md)
{% endcontent-ref %}

{% content-ref url="../agentic-development/README.md" %}
[README.md](../agentic-development/README.md)
{% endcontent-ref %}
