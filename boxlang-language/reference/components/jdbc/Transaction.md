
# Component: `Transaction`

Demarcate or manage a JDBC transaction.

## Component Signature

```
<bx:Transaction action=[string]
isolation=[string]
savepoint=[string]
datasource=[string] />
```

### Attributes


| Attribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `action` | `string` | `false` | When used inside a transaction block, perform some action upon an existing transaction. One of: `begin`, `commit`, `rollback`, `setsavepoint`, or `releasesavepoint`. | `begin` |
| `isolation` | `string` | `false` | The isolation level to use for the transaction. Can only be set upon transaction begin. One of: `read_uncommitted`, `read_committed`, `repeatable_read`, or `serializable`. |  |
| `savepoint` | `string` | `false` | The name of the savepoint to set, roll back to, or release. Required for `setsavepoint` and `releasesavepoint`. |  |
| `datasource` | `string` | `false` | The name of the datasource to use for the transaction. If not provided, the first query execution inside the transaction will set the datasource. |  |

## Examples

### Simple Transaction

A "simple" transaction might look like this:

```js
transaction{
    queryExecute( "UPDATE users SET name=:name WHERE id=:id", { id: variables.id, name: variables.name } );
    queryExecute(
        "INSERT INTO userLog( action, id, changes ) VALUES ( 'UPDATE', :id, :change)",
        { id: variables.id, change: "changed name to #variables.name#" }
    );
}
```

Note that you can specify a custom isolation level using the `isolation` attribute on the component:

```js
transaction isolation="serializable"{
    // ...
}
```


### Release a Savepoint

{% hint style="info" %}
The `releasesavepoint` action is added in BoxLang 1.19.0 (currently unreleased).
{% endhint %}

Release is optional cleanup of a recovery boundary. It does not commit or roll back changes. Releasing a savepoint invalidates it and all savepoints created after it; earlier savepoints remain available, and the released name can be reused.

```js
transaction {
	bx:transaction action="setsavepoint" savepoint="beforeUpdate";
	queryExecute( "UPDATE products SET price = ? WHERE id = ?", [ { value: 19.99, sqltype: "decimal", scale: 2 }, 42 ] )
	bx:transaction action="releasesavepoint" savepoint="beforeUpdate";
}
```

The statement-only component actions above require terminating semicolons. This example assumes a configured default datasource and an existing `products` table. The update commits when the outer transaction completes successfully.

```xml
<bx:transaction>
	<bx:transaction action="setsavepoint" savepoint="pending" />
	<bx:transaction action="releasesavepoint" savepoint="pending" />
</bx:transaction>
```

A savepoint set before the first query is pending, so the template above needs no database connection. Once a connection exists, release requires JDBC driver support. Invalid names, missing savepoints, and unsupported or failed JDBC release raise errors. Outside an active transaction, the action is silently ignored, matching the other non-begin component actions.

See [`transactionReleaseSavepoint()`](../../built-in-functions/jdbc/TransactionReleaseSavepoint.md) for errors and lifetime rules, or the [transaction guide](../../../../boxlang-framework/jdbc/transactions.md#release-savepoints-after-use) for a batch example.

### Nested Transaction

When `enableNestedTransactions` is enabled, BoxLang uses savepoints to control transaction state between parent and child transactions. By default the setting is disabled, and nested blocks share the outer transaction context.

```js
transaction{
    queryExecute( "UPDATE users SET name=:name WHERE id=:id", { id: variables.id, name: variables.name } );

    transaction{
        try{
            queryExecute(
                "INSERT INTO userLog( action, id, changes ) VALUES ( 'UPDATE', :id, :change)",
                { id: variables.id, change: "changed name to #variables.name#" }
            );
        } catch( any e ){
            // user log errored; rollback!
            transactionRollback();
            // log error here
        }
    }
}
```

Here, we have a nested transaction that may (or may not) error; if this happens we want to roll back the logging query but NOT roll back the user query. This functions the same as if we were rolling back to a named savepoint created just after the `UPDATE users` query.
### Script Syntax



<a href="https://try.boxlang.io/?code=eJxLqrAqKUrMK05MLsnMz1Oo5uIsKaoEUZz6%2BgrJ%2BSmpCiX5CkWleUCBJFSlEMpWKTk%2FNzezRMmai7NWITmxJDlDQSMxr1IhVRNsCg5NRfk5OUmJydlgbVy1XADL1Cvw" target="_blank">Run Example</a>

```java
bx:transaction {
	try {
		// code to run
		bx:transaction action="commit";
	} catch (any e) {
		bx:transaction action="rollback";
	}
}

```


### Tag Syntax




```java
<bx:transaction> 
 <bx:try> 
 <!--- code to run ---> 
   <bx:transaction action="commit"/> 
  
 <bx:catch type="any"> 
 <bx:transaction action="rollback"/> 
 </bx:catch></bx:try> 
 </bx:transaction>
```


