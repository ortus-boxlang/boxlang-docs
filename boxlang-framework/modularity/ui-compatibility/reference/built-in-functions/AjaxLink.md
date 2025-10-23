
# Function: `AjaxLink`

Generates a URL that causes link results to display within the current AJAX container rather than replacing the current page content.

## Method Signature

```
AjaxLink(url)
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `url` | `string` | `true` | The URL to load when the link is clicked |  |

## Examples

```boxlang
// Generate an AJAX link
ajaxUrl = AjaxLink("/api/data");
// Returns: "javascript:void(BoxLangAjax && BoxLangAjax.utils ? BoxLangAjax.utils.handleAjaxLink('/api/data', event) : console.error('BoxLang AJAX not initialized'))"

// Use in an HTML anchor tag
writeOutput('<a href="#ajaxUrl#">Load Data</a>');
```

## Related

* [AjaxOnLoad](./AjaxOnLoad.md)
* [QueryConvertForGrid](./QueryConvertForGrid.md)
