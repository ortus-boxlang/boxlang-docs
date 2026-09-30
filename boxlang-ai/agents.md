---
description: >-
  Build AI agents with instructions, tools, memory, skills, and MCP servers, and
  control runs in flight.
icon: robot
---

# Agents

An **agent** is a model plus instructions, and optionally memory, tools, skills, and MCP servers. It decides when to use them to complete a task.

## 🚀 Your First Agent

```js
agent = aiAgent(
    name: "Assistant",
    description: "A helpful AI assistant",
    instructions: "Be concise and friendly"
)

response = agent.run( "What is BoxLang?" )
println( response )
```

## 🧰 Give It Capabilities

**Tools** let the agent call your code:

```js
weatherTool = aiTool(
    "get_weather",
    "Get current weather for a location",
    location => getWeatherData( location )
).describeLocation( "City and country, e.g. Boston, MA" )

agent = aiAgent(
    name: "TaskAgent",
    instructions: "Use tools when needed. Be precise and helpful.",
    tools: [ weatherTool ]
)

agent.run( "What's the weather in Boston?" )
```

**Web search** for current information:

```js
agent = aiAgent(
    name: "ResearchAssistant",
    instructions: "Use web search for current information and cite your sources.",
    tools: [ "webSearch@bxai" ]
)
```

**Skills** inject domain knowledge into the agent's context:

```js
agent = aiAgent(
    name: "CodeReviewer",
    instructions: "Review code for quality and security",
    skills: aiSkill( ".ai/skills/security" ),
    availableSkills: aiSkill( ".ai/skills/languages" )
)
```

**MCP servers** provide tools from anywhere:

```js
agent = aiAgent(
    name: "ResearchAgent",
    mcpServers: [
        {
            url: "http://localhost:3000/mcp",
            toolNames: [ "web_search", "fetch_page" ]
        }
    ]
)
```

## 🧠 Agents That Remember

Give an agent memory and it keeps context across turns. See [Memory & RAG](memory-and-rag.md).

## 🏗️ More Patterns

* **Class-based agents** for reusable, testable agents
* **Sub-agents and hierarchies** where a coordinator delegates to specialists
* **Streaming** agent responses
* **Run control** to cancel or steer a run that is already in flight
* **Middleware** to add logging, retries, guardrails, and approvals without changing agent logic. See [Governance & Security](governance-and-security.md).

## 🔍 Go Deeper

* [Agents overview](https://ai.ortusbooks.com/main-components/agents)
* [Getting Started with Agents](https://ai.ortusbooks.com/main-components/agents/getting-started)
* [Class-Based Agents](https://ai.ortusbooks.com/main-components/agents/class-based-agents)
* [Memory Management](https://ai.ortusbooks.com/main-components/agents/memory)
* [Sub-Agents & Hierarchy](https://ai.ortusbooks.com/main-components/agents/hierarchy)
* [Run Control](https://ai.ortusbooks.com/main-components/agents/run-control)
* [Advanced Patterns](https://ai.ortusbooks.com/main-components/agents/advanced)
