[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BooleanFormat`

Returns the value formatted as a boolean string

## Method Signature

```
BooleanFormat(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to cast as a boolean and return the string value |  |

## Examples

### 1 is definitely true



<a href="https://try.boxlang.io/?code=eJxLys%2FPSU3Mc8svyk0s0VAwVNC05gIATjEGUQ%3D%3D" target="_blank">Run Example</a>

```java
booleanFormat( 1 );

```

Result: true

### 0 is definitely false



<a href="https://try.boxlang.io/?code=eJxLys%2FPSU3Mc8svyk0s0VAwUNC05gIATiwGUA%3D%3D" target="_blank">Run Example</a>

```java
booleanFormat( 0 );

```

Result: false

### Negative -1 is true as well



<a href="https://try.boxlang.io/?code=eJxLys%2FPSU3Mc8svyk0s0VDQNVTQtOYCAFTRBn4%3D" target="_blank">Run Example</a>

```java
booleanFormat( -1 );

```

Result: true

### And even a number larger then 1 is true



<a href="https://try.boxlang.io/?code=eJxLys%2FPSU3Mc8svyk0s0VAwVdC05gIATkUGVQ%3D%3D" target="_blank">Run Example</a>

```java
booleanFormat( 5 );

```

Result: true

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSXUpzS3QUHDKz89JTcxzyy%2FKTSzRUDA0MlbQVNC0VtDXVwgpKk3lKsep1ACskAuk0i0xpziVCwC7Nho6" target="_blank">Run Example</a>

```java
writeDump( BooleanFormat( 123 ) ); // True
writeDump( BooleanFormat( 0 ) );
 // False

```



## Related

  * [DecimalFormat](./DecimalFormat.md)
  * [LSNumberFormat](./LSNumberFormat.md)
  * [NumberFormat](./NumberFormat.md)
