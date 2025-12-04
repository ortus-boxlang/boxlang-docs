---
icon: robot
description: Build AI-powered applications with semantic search using Couchbase's native vector search capabilities. Perfect for RAG (Retrieval Augmented Generation), chatbots, recommendation systems, and semantic search engines.
---

# 🤖 AI Vector Memory

Build AI-powered applications with semantic search using Couchbase's native vector search capabilities. Perfect for RAG (Retrieval Augmented Generation), chatbots, recommendation systems, and semantic search engines.

## 🎯 What is Vector Search?

Vector search enables semantic similarity matching by comparing numerical representations (embeddings) of text. Unlike keyword search, it understands meaning and context.

**Example:**
- Query: "machine learning tutorial"
- Matches: "intro to ML", "AI training guide", "neural network basics"
- Traditional search would miss these!

## 🚀 Quick Start

```js
// 1. Get an embedding (e.g., from OpenAI)
embedding = getOpenAIEmbedding("How do I cache data in BoxLang?");

// 2. Store documents with embeddings
couchbaseVectorAdd(
    cacheName = "default",
    text = "BoxLang provides cacheSet() to store data",
    embedding = getOpenAIEmbedding("BoxLang provides cacheSet() to store data"),
    metadata = { "category": "documentation", "topic": "caching" }
);

// 3. Search for similar content
results = couchbaseVectorSearch(
    cacheName = "default",
    collection = "docs._default._default",
    embedding = embedding,
    limit = 5
);

// 4. Use results
for (doc in results) {
    println("#doc.text# (Similarity: #doc.score#)");
}
```

## 📦 Setup Requirements

### Couchbase Version
- Couchbase Server 7.6+ recommended for vector search
- Vector index support is built-in (no manual FTS setup needed!)

### Get Embeddings
You'll need an embedding model. Popular options:
- **OpenAI**: text-embedding-3-small (1536 dimensions)
- **Cohere**: embed-english-v3.0
- **Local**: sentence-transformers models

## 🎨 Complete RAG Chatbot Example

```js
component {
    this.name = "RAGChatbot";

    // Configure Couchbase
    this.caches["memory"] = {
        "provider": "Couchbase",
        "properties": {
            "connectionString": "couchbase://localhost",
            "username": "Administrator",
            "password": "password",
            "bucket": "chatbot"
        }
    };

    /**
     * Add knowledge to the chatbot
     */
    function learnDocument(text, metadata={}) {
        // Split into chunks for better search
        var chunks = splitIntoChunks(text, 500);
        var docIds = [];

        for (var chunk in chunks) {
            var embedding = getOpenAIEmbedding(chunk);

            var docId = couchbaseVectorAdd(
                cacheName = "memory",
                text = chunk,
                embedding = embedding,
                metadata = metadata
            );

            docIds.append(docId);
        }

        return docIds;
    }

    /**
     * Ask a question and get context-aware answer
     */
    function ask(question, userId="anonymous") {
        // 1. Get relevant context
        var queryEmbedding = getOpenAIEmbedding(question);

        var context = couchbaseVectorSearch(
            cacheName = "memory",
            collection = "chatbot._default._default",
            embedding = queryEmbedding,
            limit = 3
        );

        // 2. Build context for LLM
        var contextText = context.map(function(doc) {
            return doc.text;
        }).toList("\n\n");

        // 3. Get AI response with context
        var prompt = "
            Context information:
            #contextText#

            Question: #question#

            Answer based on the context above:
        ";

        var answer = callOpenAI(prompt);

        // 4. Store the conversation
        couchbaseVectorAdd(
            cacheName = "memory",
            text = "Q: #question# A: #answer#",
            embedding = getOpenAIEmbedding(question & " " & answer),
            metadata = {
                "type": "conversation",
                "question": question,
                "answer": answer,
                "timestamp": now()
            },
            userId = userId
        );

        return {
            "answer": answer,
            "sources": context,
            "confidence": context[1].score
        };
    }

    /**
     * Get conversation history
     */
    function getHistory(userId, limit=10) {
        return couchbaseVectorList(
            cacheName = "memory",
            collection = "chatbot._default._default",
            userId = userId,
            filter = { "type": "conversation" },
            limit = limit
        );
    }

    // Helper functions
    private function getOpenAIEmbedding(text) {
        var response = http(
            url = "https://api.openai.com/v1/embeddings",
            method = "POST",
            headers = {
                "Authorization": "Bearer #env('OPENAI_API_KEY')#",
                "Content-Type": "application/json"
            },
            body = serializeJSON({
                "model": "text-embedding-3-small",
                "input": text
            })
        );

        var result = deserializeJSON(response.fileContent);
        return result.data[1].embedding;
    }

    private function callOpenAI(prompt) {
        var response = http(
            url = "https://api.openai.com/v1/chat/completions",
            method = "POST",
            headers = {
                "Authorization": "Bearer #env('OPENAI_API_KEY')#",
                "Content-Type": "application/json"
            },
            body = serializeJSON({
                "model": "gpt-4",
                "messages": [
                    { "role": "user", "content": prompt }
                ]
            })
        );

        var result = deserializeJSON(response.fileContent);
        return result.choices[1].message.content;
    }

    private function splitIntoChunks(text, chunkSize=500) {
        var chunks = [];
        var words = listToArray(text, " ");
        var currentChunk = [];
        var currentSize = 0;

        for (var word in words) {
            if (currentSize + len(word) > chunkSize && currentChunk.len() > 0) {
                chunks.append(currentChunk.toList(" "));
                currentChunk = [];
                currentSize = 0;
            }
            currentChunk.append(word);
            currentSize += len(word) + 1;
        }

        if (currentChunk.len() > 0) {
            chunks.append(currentChunk.toList(" "));
        }

        return chunks;
    }
}

// Usage
chatbot = new RAGChatbot();

// Learn from documentation
chatbot.learnDocument(
    fileRead("docs/caching-guide.txt"),
    { "source": "documentation", "category": "caching" }
);

// Ask questions
response = chatbot.ask("How do I cache database queries?");
println(response.answer);
println("Confidence: #response.confidence#");

// View history
history = chatbot.getHistory("user123");
```

