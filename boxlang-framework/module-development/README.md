---
description: Complete guide to creating, configuring, and publishing BoxLang modules using pure BoxLang or Java
icon: box-archive
layout:
  width: wide
---

# Module Development

Build extensible plugins for the BoxLang runtime through an isolated, convention-based module system. Choose between **pure BoxLang** for rapid development or **Java + BoxLang** for performance-critical integrations.

{% hint style="info" %}
All examples in this guide reference real, open-source modules from the [ortus-boxlang GitHub organization](https://github.com/orgs/ortus-boxlang/repositories?q=bx-). The modules listed under [Modules](../modularity/) focus on *using* existing modules — this section focuses on *building* them.
{% endhint %}

## Choose Your Approach

{% tabs %}
{% tab title="🟦 Pure BoxLang" %}
No compilation required. Perfect for utilities, configurations, and simple BIFs/components.

**Best for:** Rapid prototyping, simple logic, no external dependencies

✅ BIFs (`.bx` files)  
✅ Components (`.bx` files)  
✅ Interceptors (via `configure()`)  
✅ Custom interception points  
✅ Settings & configuration  
✅ Public web folders  
✅ Libs/JARs  

❌ Services (Java only)  
❌ Schedulers (Java only)  
❌ Cache Providers (Java only)  
❌ JDBC Drivers (Java only)

[→ Start with Pure BoxLang](getting-started.md#pure-boxlang-modules)
{% endtab %}

{% tab title="☕ Java + BoxLang" %}
Gradle-based with shadow JAR support. For complex logic and advanced integrations.

**Best for:** Performance-critical code, external libraries, services, JDBC drivers

✅ Everything from Pure BoxLang  
✅ Services (`IService`)  
✅ Schedulers (`IScheduler`)  
✅ Cache Providers (`ICacheProvider`)  
✅ JDBC Drivers (`java.sql.Driver`)  
✅ Advanced Java library integration  
✅ ServiceLoader discovery  

[→ Start with Java Modules](getting-started.md#javaboxlang-modules)
{% endtab %}
{% endtabs %}

## What Modules Can Provide

{% columns %}
{% column %}

**BoxLang or Java**

- ✅ **BIFs** — Custom built-in functions
- ✅ **Components** — XML-style tags (`bx:mytag`)
- ✅ **Interceptors** — Event listeners
- ✅ **Settings** — Module configuration
- ✅ **Mappings** — URL routing & class resolution
- ✅ **Public Folders** — Static web assets
- ✅ **Libs** — JAR dependencies

{% endcolumn %}

{% column %}

**Java Only**

- ✅ **Services** — Global runtime services
- ✅ **Schedulers** — Cron-like scheduled tasks
- ✅ **Cache Providers** — Custom caching backends
- ✅ **JDBC Drivers** — Database connectivity
- ✅ **System Setting Providers** — Custom `getSystemSetting()` sources
- ✅ **Class Resolvers** — Custom `prefix:ClassName` resolution

{% endcolumn %}
{% endcolumns %}

## Quick Navigation

| Topic | Description |
|-------|-------------|
| [Getting Started](getting-started.md) | Choose your approach, use templates, create your first module |
| [Architecture](architecture.md) | Understand module isolation, class loaders, and discovery |
| [Module Descriptor](module-descriptor.md) | Configure `box.json`, `ModuleConfig.bx`, and Java `IModuleConfig` |
| [Lifecycle](lifecycle.md) | Registration → Activation → Running → Deactivation |
| [Capabilities](capabilities/) | BIFs, components, interceptors, services, and more |
| [Mappings & Class Resolution](mappings.md) | Module mappings, `@moduleName` notation, and class loading |
| [Configuration](configuration.md) | Settings, runtime overrides, dependency management |
| [Advanced Collaboration](advanced-collaboration.md) | System settings providers, custom resolvers, inter-module communication |
| [Packaging & Publishing](packaging-publishing.md) | Build output, ForgeBox workflow, versioning |
| [Testing](testing.md) | TestBox integration, CI/CD patterns |
| [Troubleshooting](troubleshooting.md) | Common issues and solutions |

## Open Source Module Examples

Learn from production-ready modules in our ecosystem:

{% tabs %}
{% tab title="Pure BoxLang" %}

| Module | Purpose | Complexity |
|--------|---------|------------|
| [bx-ai](https://github.com/ortus-boxlang/bx-ai) | AI integration helpers | 🟢 Simple |
| [bx-csrf](https://github.com/ortus-boxlang/bx-csrf) | CSRF token management | 🟢 Simple |
| [bx-jwt](https://github.com/ortus-boxlang/bx-jwt) | JWT token handling | 🟡 Medium |
| [bx-ftp](https://github.com/ortus-boxlang/bx-ftp) | FTP client operations | 🟡 Medium |
| [bx-image](https://github.com/ortus-boxlang/bx-image) | Image manipulation | 🟡 Medium |
| [bx-yaml](https://github.com/ortus-boxlang/bx-yaml) | YAML parsing/generation | 🟢 Simple |
| [bx-ini](https://github.com/ortus-boxlang/bx-ini) | INI file handling | 🟢 Simple |
| [bx-markdown](https://github.com/ortus-boxlang/bx-markdown) | Markdown rendering | 🟡 Medium |
| [bx-wddx](https://github.com/ortus-boxlang/bx-wddx) | WDDX serialization | 🟢 Simple |

{% endtab %}

{% tab title="Java + BoxLang" %}

| Module | Purpose | Complexity |
|--------|---------|------------|
| [bx-compat-cfml](https://github.com/ortus-boxlang/bx-compat-cfml) | CFML compatibility layer | 🔴 Complex |
| [bx-mail](https://github.com/ortus-boxlang/bx-mail) | Email sending service | 🟡 Medium |
| [bx-esapi](https://github.com/ortus-boxlang/bx-esapi) | Security/encryption | 🟡 Medium |
| [bx-password-encrypt](https://github.com/ortus-boxlang/bx-password-encrypt) | Password hashing | 🟡 Medium |
| [bx-ui-forms](https://github.com/ortus-boxlang/bx-ui-forms) | HTML form generation | 🟡 Medium |
| [bx-groovy](https://github.com/ortus-boxlang/bx-groovy) | Groovy language support | 🟡 Medium |

{% endtab %}

{% tab title="JDBC Drivers" %}

| Module | Database | Type |
|--------|----------|------|
| [bx-mysql](https://github.com/ortus-boxlang/bx-mysql) | MySQL/MariaDB | Java |
| [bx-postgresql](https://github.com/ortus-boxlang/bx-postgresql) | PostgreSQL | Java |
| [bx-mssql](https://github.com/ortus-boxlang/bx-mssql) | Microsoft SQL Server | Java |
| [bx-oracle](https://github.com/ortus-boxlang/bx-oracle) | Oracle Database | Java |
| [bx-sqlite](https://github.com/ortus-boxlang/bx-sqlite) | SQLite | Java |
| [bx-derby](https://github.com/ortus-boxlang/bx-derby) | Apache Derby | Java |
| [bx-hypersql](https://github.com/ortus-boxlang/bx-hypersql) | HyperSQL | Java |

{% endtab %}

{% tab title="Advanced" %}

| Module | Purpose | Type |
|--------|---------|------|
| [bx-orm](https://github.com/ortus-boxlang/bx-orm) | Hibernate/JPA ORM | Java |
| [bx-lens](https://github.com/ortus-boxlang/bx-lens) | Observability/monitoring | Java |
| [bx-ui-compat](https://github.com/ortus-boxlang/bx-ui-compat) | UI compatibility | JavaScript |

{% endtab %}
{% endtabs %}

{% hint style="success" %}
Browse all 40+ open-source modules at [github.com/ortus-boxlang](https://github.com/orgs/ortus-boxlang/repositories?q=bx-)
{% endhint %}

## Module Templates

Start with official templates to bootstrap your module. Both templates are available on GitHub:

**Pure BoxLang Template:**
```bash
git clone https://github.com/ortus-boxlang/boxlang-module-template-bx.git my-module
cd my-module
```

**Java + BoxLang Template:**
```bash
git clone https://github.com/ortus-boxlang/boxlang-module-template.git my-module
cd my-module
./gradlew build
```

{% hint style="info" %}
The templates include placeholder files and configuration you can customize. See [Getting Started](getting-started.md) for a detailed walkthrough.
{% endhint %}

## Next Steps

1. **[Choose Your Approach](getting-started.md)** — Decide between pure BoxLang or Java+BoxLang
2. **[Understand the Architecture](architecture.md)** — Learn about module isolation and discovery
3. **[Explore Real Examples](#open-source-module-examples)** — Study production modules like bx-ai and bx-compat-cfml
4. **[Start Building](getting-started.md)** — Create your first module with our templates

---

{% hint style="info" %}
Need help? Check out the [Troubleshooting Guide](troubleshooting.md) for common issues and solutions.
{% endhint %}
