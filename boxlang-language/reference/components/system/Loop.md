
# Component: `Loop`

Executes the appropriate loop type based on the provided attributes.

## Component Signature

```
<bx:Loop array=[array]
item=[string]
index=[string]
to=[double]
from=[double]
step=[number]
file=[string]
list=[string]
delimiters=[string]
collection=[collection]
condition=[function]
query=[any]
group=[string]
groupCaseSensitive=[boolean]
startRow=[integer]
endRow=[integer]
label=[string]
times=[integer] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array` | `array` | `false` | An Array object to iterate over. When specified, the loop will process each element<br>                  in the array. Can be used with <code>item</code> and/or <code>index</code> attributes.<br>                  <br><br>                  <strong>Example:</strong> <code>&lt;bx:loop array="#myArray#" item="element"&gt;</code> |  |
| `item` | `string` | `false` | Variable name to hold the current item value during iteration. Behavior varies by loop type:<br>                 <ul><br>                 <li><strong>Array loops:</strong> Contains the current array element</li><br>                 <li><strong>List loops:</strong> Contains the current list item</li><br>                 <li><strong>Collection loops:</strong> Contains the current collection key</li><br>                 <li><strong>Times loops:</strong> If no index specified, contains the current iteration number</li><br>                 </ul><br>                 <br><br>                 <strong>Example:</strong> <code>&lt;bx:loop array="#colors#" item="color"&gt;</code> |  |
| `index` | `string` | `false` | Variable name to hold the current index/position during iteration. Behavior varies by loop type:<br>                  <ul><br>                  <li><strong>Array loops:</strong> Contains the 1-based array index</li><br>                  <li><strong>Numeric range loops:</strong> Contains the current numeric value (required)</li><br>                  <li><strong>File loops:</strong> Contains the current line content (required)</li><br>                  <li><strong>Times loops:</strong> Contains the current iteration number</li><br>                  </ul><br>                  <br><br>                  <strong>Example:</strong> <code>&lt;bx:loop from="1" to="10" index="i"&gt;</code> |  |
| `to` | `double` | `false` | End value for numeric range loops. The loop continues while the index value<br>               has not exceeded this value (considering step direction). Required when using<br>               numeric range loops with <code>from</code> and <code>index</code>.<br>               <br><br>               <strong>Example:</strong> <code>&lt;bx:loop from="1" to="100" step="5" index="i"&gt;</code> |  |
| `from` | `double` | `false` | Starting value for numeric range loops. Defaults to 0 if not specified.<br>                 Used in conjunction with <code>to</code> and <code>index</code> for numeric iteration.<br>                 <br><br>                 <strong>Example:</strong> <code>&lt;bx:loop from="10" to="1" step="-1" index="i"&gt;</code> |  |
| `step` | `number` | `false` | Increment/decrement value for numeric range loops. Defaults to 1.<br>                 Positive values increment the index, negative values decrement.<br>                 Zero values are ignored to prevent infinite loops.<br>                 <br><br>                 <strong>Example:</strong> <code>&lt;bx:loop from="0" to="20" step="2" index="even"&gt;</code> | `1` |
| `file` | `string` | `false` | Absolute path to a text file to read line by line. Each iteration provides<br>                 one line of the file content in the <code>index</code> variable. The file<br>                 is automatically closed when the loop completes. Requires <code>index</code> attribute.<br>                 <br><br>                 <strong>Example:</strong> <code>&lt;bx:loop file="/path/to/data.txt" index="line"&gt;</code> |  |
| `list` | `string` | `false` | A delimited string to process item by item. Each item becomes available<br>                 through the <code>item</code> or <code>index</code> variable. Use with<br>                 <code>delimiters</code> to specify custom separators.<br>                 <br><br>                 <strong>Example:</strong> <code>&lt;bx:loop list="red,green,blue" item="color"&gt;</code> |  |
| `delimiters` | `string` | `false` | Characters that separate items in the <code>list</code> attribute.<br>                       Defaults to comma (",") if not specified. Multiple delimiter characters<br>                       can be specified.<br>                       <br><br>                       <strong>Example:</strong> <code>&lt;bx:loop list="a|b|c" delimiters="|" item="letter"&gt;</code> |  |
| `collection` | `collection` | `false` | A Java Collection object (including BoxLang Structs) to iterate over.<br>                       For Structs, each iteration provides a key. Requires <code>item</code> attribute<br>                       to specify the variable name for the current key.<br>                       <br><br>                       <strong>Example:</strong> <code>&lt;bx:loop collection="#myStruct#" item="key"&gt;</code> |  |
| `condition` | `function` | `false` | A function/closure that returns a boolean value. The loop continues<br>                      while this condition evaluates to true. The condition is evaluated<br>                      before each iteration.<br>                      <br><br>                      <strong>Example:</strong> <code>&lt;bx:loop condition="#() => hasMoreData()#"&gt;</code> |  |
| `query` | `any` | `false` | A Query object or variable name containing a query to iterate over.<br>                  Each iteration makes one row of the query available. Can be combined<br>                  with <code>group</code> for grouped processing, or <code>startRow</code>/<br>                  <code>endRow</code> for range constraints.<br>                  <br><br>                  <strong>Example:</strong> <code>&lt;bx:loop query="#employeeQuery#"&gt;</code> |  |
| `group` | `string` | `false` | Comma-separated list of query column names to group by. When specified,<br>                  the loop processes data in groups, executing the body once per group<br>                  change rather than once per row. Enables nested looping for hierarchical<br>                  data processing. Requires <code>query</code> attribute.<br>                  <br><br>                  <strong>Example:</strong> <code>&lt;bx:loop query="#data#" group="department,manager"&gt;</code> |  |
| `groupCaseSensitive` | `boolean` | `false` | Boolean flag controlling whether group comparisons are case-sensitive.<br>                               Defaults to false (case-insensitive). Only meaningful when<br>                               <code>group</code> attribute is specified.<br>                               <br><br>                               <strong>Example:</strong> <code>&lt;bx:loop query="#data#" group="name" groupCaseSensitive="true"&gt;</code> | `false` |
| `startRow` | `integer` | `false` | 1-based starting row number for query loops. Only rows from this<br>                     position onward will be processed. Must be 1 or greater.<br>                     <br><br>                     <strong>Example:</strong> <code>&lt;bx:loop query="#data#" startRow="10" endRow="20"&gt;</code> |  |
| `endRow` | `integer` | `false` | 1-based ending row number for query loops. Processing stops after<br>                   this row. Must be 1 or greater and typically greater than <code>startRow</code>.<br>                   <br><br>                   <strong>Example:</strong> <code>&lt;bx:loop query="#data#" startRow="1" endRow="50"&gt;</code> |  |
| `label` | `string` | `false` | Optional label for the loop, used with break and continue statements<br>                  to control nested loop execution. Allows targeting specific loops<br>                  in complex nested structures.<br>                  <br><br>                  <strong>Example:</strong> <code>&lt;bx:loop label="outerLoop" array="#data#"&gt;...&lt;bx:break label="outerLoop"&gt;</code> |  |
| `times` | `integer` | `false` | Number of iterations to perform. Creates a simple counting loop<br>                  from 1 to the specified number. Can be used with <code>item</code><br>                  or <code>index</code> to access the current iteration number.<br>                  <br><br>                  <strong>Example:</strong> <code>&lt;bx:loop times="5" index="i"&gt;</code> |  |

