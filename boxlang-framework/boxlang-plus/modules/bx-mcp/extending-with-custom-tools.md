---
description: Register custom MCP tools and prompts from your own modules and applications at runtime.
icon: puzzle-piece
---

# 🧩 Extending with Custom Tools

You are not limited to the built-in introspection tools. Any module or application can register its own tools, resources, and prompts into the BoxLang MCP server at runtime using the `bx-ai` BIF `mcpServer( "boxlang" )`.

---

## 🔧 Getting the Server Instance

```js
var server = mcpServer( "boxlang" )
```

This returns the `MCPServer` instance that manages all tools, prompts, and resources.

---

## 🛠️ Registering a Simple Tool

The simplest way to register a tool is with a handler closure:

```js
server.registerTool(
  aiTool(
    "check_deployment_status",
    "Check the current deployment status of the application",
    ( environment ) => {
      var status = deploymentService.getStatus( environment )
      return {
        environment: arguments.environment,
        version: status.version,
        deployedAt: status.deployedAt.toString(),
        healthy: status.healthy
      }
    }
  )
  .addParameter(
    aiToolParam( "environment", "string", "The deployment environment to check (e.g., staging, production)" )
      .required()
  )
)
```

### How it Works

1. `aiTool()` creates a tool definition with a name, description, and handler function
2. `.addParameter()` defines the arguments the tool accepts
3. `.registerTool()` makes the tool available to MCP clients

---

## 📝 Registering a Custom Prompt

```js
mcpServer( "boxlang" ).registerPrompt(
  "deployment_health_check",
  "Check the health of the current deployment",
  ( args ) => [
    {
      role: "system",
      content: "You are a deployment operations expert. Verify the current deployment."
    },
    {
      role: "user",
      content: "Check the deployment health using `check_deployment_status` for the '#args.environment ?: 'production'#' environment."
    }
  ],
  [
    { name: "environment", description: "The deployment environment", required: false }
  ]
)
```

The prompt handler receives arguments and returns an array of messages (system and user roles) that guide the AI agent.

---

## 🔍 Classpath Scanning

For larger tool sets, annotate methods with `@mcpTool` and scan a package:

```boxlang
// In your module config or application startup
mcpServer( "boxlang" ).scan( "myapp.tools" )
```

The scanner discovers all methods annotated with `@mcpTool` and registers them automatically. Each method becomes a tool with the method name as the tool name.

```boxlang
@mcpTool
@AITool
public struct function deployment_get_status( string environment ) {
  var status = deploymentService.getStatus( arguments.environment )
  return {
    environment: arguments.environment,
    version: status.version,
    healthy: status.healthy
  }
}
```

---

## 📦 Batch Registration

Register multiple tools at once from an array of `AITool` instances:

```js
server.registerTools( [
  aiTool( "tool_one", "Description one", handlerOne ),
  aiTool( "tool_two", "Description two", handlerTwo )
] )
```

---

## 🔎 Accessing Existing Tools

You can look up any registered tool by name:

```js
var tool = mcpServer( "boxlang" ).getTool( "runtime_get_info" )
systemOutput( tool.getDescription() )
```

---

## 🏗️ Best Practices for Registration

### Module Startup (Recommended)

Register custom tools in your module's `onLoad` method in `ModuleConfig.bx`:

```boxlang
function onLoad() {
  mcpServer( "boxlang" )
    .registerTool(
      aiTool( "my_custom_tool", "Description", handler )
    )
}
```

This ensures your tools are available as soon as the MCP server is active.

### Application Startup

For application-level tools, use the `onApplicationStart` lifecycle method in your `Application.bx`.

### ColdBox Applications

Register tools in `config/ColdBox.cfc` in the `configure()` method, or in the `onApplicationStart` handler.

### Use Descriptive Names

Follow the existing naming convention: `domain_action_description`. For example:
- `deployment_get_status`
- `analytics_get_dashboard`
- `notification_send_alert`

### Return Structured Data

Always return a struct from your tool handler. The MCP server serializes the return value as JSON in the response.

---

## 💡 Complete Working Example

Here's a full example that registers a deployment health tool from a module:

```boxlang
// ModuleConfig.bx
component {
  // ... standard module metadata ...

  function onLoad() {
    mcpServer( "boxlang" )
      .registerTool( buildDeploymentTool() )
      .registerPrompt( buildDeploymentPrompt() )
  }

  private function buildDeploymentTool() {
    return aiTool(
      "deployment_get_health",
      "Get the health status of a deployment environment"
    )
    .addParameter(
      aiToolParam( "environment", "string", "The environment name (staging, production)" )
        .required()
    )
    .withHandler( ( environment ) => {
      var health = getDeploymentHealth( arguments.environment )
      return {
        environment: arguments.environment,
        status: health.status,
        version: health.version,
        deployedAt: health.deployedAt,
        uptimeSeconds: health.uptimeSeconds,
        healthy: health.healthy
      }
    } )
  }

  private function buildDeploymentPrompt() {
    return mcpServer( "boxlang" ).registerPrompt(
      "deployment_check",
      "Check the latest deployment health",
      ( args ) => [
        {
          role: "system",
          content: "You verify deployment health. Be concise."
        },
        {
          role: "user",
          content: "Run `deployment_get_health` for the '#args.environment ?: 'production'#' environment and report the result."
        }
      ],
      [
        { name: "environment", description: "Deployment environment", required: false }
      ]
    )
  }
}
```

---

## 📚 Next Steps

- [MCP Tools Reference](reference/tools/README.md) — Complete catalog of built-in tools
- [MCP Prompts Reference](reference/prompts/README.md) — Pre-built prompt catalog
- [Protocol Reference](reference/protocol.md) — JSON-RPC 2.0 endpoint details
