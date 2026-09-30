---
description: BoxLang Runtime for Microsoft Azure Functions! Serverless for the win!
icon: microsoft
---

# Azure Functions

## What is Azure Functions?

Azure Functions is a serverless computing service provided by Microsoft Azure that lets you run code without provisioning or managing servers. It automatically scales applications by running code in response to events and allocates compute resources as needed, allowing developers to focus on writing code rather than managing infrastructure ([https://learn.microsoft.com/en-us/azure/azure-functions/](https://learn.microsoft.com/en-us/azure/azure-functions/)).

The **BoxLang Azure Functions Runtime** allows you to code in BoxLang and create Azure Functions in this ecosystem. We provide you a nice template so you can work with serverless: [https://github.com/ortus-boxlang/boxlang-starter-azure-functions](https://github.com/ortus-boxlang/boxlang-starter-azure-functions). This template will give you a turnkey application with features like:

* Unit and Integration Testing
* Java dependency management via Gradle
* BoxLang dependency management
* Class compilation caching for improved performance
* Configuration management with environment overrides
* Official Azure Functions Gradle plugin for local run and deployment
* GitHub actions to: test, build and release automatically

{% @github-files/github-code-block url="https://github.com/ortus-boxlang/boxlang-starter-azure-functions" %}

{% hint style="success" %}
**Cloud-agnostic by design**: The Azure runtime is a structural mirror of the [AWS Lambda](aws-lambda.md) and [Google Cloud Functions](google-cloud-functions.md) runtimes - same `handlers/` routing convention, same `manifest.json` build-time routing table, same `x-bx-function` header dispatch, and the exact same `run( event, context, response )` handler contract. Your `.bx` code can move between all three providers unmodified.
{% endhint %}

## BoxLang Azure Function Handler

Our BoxLang Azure Handler acts as a front controller to all incoming Function executions. It provides you with:

* Automatic request management to an `event` structure
* Automatic logging and tracing
* Execution of your handler classes by convention
* Automatic error management and exception handling
* Automatic response management and serialization
* Life-Cycle Events via our `Application.bx`
* Class compilation caching for improved performance
* Custom method resolution via headers

The BoxLang Azure runtime provides a pre-built Java entry point already configured to accept an HTTP request as a BoxLang Struct and then output either by returning a simple or complex object or using our `response` convention struct. Our runtime will automatically convert your results to JSON.

{% hint style="warning" %}
**The `Function.java` wrapper**: Unlike AWS Lambda or Google Cloud Functions (where the entry point is just a configuration string), the Azure Functions build plugins only scan **your own project's compiled classes** for `@FunctionName` methods when generating `function.json` - they never look inside dependency jars. Since the actual routing/execution logic lives in the `boxlang-azure-functions` runtime dependency, the starter template includes a two-line wrapper class (`src/main/java/com/myproject/Function.java`) that carries the `@FunctionName`/`@HttpTrigger` annotations and forwards every request straight to `AzureFunctionRunner`. You should never need to touch this file.
{% endhint %}

{% hint style="info" %}
You can see the code for the handler here: [https://github.com/ortus-boxlang/boxlang-azure-functions](https://github.com/ortus-boxlang/boxlang-azure-functions)
{% endhint %}

The handler will look for a `Lambda.bx` in your package and execute the `run()` method by convention - the same default handler filename used across all three BoxLang serverless runtimes.

{% code title="Lambda.bx" %}
```java
class {

    function run( event, context, response ){


    }

}
```
{% endcode %}

## Environment Variables

The following are all the environment variables the Azure Functions runtime can read and detect. If they are set by you or the Azure Functions host, then it will use those values to alter operations.

| Environment Variable | Description |
|---------------------|-------------|
| `BOXLANG_AZURE_ROOT` | Root directory for `.bx` files. Defaults to the Azure-provided `AzureWebJobsScriptRoot`, else `/home/site/wwwroot`. |
| `BOXLANG_AZURE_CLASS` | Absolute path to the default handler to execute. The default is `Lambda.bx` at the function root. |
| `BOXLANG_AZURE_DEBUGMODE` | Turn runtime debug mode on or off. When enabled, disables handler-class caching so `.bx` changes are picked up immediately, and enables verbose logging. |
| `BOXLANG_AZURE_CONFIG` | Absolute path to a custom `boxlang.json` configuration for the runtime. Defaults to `boxlang.json` in the function root. |

You can also leverage ANY environment variable to configure the BoxLang runtime using our runtime [environment conventions](../configuration.md).

## BoxLang Azure Functions Template

The BoxLang default template for Azure Functions can be found here: [https://github.com/ortus-boxlang/boxlang-starter-azure-functions](https://github.com/ortus-boxlang/boxlang-starter-azure-functions). The structure of the project is the following:

```
/.vscode - Some useful vscode tasks and settings
/gradle - The gradle runtime, keep in source control
/host.json - Azure Functions host configuration (routePrefix is set to "")
/local.settings.json.example - Copy to local.settings.json for local runs
/src
  + main
    + java
      + com
        + myproject
          + Function.java (Thin Azure entry point - forwards to AzureFunctionRunner)
    + bx
      + Application.bx (Your life-cycle class)
      + Lambda.bx (Your default BoxLang handler)
      + handlers (Routed handlers, see Convention-Based URI Routing below)
      + manifest.json (Generated by `./gradlew generateManifest`, gitignored)
  + resources
    + boxlang.json (A custom BoxLang configuration file)
    + boxlang_modules (Where you will install BoxLang modules)
  + test
    + java
      + com
        + myproject
          + AzureFunctionIntegrationTest.java (An integration test for your function)
          + mocks (Mock Azure request/context objects for fast, no-network tests)
/box.json - Your project's dependency descriptor for CommandBox
/build.gradle - The gradle build configuration, including the azurefunctions {} plugin config
/gradle.properties - Where you store your version and metadata
/gradlew - The gradle shell executor, keep in source control
/gradlew.bat - The gradle shell executor, keep in source control
/settings.gradle - The project settings
```

The BoxLang Azure Functions runtime will look for a `Lambda.bx` in your package by convention and execute the `run()` method for you.

### Key Template Features

* **Configuration Management**: `boxlang.json` controls caching, class generation, logging, and timeouts
* **Official Azure Plugin Integration**: `azureFunctionsRun`/`azureFunctionsPackage`/`azureFunctionsDeploy` via the official `com.microsoft.azure.azurefunctions` Gradle plugin
* **Gradle Dependency Resolution**: Automatic dependency management via Gradle
* **Performance Optimizations**: Class caching built-in
* **Local Testing**: Fast, mock-based integration tests plus a real local HTTP server via `azureFunctionsRun`
* **AI Development Support**: Comprehensive GitHub Copilot instructions for enhanced development experience

{% hint style="info" %}
**AI-Assisted Development**: The BoxLang Azure Functions template includes comprehensive GitHub Copilot instructions (`.github/copilot-instructions.md`) that provide AI assistants with detailed context about:

* Project architecture and conventions
* Build system and deployment workflows
* Convention-based routing patterns
* Configuration management
* Testing strategies and file locations

This enables more accurate and contextual assistance when developing BoxLang Azure Functions.
{% endhint %}

### Building and Testing

```bash
# Copy the local settings template
cp local.settings.json.example local.settings.json

# Regenerate manifest.json from src/main/bx/handlers/ (also runs automatically
# before test/azureFunctionsRun/azureFunctionsPackage/azureFunctionsDeploy)
./gradlew generateManifest

# Run the tests
./gradlew test

# Build the project
./gradlew build

# Start a local Azure Functions host (via Azure Functions Core Tools)
./gradlew azureFunctionsRun

# Clean build artifacts
./gradlew clean
```

## Lambda.bx

The default handler is a BoxLang class with a single function called `run()`.

<pre class="language-groovy" data-title="Lambda.bx" data-line-numbers><code class="lang-groovy"><strong>/**
</strong> * My BoxLang Azure Function
 */
class{

	function run( event, context, response ){
		response.body = {
			"error": false,
			"messages": [],
			"data": "====> Incoming event " &#x26; event.toString()
		};
		response.statusCode = 200;
	}
}
</code></pre>

### Arguments

It accepts three arguments:

<table><thead><tr><th width="137">Argument</th><th width="264">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>event</code></td><td><code>Struct</code></td><td>The incoming HTTP request as a BoxLang struct (method, path, headers, body, queryStringParameters, requestContext.http, etc.) - the same shape used by the AWS Lambda and Google Cloud Functions runtimes.</td></tr><tr><td><code>context</code></td><td><code>Struct</code></td><td>The Azure runtime context struct: <code>functionName</code>, <code>invocationId</code>, <code>requestId</code>.</td></tr><tr><td><code>response</code></td><td><code>Struct</code></td><td>A BoxLang struct convention for a response.</td></tr></tbody></table>

{% hint style="success" %}
The `context` struct's `invocationId` is sourced directly from Azure's `com.microsoft.azure.functions.ExecutionContext#getInvocationId()`, so you can correlate it with Application Insights / Azure Monitor traces.
{% endhint %}

#### Event

The `event` structure is a snapshot of the input to your function. We deserialize the incoming HTTP request for you and give you a nice struct.

#### Context

This is a BoxLang struct built from Azure's `ExecutionContext` Java object, which provides invocation metadata. For more information on the underlying Java type, check out [Microsoft's Azure Functions Java reference](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-java).

#### Context fields

* `functionName` - The name of the Azure Function, from `ExecutionContext#getFunctionName()`.
* `invocationId` - The unique identifier for this invocation, from `ExecutionContext#getInvocationId()`. Use this to correlate with Application Insights traces.
* `requestId` - Alias of `invocationId`, for naming parity with the AWS/GCF context structs.

#### Response

The `response` argument is our convention to help you build a nice return structure. However, it is completely optional. You can easily return a simple or complex object from your function, and we will convert it to JSON.

```json
response : {
  statusCode : 200,
  headers : {
    content-type :  "application/json",
    access-control-allow-origin : "*",
  },
  body : YourFunction.run() results
}
```

{% code lineNumbers="true" %}
```groovy
/**
 * My BoxLang Azure Function Simple Return
 */
class{

  function run( event, context, response ){
    return "Hello World!"
  }

}

/**
 * My BoxLang Azure Function Complex Return
 */
class{

  function run( event, context, response ){
    return {
      age : 1,
      when : now(),
      data : [ 12,3234,23423 ]
    };
  }

}
```
{% endcode %}

Now you can go ahead and build your function. You can use TestBox to unit test your `Lambda.bx`, or use the included Java integration test in `src/test/java/com/myproject/AzureFunctionIntegrationTest.java`, which exercises the full request pipeline against `AzureFunctionRunner` directly using mock Azure request/context objects - no live Azure environment needed. Just run `./gradlew test` or use VSCode BoxLang IDE to run the tests. Now we go to production!

## Convention-Based URI Routing

The runtime supports automatic routing using a **`handlers/` directory convention**, allowing you to build multi-class functions with BoxLang easily following our conventions.

{% hint style="danger" %}
**Security note**: Only files under a `handlers/` directory (or listed in a build-time `manifest.json`) are ever eligible routing targets. `Application.bx` and the default `Lambda.bx` are never routable, no matter what's on disk.
{% endhint %}

When your function is exposed as a URL, the runtime automatically routes to different BoxLang classes under `src/main/bx/handlers/` based on the URI path:

```javascript
// URL: /products      -> handlers/Products.bx
// URL: /home-savings   -> handlers/HomeSavings.bx
// URL: /api/test       -> handlers/api/Test.bx
```

### Example Multi-Class Structure

```
/src/main/bx/
  ├── Lambda.bx                # Default handler (fallback)
  ├── Application.bx           # Never a routing target
  ├── manifest.json            # Generated, see below
  └── handlers/
      ├── Products.bx          # Handles /products
      ├── HomeSavings.bx       # Handles /home-savings
      └── api/
          └── Test.bx          # Handles /api/test (nested)
```

Each class should implement a `run` function:

```groovy
// handlers/Products.bx
class {
    function run( event, context, response ) {
        return {
            "statusCode" : 200,
            "body" : serializeJSON( getProductCatalog() )
        };
    }

    function getProductCatalog() {
        return [
            { "id": 1, "name": "BoxLang Runtime" },
            { "id": 2, "name": "CommandBox" }
        ];
    }
}
```

### URI to Class Name Conversion

The routing follows these conventions:

* `/products` → `handlers/Products.bx`
* `/home-savings` → `handlers/HomeSavings.bx`
* `/user-profile` → `handlers/UserProfile.bx`
* `/api/test` → `handlers/api/Test.bx` (nested)

Hyphens are converted to PascalCase for the **leaf filename only**. Subdirectories under `handlers/` can use any case you like and are matched literally (lowercased), so `handlers/Api/Test.bx` and `handlers/api/Test.bx` both register as `/api/test`. Matching is case-insensitive, and the longest matching prefix wins, so a request like `/products/categories/electronics` still falls through to the flat `products` route when no more specific nested route exists - a request to a route that isn't registered anywhere just runs `Lambda.bx`, same as if routing had never happened.

### Understanding `manifest.json`

`manifest.json` is the routing table behind Convention-Based URI Routing. It's a plain JSON file listing every handler under `handlers/`, mapped from its route key to its relative file path, plus the default handler and the filenames that can never be routed to. The runtime reads it **once, at cold start** - it never scans the filesystem at request time.

**Example** - generated from a `handlers/Products.bx` and a nested `handlers/api/Test.bx`:

```json
{
	"manifestVersion": 1,
	"generatedAt": "2026-01-15T10:32:01Z",
	"generator": "boxlang-starter-azure-functions-gradle",
	"defaultHandler": { "file": "Lambda.bx", "method": "run" },
	"handlers": {
		"products": { "file": "handlers/Products.bx" },
		"api/test": { "file": "handlers/api/Test.bx" }
	},
	"reserved": ["Application.bx", "Lambda.bx"]
}
```

**Creating or recreating it**: run the `generateManifest` Gradle task. It scans `handlers/` and rewrites `manifest.json` next to `Lambda.bx`:

```bash
./gradlew generateManifest
```

You'll rarely need to run this by hand - it's wired as a dependency of `test`, `azureFunctionsRun`, `azureFunctionsPackage`, and `azureFunctionsDeploy`, so it's always regenerated before you test, run, package, or deploy. `manifest.json` is gitignored; never edit it by hand or commit it, since any change you make is overwritten on the next build.

If it's ever missing or invalid at cold start (for example, a deployment package built without running `generateManifest`), the runtime falls back to scanning `handlers/` directly, and if that directory doesn't exist either, to scanning the function root for backward compatibility with pre-`handlers/` deployments - always excluding `Application.bx` and `Lambda.bx` from that last, legacy tier. Either fallback logs a `WARNING` in your function logs listing every handler it discovered and registered, so a stale or missing manifest is never a silent surprise - check Application Insights / the Azure portal's log stream if routing looks off after a deploy.

## Multiple Functions Header

The runtime also allows you to create other functions inside of your `Lambda.bx` (or any `handlers/` class) that can be targeted when your Azure Function is exposed as a URL, by using the following header when executing your function:

```bash
x-bx-function=methodName
```

This makes it incredibly flexible where you can respond to that incoming header in a different function than the one by convention.

{% hint style="info" %}
This header can only ever reach a `public` (or `remote`) method - BoxLang's own scope rules mean a `private` method is never even visible to the runtime's dispatch mechanism, the same rule that governs any other BoxLang class. Don't mark a method public if you don't want it externally callable this way.
{% endhint %}

## Azure Function Modules

You can use any BoxLang module with the BoxLang Azure Functions runtime by installing them to the `src/resources/boxlang_modules` folder. All modules placed there during the build process will be packaged into your deployment.

```bash
# Using CommandBox to install modules directly
box install id=bx-module directory=src/resources/boxlang_modules

# Or add them to box.json and install
cd src/resources && box install
```

## Local Development & Testing

The template provides two layers of local testing:

### Fast, Mock-Based Integration Tests

```bash
./gradlew test
```

These run against `AzureFunctionRunner` directly with mock Azure request/context objects - no network, no Core Tools, no live Azure environment needed. This is what CI runs.

### Real Local HTTP Server

```bash
# Start a local Azure Functions host (requires Azure Functions Core Tools)
./gradlew azureFunctionsRun
```

Then test with curl in another terminal:

```bash
curl http://localhost:7071/
curl http://localhost:7071/products
curl http://localhost:7071/api/test
curl http://localhost:7071/ -H "x-bx-function: anotherLambda"
```

Set `BOXLANG_AZURE_DEBUGMODE=true` in `local.settings.json` to enable verbose logging and disable class caching, so `.bx` file changes are reflected immediately without a restart.

## Deploy to Azure

You can deploy your function using the official Azure Functions Gradle plugin or GitHub Actions.

### Gradle Deployment

```bash
az login

export AZURE_SUBSCRIPTION_ID=<your-subscription-id>
export AZURE_RESOURCE_GROUP=<your-resource-group>
export AZURE_FUNCTION_APP_NAME=<your-function-app-name>
export AZURE_REGION=eastus

./gradlew azureFunctionsDeploy
```

The `azurefunctions {}` block in `build.gradle` reads all deployment settings from these environment variables - nothing is hard-coded, so the same `build.gradle` works in CI/CD and locally.

### GitHub Actions Deployment

```yaml
- name: Deploy BoxLang Azure Function
  run: |
    ./gradlew azureFunctionsDeploy
  env:
    AZURE_SUBSCRIPTION_ID: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
    AZURE_RESOURCE_GROUP: ${{ secrets.AZURE_RESOURCE_GROUP }}
    AZURE_FUNCTION_APP_NAME: ${{ secrets.AZURE_FUNCTION_APP_NAME }}
    AZURE_REGION: ${{ secrets.AZURE_REGION }}
```

{% hint style="warning" %}
The GitHub Actions runner needs to be authenticated to Azure first (e.g. via `azure/login@v2` with a service principal or OIDC federated credential) before `azureFunctionsDeploy` can run.
{% endhint %}

### Manual Deployment via the Azure Portal

1. Build the project: `./gradlew azureFunctionsPackageZip`
2. Log in to the [Azure Portal](https://portal.azure.com) and create (or select) a Function App
3. Choose **Java 21** as your runtime stack and **Linux** as your OS
4. Deploy the generated zip from `build/azure-functions/` using your preferred method (Azure CLI `func azure functionapp publish`, the portal's deployment center, or a CI/CD pipeline)

{% hint style="danger" %}
Please note that the memory/plan tier you choose determines your CPU allocation as well. For consistent cold-start performance, consider a Premium plan over Consumption for production workloads.
{% endhint %}

## Runtime Source Code

The Azure Functions Runtime source code can be found here: [https://github.com/ortus-boxlang/boxlang-azure-functions](https://github.com/ortus-boxlang/boxlang-azure-functions)

### Performance Best Practices

For optimal performance with the BoxLang Azure Functions runtime:

1. **Enable Class Caching**: Use `trustedCache=true` in your `boxlang.json` for production
2. **Memory/Plan Allocation**: Consider a Premium plan for consistent cold-start performance in production
3. **Static Initialization**: The runtime already uses static blocks for expensive one-time setup - avoid adding your own heavy work to `Application.bx`'s `onApplicationStart()`
4. **Early Returns**: Validate input early and return immediately on errors

We welcome any pull requests, testing, documentation contributions, and feedback.
