---
description: Native Markdown Support for BoxLang
icon: file-code
---

# Markdown

Welcome to the BoxLang Markdown module. This provides native support for Markdown in BoxLang based on the popular Flexmark library.

```
# For Operating Systems using our Quick Installer.
install-bx-module bx-markdown

# Using CommandBox to install for web servers.
box install bx-markdown
```

### Built In Functions (BIFs)

The following BIFs are available for use in your BoxLang code:

* `markdown()`
* `HtmlToMarkdown()`

#### `markdown()`

Converts markdown markup to HTML.

```js
markdown( txt )
```

**Arguments:**

* `txt` - The markdown text to convert to HTML

**Returns:**

The HTML equivalent string of the markup.

**Example:**

```js
markdown( "# Hello World" )
```

**Output:**

```html
<h1>Hello World</h1>
```

#### `HtmlToMarkdown()`

Converts HTML markup to markdown.

```js
HtmlToMarkdown( markup )
```

**Arguments:**

* `markup` - The HTML string to convert.

**Returns:**

* The markdown equivalent string of the markup.

**Example:**

```js
HtmlToMarkdown( "<h1>Hello World</h1>" )
```

**Output:**

```markdown
# Hello World
```

### Components

This module also provides a `bx:markdown` component that can be used to convert markdown to HTML in a wrapping approach. You can use it in script or in the templating language. The following attributes are available:

* `variable` - The variable to store the output in. If not set, the output will be written to the response.

Example with variable:

```js
// The content of the component will be parsed and stored in the variable: data.
bx:markdown variable="data"{
	writeOutput( "## Hola" )
}
```

Example with no variable, outputs to the response:

```js
bx:markdown{
	writeOutput( "## Hola" )
}
```

Example in the templating language using a variable:

```html
<bx:markdown variable="html">
	## Hola Mundo

	My beautiful markdown text
</bx:markdown>
<bx:output>#html#</bx:output>
```

Example in the templating language with no variable:

```html
<bx:markdown>
	## Hola mundo

	This is a markdown test
</bx:markdown>
```

### Settings

A subset of the flexmark options are supported. These can be configured in your `boxlang.json` in the `modules` section:

```js
"modules" : {

	"cbmarkdown" : {
		"enabled" : true,
		"settings" : {
			// Looks for www or emails and converts them to links
			"autoLinkUrls"                  : true,
			// Creates anchor links for headings
			"anchorLinks"                   : true,
			// Set the anchor id
			"anchorSetId"                   : true,
			// Set the anchor id but also the name
			"achorSetName"                  : true,
			// Do we create the anchor for the full header or just before it. True is wrap, false is just create anchor tag
			"anchorWrapText"                : false,
			// The class(es) to apply to the anchor
			"anchorClass"                   : "anchor",
			// raw html prefix. Added before heading text, wrapped or unwrapped
			"anchorPrefix"                  : "",
			// raw html suffix. Added before heading text, wrapped or unwrapped
			"anchorSuffix"                  : "",
			// Enable youtube embedded link transformer
			"enableYouTubeTransformer"      : false,
			// default null, custom inline code open HTML
			"codeStyleHTMLOpen"             : "<code>",
			// default null, custom inline code close HTML
			"codeStyleHTMLClose"            : "</code>",
			// default "language-", prefix used for generating the <code> class for a fenced code block, only used if info is not empty and language is not defined in
			"fencedCodeLanguageClassPrefix" : "language-",
			// Table options
			"tableOptions"                  : {
				// Treat consecutive pipes at the end of a column as defining spanning column.
				"columnSpans"                 : true,
				// Whether table body columns should be at least the number or header columns.
				"appendMissingColumns"        : true,
				// Whether to discard body columns that are beyond what is defined in the header
				"discardExtraColumns"         : true,
				// Class name to use on tables
				"className"                   : "table",
				// When true only tables whose header lines contain the same number of columns as the separator line will be recognized
				"headerSeparationColumnMatch" : true
			}
		}
	}
	// end markdown config

};
```
