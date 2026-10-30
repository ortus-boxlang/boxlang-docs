---
description: MatchBox is the Rust runtime for BoxLang, shipping to native binaries, the browser, WASI, AWS Lambda and ESP32
icon: fire
---

# MatchBox

## What is MatchBox?

MatchBox is a **Rust implementation of the BoxLang runtime**. It sits alongside the JVM runtime as its Rust counterpart. BoxLang compiles to bytecode, and a Rust VM runs it. Core and native builds need no JVM.

{% hint style="success" %}
**All MatchBox documentation now lives at [matchbox.boxlang.io](https://matchbox.boxlang.io).** This page is a short introduction. Use the links below for guides, the CLI reference, examples, and the interactive tools.
{% endhint %}

{% columns %}
{% column %}
### 🎮 Playground

Write and run BoxLang in your browser. MatchBox is compiled to WebAssembly, and your code never leaves your device.

[Open the playground →](https://matchbox.boxlang.io/playground/)
{% endcolumn %}

{% column %}
### 🎓 Online Course

Ten lessons, from your first script to building and shipping a standalone binary.

[Start the course →](https://matchbox.boxlang.io/course/)
{% endcolumn %}
{% endcolumns %}

| Resource | Link |
| :--- | :--- |
| Documentation | [matchbox.boxlang.io/getting-started](https://matchbox.boxlang.io/getting-started/) |
| CLI reference | [matchbox.boxlang.io/reference/cli](https://matchbox.boxlang.io/reference/cli/) |
| Examples | [matchbox.boxlang.io/examples](https://matchbox.boxlang.io/examples/) |
| Source code | [github.com/ortus-boxlang/matchbox](https://github.com/ortus-boxlang/matchbox) |
| Docs source | [github.com/ortus-boxlang/matchbox-docs](https://github.com/ortus-boxlang/matchbox-docs) |

## Why MatchBox?

The JVM runtime brings the full Java ecosystem and broad module coverage. MatchBox targets the places a JVM does not fit.

* **Single binaries:** ship a CLI tool or service as one file, with a VM core of about 4.7 MB.
* **Browsers:** run BoxLang through WebAssembly and JavaScript, including Cloudflare Workers.
* **WASI containers:** run WebAssembly workloads outside the browser.
* **Serverless:** AWS Lambda support is in preview.
* **Microcontrollers:** run on ESP32 devices.

## Install

[MatchBox Version Manager (MVM)](https://github.com/ortus-boxlang/matchbox-quick-installer) installs and switches MatchBox versions.

{% tabs %}
{% tab title="Linux and macOS" %}
```bash
curl -fsSL https://raw.githubusercontent.com/ortus-boxlang/matchbox-quick-installer/main/install/install.sh | bash
```
{% endtab %}

{% tab title="Windows" %}
Use the `install.ps1` script from the [matchbox-quick-installer](https://github.com/ortus-boxlang/matchbox-quick-installer) repository in PowerShell.
{% endtab %}
{% endtabs %}

Then install and activate MatchBox:

```bash
mvm install latest
mvm use latest
matchbox --version
```

If `matchbox` is not found, run `mvm doctor`.

## Use

Run a script:

```bash
matchbox hello.bxs
```

Build a standalone native executable:

```bash
matchbox --target native hello.bxs
```

The executable contains your bytecode appended to a runner stub. Use `--strip-source` to remove the source text.

## Targets

| Target | Use it for |
| :--- | :--- |
| **Native** | CLI tools and local applications |
| **Browser and JavaScript** | Client-side apps, libraries and Cloudflare Workers |
| **WASI** | Experimental WebAssembly workloads in WASI hosts |
| **AWS Lambda (preview)** | Serverless functions with small cold starts |
| **ESP32** | Embedded devices |

See the dedicated pages for [compiled native binaries](compiled-native-binaries.md), [WASM in the browser](wasm-in-the-browser.md), [WASM containers](wasm-container.md), and [ESP32](esp32.md).

## How MatchBox Relates to BoxLang on the JVM

MatchBox complements the JVM runtime and does not replace it.

| | BoxLang on the JVM | MatchBox |
| :--- | :--- | :--- |
| Runtime | JVM | Rust bytecode VM with a tiered Cranelift JIT |
| Java ecosystem and interop | Full | Experimental in native builds, needs a JDK |
| Module coverage | Broad | Differs, check your target |
| Single-file executable | No | Yes |
| Browser and ESP32 | No | Yes |

Runtime APIs and module support differ between the two. Check compatibility for your target before you commit, and read [Differences from BoxLang](https://matchbox.boxlang.io/differences-from-boxlang/).

## Native Fusion

Native Fusion lets you call Rust from BoxLang, call BoxLang from Rust, and reach Java classes from native builds. Learn more in the [Native Fusion guide](https://matchbox.boxlang.io/building-and-deploying/native-fusion/).
