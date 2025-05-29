
# Component: `SaveContent`

I capture the generated content from the body statements and save it into a variable

## Component Signature

```
<bx:SaveContent variable=[string]
trim=[boolean]
append=[boolean] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `variable` | `string` | `true` |  |  |
| `trim` | `boolean` | `false` |  | `false` |
| `append` | `boolean` | `false` |  | `false` |

## Examples

### Script Syntax



<a href="https://try.boxlang.io/?code=eJxLqrAqTixLTc7PK0nNK1EoSyzKTEzKSbVVyq10hogpKVRzcZYXZZak%2BpeWFJSWaCgoBefnwnToKSloWnPVcgEA0RIZLw%3D%3D" target="_blank">Run Example</a>

```java
bx:savecontent variable="myContent" {
	writeOutput( "Somecontent." );
}

```


### Tag Syntax




```java
<bx:savecontent variable="myContent">
<bx:output>Some content.</bx:output>
</bx:savecontent>
```


