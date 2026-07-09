---
description: Register JDBC database drivers in your BoxLang module (Java only)
icon: plug
---

# JDBC Drivers

{% hint style="warning" %}
JDBC drivers require **Java**. There is no BoxLang-only mechanism for registering database drivers.
{% endhint %}

JDBC driver modules provide database connectivity for BoxLang's datasource system. Common examples include `bx-mysql`, `bx-postgresql`, and `bx-sqlite`.

## Registration Methods

There are two approaches to register JDBC drivers:

{% tabs %}
{% tab title="Standard java.sql.Driver" %}

Implement `java.sql.Driver` and register via `DriverManager`:

**File:** `src/main/java/ortus/boxlang/modules/mymodule/jdbc/MyJDBCDriver.java`

```java
import java.sql.*;

public class MyJDBCDriver implements Driver {

    static {
        try {
            DriverManager.registerDriver( new MyJDBCDriver() );
        } catch ( SQLException e ) {
            throw new RuntimeException( "Failed to register driver", e );
        }
    }

    @Override
    public Connection connect( String url, Properties info ) {
        // Return connection if URL matches
    }

    @Override
    public boolean acceptsURL( String url ) {
        return url.startsWith( "jdbc:mydb:" );
    }

    // ... other Driver methods
}
```

**ServiceLoader Config:** `META-INF/services/java.sql.Driver`

```
ortus.boxlang.modules.mymodule.jdbc.MyJDBCDriver
```

{% endtab %}

{% tab title="BoxLang IJDBCDriver" %}

Implement `IJDBCDriver` for BoxLang-specific features:

```java
import ortus.boxlang.runtime.jdbc.IJDBCDriver;

public class MyBoxLangJDBCDriver implements IJDBCDriver {

    @Override
    public String getPrefix() {
        return "jdbc:mydb:";
    }

    @Override
    public Connection connect( String url, Properties info ) {
        // Return connection
    }

    @Override
    public boolean acceptsURL( String url ) {
        return url.startsWith( getPrefix() );
    }
}
```

{% endtab %}
{% endtabs %}

## Module Structure

JDBC driver modules are typically simple — just the driver JAR and registration:

```
bx-mydb/
├── box.json
├── ModuleConfig.bx
├── libs/
│   └── mydb-jdbc.jar
└── src/main/java/
    └── ortus/boxlang/modules/mydb/
        └── MyDBDriver.java
```

## Open Source JDBC Modules

Reference these existing JDBC driver modules:

| Module | Database |
|--------|----------|
| [bx-mysql](https://github.com/ortus-boxlang/bx-mysql) | MySQL/MariaDB |
| [bx-postgresql](https://github.com/ortus-boxlang/bx-postgresql) | PostgreSQL |
| [bx-mssql](https://github.com/ortus-boxlang/bx-mssql) | SQL Server |
| [bx-oracle](https://github.com/ortus-boxlang/bx-oracle) | Oracle |
| [bx-sqlite](https://github.com/ortus-boxlang/bx-sqlite) | SQLite |
| [bx-derby](https://github.com/ortus-boxlang/bx-derby) | Apache Derby |

## Next Steps

- [Services](services.md) — Global runtime services (Java only)
- [Cache Providers](cache-providers.md) — Custom caching backends (Java only)
- [Packaging & Publishing](../packaging-publishing.md) — Build and distribute your module
