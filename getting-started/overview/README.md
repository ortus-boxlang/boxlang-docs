---
description: BoxLang is a software productivity platform with two runtimes, the JVM and MatchBox on Rust
icon: crosshairs-simple
layout:
  width: wide
---

# Overview

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption><p>BoxLang</p></figcaption></figure>

## What is BoxLang?

**BoxLang is the software productivity platform for building, modernizing and running applications, with developers and AI agents working together.**

At its core is a modern, dynamic language with a batteries-included runtime and framework for files, HTTP, databases, async, caching, scheduling, templating, and AI. It is **built for developers**, **built for AI**, and **built to ship**: predictable conventions that AI agents can follow, professional open source you can start with for free, and enterprise support and premium modules when you need them.

BoxLang combines ideas from Java, CFML, Python, Ruby, Go, and PHP into a modern, fluent, and expressive syntax.

{% hint style="success" %}
**Try every BoxLang+ module free for 60 days.** The trial starts automatically the first time you start a BoxLang server or CLI with a BoxLang+ module installed. No sign-up and no key. Learn more on the [BoxLang+ page](../../boxlang-framework/boxlang-plus/README.md) or the [plans page](https://www.boxlang.io/plans).
{% endhint %}

## Two Runtimes, One Language

BoxLang runs on two runtimes. Pick the one that fits where your code needs to live. See [Multi-Runtime](multi-runtime.md) for every deployment target.

{% columns %}
{% column %}
### ☕ BoxLang on the JVM

The official, full-featured runtime.

* 100% Java interoperability
* The full BoxLang language, standard library and module ecosystem
* Web servers, servlet containers, serverless, Docker, desktop and more
* CFML compatibility

{% hint style="info" %}
Choose it when you need Java libraries, the broadest module coverage, or established JVM infrastructure.
{% endhint %}
{% endcolumn %}

{% column %}
### 🔥 MatchBox on Rust

An independent Rust implementation of BoxLang.

* Bytecode VM with a tiered Cranelift JIT
* Single-file native executables, no JVM required
* Browser and JavaScript, WASI, AWS Lambda (preview) and ESP32
* Native Fusion: call Rust from BoxLang and BoxLang from Rust

{% hint style="info" %}
Choose it when you need a tiny binary, fast startup, the browser, or a microcontroller.
{% endhint %}
{% endcolumn %}
{% endcolumns %}

{% hint style="warning" %}
MatchBox complements the JVM runtime and does not replace it. Runtime APIs and module support differ, so check [compatibility](../running-boxlang/matchbox.md) for your target.
{% endhint %}

## Get Started

{% tabs %}
{% tab title="BoxLang (JVM)" %}
{% stepper %}
{% step %}
### Install BoxLang

```bash
# Linux and macOS
curl -fsSL https://install.boxlang.io | bash

# Or with Homebrew
brew install ortus-boxlang/boxlang/boxlang
```

See all [installation options](../installation/README.md).
{% endstep %}

{% step %}
### Write a script

Create `hello.bxs`:

```js
name = "BoxLang"
println( "Hello, #name#!" )
```
{% endstep %}

{% step %}
### Run it

```bash
boxlang hello.bxs
```
{% endstep %}

{% step %}
### Keep learning

Jump into [BoxLings](https://github.com/ortus-boxlang/boxlings), our interactive CLI learning tool, or try the [online playground](../running-boxlang/try-boxlang.md).
{% endstep %}
{% endstepper %}
{% endtab %}

{% tab title="MatchBox (Rust)" %}
{% stepper %}
{% step %}
### Install MVM, the MatchBox Version Manager

```bash
# Linux and macOS
curl -fsSL https://raw.githubusercontent.com/ortus-boxlang/matchbox-quick-installer/main/install/install.sh | bash
```

On Windows, use the `install.ps1` script from the same repository.
{% endstep %}

{% step %}
### Install MatchBox

```bash
mvm install latest
mvm use latest
matchbox --version
```
{% endstep %}

{% step %}
### Run a script, then ship it

```bash
matchbox hello.bxs
matchbox --target native hello.bxs
```

The second command produces a standalone executable.
{% endstep %}

{% step %}
### Learn in the browser

Try the [MatchBox playground](https://matchbox.boxlang.io/playground/) or follow the ten-lesson [online course](https://matchbox.boxlang.io/course/). Both are free.
{% endstep %}
{% endstepper %}
{% endtab %}
{% endtabs %}

## Explore

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Multi-Runtime</strong></td><td>Every JVM and MatchBox deployment target</td><td><a href="multi-runtime.md">multi-runtime.md</a></td></tr><tr><td><strong>Quick Syntax Guide</strong></td><td>The language in ten minutes</td><td><a href="syntax-style-guide/README.md">README.md</a></td></tr><tr><td><strong>CommandBox CLI</strong></td><td>The package manager, CLI and servlet server, now in pure BoxLang (bx-cli)</td><td><a href="commandbox-cli.md">commandbox-cli.md</a></td></tr><tr><td><strong>Agentic Development</strong></td><td>Build with AI agents using skills, MCP and checks</td><td><a href="../agentic-development/README.md">README.md</a></td></tr></tbody></table>

## Key Features

{% tabs %}
{% tab title="Language" %}
* **Dynamic:** types are optional, with inference, auto-casting and promotions. Add, remove and modify methods and properties at runtime.
* **Low verbosity:** functional, fluent, human-readable and low ceremony.
* **Functional:** first-class functions, closures, and pure `lambda` functions with no access to the surrounding context.
* **Scripting and applications:** from quick scripts to modular enterprise applications and cloud functions.
* **Portable scheduled tasks:** a scheduling DSL you can keep in source control.
{% endtab %}

{% tab title="JVM Runtime" %}
* **InvokeDynamic:** a core built on the JVM's `InvokeDynamic` for speed, predictability and adaptability.
* **Java interoperability:** extend and implement Java objects, use annotations, import classes, even write Java. Everything is interoperable thanks to `DynamicObject`.
* **Event driven:** an internal interception bus lets you listen to almost every part of the language, parser and runtime.
* **Modular:** modules add built-in functions, components, runtime debuggers, AOP aspects and event listeners.
{% endtab %}

{% tab title="MatchBox Runtime" %}
* **Bytecode VM:** BoxLang compiles to bytecode that a Rust VM runs, with a four-tier Cranelift JIT in the native CLI.
* **Single-file executables:** append your bytecode to a runner stub, about 4.7 MB for the VM core. Use `--strip-source` to remove source text.
* **No JVM:** core and native builds do not need Java. Java interop in native builds is experimental and needs a JDK.
* **Native Fusion:** call Rust from BoxLang, BoxLang from Rust, and reach Java classes from native builds.
* **Cooperative fibers:** `runAsync`, non-blocking `sleep` and HTTP run on a fiber scheduler.
{% endtab %}

{% tab title="Ecosystem" %}
* **Java and CFML libraries:** almost any project on [Maven Central](https://central.sonatype.com/) and [ForgeBox](https://www.forgebox.io) works with the JVM runtime.
* **Tooling:** a VS Code extension with syntax highlighting, a debugger, code insight, formatting and LSP. BoxLang+ adds enhanced debuggers and CFML transformers.
* **Package manager:** [CommandBox](commandbox-cli.md) is our package manager, CLI and servlet server, now available in pure BoxLang as the `bx-cli` module, with ForgeBox integration.
* **Learning:** [BoxLings](https://github.com/ortus-boxlang/boxlings) for the JVM runtime, the [MatchBox course](https://matchbox.boxlang.io/course/) and [playground](https://matchbox.boxlang.io/playground/).
* **Professional open source:** Apache 2 licensed, with BoxLang+ for support and premium modules.
{% endtab %}
{% endtabs %}

## Goals

* Be dynamic, modular, lightweight and fast
* Be 100% interoperable with Java on the JVM runtime
* Be modern, functional and fluent
* Take advantage of the modern JVM, and of Rust where the JVM does not fit
* Support and adapt to multiple runtimes
* Be fully tested with TDD and BDD
* Use a multi-parser design to run other dynamic languages such as CFML
* Provide great tooling and IDE support

## Is it CFML compatible?

BoxLang has a multi-parser design, one for BoxLang and one for CFML. The CFML parser transpiles to BoxLang at runtime, or you can translate your code with our [CLI tools](../ide-tooling/README.md). We support as much CFML as we can, but BoxLang is a fresh start with different decisions. The [compatibility module](https://forgebox.io/view/bx-compat-cfml) keeps old-school CFML working as it is on the BoxLang runtime.

You can stay on CFML-compatible code or move to the new vision of BoxLang. We will support both indefinitely.

{% hint style="info" %}
Thanks to the multi-parser architecture, these parsers are being developed as modules for the BoxLang ecosystem:

* Apache Groovy
* COBOL (yes, finally migrate to a modern language easily!)
{% endhint %}
