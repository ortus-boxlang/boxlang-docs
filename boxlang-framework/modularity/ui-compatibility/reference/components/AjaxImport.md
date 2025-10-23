# Component: `AjaxImport`

Imports JavaScript and CSS files required for BoxLang AJAX tags and features.

## Syntax

```boxlang
<bx:ajaximport 
    tags="string"
    cssSrc="string" 
    scriptSrc="string"
    params="string" />
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `tags` | `string` | No | Comma-delimited list of BoxLang AJAX tags for which to import supporting files | `""` |
| `cssSrc` | `string` | No | URL of the directory containing CSS files for BoxLang AJAX features | `"/bxmodules/bxUICompat/public/index.bxm?target=css"` |
| `scriptSrc` | `string` | No | URL of the directory containing JavaScript files for BoxLang AJAX features | `"/bxmodules/bxUICompat/public/index.bxm?target=js"` |
| `params` | `string` | No | Parameters to pass, such as API keys (e.g., googlemapkey) | `""` |

## Examples

### Import files for specific tags

```boxlang
<bx:ajaximport tags="div,layout,grid" />
```

### Custom source directories

```boxlang
<bx:ajaximport cssSrc="/custom/css" scriptSrc="/custom/js" />
```

### Import all common AJAX files

```boxlang
<bx:ajaximport />
```

## Usage Notes

- This component should be placed in the `<head>` section of your HTML document
- If no `tags` attribute is specified, all common AJAX CSS and JavaScript files are imported
- The component generates `<link>` tags for CSS files and `<script>` tags for JavaScript files
- Also generates initialization JavaScript for the BoxLang AJAX framework

## Related Components

- [Div](Div.md) - Dynamic div element that may require AJAX imports
- [Grid](Grid.md) - Data grid that requires AJAX functionality
- [Layout](Layout.md) - Layout containers that use AJAX features
