# Query Invocations

* [`onQueryBuild`](#onquerybuild)
* [`preQueryExecute`](#prequeryexecute)
* [`postQueryExecute`](#postqueryexecute)
* [`queryAddRow`](#queryaddrow)

## onQueryBuild

Triggered upon construction of a JDBC `PendingQuery` class, used for all query executions from `queryExecute()` to `bx:query`.

| Data Key   | Type          | Description                                                                   |
| ---------- | ------------- | ----------------------------------------------------------------------------- |
| `sql`      | String        | The SQL statement being executed.                      |
| `bindings` | Array|Struct  | Unprocessed data bindings to use in the SQL statement. |
| `pendingQuery`    | Java class    | `PendingQuery` instance.                                          |
| `options` | Java class    | `QueryOptions` instance.                                          |

### Example

```js
function onQueryBuild( struct data ) {
    println("Query build in progress!");
}
```

## preQueryExecute

Triggered immediately before query execution.

| Data Key   | Type          | Description                                                                   |
| ---------- | ------------- | ----------------------------------------------------------------------------- |
| `sql`      | String        | The SQL statement being executed.                      |
| `bindings` | List  | Data bindings, processed and normalized for use as query parameters. |
| `pendingQuery`    | Java class    | `PendingQuery` instance.                                          |

### Example

```js
function preQueryExecute( struct data ) {
    println("Query ready to execute!");
}
```

## postQueryExecute

Triggered immediately after query execution.

| Data Key   | Type          | Description                                                                   |
| ---------- | ------------- | ----------------------------------------------------------------------------- |
| `sql`      | String        | The SQL statement being executed
| `bindings` | List  | Data bindings, processed and normalized for use as query parameters. |
| `executionTime` | Number        | Execution time in milliseconds.                                               |
| `data`    | Query  | Result set populated into a Query object.                                                                 |
| `result` | Struct  | Struct of result metadata, including `cached`, `cacheKey`, `sql`, `sqlParameters`, `executionTime`, `recordCount`, and, optionally, `generatedKey`. |
| `pendingQuery`    | Java class    | `PendingQuery` instance.                                          |
| `executedQuery`    | Java class    | `ExecutedQuery` instance.                                          |

### Example

```js
function postQueryExecute( struct data ) {
    println("Query execution complete!");
}
```

## queryAddRow