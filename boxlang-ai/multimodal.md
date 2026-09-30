---
description: >-
  Generate images, convert text to speech and back, translate audio, and search
  the web from BoxLang with provider-agnostic APIs.
icon: wand-magic-sparkles
---

# Multimodal

BoxLang AI goes beyond text. The same provider-agnostic style covers audio, images, and web search.

## 🖼️ Image Generation

`aiImage()` generates images from a prompt, with a fluent builder for control:

```js
image = aiImage()
    .prompt( "A friendly robot writing code, flat illustration" )
    .provider( "openai" )
    .landscape()
    .high()
    .generate()
```

## 🎤 Text to Speech

`aiSpeak()` turns text into audio. It returns a response object you can save, Base64 encode, or embed in a page:

```js
aiSpeak(
    "Welcome to BoxLang.",
    {},
    { provider: "openai", voice: "female", outputFile: "/tmp/welcome.mp3" }
)
```

Providers include OpenAI, Mistral, Gemini, Grok, and ElevenLabs.

## 🎧 Speech to Text and Translation

* `aiTranscribe()` converts audio to text, for meeting notes and voice commands.
* `aiTranslate()` translates audio between languages.

## 🌐 Web Search

`aiWebSearch()` retrieves current information and works as an agent tool:

```js
results = aiWebSearch( "BoxLang programming language" )

results.each( ( result ) => {
    println( "#result.title# - #result.url#" )
} )
```

Choose a provider with options such as `{ provider: "brave", maxResults: 10 }`. Give it to an agent with `tools: [ "webSearch@bxai" ]`.

## 👁️ Vision and Multimodal Input

Vision-capable models can analyze images, and content such as images, audio, video, and documents can be combined with text in a request. Check the provider table in [Providers & Gateways](providers-and-gateways.md) for vision support.

## 🧠 Reasoning

BoxLang AI normalizes reasoning output into one `reasoning` envelope across every reasoning-capable provider, so your code does not change when your model does.

## 🔍 Go Deeper

* [Audio and Speech](https://ai.ortusbooks.com/main-components/audio)
* [Image Generation](https://ai.ortusbooks.com/main-components/image-generation)
* [Web Search](https://ai.ortusbooks.com/main-components/web-search)
* [Reasoning](https://ai.ortusbooks.com/main-components/reasoning)
