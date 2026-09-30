---
description: >-
  Chat with AI models using aiChat, stream responses, and get typed, validated
  structured output from classes and templates.
icon: message
---

# Chat & Structured Output

## 💬 aiChat

`aiChat()` is the simplest way to talk to a model. Pass a message, get an answer.

```js
answer = aiChat( "What is the capital of France?" )
println( answer )
```

Signature:

```js
aiChat( message, params = {}, options = {} )
```

| Argument | Purpose |
| --- | --- |
| `message` | A string, or an array of messages for a conversation |
| `params` | Model parameters such as `temperature` and `max_tokens` |
| `options` | Module options such as `provider`, `apiKey`, and `returnFormat` |

Tune the response:

```js
poem = aiChat( "Write a haiku about coding", { temperature: 0.9 } )
```

## 📡 Streaming

Stream a response as it is generated, which is ideal for chat interfaces:

```js
aiChatStream(
    "Tell me a story about a robot",
    ( chunk ) => {
        content = chunk.choices?.first()?.delta?.content ?: ""
        print( content )
    }
)
```

## 🧱 Structured Output

Stop parsing free text. Give BoxLang a class or a template and get a validated, typed result back.

### From a Class

```js
class Person {
    property name="name" type="string";
    property name="age" type="numeric";
    property name="email" type="string";
}

person = aiChat(
    messages: "Extract: John Doe, 30, john@example.com",
    returnFormat: new Person()
)

println( person.getName() )
println( person.getAge() )
```

### From a Struct Template

For quick prototypes:

```js
product = aiChat(
    messages: "Generate a laptop product",
    returnFormat: {
        "productName": "",
        "price": 0.0,
        "inStock": false,
        "tags": []
    }
)

println( product.productName )
println( product.price )
```

Use classes for production code, and struct templates for prototypes.

## 🎯 Why It Matters

* **Type safety** with real objects instead of generic structs
* **Automatic validation** against the schema
* **Fewer hallucinated fields**, because the shape is constrained
* **No manual parsing** of AI text

## 🔍 Go Deeper

* [Basic Chatting](https://ai.ortusbooks.com/main-components/chatting/basic-chatting)
* [Advanced Chatting](https://ai.ortusbooks.com/main-components/chatting/advanced-chatting)
* [Service-Level Chatting](https://ai.ortusbooks.com/main-components/chatting/service-chatting)
* [Structured Output](https://ai.ortusbooks.com/main-components/chatting/structured-output)
* [Pipelines](https://ai.ortusbooks.com/main-components/pipelines) for multi-step and multi-model workflows
* [Message Templates](https://ai.ortusbooks.com/main-components/messages)
