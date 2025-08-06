# Header

Specifies a response header for the current page (only useful in cases where the page is being used in a HTTP request).

## Component Signature

```
<bx:Header charset=[string]
name=[string]
statusCode=[number]
value=[string] />
```

## Attributes

| Attribute    | Type     | Required                               | Description                         | Default |
| ------------ | -------- | -------------------------------------- | ----------------------------------- | ------- |
| `charset`    | `string` | `false`                                | Character encoding for header value | `UTF-8` |
| `name`       | `string` | Required if `statusCode` not specified | Name of the header                  |         |
| `statusCode` | `number` | Required if `name` not specified       | HTTP status code                    |         |
| `value`      | `string` |                                        | Value for the header                |         |

## Examples

Script Syntax

```java
bx:header name="Content-Type" value="application/pdf";
```
