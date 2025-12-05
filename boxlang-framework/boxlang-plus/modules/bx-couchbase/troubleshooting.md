---
icon: bug
description: Common issues and solutions when working with the Couchbase module.
---

# 🔧 Troubleshooting

Common issues and solutions when working with the Couchbase module.

## 🚨 Connection Issues

### Cannot connect to Couchbase

**Symptoms:**
```
Error: Timeout during bootstrap
```

**Solutions:**

1. **Verify Couchbase is running:**
```bash
curl -u Administrator:password http://localhost:8091/pools
```

2. **Check connection string:**
```js
// Single node
"connectionString": "couchbase://localhost"

// Multiple nodes
"connectionString": "couchbase://node1,node2,node3"

// Secure connection
"connectionString": "couchbases://cluster.example.com"
```

3. **Verify credentials:**
```js
// Make sure username/password are correct
"username": "Administrator",
"password": "your_actual_password"
```

4. **Check firewall rules:**
- Port 8091: Management/REST API
- Port 8093: N1QL Query
- Port 11210: Key-Value operations

### Connection timeout errors

**Symptoms:**
```
Error: connectTimeout exceeded
```

**Solution:**
Increase timeout values:
```js
this.caches["default"] = {
    "provider": "Couchbase",
    "properties": {
        "connectionString": "couchbase://localhost",
        "username": "Administrator",
        "password": "password",
        "bucket": "default",
        "connectTimeout": "30000", // 30 seconds
        "kvTimeout": "5000"
    }
};
```

## 🗄️ Bucket/Collection Issues

### Bucket not found

**Symptoms:**
```
Error: Bucket "mybucket" not found
```

**Solutions:**

1. **Verify bucket exists in Couchbase:**
```bash
curl -u Administrator:password http://localhost:8091/pools/default/buckets
```

