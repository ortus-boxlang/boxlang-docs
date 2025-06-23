[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `XMLFormat`

Formats a string so that special XML characters can be used as text in XML

## Method Signature

```
XMLFormat(string=[string], escapeChars=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The string to format |  |
| `escapeChars` | `boolean` | `false` | whether to escape additional characters restricted as per XML standards. For details, see<br>                       http://www.w3.org/TR/2006/REC-xml11-20060816/#NT-RestrictedChar. | `false` |

## Examples

### Basic xmlFormat() usage

In this example we demonstrate passing the invalid characters < and & into the xmlFormat() function to make them XML safe.

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQqMjNccsvyk0EMpVs8vJTUu3c8%2FNTFNQScwusFbxKM5MrbfTBwkoKmgqa1lwAp5cT%2FQ%3D%3D" target="_blank">Run Example</a>

```java
writeOutput( xmlFormat( "<node>Good &amp; Juicy</node>" ) );

```

Result: &lt;node&gt;Good &amp;amp; Juicy&lt;/node&gt;

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrLinKzEtXsFVQ8lTIycxOVShITcwrLVFIKi0pSS1SUFPISs3JqdRTsuZKKc0t0FCIyM1xyy%2FKTSzRUCiGaNVU0LTmUtDXV8BuQGJugTXUEC4AsI0jVw%3D%3D" target="_blank">Run Example</a>

```java
string = "I like peanut butter & jelly.";
dump( XmlFormat( string ) );
 // I like peanut butter &amp; jelly.

```



## Related

  * [XMLChildPos](./XMLChildPos.md)
  * [XMLElemNew](./XMLElemNew.md)
  * [XMLGetNodeType](./XMLGetNodeType.md)
  * [XMLNew](./XMLNew.md)
  * [XMLParse](./XMLParse.md)
  * [XMLSearch](./XMLSearch.md)
  * [XMLTransform](./XMLTransform.md)
  * [XMLValidate](./XMLValidate.md)
