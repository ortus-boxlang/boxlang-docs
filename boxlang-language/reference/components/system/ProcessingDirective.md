
# Component: `ProcessingDirective`

This tag does nothing for now.

## Component Signature

```
<bx:ProcessingDirective pageEncoding=[string]
suppressWhiteSpace=[boolean] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `pageEncoding` | `string` | `false` |  |  |
| `suppressWhiteSpace` | `boolean` | `false` |  |  |

## Examples

### Set page encoding and suppress whitespace

Controls page-level processing directives for the enclosed content.

```java
<bx:processingDirective pageEncoding="UTF-8" suppressWhiteSpace="true">
    <h1>Compact Output</h1>
    <p>No extra whitespace.</p>
</bx:processingDirective>

```

### Suppress whitespace only

```java
<bx:processingDirective suppressWhiteSpace="true">
    #trim( output )#
</bx:processingDirective>

```
