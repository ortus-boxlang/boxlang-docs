---
description: >-
  BxLens is the debug bar and ops console for BoxLang. See what a request did,
  what a server is doing, and hear about problems before your users do.
icon: magnifying-glass-chart
---

# BxLens

**BxLens** is the debug bar and ops console for BoxLang. It shows what your application and your servers are doing, from one request up to a whole group of servers.

{% hint style="info" %}
BxLens is freeware with limits. The debug bar and the basics of the console are free, for one server, in production too. [BoxLang+](../boxlang-plus/README.md) lifts the limits and adds history, alerts, many servers and AI. It needs BoxLang 1.19 or newer and Java 21.
{% endhint %}

## 🪟 Two surfaces

| Surface | What it is | Where |
| --- | --- | --- |
| **The bar** | A strip docked on every HTML page. It shows what that one request did: timeline, queries, HTTP calls, exceptions, timers and scopes. | On your own pages |
| **The console** | A password protected page for the server: requests, errors, queries, datasources, caches, logs, tasks, the JVM and threads. | `/~bxlens/index.bxm` |

Use the bar while you build, and open the console when you run it. Both are off by default.

## 🎯 What can I do with it?

| I want to... | Free | BoxLang+ adds |
| --- | --- | --- |
| See what one request did, step by step | Full waterfall of templates, queries, HTTP and transactions | Cost per request (CPU and memory) |
| Find slow queries and N+1 problems | Every statement of a request, the 10 heaviest across requests | Every statement across requests |
| Work errors as issues | Grouped issues in memory, with resolve, ignore and notes | Saved to disk, 7 and 30 day trends, all servers |
| See what is running right now | | Live stack of every running request |
| Watch outgoing HTTP calls | Last hour, by host and endpoint | 24 hours to 15 days |
| Check the JVM | Memory, garbage collection, deadlock detection | Thread dumps, heap dumps |
| See tasks, caches and datasources | View everything | Run, pause, evict and other actions |
| Debug a ColdBox application | Events, views, routes, modules and findings | Cache actions |
| Watch the mail your app sends | Counters and the last ten messages | Message viewer, delivery attempts, queue |
| Get a message when something breaks | | 17 alert rules by email, Slack, Teams, Telegram or webhook |
| Get a daily, weekly or monthly report | | Reports for every server |
| Watch more than one server | This server in full | The whole fleet in one table |
| See what AI agents do and cost | A few counters for the last hour | [Runs, traces, cost and MCP servers](ai-and-mcp.md) |
| Ask about the server in plain words | Copy a redacted prompt | Lensy, the assistant that asks before it acts |

## ⚙️ Enable it

BxLens ships with both surfaces off. Turn each on in `boxlang.json`, under `modules.bxLens.settings`.

{% tabs %}
{% tab title="The bar" %}

```json
{
  "modules": {
    "bxLens": {
      "settings": {
        "bar": { "enabled": true }
      }
    }
  }
}
```

The bar shows on HTML pages for callers on the same machine.

{% endtab %}

{% tab title="The console" %}

```json
{
  "modules": {
    "bxLens": {
      "settings": {
        "console": {
          "enabled": true,
          "password": "${env.BXLENS_PASSWORD}"
        }
      }
    }
  }
}
```

The console needs a password. Use an environment variable or an encrypted `bxsecret:` value. Restart the runtime, then open `/~bxlens/index.bxm`.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
The bar is a development tool. The console can run on a live server, but only with a password, an access list and HTTPS. Read the [security guide](https://bxlens.boxlang.io/security/) and the [production guide](https://bxlens.boxlang.io/guides/production/) before you open it to real users.
{% endhint %}

## 🔐 Registration and trial

The console on the free tier needs a one time, free registration of the server. The debug bar needs none, and neither does a server with an active BoxLang+ subscription. See [Licensing and registration](../boxlang-plus/modules/bx-lens/licensing-and-registration.md).

## 📸 See it

{% content-ref url="gallery.md" %}
[gallery.md](gallery.md)
{% endcontent-ref %}

## 📖 Full documentation

The complete BxLens documentation lives at **[bxlens.boxlang.io](https://bxlens.boxlang.io)**: every console page, every tab of the bar, configuration, security, production guides and walkthroughs.

{% content-ref url="../boxlang-plus/modules/bx-lens/README.md" %}
[README.md](../boxlang-plus/modules/bx-lens/README.md)
{% endcontent-ref %}
