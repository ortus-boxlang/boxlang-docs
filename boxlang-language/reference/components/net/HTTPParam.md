
# Component: `HTTPParam`

I add an HTTP param to an HTTP call.

## Component Signature

```
<bx:HTTPParam type=[string]
name=[string]
value=[any]
file=[string]
encoded=[boolean]
mimetype =[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `true` | The type of parameter: header, body, xml, cgi, file, url, formfield, cookie |  |
| `name` | `string` | `false` | The name of the parameter (not required for body, xml, or file types) |  |
| `value` | `any` | `false` | The value of the parameter (not required for file type) |  |
| `file` | `string` | `false` | The path to the file (required for file type) |  |
| `encoded` | `boolean` | `false` | Whether the value is URL encoded. Applies to CGI Params and Form Fields (default: false). If passed as false to a URL param, it will bypass the default encoding that occurs. |  |
| `mimetype ` | `string` | `false` |  |  |

## Examples

### Script Syntax



<a href="https://try.boxlang.io/?code=eJwtjEEKwjAQRdfmFMOsdGGzlZbs3CvoBdJ20hYyJqYTo4h3t1JX%2F%2FF5vPZZjyIRmGQMvcHz6XJF6EabZhKDWdz%2BgJCTN%2Fjz5lrrUko1hDB4qrrAGiHRnP0ir4vwVpt2zUabLMPNMhm8I8grLuBCYjeR7xEe1ufl6Rx7bNRHlTQJHTPH7T8Ku0Z9Afh2N4k%3D" target="_blank">Run Example</a>

```java
bx:http method="POST" charset="utf-8" url="https://www.google.com/" result="result" {
	bx:httpparam name="q" type="formfield" value="bx";
}
writeDump( result );

```


### BX:HTTP Tag Syntax




```java
<bx:http result="result" method="POST" charset="utf-8" url="https://www.google.com/">
    <bx:httpparam name="q" type="formfield" value="bx">
</bx:http>
<bx:dump var="#result#">
```


