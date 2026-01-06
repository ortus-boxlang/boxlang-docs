---
description: >-
  Use Couchbase as a vector memory provider for BoxLang AI applications. Store
  conversation history with semantic search capabilities for intelligent context
  retrieval in chatbots, agents, and RAG syste
icon: robot
---

# AI Memory

Use Couchbase as a **vector memory provider** for BoxLang AI applications. Store conversation history with semantic search capabilities for intelligent context retrieval in chatbots, agents, and RAG systems.

> **Note**: This feature requires the **BoxLang AI Module (bx-ai)** to be installed and Couchbase Server 7.6+ with vector search capabilities.

## Overview

The bx-couchbase module integrates with BoxLang AI's memory system, allowing you to use Couchbase as a vector memory backend. This enables:

* **Semantic Search**: Find relevant conversations based on meaning, not just keywords
* **Multi-Tenant Isolation**: Separate vector storage per user and conversation
* **Scalable Storage**: Handle thousands of conversations with Couchbase's performance
* **Persistent Memory**: Conversation history survives application restarts
* **Hybrid Search**: Combine vector similarity with metadata filtering

## Installation

### 1. Install BoxLang AI Module

```bash
boxlang install bx-ai
```

### 2. Install Couchbase Module

```bash
boxlang install bx-couchbase
```

### 3. Configure Couchbase Cache

In your `Application.bx`:

```js
component {
    this.name = "MyAIApp";

    // Configure Couchbase cache
    this.caches["ai_memory"] = {
        "provider": "Couchbase",
        "properties": {
            "connectionString": "couchbase://localhost",
            "username": "Administrator",
            "password": "password",
            "bucket": "ai_conversations",
            "scope": "_default",
            "collection": "_default"
        }
    };
}
```

## Basic Usage

### Creating Vector Memory

```js
// Create Couchbase vector memory for an AI agent
memory = aiMemory( "cache", {
    cacheName: "ai_memory",
    collection: "ai_conversations._default._default",
    embeddingProvider: "openai",
    embeddingModel: "text-embedding-3-small"
});

// Use with an AI agent
agent = aiAgent(
    name: "Support Bot",
    memory: memory,
    model: aiModel( "openai" )
);

// Agent automatically stores and retrieves from Couchbase
response = agent.run( "What were we talking about yesterday?" );
```

### Multi-Tenant Isolation

Isolate conversations per user and conversation:

```js
// Alice's support conversation
aliceMemory = aiMemory( "cache",
    key: createUUID(),
    userId: "alice",
    conversationId: "support-123",
    config: {
        cacheName: "ai_memory",
        collection: "ai_conversations._default._default",
        embeddingProvider: "openai"
    }
);

// Bob's support conversation (completely isolated)
bobMemory = aiMemory( "cache",
    key: createUUID(),
    userId: "bob",
    conversationId: "support-456",
    config: {
        cacheName: "ai_memory",
        collection: "ai_conversations._default._default",
        embeddingProvider: "openai"
    }
);

// Each user only sees their own conversation history
aliceAgent = aiAgent( name: "Alice Support", memory: aliceMemory );
bobAgent = aiAgent( name: "Bob Support", memory: bobMemory );
```

## Configuration

### Memory Configuration Options

```js
memory = aiMemory( "cache", {
    // Required: Couchbase cache name (configured in Application.bx)
    cacheName: "ai_memory",

    // Required: Full collection path (bucket.scope.collection)
    collection: "ai_conversations._default._default",

    // Required: Embedding provider (openai, voyage, cohere, etc.)
    embeddingProvider: "openai",

    // Optional: Embedding model (default: text-embedding-3-small)
    embeddingModel: "text-embedding-3-small",

    // Optional: Vector dimensions (default: 1536 for OpenAI)
    dimensions: 1536,

    // Optional: Distance metric (cosine, euclidean, dot)
    metric: "cosine",

    // Optional: Message limit for retrieval (default: 10)
    limit: 10
});
```

### Multi-Tenant Configuration

```js
memory = aiMemory( "cache",
    // Unique memory instance key
    key: createUUID(),

    // User isolation
    userId: "user123",

    // Conversation isolation
    conversationId: "conv-abc",

    // Cache configuration
    config: {
        cacheName: "ai_memory",
        collection: "ai_conversations._default._default",
        embeddingProvider: "openai"
    }
);
```

## Working with Memory

### Adding Messages

```js
// Add user message
memory.add( {
    role: "user",
    content: "How do I configure caching in BoxLang?"
} );

// Add assistant response
memory.add( {
    role: "assistant",
    content: "You can configure caching in Application.bx using this.caches..."
} );

// Add system message
memory.setSystemMessage( "You are a helpful BoxLang assistant." );
```

