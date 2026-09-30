---
description: >-
  Use the AI provider you want, from OpenAI and Claude to local models, and
  connect agents to the channels your people use with gateways.
icon: network-wired
---

# Providers & Gateways

## 🌐 One API, Many Providers

Write your code once and switch providers with configuration. Cloud and local providers share the same API.

| Provider | Type | Chat | Stream | Tools | Embeddings | Vision |
| --- | --- | --- | --- | --- | --- | --- |
| Bedrock | Cloud | ✅ | ✅ | ✅ | ✅ | |
| Claude | Cloud | ✅ | ✅ | ✅ | | ✅ |
| Cloudflare | Cloud | ✅ | ✅ | ✅ | ✅ | |
| Cohere | Cloud | ✅ | ✅ | ✅ | ✅ | |
| DeepSeek | Cloud | ✅ | ✅ | ✅ | ✅ | |
| Docker Desktop | Local | ✅ | ✅ | ✅ | ✅ | |
| Gemini | Cloud | ✅ | ✅ | ✅ | ✅ | ✅ |
| Grok | Cloud | ✅ | ✅ | ✅ | | ✅ |
| Groq | Cloud | ✅ | ✅ | ✅ | | |
| HuggingFace | Cloud | ✅ | ✅ | ✅ | ✅ | |
| MiniMax | Cloud | ✅ | ✅ | ✅ | ✅ | ✅ |
| Mistral | Cloud | ✅ | ✅ | ✅ | ✅ | |
| Ollama | Local | ✅ | ✅ | ✅ | ✅ | ✅ |
| OpenAI | Cloud | ✅ | ✅ | ✅ | ✅ | ✅ |
| OpenRouter | Gateway | ✅ | ✅ | ✅ | ✅ | ✅ |
| Perplexity | Cloud | ✅ | ✅ | | | |
| Voyage | Cloud | | | | ✅ | |
| ElevenLabs | Cloud | Audio only | | | | |

Capabilities can vary by model. Vision requires a multimodal model, and OpenRouter capabilities depend on the underlying model. See the [full provider table](https://ai.ortusbooks.com) for details.

### Configure a Provider

Keep credentials in environment variables:

```json
{
  "modules": {
    "bxai": {
      "settings": {
        "provider": "openai",
        "apiKey": "${OPENAI_API_KEY}"
      }
    }
  }
}
```

### Run Models Locally

Use Ollama for private, offline, cost-free AI:

```json
{
  "modules": {
    "bxai": {
      "settings": {
        "provider": "ollama",
        "chatURL": "http://localhost:11434",
        "defaultParams": {
          "model": "llama3.2"
        }
      }
    }
  }
}
```

Need a provider that is not listed? Write a [custom provider](https://ai.ortusbooks.com/extending-boxlang-ai/custom-providers).

## 🔌 Gateways

A **gateway** connects agents to people and platforms. It translates platform events, such as a CLI keystroke, a signed webhook, or a chat button click, into agent input, and turns agent events, such as a suspended approval, into a native experience.

| Gateway | Use it for |
| --- | --- |
| `cli` | A blocking terminal approval prompt for scripts and local development |
| `http` | Network-reachable approvals and messages over signed webhooks |
| `mock` | Tests and examples, fully offline |

```js
cli = aiGateway( "cli" )
http = aiGateway( "http", { secret: "shared-hmac-secret" } )
mock = aiGateway( "mock" )
```

Platform modules can register more gateways through `aiGatewayRegistry()`. **Gateway sessions** wire an agent to inbound messages with policies for what to do when a thread is busy: reject, queue, steer, or interrupt.

## 🧱 ColdBox

In ColdBox, mount a gateway on a route with `toAiGateway()`:

```js
route( "/gateways" ).toAiGateway( session: "SupportAgentSession" )
```

See the [ColdBox AI gateway routing](https://coldbox.ortusbooks.com/the-basics/routing/routing-dsl/ai-gateway-routing) documentation.

## 🔍 Go Deeper

* [Provider Setup](https://ai.ortusbooks.com/getting-started/installation/provider-setup)
* [Working with Models](https://ai.ortusbooks.com/main-components/models)
* [Gateways](https://ai.ortusbooks.com/main-components/gateways)
* [Gateway Sessions](https://ai.ortusbooks.com/main-components/gateway-sessions)
