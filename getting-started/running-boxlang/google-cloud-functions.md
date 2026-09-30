---
description: Run BoxLang on Google Cloud Functions with the official starter and runtime
icon: google
---

# BoxLang on Google Cloud Functions

Run BoxLang handlers on Google Cloud Functions Gen 2 using the Java 21 runtime and the BoxLang GCF bridge entry point: `ortus.boxlang.runtime.gcp.FunctionRunner`.

This page matches the current starter project and runtime behavior.

{% hint style="success" %}
BoxLang serverless functions are portable across providers. The same handler code written for Google Cloud Functions also runs unmodified on [AWS Lambda](aws-lambda.md) and [Azure Functions](azure-functions.md), giving you a single codebase you can deploy anywhere.
{% endhint %}

## 🚀 What You Get

- BoxLang handler files in `src/main/bx`
- Convention-based routing from URI to handler class
- Local HTTP server via the Google Functions Java Invoker
- Deployable ZIP with handlers, config, modules, and runtime JAR

## 🏛️ Runtime + Starter Architecture

This experience is intentionally a combination of two projects:

- **Starter project** (`boxlang-starter-google-functions`): your app shell, handlers, tests, and Gradle tasks
- **Runtime project** (`boxlang-google-functions`): the Java bridge that adapts GCF HTTP requests to BoxLang execution

The runtime entry point is:

- `ortus.boxlang.runtime.gcp.FunctionRunner`

At execution time, the runtime handles:

- HTTP request mapping into a BoxLang-friendly `event` struct
- route resolution from URI to `.bx` handler file
- class compilation/loading and warm-invocation class caching
- method dispatch (default `run()` or `x-bx-function` override)
- response mapping from BoxLang `response` struct to GCF HTTP output

This split lets you keep all business logic in BoxLang files while using Java only as the serverless runtime bridge.

## 🔬 Runtime Execution Flow

```text
HTTP Request
    -> Google Cloud Functions Gen 2 (java21)
    -> FunctionRunner (HttpFunction)
    -> RequestMapper (HttpRequest -> event struct)
    -> Route resolution (URI path -> routing table built at cold start -> .bx file)
    -> Handler compilation/load (cached on warm invocations)
    -> Method resolution (x-bx-function header or run)
    -> BoxLang handler method execution
    -> ResponseMapper (response struct -> HttpResponse)
```

{% hint style="danger" %}
**Security note**: Only files under a `handlers/` directory (or listed in a build-time `manifest.json`) are ever eligible routing targets. Earlier versions of this runtime (before 1.18.0) routed to *any* `.bx` file at the function root, including `Application.bx` and `Lambda.bx` themselves, which allowed an unauthenticated request to reach lifecycle callbacks and any other public method via the `x-bx-function` header. If you're on an older runtime, upgrade to 1.18.0+ and move your routed handlers into `handlers/`.
{% endhint %}

## ⚡ Cold Start, Warm Start, and Debug Mode

- **Cold start:** runtime initializes in the container before first request handling.
- **Warm invocations:** compiled handler classes are reused to avoid repeated compilation work.
- **Debug mode (`BOXLANG_GCP_DEBUGMODE=true`):** class caching is disabled so handler edits are picked up quickly during development.
- **Production guidance:** keep debug mode off for best performance.

## 🔁 Portability Notes

The runtime keeps the handler contract familiar across serverless targets. In practice, many handler patterns can be shared between BoxLang AWS Lambda and BoxLang GCF with minimal changes.

## ✅ Requirements

| Requirement | Version |
| --- | --- |
| Java | 21 |
| Google Cloud SDK (`gcloud`) | Latest |
| Gradle | Wrapper included |

## 📦 Starter Project Setup

Use the official starter:

```bash
git clone https://github.com/ortus-boxlang/boxlang-starter-google-functions.git
cd boxlang-starter-google-functions
```

Run tests once to verify your environment:

```bash
./gradlew clean test
```

Regenerate `manifest.json` from `src/main/bx/handlers/` any time (also runs automatically before `test`, `runFunction`, and `buildLambdaZip`):

```bash
./gradlew generateManifest
```

## 🧪 Launch Locally

Start the local function server:

```bash
./gradlew runFunction
```

By default it runs on port `9099` and uses `src/main/bx` as the function root.

Try a request:

```bash
curl http://localhost:9099/
```

Call a specific method via header:

```bash
curl -H "x-bx-function: anotherLambda" http://localhost:9099/
```

Send JSON payload:

```bash
curl -X POST http://localhost:9099/ \
  -H "Content-Type: application/json" \
  -d @workbench/sampleRequests/event-local.json
```

### Local overrides

```bash
./gradlew runFunction -PtestPort=8080
./gradlew runFunction -PdebugMode=true
./gradlew runFunction -PfunctionRoot=/absolute/path/to/bx/files
```

### Local `runFunction` Runner Details

The starter's `runFunction` Gradle task uses the official Google Functions Java Invoker and wires it to the BoxLang runtime entry point.

What it does:

