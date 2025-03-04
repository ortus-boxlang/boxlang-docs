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
    "ASTCapture": false
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
