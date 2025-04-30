---
description: Configure how modules are loaded and work in BoxLang
icon: chart-tree-map
---

# Modules

BoxLang is a modular language. Each module can have a configuration structure for usage within the language. The name of the key is the name of the module and each module config has the following keys available:

* `enabled` : Boolean indicator to disable or eanble the module from loading. Defaults to \`true\`
* `settings` : A structure of configuration settings each module exposes

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