2. **Create bucket if needed:**
- Via Couchbase Web Console (http://localhost:8091)
- Or via CLI:
```bash
couchbase-cli bucket-create -c localhost:8091 \
  -u Administrator -p password \
  --bucket mybucket --bucket-type couchbase --bucket-ramsize 256
```

3. **Check bucket name in config:**
```js
"bucket": "default" // Must match exactly (case-sensitive)
```

### Scope or collection not found

**Symptoms:**
```
Error: Collection not found
```

**Solution:**
Create scope/collection or use defaults:
```js
// Use default scope/collection
"scope": "_default",
"collection": "_default"

// Or specify custom ones (must exist in Couchbase)
"scope": "myapp",
"collection": "sessions"
```

## 🔐 Authentication Issues

### Invalid credentials

**Symptoms:**
```
Error: Authentication failed
```

**Solutions:**

1. **Check username/password:**
```js
"username": "Administrator", // Case-sensitive!
"password": "password" // Check for typos
```

2. **Verify user has permissions:**
```bash
# List users
couchbase-cli user-list -c localhost:8091 -u Administrator -p password

# Grant permissions if needed
couchbase-cli user-manage -c localhost:8091 \
  -u Administrator -p password \
  --set --rbac-username myuser --rbac-password mypass \
  --roles bucket_full_access[mybucket]
```

3. **Use environment variables for security:**
```js
"username": env("COUCHBASE_USER"),
"password": env("COUCHBASE_PASS")
```

## 📝 Query Issues

### N1QL query errors

**Symptoms:**
```
Error: syntax error - at FROM
```

**Solutions:**

1. **Escape bucket names with backticks:**
```js
// ❌ Wrong
query = "SELECT * FROM mybucket WHERE type = 'user'"

// ✅ Correct
query = "SELECT * FROM `mybucket` WHERE type = 'user'"
```

2. **Use proper collection path:**
```js
// Full path format: `bucket`.`scope`.`collection`
query = "SELECT * FROM `myapp`.`_default`.`_default` WHERE ..."
```

3. **Use parameterized queries:**
```js
couchbaseQuery(
    cacheName = "default",
    query = "SELECT * FROM `mybucket` WHERE type = $type",
    parameters = { "type": "user" }
);
```

### Index not found

**Symptoms:**
```
Error: No index available
```

**Solution:**
Create a primary index:
```js
couchbaseQuery(
    cacheName = "default",
    query = "CREATE PRIMARY INDEX ON `mybucket`"
);

// Or create specific index
couchbaseQuery(
    cacheName = "default",
    query = "CREATE INDEX idx_type ON `mybucket`(type)"
);
```

## 🤖 Vector Search Issues

### Vector search returns no results

**Solutions:**

1. **Verify vector index exists:**
```js
// Check system:indexes
results = couchbaseQuery(
    cacheName = "default",
    query = "SELECT * FROM system:indexes WHERE name LIKE '%vector%'"
);
```

2. **Create vector index if needed:**
```js
couchbaseQuery(
    cacheName = "default",
    query = "CREATE INDEX idx_embedding ON `mybucket`(embedding VECTOR) WHERE type = 'vector_document'"
);
```

3. **Check embedding dimensions:**
```js
// Make sure all embeddings have same dimension
var embedding = getOpenAIEmbedding(text); // Should be 1536 for text-embedding-3-small
println("Embedding dimensions: #embedding.len()#");
```

4. **Verify documents are stored correctly:**
```js
doc = couchbaseVectorGet(cacheName="default", id="vec_test");
println("Embedding exists: #structKeyExists(doc, 'embedding')#");
println("Embedding length: #doc.embedding.len()#");
```

### Low similarity scores

**Solutions:**

1. **Use same embedding model for storage and search:**
```js
// Store
storeEmbedding = getOpenAIEmbedding(text); // text-embedding-3-small

// Search - must use same model!
searchEmbedding = getOpenAIEmbedding(query); // text-embedding-3-small
```

2. **Improve query quality:**
```js
// ❌ Too generic
query = "help"

// ✅ More specific
query = "How do I configure session storage with Couchbase?"
```

3. **Adjust result limit:**
```js
// Get more results and filter by score
results = couchbaseVectorSearch(
    cacheName = "default",
    collection = "docs._default._default",
    embedding = embedding,
    limit = 20
);

relevant = results.filter(function(r) {
    return r.score > 0.75; // Only high confidence results
});
```

## 🗄️ Session Storage Issues

### Sessions not persisting

**Solutions:**

1. **Verify session storage is configured:**
```js
this.sessionManagement = true;
this.sessionStorage = "couchbase-sessions"; // Must match cache name!

this.caches["couchbase-sessions"] = {
    "provider": "Couchbase",
    "properties": { ... }
};
```

2. **Check cache name matches:**
```js
// These must match!
this.sessionStorage = "my-sessions";
this.caches["my-sessions"] = { ... };
```

3. **Verify Couchbase is accessible:**
```js
try {
    provider = couchbaseGetProvider("couchbase-sessions");
    println("Session cache connected!");
} catch (any e) {
    println("Session cache error: #e.message#");
}
```

## ⚡ Performance Issues

### Slow cache operations

**Solutions:**

1. **Check network latency:**
```bash
ping couchbase-server-hostname
```

2. **Increase connection pool:**
```js
"maxConnections": 50 // Default is lower
```

3. **Use appropriate timeouts:**
```js
"kvTimeout": "1000", // Faster for local
"kvTimeout": "5000" // Higher for remote clusters
```

4. **Monitor with statistics:**
```js
stats = cache("default").getStats();
println("Object Count: #stats.getObjectCount()#");
println("Cache Size: #stats.getSize()# bytes");
```

### High memory usage

**Solutions:**

1. **Set appropriate TTLs:**
```js
// Don't cache forever!
cache("default").set("key", value, 60); // 60 minutes
```

2. **Use cache eviction:**
```js
// Configure in Couchbase bucket settings
// - Set bucket quota
// - Enable eviction policy
```

3. **Clear old data:**
```js
// Regular cleanup
couchbaseQuery(
    cacheName = "default",
    query = "DELETE FROM `mybucket` WHERE createdAt < $cutoff",
    parameters = { cutoff: dateAdd("d", -30, now()) }
);
```

## 🐛 Debugging Tips

### Enable debug logging

In `boxlang.json`:
```json
{
    "modules": {
        "bx-couchbase": {
            "debug": true
        }
    }
}
```

### Check Couchbase logs

```bash
# Docker
docker logs couchbase

# Native install
tail -f /opt/couchbase/var/lib/couchbase/logs/couchbase.log
```

### Test connectivity

```js
// Simple connectivity test
try {
    provider = couchbaseGetProvider("default");
    cluster = couchbaseGetCluster("default");
    bucket = couchbaseGetBucket("default");

    println("✅ Connection successful!");
    println("Bucket: #bucket.name()#");

    // Test write
    cache("default").set("test_key", { "test": true });

    // Test read
    result = cache("default").get("test_key");
    println("✅ Read/Write working!");

    // Cleanup
    cache("default").clear("test_key");

} catch (any e) {
    println("❌ Error: #e.message#");
    println("Detail: #e.detail#");
}
```

## 📞 Getting Help

If you're still having issues:

1. **Check logs** - Enable debug mode and check BoxLang and Couchbase logs
2. **Verify Couchbase health** - Use Web Console (http://localhost:8091)
3. **Test isolation** - Create minimal reproduction case
4. **Community support** - Post on [Ortus Community](https://community.ortussolutions.com)
5. **Professional support** - [Ortus Solutions Support](https://www.ortussolutions.com/services/support)

## 🔗 Useful Links

- [Couchbase Server Documentation](https://docs.couchbase.com/)
- [N1QL Query Language Reference](https://docs.couchbase.com/server/current/n1ql/n1ql-language-reference/index.html)
- [BoxLang Documentation](https://boxlang.ortusbooks.com/)
- [Community Forums](https://community.ortussolutions.com)