## 🎯 Use Cases

### 1. Documentation Search

```js
// Index your docs
docs = directoryList("/path/to/docs", true, "path", "*.md");
for (docPath in docs) {
    content = fileRead(docPath);
    embedding = getOpenAIEmbedding(content);

    couchbaseVectorAdd(
        cacheName = "docs",
        text = content,
        embedding = embedding,
        metadata = {
            "path": docPath,
            "filename": getFileFromPath(docPath)
        }
    );
}

// Search
query = "How do I configure caching?";
results = couchbaseVectorSearch(
    cacheName = "docs",
    collection = "docs._default._default",
    embedding = getOpenAIEmbedding(query),
    limit = 3
);
```

### 2. Customer Support Bot

```js
// Store support tickets and resolutions
function storeTicket(ticketId, problem, solution) {
    var text = "Problem: #problem# Solution: #solution#";
    var embedding = getOpenAIEmbedding(text);

    couchbaseVectorAdd(
        cacheName = "support",
        text = text,
        embedding = embedding,
        metadata = {
            "ticketId": ticketId,
            "problem": problem,
            "solution": solution,
            "resolved": now()
        },
        id = "ticket_#ticketId#"
    );
}

// Find similar resolved tickets
function findSimilarTickets(problem) {
    var embedding = getOpenAIEmbedding(problem);

    return couchbaseVectorSearch(
        cacheName = "support",
        collection = "support._default._default",
        embedding = embedding,
        limit = 5
    );
}
```

### 3. Recommendation System

```js
// Store user preferences
function storeUserPreferences(userId, preferences) {
    var text = serializeJSON(preferences);
    var embedding = getOpenAIEmbedding(text);

    couchbaseVectorAdd(
        cacheName = "users",
        text = text,
        embedding = embedding,
        metadata = preferences,
        userId = userId,
        id = "pref_#userId#"
    );
}

// Find similar users
function findSimilarUsers(userId, limit=10) {
    var userDoc = couchbaseVectorGet(
        cacheName = "users",
        id = "pref_#userId#"
    );

    return couchbaseVectorSearch(
        cacheName = "users",
        collection = "users._default._default",
        embedding = userDoc.embedding,
        limit = limit + 1 // Exclude self
    ).filter(function(user) {
        return user.id != "pref_#userId#";
    });
}
```

### 4. Conversation Context

```js
// Store conversation messages
function storeMessage(userId, conversationId, role, content) {
    var embedding = getOpenAIEmbedding(content);

    couchbaseVectorAdd(
        cacheName = "chat",
        text = content,
        embedding = embedding,
        metadata = {
            "role": role,
            "timestamp": now()
        },
        userId = userId,
        conversationId = conversationId
    );
}

// Get relevant context for current message
function getRelevantContext(userId, conversationId, currentMessage, limit=5) {
    var embedding = getOpenAIEmbedding(currentMessage);

    return couchbaseVectorSearch(
        cacheName = "chat",
        collection = "chat._default._default",
        embedding = embedding,
        userId = userId,
        conversationId = conversationId,
        limit = limit
    );
}
```

## 🔧 Best Practices

### 1. Chunk Large Documents

```js
// Instead of storing entire book
couchbaseVectorAdd(text=entireBook, ...); // ❌

// Store chapters or paragraphs
for (chapter in chapters) {
    couchbaseVectorAdd(text=chapter, ...); // ✅
}
```

### 2. Use Metadata Filters

```js
// Narrow search scope
results = couchbaseVectorSearch(
    cacheName = "default",
    collection = "docs._default._default",
    embedding = embedding,
    limit = 10,
    filter = {
        "category": "tutorials",
        "language": "en",
        "version": "1.0"
    }
);
```

### 3. Cache Embeddings

```js
// Don't regenerate same embedding
var embeddingCache = {};

function getCachedEmbedding(text) {
    var hash = hash(text, "MD5");

    if (!structKeyExists(embeddingCache, hash)) {
        embeddingCache[hash] = getOpenAIEmbedding(text);
    }

    return embeddingCache[hash];
}
```

### 4. Monitor Search Quality

```js
results = couchbaseVectorSearch(...);

// Check confidence scores
for (result in results) {
    if (result.score < 0.7) {
        println("Low confidence result: #result.text#");
    }
}

// Use a threshold
relevantResults = results.filter(function(r) {
    return r.score >= 0.75;
});
```

## 📊 Performance Tips

### Batch Operations

```js
// Store multiple documents efficiently
documents = [...]; // Array of documents

for (doc in documents) {
    var embedding = getOpenAIEmbedding(doc.text);
    couchbaseVectorAdd(
        cacheName = "default",
        text = doc.text,
        embedding = embedding,
        metadata = doc.metadata
    );
}
```

### Limit Result Size

```js
// Don't fetch too many results
results = couchbaseVectorSearch(
    cacheName = "default",
    collection = "docs._default._default",
    embedding = embedding,
    limit = 10 // Keep reasonable
);
```

## 🔗 Next Steps

- **[API Usage](api-usage.md)** - Complete BIF documentation
- **[BIF Reference](reference/built-in-functions/)** - Detailed API reference
- **[Code Usage](code-usage.md)** - Basic cache operations
