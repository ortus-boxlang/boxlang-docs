---
description: >-
  What is free in BxLens, what needs BoxLang+, and how the one time registration
  and its trial work.
icon: badge-check
---

# Licensing and registration

BxLens is freeware with limits. You can use the free features without a subscription, including in production. The BoxLang+ features and the removal of the free limits need a BoxLang+ subscription or a trial. The exact terms are in the `LICENSE` file of the module.

{% hint style="info" %}
This page describes the current split and it may change. The full, current comparison is in the [licensing page of the BxLens docs](https://bxlens.boxlang.io/licensing/).
{% endhint %}

## 🆓 Free and ⭐ BoxLang+

| Area | Free | BoxLang+ or trial |
| --- | --- | --- |
| Debug bar, every tab | Yes | Adds cost per request |
| Console basics: requests, errors in memory, executors, tasks, datasources, caches, logs, JVM, system | Yes, one server | Yes |
| Requests kept in memory | Last 25 | As configured |
| Errors and reports | In memory | Saved to disk, longer trends |
| Task, cache and application actions, thread dumps, heap dumps | View only | Yes |
| Many servers in one console | No | Yes |
| Alerts and reports by email, Slack, Teams, Telegram or webhook | No | Yes |
| Lensy, the assistant | Copy a redacted prompt | Yes |
| AI observability | A few counters | Runs, traces, cost and MCP servers |

## 📝 Registration

The debug bar needs no registration. The **console** on the free tier or a trial needs a one time, free registration of the server, before the sign in. A server with an active BoxLang+ subscription needs none.

1. Open the console. A Register page asks for your name, work email and, optionally, your company.
2. Say where BxLens runs (a server or VM, or a container) and **what the server is used for**: development, testing, staging or production.
3. Agree to the [privacy notice](https://bxlens.boxlang.io/privacy/) and press **Register and email my key**.
4. Paste the key from the email and press **Activate**. You are not asked again for this server.

The form goes from the server to the registration service once. Nothing about your application is sent, and the key is checked offline afterwards. An air gapped server cannot register and should use BoxLang+.

A key belongs to a server name. In a container, choose a name for the service and set `LENS_SERVER_NAME` to it, so every replica shares one key.

## ⏱️ The 7 day trial

A registration for **development or testing** starts a **7 day trial** of the BoxLang+ features of BxLens. One trial belongs to one email address, and more development or testing servers of the same address share its end date. After the trial BxLens stays free and registered.

{% hint style="warning" %}
The trial is for development, testing and evaluation. A server registered for **staging or production** is registered on the free tier with no trial. Using a trial of the BoxLang+ features on a staging or production server breaches the BxLens license.
{% endhint %}

A trial license from `bx-plus` counts only for a registered server. For a development or testing registration, it is capped at the BxLens trial, even if the `bx-plus` trial has more days.

## 🔎 License states

BxLens detects BoxLang+ through the [`bx-plus`](../bx-plus/README.md) module. It makes no network call of its own for licensing.

| State | Console label | When |
| --- | --- | --- |
| Plus | `BoxLang+ active` | A valid license that is not a trial |
| Trial | `Trial`, with the days left | A registered development or testing server, or a valid trial license on a registered server |
| Expired | `License expired` | The license is present but not valid |
| Free | `Free` | `bx-plus` is not installed, or the check failed |

If `bx-plus` is missing or the license is not valid, BxLens reports Free and carries on. Nothing breaks.

For plans and trials, see [boxlang.io/plans](https://www.boxlang.io/plans).
