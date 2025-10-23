
# Function: `AjaxOnLoad`

Specifies a JavaScript function to run when a page loads in the browser.

## Method Signature

```
AjaxOnLoad(functionName)
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `functionName` | `string` | `true` | The name of the JavaScript function to execute on page load |  |

## Examples

```boxlang
// Register a JavaScript function to run on page load
AjaxOnLoad("initializeApp");

// Define the JavaScript function somewhere in your page
writeOutput('<script>
function initializeApp() {
    console.log("Page loaded and ready!");
    // Your initialization code here
}
</script>');
```

## Related

* [AjaxLink](./AjaxLink.md)
* [QueryConvertForGrid](./QueryConvertForGrid.md)
