# Modules

### BoxLang Modules

Here are the current BoxLang Modules that are available to you:

* [BoxLang ESAPI 4](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-esapi/bx-esapi-1.0.0.zip) - ESAPI and AntiSamy Sanitizers
* [BoxLang Compat 2](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-compat/bx-compat-1.0.0.zip) - Compatibility module for Adobe/Lucee CFML Engines
* [BoxLang Mail 2](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-mail/bx-mail-1.0.0.zip) Mail components for BoxLang

#### JDBC Drivers <a href="#jdbc-drivers-4" id="jdbc-drivers-4"></a>

* [PostgreSQL 3](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-postgresql/bx-postgresql-1.0.0.zip)
* [Apache Derby 1](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-derby/bx-derby-1.0.0.zip)
* [MySQL 2](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-mysql/bx-mysql-1.0.0.zip)
* [MariaDB 4](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-mariadb/bx-mariadb-1.0.0.zip)
* [Microsoft SQL Server 4](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-mssql/bx-mssql-1.0.0.zip)
* [Oracle 1](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-oracle/bx-oracle-1.0.0.zip)
* [HyperSQL 1](https://ortus-temp.s3.amazonaws.com/boxlang-modules/bx-hypersql/bx-hypersql-1.0.0.zip)

#### Module Installation <a href="#module-installation-5" id="module-installation-5"></a>

Unzip the module `.zip` file into the location `.boxlang/modules/` located inside your user home directory (by default):

```bash
.boxlang/modules/bx-derby/ModuleConfig.bx ...
```

OR, if you have a custom `runtime.modulesDirectory` configured in `boxlang.json`, use that location.