### Retrieving Relevant Context

```js
// Semantic search - finds relevant past messages
relevant = memory.getRelevant(
    query: "caching configuration",
    limit: 5
);

// Returns most semantically similar messages
for ( message in relevant ) {
    writeOutput( "#message.role#: #message.content#<br>" );
}
```

### Getting All Messages

```js
// Get all messages chronologically
allMessages = memory.getAll();

// Count total messages
totalCount = memory.count();

// Clear all messages
memory.clear();
```

## Integration with AI Agents

### Simple Agent with Couchbase Memory

```js
component {

    function onApplicationStart() {
        // Configure Couchbase cache
        application.memory = aiMemory( "cache", {
            cacheName: "ai_memory",
            collection: "conversations._default._default",
            embeddingProvider: "openai"
        });

        // Create AI agent
        application.agent = aiAgent(
            name: "Customer Support",
            instructions: "You are a helpful customer support agent",
            memory: application.memory,
            model: aiModel( "openai", {
                model: "gpt-4",
                temperature: 0.7
            })
        );
    }

    function handleCustomerQuery( userId, query ) {
        // Create user-specific memory
        var userMemory = aiMemory( "cache",
            key: createUUID(),
            userId: userId,
            config: {
                cacheName: "ai_memory",
                collection: "conversations._default._default",
                embeddingProvider: "openai"
            }
        );

        // Create user-specific agent
        var userAgent = aiAgent(
            name: "Support for " & userId,
            instructions: "You are a helpful customer support agent",
            memory: userMemory,
            model: aiModel( "openai" )
        );

        // Process query with conversation history
        return userAgent.run( query );
    }
}

// Usage
response = handleCustomerQuery( "alice", "What's my account status?" );
```

### Multi-Conversation Support

```js
// User has multiple conversations (support + sales)
component {

    function getSupportAgent( userId ) {
        var memory = aiMemory( "cache",
            key: createUUID(),
            userId: userId,
            conversationId: "support",
            config: {
                cacheName: "ai_memory",
                collection: "conversations._default._default",
                embeddingProvider: "openai"
            }
        );

        return aiAgent(
            name: "Support Agent",
            memory: memory,
            model: aiModel( "openai" )
        );
    }

    function getSalesAgent( userId ) {
        var memory = aiMemory( "cache",
            key: createUUID(),
            userId: userId,
            conversationId: "sales",
            config: {
                cacheName: "ai_memory",
                collection: "conversations._default._default",
                embeddingProvider: "openai"
            }
        );

        return aiAgent(
            name: "Sales Agent",
            memory: memory,
            model: aiModel( "openai" )
        );
    }
}

// Completely isolated conversations
supportBot = getSupportAgent( "alice" );
salesBot = getSalesAgent( "alice" );

supportBot.run( "I need help with billing" );  // Only in support context
salesBot.run( "Tell me about premium plans" ); // Only in sales context
```

## Hybrid Memory (Recent + Semantic)

Combine windowed memory (recent messages) with vector search (relevant history):

```js
// Create hybrid memory - best of both worlds
memory = aiMemory( "hybrid",
    key: createUUID(),
    userId: "alice",
    config: {
        // Recent messages (last 10)
        window: {
            type: "windowed",
            size: 10
        },

        // Semantic search in Couchbase
        vector: {
            type: "cache",
            cacheName: "ai_memory",
            collection: "conversations._default._default",
            embeddingProvider: "openai",
            limit: 5
        }
    }
);

// Agent gets both recent context AND relevant history
agent = aiAgent(
    name: "Smart Assistant",
    memory: memory,
    model: aiModel( "openai" )
);

// Automatically retrieves:
// - Last 10 messages (for immediate context)
// - 5 most relevant past messages (for long-term memory)
response = agent.run( "What did I ask about last week?" );
```

## Storage Structure

### How Messages are Stored

Each message is stored in Couchbase as:

```json
{
    "id": "msg_uuid",
    "userId": "alice",
    "conversationId": "support-123",
    "role": "user",
    "content": "How do I configure caching?",
    "embedding": [0.023, -0.015, 0.089, ...],  // 1536-dim vector
    "timestamp": "2024-12-05T10:30:00Z",
    "metadata": {
        "key": "conversation-key-uuid"
    }
}
```

### Multi-Tenant Filtering

All queries automatically filter by userId and conversationId:

```js
// Couchbase N1QL query example (handled internally)
SELECT * FROM ai_conversations
WHERE userId = 'alice'
  AND conversationId = 'support-123'
  AND VECTOR_SEARCH(embedding, query_vector, 'cosine', 10)
```

