
# Component: `Output`

I capture the generated content from the body statements and save it into a variable

## Component Signature

```
<bx:Output query=[any]
group=[string]
groupCaseSensitive=[boolean]
startRow=[integer]
maxRows=[integer]
encodefor=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `any` | `false` |  |  |
| `group` | `string` | `false` |  |  |
| `groupCaseSensitive` | `boolean` | `false` |  | `false` |
| `startRow` | `integer` | `false` |  |  |
| `maxRows` | `integer` | `false` |  |  |
| `encodefor` | `string` | `false` |  |  |

## Examples

### Simple Tag Example




```java
<bx:output>Some text and a #encodeForHTML( variable )#</bx:output>
```


### Loop over a query

Loops over each row of the query specified and outputs the result.


```java
<bx:output query="news">
    <h2>#encodeForHTML( news.HEADLINE )#</h2>
    <p>#encodeForHTML( news.BYLINE )#</p>
</bx:output>
```


### Loop over a range of rows of a query

Loops over 10 rows of the query specified starting from row 5 and outputs the result.


```java
<bx:output query="news" startrow="5" maxrows="10">
    <h2>#encodeForHTML( news.HEADLINE )#</h2>
    <p>#encodeForHTML( news.BYLINE )#</p>
</bx:output>
```


### Using the encodeFor attribute

By specifying `encodefor="html"` each variable is encoded using the `encodeForHTML` function before it is output.


```java
<bx:output query="news" encodefor="html">
    <h2>#news.HEADLINE#</h2>
    <p>#news.BYLINE#</p>
</bx:output>
```


### Using the group attribute

Creates a dummy query `food`, with columns `name` and `type`. Then outputs the food by grouping by the type.


```java
<bx:set food = queryNew( "name,type", "varchar,varchar", [ 
	{
		NAME : "Apple",
		TYPE : "Fruit"
		},
	{
		NAME : "Orange",
		TYPE : "Fruit"
		},
	{
		NAME : "Chicken",
		TYPE : "Meat"
		}
	] ) >
<bx:output query="food" group="type">
    <h2>#type#</h2>
    <ul>
      <bx:output><li>#name#</li></bx:output>
    </ul>
</bx:output>
```