## Examples

### For Loop (Script Syntax)

General Purpose Loop

<a href="https://try.boxlang.io/?code=eJxLyy%2FSUMhUsFUwtAZSNkDaAMjQ1lbQVKjm4iwvyixJ9S8tKSgtAanStOaq5QIARYkNGA%3D%3D" target="_blank">Run Example</a>

```java
for( i = 1; i <= 10; i++ ) {
	writeOutput( i );
}

```

Result: 12345678910

### Destructuring Loop Syntax (Script)

**New in 1.10.0**: Loop destructuring allows you to get multiple values in a single declaration.

#### Array Destructuring

Get both element and index when looping over arrays:

```java
fruits = [ "apple", "banana", "cherry" ]

// Get both item and index
for( item, index in fruits ) {
    writeOutput( "#index#: #item#<br>" )
}
```

Result:
```
1: apple
2: banana
3: cherry
```

#### Struct Destructuring

Get both key and value when looping over structures:

```java
produce = {
    "grapes": 2,
    "lemons": 1,
    "eggplants": 6
}

// Get both key and value
for( key, value in produce ) {
    writeOutput( "I have #value# #key#<br>" )
}
```

Result:
```
I have 2 grapes
I have 1 lemons
I have 6 eggplants
```

{% hint style="info" %}
**Syntax Note**: The destructuring syntax follows the pattern `for (first, second in collection)` where:
- For **arrays**: `first` = element value, `second` = 1-based index
- For **structs**: `first` = key, `second` = value
{% endhint %}

