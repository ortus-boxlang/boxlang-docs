---
description: The Officially supported BoxLang modules
icon: atom-simple
---

# Modules

Our official modules can be found in the BoxLang Software Directory: **FORGEBOX**: [www.forgebox.io](https://www.forgebox.io).

{% hint style="success" %}
Every runtime can use modules, and the installation process can differ. So, make sure you review each of the sections on Running BoxLang and adapt your installation process accordingly.
{% endhint %}

For web runtimes running on CommandBox, our servlet server, then use the `box` CommandBox CLI for installation and `server.json` for tracking dependencies.  For our operating system runtime, use our `install-bx-module` binary.

### Operating System Modules

{% code title="Operating System" %}
```bash
# Install os-wide modules
install-bx-module bx-compat-cfml

# Install BoxLang+ MCP stack (requires subscription)
install-bx-module bx-plus bx-ai bx-mcp

# Install os-wide modules with a specific version
install-bx-module bx-compat-cfml@1.0.0

# Install multiple modules
install-bx-module bx-compat-cfml bx-esapi bx-orm
```
{% endcode %}

#### Local CLI Application Modules

BoxLang also supports the concept of local loading. Meaning, if you have a `boxlang_modules` folder in the root of where you run your CLI applications, then BoxLang will load those modules first and then fall back to the user's home directory for the operating system.

{% code title="myAppDirectory" %}
```bash
# Install locally
install-bx-module bx-compat-cfml --local

# Install locally
install-bx-module bx-compat-cfml@1.0.0 --local

# Install multiple modules locally
install-bx-module bx-compat-cfml bx-esapi bx-orm --local
```
{% endcode %}

### CommandBox Runtimes

The CommandBox CLI installs BoxLang modules into web runtimes.

{% hint style="warning" %}
Eventually, CommandBox will be the de-facto standard of installation once it's migrated to BoxLang.
{% endhint %}

{% code title="CommandBox" %}
```bash
box install bx-compat-cfml,bx-esapi

# Install BoxLang+ MCP stack (requires subscription)
box install bx-plus,bx-ai,bx-mcp
```
{% endcode %}

{% hint style="info" %}
The `bx-mcp` module is a premium BoxLang+/++ module and requires both `bx-plus` and `bx-ai`.
{% endhint %}

### Configuration

You can customize the boxlang module directory by changing the `runtime.modulesDirectory` setting in your `config/boxlang.json` file:

{% code title="boxlang.json" %}
```json
{

    // A collection of BoxLang module directories, they must be absolute paths
    "modulesDirectory": [
      "${boxlang-home}/modules"
    ],

}
```
{% endcode %}



## Core Modules

Visit the [Modules](../../boxlang-framework/modularity/) section of our docs for the most up to date listing of our supported modules.



