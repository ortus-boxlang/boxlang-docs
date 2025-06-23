[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryAddColumn`

Adds a column to a query and populates its rows with the contents of a one-dimensional array.

## Method Signature

```
QueryAddColumn(query=[query], columnName=[string], datatype=[any], array=[array])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query object to which the column should be added. |  |
| `columnName` | `string` | `true` | The name of the column to add. |  |
| `datatype` | `any` | `false` | The column data type of the new column or the array to populate the column with a generic type of anything. | `object` |
| `array` | `array` | `false` |  | `[]` |

## Examples

### Tag Example

 


```java
<!--- Make a query. ---> 
 <bx:set myQuery = queryNew( "" ) > 
  <!--- Create an array. ---> 
 <bx:set FastFoodArray = arrayNew( 1 ) > 
 <bx:set FastFoodArray[ 1 ] = "French Fries" > 
 <bx:set FastFoodArray[ 2 ] = "Hot Dogs" > 
 <bx:set FastFoodArray[ 3 ] = "Fried Clams" > 
 <bx:set FastFoodArray[ 4 ] = "Thick Shakes" > 
 <!--- Use the array to add a column to the query. ---> 
 <bx:set nColumnNumber = queryAddColumn( myQuery, "FastFood", "VarChar", FastFoodArray ) > 
 <bx:dump var="#myQuery#"/> 
```


### member syntax example

add a column to a query using member syntax

<a href="https://try.boxlang.io/?code=eJxLys%2FPLlawVSgsTS2q9Est11BQykzRKcksyUlV0gGy80pS01OLdMoSi5IzEouUFDStuZJAWvQSU1Kc83NKc%2FOAOhJLSzLyi0DqYep0FKJjQWrLizJLUl1Kcws0FMDaQGIAukUlgg%3D%3D" target="_blank">Run Example</a>

```java
books = queryNew( "id,title", "integer,varchar" );
books.addColumn( "author", "varchar", [] );
writeDump( books );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrLKpUsFUoLE0tqvRLLddQUEpMTNRJSkpSUtC05goECTumpATlA2UKgSphYsGpJc6pOTlgQR2wHiUgZahnqIRLCchIsBIjckw2ImyyEZrJzvk5pbl5MEXJyclARTmZxSUh%2BY5FRYmVQJ8a6xnqGIN14daXkpICMjwzryQ1PbUIwwgToBEmcCPKizJLUl1KcwvAuvWc%2FX1Cff18PINDQJIAVuJqfw%3D%3D" target="_blank">Run Example</a>

```java
qry = queryNew( "aaa,bbb" );
QueryAddRow( qry );
QuerySetCell( qry, "aaa", "1.1" );
QuerySetCell( qry, "bbb", "1.2" );
QueryAddRow( qry );
QuerySetCell( qry, "aaa", "2.1" );
QuerySetCell( qry, "bbb", "2.2" );
QueryAddColumn( qry, "ccc", listToArray( "3.1,3.2" ) );
QueryAddColumn( qry, "ddd", "integer", listToArray( "4.1,4.2" ) );
writeDump( qry.COLUMNLIST );

```



## Related

  * [QueryAddRow](./QueryAddRow.md)
  * [QueryAppend](./QueryAppend.md)
  * [QueryClear](./QueryClear.md)
  * [QueryColumnArray](./QueryColumnArray.md)
  * [QueryColumnCount](./QueryColumnCount.md)
  * [QueryColumnData](./QueryColumnData.md)
  * [QueryColumnExists](./QueryColumnExists.md)
  * [QueryColumnList](./QueryColumnList.md)
  * [QueryCurrentRow](./QueryCurrentRow.md)
  * [QueryDeleteColumn](./QueryDeleteColumn.md)
  * [QueryDeleteRow](./QueryDeleteRow.md)
  * [QueryEach](./QueryEach.md)
  * [QueryEvery](./QueryEvery.md)
  * [QueryFilter](./QueryFilter.md)
  * [QueryGetCell](./QueryGetCell.md)
  * [QueryGetResult](./QueryGetResult.md)
  * [QueryInsertAt](./QueryInsertAt.md)
  * [QueryKeyExists](./QueryKeyExists.md)
  * [QueryMap](./QueryMap.md)
  * [QueryNew](./QueryNew.md)
  * [QueryNone](./QueryNone.md)
  * [QueryPrepend](./QueryPrepend.md)
  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryReduce](./QueryReduce.md)
  * [QueryRegisterFunction](./QueryRegisterFunction.md)
  * [QueryReverse](./QueryReverse.md)
  * [QueryRowData](./QueryRowData.md)
  * [QueryRowSwap](./QueryRowSwap.md)
  * [QuerySetCell](./QuerySetCell.md)
  * [QuerySetRow](./QuerySetRow.md)
  * [QuerySlice](./QuerySlice.md)
  * [QuerySome](./QuerySome.md)
  * [QuerySort](./QuerySort.md)