### For Loop using Bx:loop Tag

General Purpose Loop


```java
<bx:loop index="i" from="1" to="10">
    <bx:output>#i#</bx:output>
</bx:loop>
```

Result: 1 2 3 4 5 6 7 8 9 10

### Loop Over an Array (Script Syntax)

Array Loop

<a href="https://try.boxlang.io/?code=eJxlkMGqwjAQRdfmKy5dSEul2uVTK6goCML7AHER64gBk0hI0SL%2Bu5Pap09cZEImN%2BcM0fXUOVmjwAaiE8mox3XX1DIS25Ho97G0Dmtrz5jVUGZPVxy4M1%2F%2BZINsAGn2ONkLOcHdGIpR%2BYi3cQEZ0GsyMXSrSfgmTZHgJjoXpzz9Vv5c%2BVdgww%2B3nBL3IGZfcK9MK8vTp6OsnCPjV80syrzpX9iP5D9sM9lClsc4gSa9I4dDZUqvbHDlLGqZGYUQYkxNDTqRZlqvOTx%2FIkEx%2BbK2OXQRYcir%2BxfmAUJ5AJJxb5I%3D" target="_blank">Run Example</a>

```java
myArray = [
	"a",
	"b",
	"c"
];
// For Loop By index
for( i = 1; i <= arrayLen( myArray ); i++ ) {
	writeOutput( myArray[ i ] );
}
// By For
for( currentIndex in myArray ) {
	writeOutput( currentIndex );
}
// By arrayEach()
myArray.each( ( Any element, Any index ) => {
	writeOutput( element & " : " & index );
} );

```


### Bx:loop over an Array

Array Loop


```java
<bx:set myArray = [
	"a",
	"b",
	"c"
	] >
 <!--- By index --->
 <bx:loop index="i" from="1" to="#arrayLen( myArray )#">
 <bx:output>#myArray[ i ]#</bx:output>
 </bx:loop>
 <!--- By array --->
 <bx:loop index="currentIndex" item="currentItem" array="#myArray#">
 <bx:output>#currentIndex#</bx:output>

 <bx:output>#currentItem#</bx:output>
 </bx:loop>
```


### Loop over a Struct (Script Syntax)

Struct Loop

<a href="https://try.boxlang.io/?code=eJx1jk0LgkAQhs%2FOrxh2LwqS9%2FwAA7tEddBbdBDbaFHX2HaLRfzv6ZJkhy7DzPC8H63JldSVwhh7BOeQ7jNcIyk6YYgPTl6khX1sm07yS0lgCCEIcGPwYXVw7aSLlZaSCbVjBrnAdvb0sAfnJbliR63uWrlIooYn9IvT0ZvO%2FGnpc6ZRMLIEvRCGn8isrG6uB7NqxaYbXUyFwZoZ3y7PstFsLBAnfzrUn3ALLrOm8QYmylXE" target="_blank">Run Example</a>

