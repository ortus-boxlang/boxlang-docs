# Location

Relocates to a different pages.

## Method Signature

```
Location(URL=[string], addToken=[boolean], statusCode=[integer])
```

### Arguments

| Argument     | Type      | Required | Description                       | Default |
| ------------ | --------- | -------- | --------------------------------- | ------- |
| `URL`        | `string`  | `true`   | The URL of web page to open.      |         |
| `addToken`   | `boolean` | `false`  | clientManagement must be enabled. |         |
| `statusCode` | `integer` | `false`  | The HTTP status code.             |         |

```
                  Values:
                  - 300
                  - 301
                  - 302
                  - 303
                  - 304
                  - 305
                  - 306
                  - 307 | 302|
```

\|----------|------|----------|-------------|---------|

## Examples

```
Location(URL=[string], addToken=[boolean], statusCode=[integer])
```

## Related

* [GetHTTPRequestData](gethttprequestdata.md)
* [GetPageContext](getpagecontext.md)
