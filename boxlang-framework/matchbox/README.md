---
icon: fire
---

# MatchBox

MatchBox is a **Rust implementation of the BoxLang runtime**. BoxLang compiles to bytecode, and a Rust VM runs it, so core and native builds need no JVM.

{% hint style="success" %}
**All MatchBox documentation now lives at [matchbox.boxlang.io](https://matchbox.boxlang.io).** The pages in this section are kept as a reference for building and extending MatchBox.
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

## Get Started

Install the MatchBox Version Manager (MVM), then install MatchBox:

```bash
curl -fsSL https://raw.githubusercontent.com/ortus-boxlang/matchbox-quick-installer/main/install/install.sh | bash
mvm install latest
mvm use latest
matchbox --version
```

On Windows, use the `install.ps1` script from the [matchbox-quick-installer](https://github.com/ortus-boxlang/matchbox-quick-installer) repository. See the [MatchBox page](../../getting-started/running-boxlang/matchbox.md) for a full introduction.

## How It Works

MatchBox is a complete, self-contained language toolchain:

1. **Parser:** a [Pest](https://pest.rs/) PEG grammar reads `.bxs` source files and produces an AST.
2. **Compiler:** a multi-stage compiler lowers the AST into a compact bytecode format.
3. **VM:** a stack-based bytecode virtual machine runs the bytecode, with a tiered Cranelift JIT in the native CLI and a cooperative fiber scheduler for async work.
4. **Targets:** the same bytecode can be embedded in a native binary, run in the browser or a WASI host, run on ESP32 devices, or executed directly by the MatchBox runner.

## MatchBox and BoxLang on the JVM

MatchBox complements the JVM runtime and does not replace it. It is an independent implementation of an evolving subset of BoxLang, so runtime APIs and module support differ. Read [Differences From BoxLang JVM](differences-from-boxlang-jvm.md) and check compatibility for your target.

| | BoxLang on the JVM | MatchBox |
| :--- | :--- | :--- |
| Runtime | JVM | Rust bytecode VM |
| Java ecosystem and interop | Full | Experimental in native builds, needs a JDK |
| Single-file executable | No | Yes |
| Browser, WASI and ESP32 | No | Yes |

## What You Can Build

* **CLI tools:** compile to a single native binary and distribute without any installer.
* **Serverless functions:** small cold starts on AWS Lambda (preview).
* **Browser applications:** run BoxLang logic in the browser through WebAssembly and JavaScript.
* **Native Fusion apps:** mix BoxLang with hand-written Rust.