- launches `com.google.cloud.functions.invoker.runner.Invoker`
- passes `ortus.boxlang.runtime.gcp.FunctionRunner` as the target
- sets `BOXLANG_GCP_ROOT` to your function root (default: `src/main/bx`)
- sets `BOXLANG_GCP_DEBUGMODE` from `-PdebugMode` or defaults
- runs on `-PtestPort` (default `9099`)

Expected startup banner:

```text
================================================================
 BoxLang GCF Function Invoker
 Listening on  : http://localhost:9099
 Function root : .../src/main/bx
 Debug mode    : true|false
 Press Ctrl+C to stop.
================================================================
```

Runner troubleshooting:

- **Port in use:** start with `-PtestPort=8080`
- **Wrong handlers loaded:** point to the right folder with `-PfunctionRoot=...`
- **Code changes not reflected:** use `-PdebugMode=true` during development
- **Missing default route:** ensure `Lambda.bx` exists in the configured function root

## 🧩 Handler Contract

Each handler method receives:

- `event`: HTTP request data mapped into a struct
- `context`: function metadata (name, revision, project, request id)
- `response`: mutable response struct (`statusCode`, `headers`, `body`, `cookies`)

Default method is `run()`.

### Event Struct Shape

The runtime maps each incoming HTTP request into an `event` struct designed for serverless portability.

```js
{
    method: "GET",
    path: "/products/42",
    rawPath: "/products/42",
    headers: {
        "content-type": "application/json"
    },
    queryStringParameters: {
        page: "1"
    },
    body: "",
    requestContext: {
        http: {
            method: "GET",
            path: "/products/42"
        }
    }
}
```

### Context Struct Shape

The `context` struct contains runtime metadata:

- `functionName`
- `functionVersion`
- `projectId`
- `requestId`

### Response Struct Shape

The runtime provides a mutable `response` struct:

```js
{
    statusCode: 200,
    headers: {
        "Content-Type": "application/json"
    },
    body: "",
    cookies: []
}
```

Response behavior:

- Returning a struct or array from your method will be JSON serialized.
- Returning a plain string writes that string as the response body.
- Writing to `response.body` gives explicit control over output.

### Example handler

```js
class {

    function run( event, context, response ) {
        response.statusCode = 200
        response.body = {
            "error": false,
            "messages": [],
            "data": "====> Incoming event " & event.toString()
        }
    }

    function anotherLambda( event, context, response ) {
        return "Hola!!"
    }

}
```

## 🛣️ Convention-Based Routing

The runtime supports multi-routing by resolving the URI path against a routing table built once at cold start, from files under `src/main/bx/handlers/`.

Routing algorithm (built once, at cold start - never per request):

1. If `manifest.json` exists at the function root and is valid, use it as the routing table directly. No filesystem scanning happens.
1. Otherwise, if `handlers/` exists, scan it once (recursively - nested folders are supported) and log a `WARNING` listing every handler registered.
1. Otherwise, scan the function root itself once, for backward compatibility with deployments that predate the `handlers/` convention - always excluding `Application.bx` and the default handler class, regardless of what's on disk - and log the same `WARNING`.

At request time, the resolved table is matched against the full URI path, longest-prefix first, so `/products/categories/electronics` still falls through to a flat `products` route when no more specific route is registered. A request to a route that isn't registered anywhere just runs `Lambda.bx`, same as if routing had never happened.

### URI to Handler Mapping

| Request URI | Resolved Handler |
| --- | --- |
| `/` | `Lambda.bx` |
| `/customers` | `handlers/Customers.bx` |
| `/customers/123` | `handlers/Customers.bx` |
| `/products` | `handlers/Products.bx` |
| `/user-profiles` | `handlers/UserProfiles.bx` |
| `/api/test` | `handlers/api/Test.bx` (nested) |
| `/unknown` | `Lambda.bx` |

### Multi-Handler Layout

```text
src/main/bx/
  Application.bx     # never a routing target
  Lambda.bx           # fallback and root route
  manifest.json        # generated, see below
  handlers/
    Customers.bx      # handles /customers/**
    Products.bx       # handles /products/**
    UserProfiles.bx   # handles /user-profiles/**
    api/
      Test.bx          # handles /api/test (nested)
```

The resolved segment(s) select the class; only the leaf `.bx` filename needs to be PascalCase, folder names under `handlers/` can be any case and are matched case-insensitively. Remaining URI segments are still available via `event.path` for your own parsing.

### Understanding `manifest.json`

`manifest.json` is the routing table behind the convention-based routing above. It's a plain JSON file listing every handler under `handlers/`, mapped from its route key to its relative file path, plus the default handler and the filenames that can never be routed to. The runtime reads it **once, at cold start** - it never walks the filesystem on a live request.

**Example** - generated from a `handlers/Products.bx` and a nested `handlers/api/Test.bx`:

