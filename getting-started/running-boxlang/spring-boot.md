---
description: >-
  Use BoxLang as your Spring Boot view layer, with full framework support built
  in.
icon: power-off
---

# Spring Boot

<figure><img src="../../.gitbook/assets/image (1).png" alt="" width="450"><figcaption></figcaption></figure>

The **BoxLang Spring Boot Starter** is a zero-configuration Spring Boot auto-configuration library that integrates the [BoxLang](https://www.boxlang.io) dynamic JVM language as a view engine inside any Spring Boot 3 web application. Write your templates in BoxLang's expressive `.bxm` markup syntax and let Spring MVC route requests to them — no boilerplate required. You can also leverage any BoxLang features and libraries directly from your Java controllers, services, or any Spring-managed bean by just talking to the `BoxRuntime` API.

```java
BoxRuntime boxlang = BoxRuntime.getInstance();
```

## ✨ Features

* ⚙️ **Zero-configuration auto-configuration** — drop the JAR on the classpath and Spring Boot wires everything automatically via `BoxLangAutoConfiguration`.
* 🖼️ **BoxLang View Resolver** — a `BoxLangViewResolver` resolves logical view names (e.g. `"home"`) to BoxLang `.bxm` templates (e.g. `classpath:/templates/home.bxm`).
* 🌐 **Full web scopes** — templates have access to the complete set of BoxLang web scopes: `URL`, `Form`, `CGI`, `Cookie`, and `Request`.
* 🔗 **Spring Model integration** — every attribute added to the Spring `Model` is automatically injected into the BoxLang `variables` scope, accessible as `#variables.myKey#` in the template.
* 🔄 **Lifecycle-managed runtime** — the `BoxRuntime` starts early in the application lifecycle and shuts down gracefully when the context stops, with no manual wiring needed.
* 🛠️ **Configurable via `application.properties`** — all settings are controlled through the `boxlang.*` property namespace; sensible defaults require no changes for basic use.
* 📄 **Custom `boxlang.json` support** — supply your own BoxLang configuration file via classpath, file URI, or absolute path.
* 🔀 **Pluggable resolver order** — configure the view resolver's position in the Spring MVC resolver chain so BoxLang can coexist with Thymeleaf, FreeMarker, or any other view technology.
* 🏷️ **Spring Boot 3 / Jakarta EE ready** — built against Spring Boot 3.x and the `jakarta.*` namespace.

## 📋 Requirements

<table><thead><tr><th width="374">Dependency</th><th>Version</th></tr></thead><tbody><tr><td>☕ Java</td><td>21+</td></tr><tr><td>🍃 Spring Boot</td><td>3.x+</td></tr><tr><td>🥊 BoxLang</td><td>1.11.0+</td></tr></tbody></table>

{% hint style="info" %}
Make sure `JAVA_HOME` points to a JDK 21+ installation before building or running.
{% endhint %}

## 📦 Installation

### Gradle

```groovy
dependencies {
    implementation 'io.boxlang:boxlang-spring-boot-starter:1.0.0'
}
```

### Maven

```xml
<dependency>
    <groupId>io.boxlang</groupId>
    <artifactId>boxlang-spring-boot-starter</artifactId>
    <version>1.0.0</version>
</dependency>
```

{% hint style="success" %}
No `@EnableBoxLang` annotation or manual bean registration is required. Spring Boot's auto-configuration mechanism detects the starter on the classpath and configures everything automatically.
{% endhint %}

## 🚀 Quick Start

Get a BoxLang-powered Spring Boot application running in minutes.

{% stepper %}

{% step %}
### Add the dependency

Add `boxlang-spring-boot-starter` to your project as shown in the [Installation](spring-boot.md#installation) section.

{% endstep %}

{% step %}
### Create a Spring MVC controller

```java
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class HomeController {

    @GetMapping( "/" )
    public String home( Model model ) {
        model.addAttribute( "title", "Hello from BoxLang + Spring Boot!" );
        model.addAttribute( "framework", "Spring Boot 3" );
        return "home"; // resolves to classpath:/templates/home.bxm
    }

    @GetMapping( "/greeting" )
    public String greeting(
        @RequestParam( name = "name", defaultValue = "World" ) String name,
        Model model
    ) {
        model.addAttribute( "name", name );
        model.addAttribute( "message", "Welcome, " + name + "!" );
        return "greeting"; // resolves to classpath:/templates/greeting.bxm
    }

    @GetMapping( "/items" )
    public String items( Model model ) {
        model.addAttribute( "items", java.util.List.of( "Apple", "Banana", "Cherry" ) );
        model.addAttribute( "count", 3 );
        return "items"; // resolves to classpath:/templates/items.bxm
    }
}
```

{% endstep %}

{% step %}
### Create BoxLang templates

Place `.bxm` templates under `src/main/resources/templates/`:

**`src/main/resources/templates/home.bxm`**

```html
<bx:output>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#variables.title#</title>
</head>
<body>
    <-/tmp Variables are available directly or via the variables scope -->
    <h1>#title#</h1>
    <p>Framework: #framework#</p>
    <p>Rendered at: #dateTimeFormat( now(), "full" )#</p>

    <ul>
        <li><a href="/greeting">Default greeting</a></li>
        <li><a href="/greeting?name=Developer">Greeting with name</a></li>
        <li><a href="/items">Items list</a></li>
    </ul>
</body>
</html>
</bx:output>
```

**`src/main/resources/templates/greeting.bxm`**

```html
<bx:output>
<h2>#message#</h2>
<p><a href="/">Back Home</a></p>
</bx:output>
```

**`src/main/resources/templates/items.bxm`**

```html
<bx:output>
<h2>Items (#count#)</h2>
<ul>
    <bx:loop array="#items#" item="itemName">
        <li>#itemName#</li>
    </bx:loop>
</ul>
<p><a href="/">Back Home</a></p>
</bx:output>
```

{% endstep %}

{% step %}
### Run your application

Start your Spring Boot application as usual.

> **Important JVM Requirements:** BoxLang requires reflective access to JDK internals. Ensure you pass the following JVM arguments when starting the application:
>
> ```
> --add-opens java.base/java.lang=ALL-UNNAMED
> --add-opens java.base/java.lang.reflect=ALL-UNNAMED
> ```
>
> In a Gradle project, this can be added to your `bootRun` task:
>
> ```groovy
> bootRun {
>     jvmArgs = [
>         '--add-opens', 'java.base/java.lang=ALL-UNNAMED',
>         '--add-opens', 'java.base/java.lang.reflect=ALL-UNNAMED'
>     ]
> }
> ```

Navigate to `http://localhost:8080` in your browser.

{% endstep %}
{% endstepper %}

## ⚙️ Configuration (`application.properties`)

The starter registers `BoxLangProperties` under the `boxlang.*` namespace.

| Property                      | Type      | Default                 | Description                                                                                                                                                                                           |
| ----------------------------- | --------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `boxlang.prefix`              | `String`  | `classpath:/templates/` | Directory path where `.bxm` templates are located.                                                                                                                                                    |
| `boxlang.suffix`              | `String`  | `.bxm`                  | File extension for BoxLang templates.                                                                                                                                                                 |
| `boxlang.config-path`         | `String`  | _(none)_                | Location of the BoxLang runtime configuration file (e.g., `classpath:/boxlang.json`). If not set, it defaults to checking `classpath:/boxlang.json` and then falls back to internal runtime defaults. |
| `boxlang.debug-mode`          | `boolean` | `false`                 | Enables BoxLang debug mode. Useful for development logging.                                                                                                                                           |
| `boxlang.view-resolver-order` | `int`     | `2147483642`            | The priority of the BoxLang view resolver in Spring’s resolver chain. Default is `Ordered.MAX_VALUE - 5`.                                                                                             |
| `boxlang.runtime-home`        | `String`  | _(none)_                | Overrides the global `BOXLANG_HOME` environment directory.                                                                                                                                            |

### Example `application.properties`

```properties
boxlang.prefix=classpath:/templates/
boxlang.suffix=.bxm
boxlang.config-path=classpath:/boxlang.json
boxlang.debug-mode=false
boxlang.view-resolver-order=1

logging.level.ortus.boxlang=WARN
logging.level.org.springframework.web=INFO
```

## 📄 BoxLang Configuration (`boxlang.json`)

If no `boxlang.config-path` is set, the auto-configuration probes for `classpath:/boxlang.json` automatically. If that file is absent, BoxLang starts with its built-in defaults.

Place `boxlang.json` at `src/main/resources/boxlang.json` to customise language behaviour. For more info, please see the [Configuration](../configuration.md) documentation.

## 🌐 Template Scopes & Model Integration

BoxLang templates rendered through the view engine have access to all standard BoxLang web scopes:

| Scope       | Description                                                          |
| ----------- | -------------------------------------------------------------------- |
| `variables` | Contains all Spring `Model` attributes plus template-local variables |
| `url`       | Query string parameters from the HTTP request                        |
| `form`      | Form POST data                                                       |
| `cgi`       | CGI/server environment variables                                     |
| `cookie`    | HTTP cookies                                                         |
| `request`   | Request-scoped storage (per HTTP request)                            |

**Accessing Spring Model attributes:**

```html
<bx:output>
    <-/tmp Both forms are equivalent -->
    <p>#variables.title#</p>
    <p>#title#</p>

    <-/tmp Access URL query params -->
    <p>Page: #url.page ?: 1#</p>

    <-/tmp Access cookies -->
    <p>Theme: #cookie.theme ?: "light"#</p>
</bx:output>
```

{% hint style="warning" %}
**Security tip:** Always use `encodeForHTML()` when outputting user-supplied values (e.g., URL or form parameters) to prevent XSS attacks.
{% endhint %}

## 🔥 Hot-Reloading Templates

By default, `boxlang.prefix` points at `classpath:/templates/`, which resolves to the compiled output directory (`build/resources/main/templates/`). Editing a `.bxm` source file has no effect until your build tool copies the updated resource — meaning a restart is usually required.

**To get instant hot-reload without a restart**, switch the prefix to a `file:` path that points directly at the source tree using a Spring dev profile.

### 1. Create `src/main/resources/application-dev.properties`

```properties
# Load templates directly from the source tree — edits take effect on the next request
boxlang.prefix=file:src/main/resources/templates/

# Enable BoxLang debug mode in development
boxlang.debug-mode=true

# Verbose logging in development
logging.level.ortus.boxlang=DEBUG
logging.level.org.springframework.web=DEBUG
```

### 2. Activate the dev profile

```bash
# Pass it as a command-line argument (Gradle example)
./gradlew bootRun --args='--spring.profiles.active=dev'

# Or set it permanently during development in application.properties
echo 'spring.profiles.active=dev' >> src/main/resources/application.properties
```

{% hint style="danger" %}
Keep the `classpath:` prefix for production. The `file:` path works for local development but must not be used in packaged JARs or containers where the source tree is not present.
{% endhint %}

## 🔍 How It Works

1. **Auto-configuration** — `BoxLangAutoConfiguration` is registered and activates on any Servlet-based Spring web application.
2. **Runtime lifecycle** — the `BoxRuntime` is started very early in the application lifecycle, ensuring it is ready before the first HTTP request arrives. It shuts down gracefully when the application context stops.
3. **View resolution** — `BoxLangViewResolver` resolves logical view names to resources using the configured `prefix` + `viewName` + `suffix` pattern. If the resource does not exist, it returns `null` and Spring continues to the next resolver in the chain, enabling seamless coexistence with other view technologies like Thymeleaf or FreeMarker.
4. **Template rendering** — `BoxLangView` wraps the `HttpServletRequest` and `HttpServletResponse` in a `SpringBoxHTTPExchange`, constructs a `WebRequestBoxContext` (which exposes all BoxLang web scopes), injects the Spring `Model` map into the `variables` scope, executes the template, and flushes the output buffer to the servlet response.
