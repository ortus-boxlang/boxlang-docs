---
description: Install BxLens, enable the bar and the console, and see your first page.
icon: rocket
---

# Getting started

## 📋 Requirements

* BoxLang 1.19 or newer
* Java 21
* A BoxLang web runtime: MiniServer, a servlet container or CommandBox

## 📦 Install

```bash
# BoxLang binary
bx-module install bx-lens

# CommandBox
box install bx-lens
```

## ⚙️ Enable

BxLens ships with everything off. It has two surfaces, and you turn each one on by itself in `boxlang.json`, under `modules.bxLens.settings`.

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
          "password": "bxsecret:..."
        }
      }
    }
  }
}
```

The console lives at `/~bxlens/index.bxm` and needs a password. A plain password works for a quick try, and `"${env.BXLENS_PASSWORD}"` reads it from an environment variable. To make an encrypted value, use BoxLang:

```bash
boxlang generatesecret "a long random password"
```

Paste the whole output into `console.password`.

{% endtab %}
{% endtabs %}

Restart the runtime. Every other setting has a default.

{% hint style="warning" %}
The bar is a development tool. The console can run on a live server, but only with a password, an access list and HTTPS. Read the [production guide](https://bxlens.boxlang.io/guides/production/) before real users can reach it.
{% endhint %}

## 👀 See the bar

Create a page and load it from the same machine.

```html
<bx:output>
  <h1>Hello Lens</h1>
</bx:output>
```

A health strip appears at the bottom of the page. Click it to open the panel. Add a message and a timer from your code:

```js
lensMessage( "Page loaded", "info" )

users = lensMeasure( "load users", () => {
  return queryExecute( "SELECT 1 AS id" )
} )
```

See the [built-in functions](built-in-functions.md) for all of them.

## 🖥️ Open the console

With the console on, open `/~bxlens/index.bxm` on your server, for example `http://localhost:8085/~bxlens/index.bxm`, and sign in. On the free tier or a trial, the first visit shows a one time registration page. See [Licensing and registration](licensing-and-registration.md).

## ➡️ Next steps

* [Licensing and registration](licensing-and-registration.md)
* [Observability overview](../../../observability/README.md)
* The full docs: [bxlens.boxlang.io](https://bxlens.boxlang.io)
