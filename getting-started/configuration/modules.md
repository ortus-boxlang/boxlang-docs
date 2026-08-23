---
description: Configure how modules are loaded and work in BoxLang
icon: chart-tree-map
---

# Modules

BoxLang is a modular language. Each module can have a configuration structure for usage within the language. The name of the key is the name of the module and each module config has the following keys available:

* `enabled` : Boolean indicator to disable or eanble the module from loading. Defaults to \`true\`
* `settings` : A structure of configuration settings each module exposes

{% hint style="info" %}
This config is applied **last** and always wins. A module sets its own defaults in `configure()`, a module that bundles others can override its children's settings, and this block overrides both. See [Module Inception](../../boxlang-framework/module-development/module-inception.md#overriding-a-childs-settings) for the full precedence chain.
{% endhint %}

{% code title="boxlang.json" %}
```json
/**
 * The BoxLang module settings
 * The key is the module name and the value is a struct of settings for that specific module
 * The `enabled` property is a boolean that determines if the module should be enabled or not
 * The `settings` property is a struct of settings that are specific to the module and will be override the module settings
 */
"modules": {
    // The Compat Module
    "compat-cfml": {
        "settings": {
            "engine" : "Adobe"
        }
    },
    // The Mail module
    "mail" : {
        "settings" : {
            "spoolEnable" : true,
            // Spool interval, in minutes
            "spoolInterval" : 1.5,
            "mailServers" : [
                {
                    "tls": false,
                    "password": "",
                    "idleTimeout": "10000",
                    "lifeTimeout": "60000",
                    "port": "25",
                    "username": "",
                    "ssl": false,
                    "smtp": "127.0.0.1"
                }
            ]
        }
    }
}
```
{% endcode %}

## Example: bx-mcp Settings

The `bx-mcp` module uses the `bxmcp` module key and exposes security and tool-filtering settings for MCP clients.

{% code title="boxlang.json" %}
```json
"modules": {
    "bxmcp": {
        "enabled": true,
        "settings": {
            "enabled": true,
            "authToken": "FILL_THIS_OUT_ALWAYS",
            "allowedIPs": ["127.0.0.1"],
            "corsAllowedOrigins": [],
            "enableStats": true,
            "maxRequestBodySize": 0,
            "includedTools": ["*"],
            "excludedTools": []
        }
    }
}
```
{% endcode %}

{% hint style="warning" %}
For non-local deployments, always define `authToken`, restrict `allowedIPs`, and consider `excludedTools` for sensitive operations.
{% endhint %}
