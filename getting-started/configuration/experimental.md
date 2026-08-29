---
icon: flask-vial
description: Here you can enable/disable experimental flags in BoxLang.
---

# Experimental

This block is used to have experimental feature flags for BoxLang. Every experimental flag will be documented here once we have them.

{% code title="boxlang.json" %}
```json
"experimental": {
    // This choose the compiler to use for the runtime
    // Valid values are: "java", "asm"
    "compiler": "asm",
    // If enabled, it will generate AST JSON data under the project's /grapher/data folder
    "ASTCapture": false,
    // If enabled, a background watchdog automatically evicts the parser's
    // ANTLR DFA cache once it has been idle for a few minutes or has grown large,
    // preventing long-running server processes from accumulating unbounded parser memory
    "clearParserCache": true
},
```
{% endcode %}

### Compiler

This is the compiler used for your BoxLang source. The available options are:

* `java` : We will transpile your BoxLang source to Java, then compile it
* `asm` : We will directly compile your BoxLang source to Java bytecode (Default)

{% hint style="info" %}
Please note that `asm`will be the default and you will not be able to change it once we release.
{% endhint %}

### AST Capture

If enabled, it will activate the AST capture interceptor and on parse it will create a `/grapher/data` folder in your project with useful AST JSON captures.  The default is false.

### Clear Parser Cache

_New in 1.17.0._ ANTLR (the parser generator BoxLang's compiler is built on) caches per-parser DFA (Deterministic Finite Automaton) state to speed up repeated parses. Those structures persist indefinitely in heap memory until the JVM restarts, and in a large, long-running application can accumulate **400MB to 1GB** of cached data that serves no ongoing purpose — creating unnecessary GC pressure and, on constrained systems, a real risk of out-of-memory failures.

When enabled (the default), a background watchdog evicts the cache automatically using three independent triggers — whichever fires first:

| Trigger | Condition |
| --- | --- |
| **Heap-pressure** | The DFA cache's estimated size exceeds ⅓ of the JVM's maximum heap |
| **Idle** | No parsing activity for 3 minutes |
| **Max-age** | The cache exceeds 100MB **and** 10 minutes have passed since the last clear, even under continuous parsing load |

This requires no tuning in the common case. The watchdog is lazy — it consumes no resources in precompiled deployments that never parse — and each eviction is logged at `TRACE` level for diagnostics. Clearing the cache doesn't change application behavior; it just means the next parse of a given template rebuilds its DFA state instead of reusing a cached one.

```json
"clearParserCache": true
```

```bash
# Or via environment variable
export BOXLANG_EXPERIMENTAL_CLEARPARSERCACHE=false
```

Disable it only if you have a specific reason to keep the cache warm indefinitely (for example, a short-lived CLI process where the eviction watchdog itself is pure overhead).
