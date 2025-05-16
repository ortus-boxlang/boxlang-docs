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
box install bx-compat-cfml bx-esapi
```
{% endcode %}

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

## +/++ Modules

These modules are available for our [+/++ subscribers only](https://ww.boxlang.io/plans). However, you can install them free of charge and try them out.

### bx-redis

`Category: Caching`

This module will enhance your language by allowing you to connect to Redis instances, clusters, or sentinel instances. Here are some features:

* Add native Redis functionality to the language
* Connect to a Redis server or a Redis cluster, or Redis Sentinel
* Store session variables in a distributed Redis cluster
* Leverage the Redis publish/subscribe features to create real-time messaging
* Get rid of sticky session load balancers, come to the round-robin world!
* Session variable persistence even after server restarts
* Cache connection capabilities for providing distributed & highly scalable query, object, template, and function caching
* Much more

```
install-bx-module bx-redis
```

* Download: [https://forgebox.io/view/bx-redis](https://forgebox.io/view/bx-redis)