## Best Practices

### 1. Use Unique Keys per Conversation

```js
// ✅ Good - unique key per conversation
memory = aiMemory( "cache",
    key: createUUID(),  // New key each time
    userId: userId,
    conversationId: conversationId,
    config: { ... }
);

// ❌ Bad - reusing same key
memory = aiMemory( "cache",
    key: "shared-key",  // Don't do this
    config: { ... }
);
```

### 2. Set Appropriate Limits

```js
// Balance context size with relevance
memory = aiMemory( "cache", {
    cacheName: "ai_memory",
    collection: "conversations._default._default",
    embeddingProvider: "openai",
    limit: 10  // Don't retrieve too many messages
});
```

### 3. Use Hybrid Memory for Best Results

```js
// Combine recent + relevant context
memory = aiMemory( "hybrid", {
    window: {
        type: "windowed",
        size: 5  // Last 5 messages
    },
    vector: {
        type: "cache",
        cacheName: "ai_memory",
        collection: "conversations._default._default",
        embeddingProvider: "openai",
        limit: 3  // 3 relevant past messages
    }
});
```

### 4. Clear Old Conversations Periodically

```js
// Clean up old conversations
function cleanupOldConversations( cacheName, daysOld = 30 ) {
    var cutoffDate = dateAdd( "d", -daysOld, now() );

    // Use Couchbase N1QL to delete old messages
    var provider = couchbaseGetProvider( cacheName );
    var collection = provider.getCollection();

    collection.query( "
        DELETE FROM `#cacheName#`
        WHERE type = 'ai_message'
          AND timestamp < '#dateFormat( cutoffDate, 'yyyy-mm-dd' )#'
    " );
}

// Run periodically
cleanupOldConversations( "ai_memory", 30 );
```

## Performance Considerations

### Connection Pooling

Couchbase connections are pooled automatically by the bx-couchbase module. No additional configuration needed.

### Vector Index

For optimal performance, create a vector index in Couchbase:

```sql
CREATE INDEX idx_vectors ON ai_conversations(embedding VECTOR)
WHERE type = 'ai_message';
```

### Batch Operations

When storing multiple messages:

```js
// Store messages individually (automatic batching by SDK)
messages = [
    { role: "user", content: "Hello" },
    { role: "assistant", content: "Hi there!" },
    { role: "user", content: "How are you?" }
];

for ( message in messages ) {
    memory.add( message );
}
```

## Couchbase Server Requirements

### Minimum Version

* **Couchbase Server 7.6+** (for vector search support)
* **Couchbase SDK 3.6+** (included in bx-couchbase module)

### Bucket Configuration

```sql
-- Create bucket for AI conversations
CREATE BUCKET ai_conversations WITH {
    "ramQuota": 1024,
    "numReplicas": 1,
    "bucketType": "couchbase"
};

-- Create scope and collection (optional)
CREATE SCOPE ai_conversations._default;
CREATE COLLECTION ai_conversations._default._default;
```

### Vector Index Setup

Vector indexes are created automatically when first message is added. Manual creation:

```sql
-- Create vector search index
CREATE VECTOR INDEX idx_ai_vectors
ON ai_conversations(embedding)
WHERE type = 'ai_message'
WITH {"dimension": 1536, "metric": "cosine"};
```

## Troubleshooting

### Memory Not Persisting

**Issue**: Messages not stored in Couchbase

**Solution**: Verify cache configuration and connection:

```js
// Test cache connectivity
try {
    var testCache = cache( "ai_memory" );
    testCache.set( "test_key", "test_value", 60 );

    var result = testCache.get( "test_key" );
    if ( result.isPresent() ) {
        writeOutput( "Cache working!" );
    }
} catch ( any e ) {
    writeOutput( "Cache error: #e.message#" );
}
```

### Embedding Errors

**Issue**: "Embedding provider not configured"

**Solution**: Ensure bx-ai module is installed and embedding provider is configured:

```js
// Check bx-ai installation
var moduleService = getBoxContext().getRuntime().getModuleService();
if ( !moduleService.isLoaded( "bx-ai" ) ) {
    throw( "bx-ai module not installed. Run: boxlang install bx-ai" );
}

// Configure embedding provider in Application.bx
this.ai = {
    providers: {
        openai: {
            apiKey: env( "OPENAI_API_KEY" )
        }
    }
};
```

### Vector Search Not Finding Results

**Issue**: `getRelevant()` returns empty array

**Solutions**:

1. **Check embedding dimensions match**:

```js
// OpenAI text-embedding-3-small = 1536 dimensions
memory = aiMemory( "cache", {
    embeddingProvider: "openai",
    embeddingModel: "text-embedding-3-small",
    dimensions: 1536  // Must match model output
});
```

2. **Verify messages are stored**:

```js
var count = memory.count();
writeOutput( "Total messages: #count#" );

