# Modules

### BoxLang Modules

Here are the current BoxLang Modules that are available to you:

* [BoxLang ESAPI](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-esapi/bx-esapi-1.0.0.zip) - ESAPI and AntiSamy Sanitizers
* [BoxLang Compat](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-compat/bx-compat-1.0.0.zip) - Compatibility module for Adobe/Lucee CFML Engines
* [BoxLang Mail](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-mail/bx-mail-1.0.0.zip) Mail components for BoxLang

#### JDBC Modules

In addition, we offer a number of JDBC modules which package the appropriate JDBC driver for your database vendor of choice:

* [PostgreSQL](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-postgresql/bx-postgresql-1.0.0.zip)
* [Apache Derby](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-derby/bx-derby-1.0.0.zip)
* [MySQL](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-mysql/bx-mysql-1.0.0.zip)
* [MariaDB](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-mariadb/bx-mariadb-1.0.0.zip)
* [Microsoft SQL Server](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-mssql/bx-mssql-1.0.0.zip)
* [Oracle](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-oracle/bx-oracle-1.0.0.zip)
* [HyperSQL](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-hypersql/bx-hypersql-1.0.0.zip)

#### Module Installation

Unzip the module `.zip` file into the location `.boxlang/modules/` located inside your user home directory (by default):

```bash
.boxlang/modules/bx-derby/ModuleConfig.bx ...
```

You can customize the boxlang module directory by changing the `runtime.modulesDirectory` setting in your `config/boxlang.json` file:

{% code title="boxlang.json" %}
```json
{
	"runtime": {
		// A collection of BoxLang module directories, they must be absolute paths
		"modulesDirectory": [
			"${boxlang-home}/modules"
		],
		// ...
	}
}
```

See [Runtime Configuration](/runtime/configuration.md) for more info on using the `boxlang.json` configuration file.