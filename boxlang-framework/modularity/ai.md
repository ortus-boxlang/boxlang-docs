---
description: BoxLang AI is a powerful library for building fluent and scalable AI applications with a unified LLM API.
icon: brain-circuit
---

# BoxLang AI

<figure><img src="https://ai.ortusbooks.com/~gitbook/image?url=https%3A%2F%2F1943767527-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsTDgathYUAH0fKKuzjR%252Fuploads%252Fgit-blob-863f5e0f389cad7a75bcce132b196bb2ccaff784%252Fimage.png%3Falt%3Dmedia&width=768&dpr=1&quality=100&sign=b49cc14d&sv=2" alt=""><figcaption></figcaption></figure>

## 🤖 What is BoxLang AI?

BoxLang AI is a comprehensive artificial intelligence module for BoxLang that provides a unified, fluent API for working with multiple AI providers. Whether you're building chatbots, implementing semantic search, generating embeddings, or creating intelligent automation, BoxLang AI simplifies AI integration with a consistent interface across all major providers.

Built with enterprise developers in mind, BoxLang AI abstracts away the complexity of working with different AI APIs while giving you the power and flexibility to leverage cutting-edge AI capabilities in your BoxLang applications.

## ✨ Features

- **Multi-Provider Support** - Seamlessly work with OpenAI, Anthropic, Ollama, AWS Bedrock, Google Gemini, and more
- **Fluent API Design** - Intuitive, chainable methods for building AI interactions
- **Chat Completions** - Build conversational AI with streaming support and function calling
- **Embeddings Generation** - Create vector embeddings for semantic search and RAG applications
- **Image Generation** - Generate images using DALL-E and other image models
- **Audio Transcription** - Convert audio to text with Whisper and similar models
- **Moderation & Safety** - Built-in content moderation capabilities
- **Streaming Support** - Real-time response streaming for chat interfaces
- **Function Calling** - Let AI models call your BoxLang functions intelligently
- **Context Management** - Handle conversation context and message history
- **Token Counting** - Track and optimize token usage across requests
- **Async Operations** - Non-blocking AI calls using BoxLang's async capabilities

## 📚 Resources

### Official Documentation

For comprehensive guides, API references, and advanced usage patterns, visit the **complete BoxLang AI documentation**:

🔗 [**BoxLang AI Documentation**](https://ai.ortusbooks.com)

### Product Website

Learn more about BoxLang AI features, pricing, and use cases:

🔗 [**BoxLang AI Official Site**](https://ai.boxlang.io)

### Professional Services

Need help implementing AI solutions in your enterprise? Our team provides consulting, training, and custom development:

🔗 [**Ortus Solutions AI Services**](https://ai.ortussolutions.com)

## 🚀 Quick Start

Get started with BoxLang AI in just a few steps:

### Installation

Install the BoxLang AI module via CommandBox:

```bash
# Install at the OS level
install-bx-module bx-ai

# Use CommandBox for OS, AWS Lambda, Google Cloud Functions, and Web Runtimes
box install bx-ai
```

### Basic Configuration

You can configure the module via the `boxlang.json` or you CFConfig configuration

```js
{
  "modules": {
    "bxai": {
      "settings": {
			// The default provider LLM AI: openai, deepseek, etc
			provider = "openai",
			// The default API Key for the provider
			apiKey = "",
			// The default request params to use when calling a provider
			// Ex: { temperature: 0.5, max_tokens: 100, model: "gpt-3.5-turbo" }
			defaultParams = {
			},
			// The default memory to use
			memory : {
				provider = "window",
				config = {}
			},
			// The default timeout of the ai requests
			timeout = 30,
			// If true, the AI request will be logged into the ai.log
			logRequest = false,
			// If true, the AI request will be logged to the console
			logRequestToConsole = false,
			// If true, the AI response will be logged into the ai.log
			logResponse = false,
			// If true, the AI response will be logged to the console
			logResponseToConsole = false,
			// The default return format of the AI response: single, all, raw
			returnFormat = "single"
		}
    }
  }
}
```

### Your First AI Chat

Create a simple chat completion:

```js
result = aiChat( "Explain BoxLang in 1 sentence." )
println( result )
```

### Generate Embeddings

Create vector embeddings for semantic search:

```js
// Generate embeddings for text
embeddings = aiEmbed( "BoxLang is a modern dynamic JVM language" )
println( embeddings )
```

### Build an Agent

Leverage AI to create an intelligent agent that can perform tasks:

```js
agent = aiAgent(
    name: "MyAgent",
    instructions: "You are a helpful assistant.",
    tools: [ /* Define tools here */ ]
    memory: [ /* Define memory here */ ]
)

response = agent.run( "What's the weather like today?" )
println( response )
```

## 💡 Next Steps

Ready to dive deeper? The full documentation covers:

- Advanced provider configuration
- Function calling and tool use
- RAG (Retrieval Augmented Generation) patterns
- Multi-modal AI (text, images, audio)
- Token optimization strategies
- AI agents and tool integration
- Production deployment best practices
- Integration with BoxLang caching and async features

**👉 Visit the [complete documentation](https://ai.ortusbooks.com) to explore the full power of BoxLang AI!**