var allMessages = memory.getAll();
writeOutput( "Messages: #serializeJSON( allMessages )#" );
```

3. **Check search query**:

```js
// Use descriptive search queries
relevant = memory.getRelevant(
    query: "billing and payment issues",  // ✅ Descriptive
    limit: 5
);

// Not just single words
relevant = memory.getRelevant(
    query: "billing",  // ❌ Too vague
    limit: 5
);
```

## Complete Examples

### RAG Chatbot with Couchbase Memory

```js
component {

    property name="memory";
    property name="agent";

    function init() {
        // Configure vector memory
        variables.memory = aiMemory( "cache", {
            cacheName: "ai_memory",
            collection: "chatbot._default._default",
            embeddingProvider: "openai",
            embeddingModel: "text-embedding-3-small"
        });

        // Create AI agent
        variables.agent = aiAgent(
            name: "RAG Chatbot",
            instructions: "You are a helpful assistant. Use conversation history to provide context-aware responses.",
            memory: variables.memory,
            model: aiModel( "openai", {
                model: "gpt-4",
                temperature: 0.7
            })
        );

        return this;
    }

    function chat( message ) {
        return variables.agent.run( message );
    }

    function getChatHistory( limit = 10 ) {
        return variables.memory.getAll().slice( 1, limit );
    }

    function searchHistory( query, limit = 5 ) {
        return variables.memory.getRelevant(
            query: query,
            limit: limit
        );
    }

    function clearHistory() {
        variables.memory.clear();
    }
}

// Usage
chatbot = new RAGChatbot();

// Have conversation
response1 = chatbot.chat( "My name is Alice and I love hiking" );
response2 = chatbot.chat( "What outdoor activities do you recommend?" );
response3 = chatbot.chat( "What's my name?" );  // Remembers Alice

// Search conversation history
results = chatbot.searchHistory( "hobbies and interests" );

// View history
history = chatbot.getChatHistory( 10 );
```

### Multi-Tenant Customer Support

```js
component {

    function handleSupportRequest( userId, conversationId, message ) {
        // Create user-specific memory
        var memory = aiMemory( "hybrid",
            key: createUUID(),
            userId: userId,
            conversationId: conversationId,
            config: {
                window: {
                    type: "windowed",
                    size: 10
                },
                vector: {
                    type: "cache",
                    cacheName: "support_memory",
                    collection: "support._default._default",
                    embeddingProvider: "openai",
                    limit: 5
                }
            }
        );

        // Create support agent
        var agent = aiAgent(
            name: "Support Agent",
            instructions: "You are a helpful customer support agent. Use past conversations to provide better assistance.",
            memory: memory,
            model: aiModel( "openai" )
        );

        // Process request
        var response = agent.run( message );

        return {
            response: response,
            conversationId: conversationId,
            messageCount: memory.count()
        };
    }

    function getUserConversations( userId ) {
        // Get all conversations for user
        var provider = couchbaseGetProvider( "support_memory" );
        var collection = provider.getCollection();

        var result = collection.query( "
            SELECT DISTINCT conversationId,
                   MIN(timestamp) as startTime,
                   MAX(timestamp) as lastTime,
                   COUNT(*) as messageCount
            FROM support._default._default
            WHERE type = 'ai_message'
              AND userId = '#userId#'
            GROUP BY conversationId
            ORDER BY lastTime DESC
        " );

        return result.rows;
    }
}

// Usage
supportService = new SupportService();

// Handle requests from different users
response1 = supportService.handleSupportRequest(
    "alice",
    "conv-123",
    "I need help with billing"
);

response2 = supportService.handleSupportRequest(
    "bob",
    "conv-456",
    "How do I reset my password?"
);

// Each user only sees their own history
aliceConvos = supportService.getUserConversations( "alice" );
bobConvos = supportService.getUserConversations( "bob" );
```

## See Also

* [**BoxLang AI Documentation**](https://bx-ai.ortusbooks.com/) - Complete bx-ai module guide
* [**Vector Memory Guide**](https://bx-ai.ortusbooks.com/main-components/vector-memory) - All vector memory types
* [**AI Agents Guide**](https://bx-ai.ortusbooks.com/main-components/agents) - Building autonomous agents
* [**Code Usage**](code-usage.md) - Basic Couchbase cache operations
* [**Configuration**](configuration.md) - Couchbase connection settings
* [**Troubleshooting**](troubleshooting.md) - Common issues and solutions
