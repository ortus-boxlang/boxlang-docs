---
description: The Officially supported BoxLang modules
---

# Modules

## Core Modules

Here is the collection of modules built and supported by the BoxLang team.

bx-c

### bx-esapi

Leverages ESAPI and AntiSamy to provide your BoxLang applications with security and cleaning concerns.

```
install bx-esapi
```

* Dowload: [https://forgebox.io/view/bx-esapi](https://forgebox.io/view/bx-esapi)
* Instructions: [https://github.com/ortus-boxlang/bx-esapi](https://github.com/ortus-boxlang/bx-esapi)





* [BoxLang Compat](https://forgebox.io/view/bx-compat) - Compatibility module so your BoxLang server can work like an Adobe ColdFusion or Lucee server
* [BoxLang Mail](https://forgebox.io/view/bx-mail) Mail components for BoxLang
* [BoxLang Image](https://forgebox.io/view/bx-image) - Image manipulation library
* BoxLang PDF - PDF tooling for BoxLang (Coming Soon)
* [BoxLang Usafe Evaluate](https://forgebox.io/view/bx-unsafe-evaluate) - Gives you the `evaluate()` function back.

### JDBC Modules

In addition, we offer a number of JDBC modules which package the appropriate JDBC driver for your database vendor of choice:

* [PostgreSQL](https://forgebox.io/view/bx-postgresql)
* [Apache Derby](https://forgebox.io/view/bx-derby)
* [MySQL](https://forgebox.io/view/bx-mysql)
* [MariaDB](https://forgebox.io/view/bx-mariadb)
* [Microsoft SQL Server](https://forgebox.io/view/bx-mssql)
* [Oracle](https://forgebox.io/view/bx-oracle)
* [HyperSQL](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-hypersql/bx-hypersql-1.0.0.zip)

### Module Installation

Unzip the module `.zip` file into the location `.boxlang/modules/` located inside your user home directory (by default):

```bash
.boxlang/modules/bx-derby/ModuleConfig.bx ...
```

You can customize the boxlang module directory by changing the `runtime.modulesDirectory` setting in your `config/boxlang.json` file:

{% code title="boxlang.json" %}
```json
{
  "runtime" : {
    
    
    // A collection of BoxLang module directories, they must be absolute paths
    "modulesDirectory": [
      "${boxlang-home}/modules"
    ],
    
    
  }
}
```
{% endcode %}

See [Runtime Configuration](../configuration.md) for more info on using the `boxlang.json` configuration file.
