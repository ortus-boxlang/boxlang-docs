---
description: >-
  Fluent browser automation and testing for BoxLang, powered by Microsoft
  Playwright: drive real browsers, test web apps and APIs, and render HTML to
  PDFs and images.
icon: browser
---

# Playwright

The `bx-playwright` module brings [Microsoft Playwright](https://playwright.dev) to BoxLang with a fluent, BoxLang native API. Drive Chromium, Firefox and WebKit, test web applications end to end, mock the network, test APIs, and render HTML to PDFs or images.

{% hint style="info" %}
This page is a summary. The complete documentation lives at **[bxplaywright.boxlang.io](https://bxplaywright.boxlang.io)**, also available as [llms.txt](https://bxplaywright.boxlang.io/llms.txt) for AI agents.
{% endhint %}

## ✨ Features

* **Fluent DSL** through the `playwright()` BIF: smart selectors, chainable actions, and web-first assertions that wait for the page
* **Two assertion styles**: inline (`assertSee()`, `assertPathIs()`) and `expect()` (`toHaveText()`, `toBeVisible()`)
* **Profiles** for browsers, screens, devices and modes (`mobile`, `dark`, `ci`, `debug`) plus your own in module settings
* **Rendering**: `bx:playwrightRender` and `render()` turn HTML into PDF, PNG, JPEG or WebP with a real browser
* **Network and APIs**: request interception and mocking, and `request()` for API testing
* **Quality checks**: visual regression with diff images, console errors, smoke tests, and axe-core accessibility checks
* **Page objects, components and macros** to keep tests readable
* **Built for AI agents**: accessibility snapshots with element refs, browser tools for [BoxLang AI](../../boxlang-ai/browser-agents.md) agents, and `help()` on every object
* **`bxPlaywright` CLI** with bash completions: install browsers, `doctor`, `codegen` that records BoxLang code, screenshots, PDFs and Playwright MCP

## 📦 Installation

Two distributions are published to ForgeBox:

| Module | Size | Node.js |
| --- | --- | --- |
| `bx-playwright` | Small (about 4 MB) | Uses a system Node.js 20+, or downloads one with `bxPlaywright install` |
| `bx-playwright-full` | Large (about 200 MB) | Bundled for every platform, works offline |

```bash
# BoxLang Installer Script
install-bx-module bx-playwright
# CommandBox
box install bx-playwright

# Download the browser (and Node.js when needed), then check the setup
bxPlaywright install chromium
bxPlaywright doctor
```

## ⚡ Quick Start

```js
playwright().browse( ( page ) => {
	page.visit( "https://example.com/login" )
		.fill( "Email", "luis@ortussolutions.com" )
		.fill( "Password", "secret" )
		.click( "Sign in" )
		.assertPathIs( "/dashboard" )
		.assertSee( "Welcome back" )
		.screenshot( "dashboard.png" )
} )
```

`browse()` starts the browser, runs your closure, and cleans everything up, even when an assertion fails. Selectors can be CSS, `@testId` (for `data-testid`), or the visible text or label a user sees, as in `fill( "Email" )` and `click( "Sign in" )`.

## 🎭 Profiles

```js
// A phone in dark mode
playwright( [ "android", "dark" ] ).browse( ( page ) => {
	page.visit( "https://example.com" ).screenshot( "mobile-dark.png" )
} )
```

Run `bxPlaywright profiles` to list them. Add your own under `modules.playwright.settings.profiles` in `boxlang.json`, or override settings with `BX_PLAYWRIGHT_*` environment variables.

## 🖨️ Rendering

```js
bx:playwrightRender type="pdf" path="invoice.pdf" format="A4" {
	writeOutput( "<h1>Invoice ##42</h1>" )
}

png = playwright().render( "<h1>Hello</h1>", { type : "png", viewport : { width : 1200, height : 630 } } )
```

## ✅ Testing and Quality

bx-playwright works in any test framework, including TestBox:

```js
it( "shows the dashboard", () => {
	playwright( "ci" ).browse( ( page ) => {
		page.visit( "http://localhost:8080/dashboard" )
			.assertTitle( "Dashboard" )
			.assertNoConsoleErrors()
			.assertNoAccessibilityIssues()
			.assertScreenshotMatches( "dashboard" )
	} )
} )
```

A failed `assertScreenshotMatches()` writes the actual image and a diff image with the changed pixels in red. The `ci` profile keeps screenshots, traces and videos of failed tests.

## 🤖 AI Agents

```js
// A compact, token-efficient view of the page with element refs
println( page.snapshot( options = { mode : "ai" } ) )
// - textbox "Email" [ref=e5]
// - button "Sign in" [ref=e7]
page.fill( "ref=e5", "luis@ortussolutions.com" ).click( "ref=e7" )
```

See [Browser Agents](../../boxlang-ai/browser-agents.md) to give a BoxLang AI agent a browser, and [Build an App End to End](../../getting-started/agentic-development/end-to-end-with-playwright.md) to let a coding agent verify the application it builds.

## 🔗 Resources

* Documentation: [bxplaywright.boxlang.io](https://bxplaywright.boxlang.io)
* Source: [github.com/ortus-boxlang/bx-playwright](https://github.com/ortus-boxlang/bx-playwright)
* Agent skills: `npx skills add ortus-boxlang/skills/boxlang-modules/bx-playwright`
