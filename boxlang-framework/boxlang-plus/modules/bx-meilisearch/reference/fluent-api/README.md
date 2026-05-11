---
description: API wrapper documentation for the BoxLang Meilisearch module.
icon: book-open
---

# Fluent API Reference

## Indexes

### List indexes

List all indexes with pagination and filtering options.

```js
var result = meilisearch()
	.indexes()
	.list();
```

🔗 [Meilisearch: List All Indexes](https://www.meilisearch.com/docs/reference/api/indexes#list-all-indexes)

### Swap indexes

Swap two indexes for zero-downtime deployments.

```js
meilisearch()
	.indexes()
	.swap( [ "books", "books_staging" ] );
```

🔗 [Meilisearch: Swap Indexes](https://www.meilisearch.com/docs/reference/api/indexes#swap-indexes)

### Get stats

Get database and index statistics including document counts and sizes.

```js
var result = meilisearch()
	.indexes()
	.stats();
```

🔗 [Meilisearch: Get Stats](https://www.meilisearch.com/docs/reference/api/stats#get-stats)

## Single Index

### Get an index

Retrieve a single index by its unique identifier.

```js
var result = meilisearch()
	.index( "books" )
	.get();
```

🔗 [Meilisearch: Get One Index](https://www.meilisearch.com/docs/reference/api/indexes#get-one-index)

### Create an index

Create a new index with an optional primary key.

```js
// Create with auto-generated primary key
meilisearch()
	.index( "books" )
	.create();

// Create with specific primary key
meilisearch()
	.index( "books" )
	.create( "id" );
```

🔗 [Meilisearch: Create an Index](https://www.meilisearch.com/docs/reference/api/indexes#create-an-index)

### Get Index stats

Get index statistics.

```js
var result = meilisearch()
	.index( "books" )
	.stats();
```

🔗 [Meilisearch: Get stats of an index](https://www.meilisearch.com/docs/reference/api/stats#get-stats-of-an-index)

### Compact an index

Compact an index to reduce database fragmentation.

```js
var result = meilisearch()
	.index( "books" )
	.compact();
```

🔗 [Meilisearch: Compact an Index](https://www.meilisearch.com/docs/reference/api/compact)

### Delete an index

Permanently delete an index and all its documents.

```js
meilisearch()
	.index( "books" )
	.delete();
```

🔗 [Meilisearch: Delete an Index](https://www.meilisearch.com/docs/reference/api/indexes#delete-an-index)

## Documents

### Add or Replace Documents

Add or replace documents in an index. Replaces existing documents with the same primary key.

```js
var task = meilisearch()
	.index( "books" )
	.documents()
	.add([
		{ id: 1, title: "BoxLang for Beginners", author: "Jane Doe" },
		{ id: 2, title: "Advanced BoxLang", author: "John Smith" }
	])
	.orReplace();

// Returns a Task object - use task.getStatus() to check progress
// task.getType() == "documentAdditionOrUpdate"
```

🔗 [Meilisearch: Add or Replace Documents](https://www.meilisearch.com/docs/reference/api/documents#add-or-replace-documents)

### Add or Update Documents

Add or update documents in an index. Updates existing documents instead of replacing them entirely.

```js
var task = meilisearch()
	.index( "books" )
	.documents()
	.add([
		{ id: 1, title: "BoxLang for Beginners - Updated Edition", author: "Jane Doe" },
		{ id: 3, title: "BoxLang Cookbook", author: "New Author" }
	])
	.orUpdate();

// Returns a Task object - use task.getStatus() to check progress
// task.getType() == "documentAdditionOrUpdate"
```

🔗 [Meilisearch: Add or Update Documents](https://www.meilisearch.com/docs/reference/api/documents#add-or-update-documents)

### Delete All Documents

Delete all documents from an index.

```js
var task = meilisearch()
	.index( "books" )
	.documents()
	.deleteAll();

// Returns a Task object - use task.getStatus() to check progress
// task.getType() == "documentDeletion"
```

🔗 [Meilisearch: Delete All Documents](https://www.meilisearch.com/docs/reference/api/documents#delete-all-documents)

### Get Documents

Retrieve documents from an index with optional filtering.

```js
var result = meilisearch()
	.index( "books" )
	.documents()
	.get({ offset: 0, limit: 20 });
```

🔗 [Meilisearch: Get Documents](https://www.meilisearch.com/docs/reference/api/documents#get-documents)

### Get Single Document

Retrieve a specific document by its ID.

```js
var result = meilisearch()
	.index( "books" )
	.document( "1" )
	.get();
```

🔗 [Meilisearch: Get One Document](https://www.meilisearch.com/docs/reference/api/documents#get-one-document)

### Delete Single Document

Delete a specific document by its ID.

```js
var task = meilisearch()
	.index( "books" )
	.document( "1" )
	.delete();

// Returns a Task object
```

🔗 [Meilisearch: Delete One Document](https://www.meilisearch.com/docs/reference/api/documents#delete-one-document)

## Search

The Search DSL provides a fluent interface for querying documents in an index. It supports both POST (default) and GET request methods.

### Basic search

Search for documents using a query string.

```js
var result = meilisearch()
	.index( "books" )
	.search( "tolkien" )
	.send();

// Returns: {
//   hits: [ { id: 1, title: "The Hobbit", ... }, ... ],
//   query: "tolkien",
//   processingTimeMs: 1,
//   estimatedTotalHits: 2,
//   ...
// }
```

🔗 [Meilisearch: Search Documents](https://www.meilisearch.com/docs/reference/api/search#search-in-an-index-with-post)

### Search with parameters

Pass initial parameters as the second argument to `search()`.

```js
var result = meilisearch()
	.index( "books" )
	.search( "tolkien", { limit: 5, offset: 0 } )
	.send();
```

🔗 [Meilisearch: Search Parameters](https://www.meilisearch.com/docs/reference/api/search#query-parameters)

### Fluent DSL with chained methods

Chain parameter methods for a readable, builder-style interface.

```js
var result = meilisearch()
	.index( "books" )
	.search( "tolkien" )
	.filter( "genres = fantasy" )
	.limit( 5 )
	.offset( 0 )
	.attributesToRetrieve( "title,author" )
	.send();
```

Any Meilisearch search parameter can be used as a method call. The method name becomes the parameter name, and the method value becomes the parameter value.

Common parameters:
- `filter` - Filter results using Meilisearch filter expressions
- `limit` - Maximum number of results to return
- `offset` - Number of results to skip (for pagination)
- `attributesToRetrieve` - Comma-separated list of fields to return
- `sort` - Sort order (e.g., "price:asc")
- `facets` - Facets to compute

🔗 [Meilisearch: Search Parameters](https://www.meilisearch.com/docs/reference/api/search#query-parameters)

### Search with GET request

Use `sendWithGet()` instead of `send()` to make a GET request instead of POST.

```js
var result = meilisearch()
	.index( "books" )
	.search( "tolkien" )
	.limit( 10 )
	.sendWithGet();
```

🔗 [Meilisearch: Search with GET](https://www.meilisearch.com/docs/reference/api/search#search-in-an-index-with-get)

## Facets

The Facets API allows you to search for facet values using AI-powered prefix search and typo tolerance.

**Note:** This endpoint requires attributes to be added to `filterableAttributes` in index settings first.

### Facet search

Search for facet values within a given facet.

```js
// Search for facet values
var result = meilisearch()
	.index( "books" )
	.facetSearch( "genre", { facetQuery: "fiction" } )
	.send();

// With additional parameters
var result = meilisearch()
	.index( "books" )
	.facetSearch( "genre", {
		facetQuery: "fiction",
		q: "fantasy",
		filter: "rating > 3",
		matchingStrategy: "all"
	})
	.send();

// Returns: {
//   facetHits: [
//     { value: "fiction", count: 7 }
//   ],
//   facetQuery: "fiction",
//   processingTimeMs: 0
// }
```

🔗 [Meilisearch: Facet Search](https://www.meilisearch.com/docs/reference/api/facet_search#facet-search)

## Keys

### List API keys

List all API keys with optional pagination.

```js
var result = meilisearch()
	.keys()
	.list();

// With pagination
var result = meilisearch()
	.keys()
	.list( { offset: 0, limit: 10 } );
```

🔗 [Meilisearch: Get Keys](https://www.meilisearch.com/docs/reference/api/keys#get-keys)

### Get an API key

Retrieve a single API key by its UID or key value.

```js
var result = meilisearch()
	.keys()
	.get( "abc123" );
```

🔗 [Meilisearch: Get Key](https://www.meilisearch.com/docs/reference/api/keys#get-one-key)

### Update an API key

Update an existing API key's name or description.

```js
meilisearch()
	.keys()
	.update( "abc123", { name: "Updated Key Name" } );
```

🔗 [Meilisearch: Update Key](https://www.meilisearch.com/docs/reference/api/keys#update-a-key)

### Delete an API key

Permanently delete an API key.

```js
meilisearch()
	.keys()
	.delete( "abc123" );
```

🔗 [Meilisearch: Delete Key](https://www.meilisearch.com/docs/reference/api/keys#delete-a-key)

## Settings

### List settings

Retrieve the complete settings configuration for an index.

```js
var result = meilisearch()
	.index( "books" )
	.settings()
	.list();
```

🔗 [Meilisearch: Get Settings](https://www.meilisearch.com/docs/reference/api/settings#get-settings)

### Update settings

Update index settings including ranking rules, searchable attributes, and more.

```js
meilisearch()
	.index( "books" )
	.settings()
	.update( {
	  "searchableAttributes": [ "title", "description", "author" ],
	  "filterableAttributes": [ "genre", "year" ],
	  "sortableAttributes": [ "year", "price" ],
	  "rankingRules": [
		  "words",
		  "typo",
		  "proximity",
		  "attribute",
		  "sort",
		  "exactness"
	  ],
	  "stopWords": [ "the", "a", "an" ],
	  "synonyms": {
		  "computer": [ "pc", "laptop", "desktop" ]
	  }
  } );
```

🔗 [Meilisearch: Update Settings](https://www.meilisearch.com/docs/reference/api/settings#update-settings)

### Reset settings

Reset all index settings to their default values.

```js
meilisearch()
	.index( "books" )
	.settings()
	.reset();
```

🔗 [Meilisearch: Reset Settings](https://www.meilisearch.com/docs/reference/api/settings#reset-settings)

## Tasks

### List tasks

List all asynchronous tasks with filtering and pagination options.

```js
var result = meilisearch()
	.tasks()
	.list();

// With filters
var result = meilisearch()
	.tasks()
	.list( {
	  limit: 20,
	  statuses: "enqueued,processing",
	  types: "indexCreation,indexUpdate"
  } );
```

🔗 [Meilisearch: Get Tasks](https://www.meilisearch.com/docs/reference/api/tasks#get-tasks)

### Get a task

Retrieve a single task by its unique identifier.

```js
var result = meilisearch()
	.tasks()
	.get( "123" );
```

🔗 [Meilisearch: Get Task](https://www.meilisearch.com/docs/reference/api/tasks#get-one-task)

### Cancel tasks

Cancel enqueued or processing tasks.

```js
// Cancel specific tasks by UID
meilisearch()
	.tasks()
	.cancel( { uids: [ "1", "5", "7" ] } );

// Cancel tasks by status
meilisearch()
	.tasks()
	.cancel( { statuses: "enqueued" } );
```

🔗 [Meilisearch: Cancel Tasks](https://www.meilisearch.com/docs/reference/api/tasks#cancel-task)

### Delete tasks

Delete tasks matching specific criteria.

```js
// Delete specific tasks by UID
meilisearch()
	.tasks()
	.delete( { uids: [ "1", "5" ] } );

// Delete tasks by status
meilisearch()
	.tasks()
	.delete( { statuses: "canceled" } );

// Delete completed tasks older than a date
meilisearch()
	.tasks()
	.delete( {
		statuses: "succeeded,failed",
		beforeEnqueuedAt: "2024-01-01T00:00:00Z"
	} );
```

🔗 [Meilisearch: Delete Tasks](https://www.meilisearch.com/docs/reference/api/tasks#delete-task)

## Batches

The Batches API allows you to monitor how Meilisearch groups and processes asynchronous operations. Batches show the progress of grouped tasks.

### List batches

List all batches with filtering and pagination options.

```js
var result = meilisearch()
	.batches()
	.list();

// With filters
var result = meilisearch()
	.batches()
	.list({
		limit: 10,
		from: 0,
		reverse: false
	});

// Returns: {
//   results: [
//     {
//       uid: 2,
//       progress: null,
//       details: { receivedDocuments: 6, indexedDocuments: 6 },
//       stats: { totalNbTasks: 1, status: { succeeded: 1 } },
//       duration: "PT0.110083S",
//       startedAt: "2024-12-10T15:49:04.995321Z",
//       finishedAt: "2024-12-10T15:49:05.105404Z",
//       batchStrategy: "batched all enqueued tasks"
//     }
//   ],
//   total: 3,
//   limit: 1,
//   from: 2
// }
```

🔗 [Meilisearch: Get Batches](https://www.meilisearch.com/docs/reference/api/batches#get-batches)

### Get a batch

Retrieve a single batch by its unique identifier.

```js
var result = meilisearch()
	.batches()
	.get( "0" );

// Returns: {
//   uid: 0,
//   progress: { steps: [...], percentage: 32.8471 },
//   details: { receivedDocuments: 6, indexedDocuments: 6 },
//   stats: { totalNbTasks: 1, status: { succeeded: 1 } },
//   duration: "PT0.250518S",
//   startedAt: "2024-12-10T15:20:30.18182Z",
//   finishedAt: "2024-12-10T15:20:30.432338Z",
//   batchStrategy: "batched all enqueued tasks"
// }
```

🔗 [Meilisearch: Get One Batch](https://www.meilisearch.com/docs/reference/api/batches#get-one-batch)

## Webhooks

The Webhooks API allows you to trigger automatic workflows when Meilisearch finishes processing tasks. When a task completes, Meilisearch sends the task object to all configured webhooks.

**Note:** You can create up to 20 webhooks. Having multiple webhooks active at the same time may negatively impact performance.

### List webhooks

List all configured webhooks.

```js
var result = meilisearch()
	.webhooks()
	.list();

// Returns: {
//   results: [
//     {
//       uuid: "627ea538-733d-4545-8d2d-03526eb381ce",
//       url: "https://example.com/webhook",
//       headers: { authorization: "REDACTED" },
//       isEditable: true
//     }
//   ]
// }
```

🔗 [Meilisearch: Get Webhooks](https://www.meilisearch.com/docs/reference/api/webhooks#get-all-webhooks)

### Create a webhook

Create a new webhook to receive task completion notifications.

```js
var result = meilisearch()
	.webhooks()
	.create({
		url: "https://example.com/webhook",
		headers: {
			authorization: "Bearer SECRET_KEY",
			referer: "https://example.com"
		}
	});

// Returns: {
//   uuid: "627ea538-733d-4545-8d2d-03526eb381ce",
//   url: "https://example.com/webhook",
//   headers: {
//     authorization: "Bearer SECRET_KEY",
//     referer: "https://example.com"
//   },
//   isEditable: true
// }
```

🔗 [Meilisearch: Create Webhook](https://www.meilisearch.com/docs/reference/api/webhooks#create-a-webhook)

### Get a webhook

Retrieve a single webhook by its UUID.

```js
var result = meilisearch()
	.webhooks()
	.webhook( "WEBHOOK_UUID" )
	.get();
```

🔗 [Meilisearch: Get Webhook](https://www.meilisearch.com/docs/reference/api/webhooks#get-a-single-webhook)

### Update a webhook

Update a webhook's configuration. To remove a field, set its value to `null`.

```js
var result = meilisearch()
	.webhooks()
	.webhook( "WEBHOOK_UUID" )
	.update({
		headers: {
			referer: null  // Remove this header
		}
	});

// Returns: {
//   uuid: "627ea538-733d-4545-8d2d-03526eb381ce",
//   url: "https://example.com/webhook",
//   headers: {
//     authorization: "Bearer SECRET_KEY"
//   },
//   isEditable: true
// }
```

🔗 [Meilisearch: Update Webhook](https://www.meilisearch.com/docs/reference/api/webhooks#update-a-webhook)

### Delete a webhook

Delete a webhook to stop receiving task completion notifications.

```js
meilisearch()
	.webhooks()
	.webhook( "WEBHOOK_UUID" )
	.delete();
// Returns: 204 No Content
```

🔗 [Meilisearch: Delete Webhook](https://www.meilisearch.com/docs/reference/api/webhooks#delete-a-webhook)

## Task Object

Every asynchronous operation in Meilisearch (index creation, document updates, index swaps, etc.) returns a **Task** object. This object provides methods to track the operation's progress and wait for completion.

### Understanding Tasks

Meilisearch operations are asynchronous - when you create an index or add documents, Meilisearch creates a `Task` to track that operation while it continues in the background. You use the Task object to:

1. Check the current status of the operation
2. Wait for the operation to complete
3. Get detailed information about the operation result

### Example: Creating an Index with Task Tracking

```js
// Create an index - returns a Task object immediately
var task = meilisearch()
	.index( "books" )
	.create();

// Check initial status
print( "Task Status: " & task.getStatus() );  // "enqueued"
print( "Task Type: " & task.getType() );      // "indexCreation"
print( "Task UID: " & task.getTaskUid() );    // "123"

// Wait for the task to complete (polls every second, by default)
var completedTask = task.waitForCompletion();

// Check final status
if ( completedTask.getStatus() == "succeeded" ) {
	print( "Index created successfully!" );
} else if ( completedTask.getStatus() == "failed" ) {
	print( "Failed: " & completedTask.getError().message );
}
```

### Task.getStatus()

Get the current status of the task.

```js
var task = meilisearch()
	.index( "books" )
	.create();

print( task.getStatus() );  // "enqueued", "processing", "succeeded", "failed", or "canceled"
```

**Possible values:**
- `enqueued` - Task is in the queue, waiting to be processed
- `processing` - Task is currently being processed
- `succeeded` - Task completed successfully
- `failed` - Task failed (check `getError()` for details)
- `canceled` - Task was canceled

### Task.getType()

Get the type of operation this task represents.

```js
var task = meilisearch()
	.index( "books" )
	.documents()
	.add([ { id: 1, title: "Book" } ])
	.orReplace();

print( task.getType() );  // "documentAdditionOrUpdate"
```

**Common types:**
- `indexCreation` - Creating a new index
- `indexUpdate` - Updating an index
- `indexDeletion` - Deleting an index
- `documentAdditionOrUpdate` - Adding or updating documents
- `documentDeletion` - Deleting documents
- `indexSwap` - Swapping two indexes
- `settingsUpdate` - Updating index settings

### Task.toStruct()

Convert the Task object to a plain struct with all task data.

```js
var task = meilisearch()
	.index( "books" )
	.create();

var taskData = task.toStruct();

// Returns: {
//   taskUid: "123",
//   indexUid: "books",
//   status: "succeeded",
//   type: "indexCreation",
//   enqueuedAt: "2024-01-15T10:30:00.000Z",
//   startedAt: "2024-01-15T10:30:01.000Z",
//   finishedAt: "2024-01-15T10:30:02.000Z",
//   duration: "1s",
//   details: { ... }
// }
```

### Task.waitForCompletion( interval )

Wait for the task to complete by polling at regular intervals.

```js
var task = meilisearch()
	.index( "books" )
	.documents()
	.add([
		{ id: 1, title: "Book 1" },
		{ id: 2, title: "Book 2" }
	])
	.orReplace();

// Wait up to 30 seconds, polling every 2 seconds
var completedTask = task.waitForCompletion( 2000, 30000 );

if ( completedTask.getStatus() == "succeeded" ) {
	print( "Documents added successfully!" );
	print( "Documents processed: " & completedTask.getDetails().receivedDocuments );
}
```

**Parameters:**
- `interval` (integer) - Number of milliseconds to wait between polls (default: 1000)
- `timeout` (integer) - Maximum time to wait for task completion in milliseconds (default: 30000)

**Returns:** A new Task object with the final task status

**Note:** The original Task object is not modified; `waitForCompletion()` returns a new Task instance with updated data.

### Additional Task Getters

```js
var task = meilisearch().index( "books" ).create();

// Get basic info
task.getTaskUid();      // Unique task identifier
task.getIndexUid();     // Index this task operates on
task.getEnqueuedAt();   // When task was queued (ISO timestamp)
task.getStartedAt();    // When processing started
task.getFinishedAt();   // When processing finished
task.getDuration();     // How long processing took

// Get detailed info
task.getDetails();      // Task-specific details (varies by type)
task.getError();        // Error info if task failed
task.getCanceledBy();   // UID of task that canceled this one (if any)

// Check completion status
task.isComplete();      // Returns true if status is "succeeded", "failed", or "canceled"
```

## Experimental Features

### List experimental features

List all available experimental features and their current status.

```js
var result = meilisearch()
	.experimentalFeatures()
	.list();
```

🔗 [Meilisearch: Get Experimental Features](https://www.meilisearch.com/docs/reference/api/experimental-features#get-experimental-features)

### Get an experimental feature

Retrieve the status of a specific experimental feature.

```js
var result = meilisearch()
	.experimentalFeatures()
	.get( "metrics" );
```

🔗 [Meilisearch: Get One Experimental Feature](https://www.meilisearch.com/docs/reference/api/experimental-features#get-one-experimental-feature)

### Enable/disable an experimental feature

Enable or disable a specific experimental feature.

```js
// Enable
meilisearch()
	.experimentalFeatures()
	.set( "metrics", true );

// Disable
meilisearch()
	.experimentalFeatures()
	.set( "metrics", false );
```

🔗 [Meilisearch: Update Experimental Features](https://www.meilisearch.com/docs/reference/api/experimental-features#update-experimental-features)

### Set multiple experimental features

Enable or disable multiple experimental features at once.

```js
meilisearch()
	.experimentalFeatures()
	.setAll( {
	  "metrics": true,
	  "exportPayer": false,
	  "logs": true
  } );
```

🔗 [Meilisearch: Update Experimental Features](https://www.meilisearch.com/docs/reference/api/experimental-features#update-experimental-features)

## Snapshots

### Create a snapshot

Create a snapshot of the Meilisearch instance for backup purposes.

```js
var result = meilisearch()
	.snapshots()
	.create();
```

🔗 [Meilisearch: Create Snapshot](https://www.meilisearch.com/docs/reference/api/snapshots#create-snapshot)

## Network

The Network API allows you to create a network of Meilisearch instances for federated search and horizontal database partitioning strategies like sharding.

**Note:** This is an experimental feature. Enable it first using the experimental features endpoint.

### Get network configuration

Retrieve the current network configuration including self instance name, sharding status, and remote instances.

```js
var result = meilisearch()
	.network()
	.get();

// Returns: {
//   self: "ms-00",
//   sharding: false,
//   remotes: {
//     "ms-00": {
//       url: "http://ms-1235.example.meilisearch.io",
//       searchApiKey: "Ecd1SDDi4pqdJD6qYLxD3y7VZAEb4d9j6LJgt4d6xas"
//     }
//   }
// }
```

🔗 [Meilisearch: Get Network](https://www.meilisearch.com/docs/reference/api/network#get-the-network-object)

### Update network configuration

Update the network configuration. Updates are partial - only provide the fields you want to update.

```js
meilisearch()
	.network()
	.update({
		self: "ms-00",
		sharding: true,
		remotes: {
			"ms-00": {
				url: "http://localhost:7700",
				searchApiKey: "masterKey",
				writeApiKey: "masterKey"
			},
			"ms-01": {
				url: "http://remote-instance:7700",
				searchApiKey: "remoteSearchKey",
				writeApiKey: "remoteWriteKey"
			}
		}
	});
```

🔗 [Meilisearch: Update Network](https://www.meilisearch.com/docs/reference/api/network#update-the-network-object)

## Similar Documents

The Similar Documents API uses AI-powered search to find documents similar to a specific document. This requires the document to have vector embeddings generated by a configured embedder.

**Note:** This endpoint requires an embedder to be configured in the index settings first.

### Get similar documents

Find documents similar to a target document using POST or GET requests.

```js
// Using POST (recommended)
var result = meilisearch()
	.index( "books" )
	.document( "123" )
	.similar({ embedder: "default" })
	.send();

// Using GET
var result = meilisearch()
	.index( "books" )
	.document( "123" )
	.similar({ embedder: "default" })
	.sendGet();

// With additional parameters
var result = meilisearch()
	.index( "books" )
	.document( "123" )
	.similar({
		embedder: "default",
		limit: 10,
		filter: "genre = fiction",
		showRankingScore: true
	})
	.send();

// Returns: {
//   hits: [
//     { id: "456", title: "Similar Book 1" },
//     { id: "789", title: "Similar Book 2" }
//   ],
//   id: "123",
//   processingTimeMs: 5,
//   limit: 10,
//   offset: 0,
//   estimatedTotalHits: 2
// }
```

🔗 [Meilisearch: Similar Documents](https://www.meilisearch.com/docs/reference/api/similar#get-similar-documents-with-post)

## Health Check

### Check instance health

Check if the Meilisearch instance is available and responding.

```js
var result = meilisearch()
	.health();
// Returns: { "status": "available" }
```

🔗 [Meilisearch: Health](https://www.meilisearch.com/docs/reference/api/health)

## Version

### Get instance version

Retrieve the version information of the Meilisearch instance.

```js
var result = meilisearch()
	.version();
// Returns: { "commitSha": "...", "commitDate": "...", "pkgVersion": "1.x.x" }
```

🔗 [Meilisearch: Version](https://www.meilisearch.com/docs/reference/api/version)