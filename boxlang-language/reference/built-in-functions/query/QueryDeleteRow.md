[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryDeleteRow`

This function deletes a row from the query

## Method Signature

```
QueryDeleteRow(query=[query], row=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to delete the row from |  |
| `row` | `integer` | `true` | The row index to delete |  |

## Examples

### Implicit deletion of the last row

Builds a simple query and removes the last row by not specifying a row index.


```java
news = queryNew( "id,title", "integer,varchar", [ 
	{
		"id" : 1,
		"title" : "Dewey defeats Truman"
	},
	{
		"id" : 2,
		"title" : "Man walks on Moon"
	}
] );
queryDeleteRow( news );
writeOutput( news[ "title" ][ 1 ] );

```

Result: Dewey defeats Truman

### Deletes a specific row from the query

Builds a simple query and removes one of the rows.

<a href="https://try.boxlang.io/?code=eJxdjjELwjAUhOfkVxyZFLLUUXHrWgviVjoE%2B9RiTTR9MRTxv5u2OOh27%2B6%2Bx1mKPbZ4BPLDjuICqm00t9yR0klbpjN5%2FTT%2BeDE%2BWRWkeEkhUk1hjUyPeu6nU%2BUUaUBDJzLc4%2BDDzVglxVv%2FUKs%2FqjAW0XTXHs6icG5CZI3lRk7DcuqIae%2FSPJv2amRjFH3LVAa%2BB579Ct%2BfdZUqE%2F8BgdlAzA%3D%3D" target="_blank">Run Example</a>

```java
news = queryNew( "id,title", "integer,varchar", [ 
	{
		"id" : 1,
		"title" : "Dewey defeats Truman"
	},
	{
		"id" : 2,
		"title" : "Man walks on Moon"
	}
] );
queryDeleteRow( news, 1 );
writeOutput( news[ "title" ][ 1 ] );

```

Result: Man walks on Moon

### Additional Examples

<a href="https://try.boxlang.io/?code=eJy1kLEKwjAQhufkKY5MKcRC01F0ad2khaKTOMQQsWCtjamliO%2FutcZBcXFw%2BiDff%2BG%2Fa2wfwQya1tg%2BMx0HpsROaCaAXZXVB2XFB1FtgJINJYSpiImBO08dMUq24mWlt55avtnYW08dD5ZuIZjSsU5qjsaZosZSDbYUIAfV2dKZtK3O%2FFk6qY9tdUqVU68YUwyC0NXL8uJ4MH5ne%2Fn7kn%2FecV9bDiXWiqeI%2BQwi5GQCAdwo%2BXIAKTCGc%2Fe3E%2BB7WCySvEiTfJ2thsAD54lxZQ%3D%3D" target="_blank">Run Example</a>

```java
qry1 = queryNew( "a,b,c", "varchar,varchar,varchar", [ 
	[
		"a1",
		"b1",
		"c1"
	],
	[
		"a2",
		"b2",
		"c2"
	],
	[
		"a3",
		"b3",
		"c3"
	]
] );
queryDeleteRow( qry1, 2 );
writeDump( queryColumnData( qry1, "a" ).toList() );
qry2 = queryNew( "a,b,c", "varchar,varchar,varchar", [
	[
		"a1",
		"b1",
		"c1"
	],
	[
		"a2",
		"b2",
		"c2"
	],
	[
		"a3",
		"b3",
		"c3"
	]
] );
for( i = 3; i >= 1; i-- ) {
	queryDeleteRow( qry2, i );
}
writeDump( qry2.RECORDCOUNT );

```



## Related

  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryColumnList](./QueryColumnList.md)
  * [QueryRowSwap](./QueryRowSwap.md)
  * [QuerySort](./QuerySort.md)
  * [QueryEach](./QueryEach.md)
  * [QueryKeyExists](./QueryKeyExists.md)
  * [QueryColumnCount](./QueryColumnCount.md)
  * [QueryReduce](./QueryReduce.md)
  * [QueryCurrentRow](./QueryCurrentRow.md)
  * [QueryColumnData](./QueryColumnData.md)
  * [QueryRowData](./QueryRowData.md)
  * [QueryFilter](./QueryFilter.md)
  * [QueryAddRow](./QueryAddRow.md)
  * [QueryNew](./QueryNew.md)
  * [QueryReverse](./QueryReverse.md)
  * [QueryPrepend](./QueryPrepend.md)
  * [QueryColumnExists](./QueryColumnExists.md)
  * [QueryAddColumn](./QueryAddColumn.md)
  * [QueryGetCell](./QueryGetCell.md)
  * [QueryGetResult](./QueryGetResult.md)
  * [QueryMap](./QueryMap.md)
  * [QueryEvery](./QueryEvery.md)
  * [QueryRecordCount](./QueryRecordCount.md)
  * [QuerySome](./QuerySome.md)
  * [QueryDeleteColumn](./QueryDeleteColumn.md)
  * [QuerySetCell](./QuerySetCell.md)
  * [QueryInsertAt](./QueryInsertAt.md)
  * [QueryClear](./QueryClear.md)
  * [QuerySetRow](./QuerySetRow.md)
  * [QueryColumnArray](./QueryColumnArray.md)
  * [QueryAppend](./QueryAppend.md)
  * [QuerySlice](./QuerySlice.md)
  * [QueryRegisterFunction](./QueryRegisterFunction.md)