```java
myStruct = {
	NAME : "Tony",
	STATE : "Florida"
};
// By struct
for( currentKey in myStruct ) {
	writeOutput( "<li>#currentKey# : #myStruct[ currentKey ]#</li>" );
}
// By structEach()
myStruct.each( ( Any key, Any value ) => {
	writeOutput( "<li>#key# : #value#</li>" );
} );

```


### Bx:loop over a Struct

Loop over a Struct using the collection and item arguments of bx:loop.


```java
<!--- Define our struct --->
 <bx:set myStruct = {
	NAME : "Tony",
	STATE : "Florida"
	} >
 <!--- By struct --->
 <bx:loop item="currentKey" collection="#myStruct#">
 <bx:output><li>#currentKey# : #myStruct[ currentKey ]#</li></bx:output>
 </bx:loop>
```


### Bx:loop over a Struct

Loop over a Struct using the collection, index and item arguments of bx:loop.


```java
<!--- Define our struct --->
<bx:set myStruct = {
	NAME : "Tony",
	STATE : "Florida"
	} >
<!--- By struct --->
<bx:loop item="currentItem" collection="#myStruct#" index="currentKey">

<bx:output><li>#currentKey# : #currentItem#</li></bx:output>
</bx:loop>
```


### Loop over a List (Script Syntax)

List Loop


```java
// Define our list
myList = "a, b, c";
// By array
for( item in listToArray( myList, "," ) ) {
	writeOutput( item );
}
// By listEach()
myList.each( ( Any element, Any index ) => {
	writeOutput( element & " : " & index );
}, "," );

```


### Bx:loop over a List

List Loop


```java
<!--- Define our list --->
 <bx:set myList = "a, b, c" >
 <!--- By list --->
 <bx:loop index="item" list="#myList#">
 <bx:output>#item#</bx:output>
 </bx:loop>
 <!--- By array --->
 <bx:loop index="currentIndex" array="#listToArray( myList, "," )#">
 <bx:output>#currentIndex#</bx:output>
 </bx:loop>
```


### Loop over a Query with Grouping (Script Syntax)

Query Loop use grouping


```java
q = queryNew( "pk,fk,data", "integer,integer,varchar", [
	[
		1,
		10,
		"aa"
	],
	[
		2,
		20,
		"bb"
	],
	[
		3,
		20,
		"cc"
	],
	[
		4,
		30,
		"dd"
	],
	[
		5,
		30,
		"ee"
	],
	[
		6,
		30,
		"ff"
	]
] );
bx:loop query=q group="fk" {
	writeOutput( "<strong>#fk#</strong><br />" );
	bx:loop {
		writeOutput( "&emsp;#pk#:#data#<br />" );
	}
	writeOutput( "<hr>" );
}

```


### Bx:loop over a Query

Query Loop


```java
<!--- Define our query --->
 <bx:set platform = [
	"Adobe ColdFusion",
	"Railo",
	"Boxlang"
	] >
 <bx:set myQuery = queryNew( " " ) >
 <bx:set queryAddColumn( myQuery, "platform", "VARCHAR", platform ) >
 <!--- By row index --->
 <bx:loop index="i" from="1" to="#myQuery.RECORDCOUNT#">
 <bx:output><li>#myQuery[ "platform" ][ i ]#</li></bx:output>
 </bx:loop>
 <!--- By group --->
 <bx:loop query="myQuery" group="platform">
 <bx:output><li>#platform#</li></bx:output>
 </bx:loop>
```


### While Loop (Script Syntax)

Pre-Condition Loop This form of loop evaluates a single condition at the beginning of each iteration, and continues to loop whilst the condition is true


```java
while (condition) {
	// statements

}

```


### Do While Loop (Script Syntax)

Post-Condition Loop This form of loop evaluates a single condition at the beginning of each iteration, and continues to loop whilst the condition is true


```java
do {
	// statements

}
 while (condition);

```
