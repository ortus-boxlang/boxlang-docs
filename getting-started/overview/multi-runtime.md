---
description: BoxLang deploys to many runtimes on the JVM and on MatchBox, the Rust runtime
icon: starfighter-twin-ion-engine
layout:
  width: wide
---

# Multi-Runtime

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

BoxLang has a lightweight, fast, and modular core. The operating system binary is a whopping **8MB**, and we build on it according to the runtime of choice. There are two runtime families, and one language across both.

{% columns %}
{% column %}
### ☕ JVM Runtimes

The official BoxLang runtime on the Java Virtual Machine. Full language, full standard library, 100% Java interop and the broadest module coverage.

[Installation methods →](../installation/README.md)
{% endcolumn %}

{% column %}
### 🔥 MatchBox Runtimes

An independent Rust implementation of BoxLang. A bytecode VM with a tiered JIT that ships to native binaries, the browser, WASI, AWS Lambda and ESP32.

[MatchBox docs →](https://matchbox.boxlang.io)
{% endcolumn %}
{% endcolumns %}

## Available Runtimes

{% tabs %}
{% tab title="☕ JVM" %}
**Cloud and serverless**

| Runtime | Description | Status |
| :--- | :--- | :--- |
| [**AWS Lambda**](../running-boxlang/aws-lambda.md) | Run BoxLang with AWS Lambda | **Available** |
| [**Azure Functions**](../running-boxlang/azure-functions.md) | Run BoxLang with Microsoft Azure Functions | **Available** |
| [**Google Cloud Functions**](../running-boxlang/google-cloud-functions.md) | Run BoxLang with Google Cloud Functions | **Available** |
| [**DigitalOcean App Platform**](../running-boxlang/digitalocean-app.md) | DigitalOcean App Platform applications | **Available** |
| [**Docker**](../running-boxlang/docker.md) | BoxLang CLI, MiniServer and CommandBox images | **Available** |

**Web and servers**

| Runtime | Description | Status |
| :--- | :--- | :--- |
| [**MiniServer**](../running-boxlang/miniserver.md) | A pure Java web server built with BoxLang | **Available** |
| [**CommandBox**](../running-boxlang/commandbox.md) | A BoxLang engine for CommandBox | **Available** |
| **Servlet WAR** | A servlet capable `war` | **Available** |
| [**Spring Boot**](../running-boxlang/spring-boot.md) | A Spring Boot starter and auto configurator | **Available** |

**Local, desktop and embedded**

| Runtime | Description | Status |
| :--- | :--- | :--- |
| [**OS**](../running-boxlang/README.md) | Bare metal runtime for any OS Java runs in | **Available** |
| [**Desktop**](../running-boxlang/desktop-applications.md) | BoxLang native desktop applications | **Available** |
| [**JSR-223**](../running-boxlang/jsr-223-scripting.md) | Java scripting interfaces | **Available** |
| **WebAssembly** | Run BoxLang as WebAssembly compiled code | **Available** |
| **Android** | Run BoxLang on Android devices | *In Planning* |
| **iOS** | Run BoxLang on iOS devices | *In Planning* |
{% endtab %}

{% tab title="🔥 MatchBox" %}
| Target | Description | Status |
| :--- | :--- | :--- |
| [**Native executable**](../running-boxlang/compiled-native-binaries.md) | A single-file binary with the runner and your bytecode. No JVM needed | **Available** |
| [**Browser and JavaScript**](../running-boxlang/wasm-in-the-browser.md) | A compiled JavaScript and WebAssembly module, including Cloudflare Workers | **Available** |
| [**WASI containers**](../running-boxlang/wasm-container.md) | WebAssembly workloads in WASI hosts such as Wasmtime or WasmEdge | **Experimental** |
| **AWS Lambda** | MatchBox on AWS Lambda for very small cold starts | *Preview* |
| [**ESP32**](../running-boxlang/esp32.md) | Cross-compiled runner for supported Xtensa and RISC-V boards | **Available** |

{% hint style="info" %}
The native CLI includes a four-tier Cranelift JIT. WebAssembly and ESP32 builds use the interpreter.
{% endhint %}

Learn more on the [MatchBox page](../running-boxlang/matchbox.md), try the [online playground](https://matchbox.boxlang.io/playground/), or take the [online course](https://matchbox.boxlang.io/course/).
{% endtab %}
{% endtabs %}

## Which Runtime Should I Pick?

| If you need... | Use |
| :--- | :--- |
| Java libraries, JDBC drivers or the broadest module coverage | ☕ **JVM** |
| A web application on a servlet container or CommandBox | ☕ **JVM** |
| CFML compatibility | ☕ **JVM** |
| A single binary to hand to users, with no installer | 🔥 **MatchBox native** |
| BoxLang logic running in the browser | 🔥 **MatchBox browser** |
| Tiny serverless cold starts | 🔥 **MatchBox** or ☕ **JVM** with a Lambda runtime |
| A microcontroller | 🔥 **MatchBox ESP32** |

{% hint style="warning" %}
MatchBox implements a subset of BoxLang and evolves quickly. Code written for MatchBox generally runs on the JVM runtime, but the reverse is not guaranteed. Read the [compatibility guide](../running-boxlang/matchbox.md#how-matchbox-relates-to-boxlang-on-the-jvm) before you commit.
{% endhint %}

## Runtime Hierarchy

The core impetus of BoxLang is to grow through a hierarchical approach, targeting specific runtimes with specific behaviors. For example, the concepts of FORM, URL scope, web functions, and components are only available to runtimes that support web.

**Just because a runtime isn't listed here doesn't mean BoxLang can't run on it.** These are the officially supported runtimes. You can use the core runtime anywhere the JVM runs, and embed it in Android, Azure, OpenWhisk and more. Once we have official runtimes, we will post them here.

{% hint style="success" %}
All of our runtime source code can be found in our organization: [https://github.com/ortus-boxlang](https://github.com/ortus-boxlang). MatchBox lives at [ortus-boxlang/matchbox](https://github.com/ortus-boxlang/matchbox).
{% endhint %}

## Third-Party Runtimes

We love our community. If you have created custom runtimes for BoxLang, please let us know, and we will add them here.