```json
{
	"manifestVersion": 1,
	"generatedAt": "2026-01-15T10:32:01Z",
	"generator": "boxlang-starter-google-functions-gradle",
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

You'll rarely need to run this by hand - it's wired as a dependency of `test`, `runFunction`, and `buildLambdaZip`, so it's always regenerated before you test, run, or package. It's gitignored; never edit it by hand or commit it, since any change you make is overwritten on the next build.

If it's ever missing or invalid at cold start, the runtime falls back to scanning `handlers/` (or the function root) directly, and logs a `WARNING` in your function logs listing every handler it discovered - check your logs if routing looks off after a deploy that skipped `generateManifest`.

### Multi-Routing Handler Example

```js
class {

    function run( event, context, response ) {
        response.statusCode = 200
        response.body = {
            "error": false,
            "resource": "customers",
            "path": event.path,
            "method": event.method
        }
    }

    function findById( event, context, response ) {
        response.statusCode = 200
        response.body = {
            "error": false,
            "action": "findById",
            "path": event.path
        }
    }

}
```

## 🔀 Method Routing with x-bx-function

After URI routing resolves the handler class, method routing can choose which function to invoke.

- Without header, runtime calls `run()`.
- With header, runtime attempts the named method.

```bash
# Lambda.bx::run()
curl http://localhost:9099/

# Lambda.bx::anotherLambda()
curl -H "x-bx-function: anotherLambda" http://localhost:9099/

# Customers.bx::findById() when /customers resolves class
curl -H "x-bx-function: findById" http://localhost:9099/customers/123
```

This gives you two dispatch layers:

- URI path selects the handler class
- `x-bx-function` selects the method in that class

{% hint style="info" %}
`x-bx-function` can only ever reach a `public` (or `remote`) method - BoxLang's own scope rules mean a `private` method is never even visible to the runtime's dispatch mechanism, the same rule that governs any other BoxLang class. Don't mark a method public if you don't want it externally callable this way.
{% endhint %}

## ⚙️ Runtime Environment Variables

| Variable | Purpose |
| --- | --- |
| `BOXLANG_GCP_ROOT` | Root directory for `.bx` handlers |
| `BOXLANG_GCP_CLASS` | Override default handler path |
| `BOXLANG_GCP_DEBUGMODE` | Enable verbose logging and disable class caching |
| `BOXLANG_GCP_CONFIG` | Custom `boxlang.json` path |
| `K_SERVICE` | Function name (set by GCF) |
| `K_REVISION` | Function revision (set by GCF) |
| `GOOGLE_CLOUD_PROJECT` | Project ID (set by GCF) |

## 🏗️ Build Deployable Artifacts

Build the GCF package:

```bash
./gradlew clean shadowJar buildLambdaZip
```

Output ZIP:

- `build/distributions/boxlang-google-function-project-<version>.zip`

The ZIP includes:

- `.bx` handlers at ZIP root
- `boxlang.json`
- `boxlang_modules/`
- `lib/` with runtime and dependencies

## ☁️ Deploy to Google Cloud Functions Gen 2

Authenticate and select project:

```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

Deploy:

```bash
gcloud functions deploy YOUR_FUNCTION_NAME \
  --gen2 \
  --runtime=java21 \
  --region=us-central1 \
  --entry-point=ortus.boxlang.runtime.gcp.FunctionRunner \
  --trigger-http \
  --allow-unauthenticated \
  --source=build/distributions/boxlang-google-function-project-1.0.0.zip
```

If you changed `version` in `gradle.properties`, update the ZIP filename in `--source`.

## 🧪 Testing

Run tests:

```bash
./gradlew test
```

Run the integration test class:

```bash
./gradlew test --tests "com.myproject.FunctionRunnerTest"
```

Open report:

- `build/reports/tests/test/index.html`

### Unit and Integration Tests Shipped in the Starter

The starter currently ships one primary integration test class and two GCF HTTP mock classes:

| File | Purpose |
| --- | --- |
| `src/test/java/com/myproject/FunctionRunnerTest.java` | End-to-end tests of request -> BoxLang handler -> HTTP response |
| `src/test/java/com/myproject/mocks/MockHttpRequest.java` | Fluent test request builder implementing GCF `HttpRequest` |
| `src/test/java/com/myproject/mocks/MockHttpResponse.java` | Captures status/body/headers implementing GCF `HttpResponse` |

`FunctionRunnerTest` validates:

- missing handler path error behavior
- default `run()` execution and JSON response assertions
- `x-bx-function` method routing (`anotherLambda`)
- response headers (`Content-Type`)
- empty headers and large-body handling
- query parameter handling
- concurrent invocation behavior
- core accessor behavior (`getDefaultFunctionPath`, `inDebugMode`, `getRuntime`)

Run only the shipped integration test:

```bash
./gradlew test --tests "com.myproject.FunctionRunnerTest"
```

## 📝 Notes

- The starter currently keeps handlers in `src/main/bx`, not `src/main/resources`.
- Routed handlers live under `src/main/bx/handlers/`; `Lambda.bx` and `Application.bx` stay at the project root and are never routing targets.
- Local launch uses `-PtestPort` and `-PdebugMode` flags.
- For this starter, deployment source is the generated ZIP in `build/distributions`.
