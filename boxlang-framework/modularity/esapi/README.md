---
description: ESAPI & Antisamy Module
icon: vault
---

# ESAPI

This module provides ESAPI functionality for stronger, more secure applications in BoxLang based on the OWASP ESAPI project: [https://owasp.org/www-project-enterprise-security-api](https://owasp.org/www-project-enterprise-security-api) and OWASP AntiSamy project: [https://owasp.org/www-project-antisamy/](https://owasp.org/www-project-antisamy/)

It includes encoding, decoding, and sanitization functions to help protect your application from common security vulnerabilities. It also includes the AntiSamy library for cleaning up HTML content.

```bash
# For Operating Systems using our Quick Installer.
install-bx-module bx-esapi

# Using CommandBox to install for web servers.
box install bx-esapi
```

Once installed, several built-in-functions and components will be available for use in your BoxLang code.  Here are the built-in-functions (BIFs) that are available in this module. You can also check out the module API documentation for more details: [https://apidocs.ortussolutions.com/boxlang-modules/bx-esapi/1.1.0/ortus/boxlang/modules/esapi/bifs/package-summary.html](https://apidocs.ortussolutions.com/boxlang-modules/bx-esapi/1.1.0/ortus/boxlang/modules/esapi/bifs/package-summary.html)

## Encoding

This module contributes the following ESAPI encoding BIFs:

* `encodeFor( context, value )` - Encode for a specific context: HTML, XML, URL, etc.
* `encodeForCSS( value, [canonicalize=false] )` - Encode for CSS contexts
* `encodeForDN( value, [canonicalize=false] )` - Encode for Distinguished Name contexts
* `encodeForHTML( value, [canonicalize=false] )` - Encode for HTML contexts
* `encodeForHTMLAttribute( value, [canonicalize=false] )` - Encode for HTML attribute contexts
* `encodeForJavaScript( value, [canonicalize=false] )` - Encode for JavaScript contexts
* `encodeForLDAP( value, [canonicalize=false] )` - Encode for LDAP contexts
* `encodeForSQL( string, dialect, [canonicalize=false] )` - Encode for SQL contexts
* `encodeForURL( value, [canonicalize=false])` - Encode for URL contexts
* `encodeForXML( value, [canonicalize=false])` - Encode for XML contexts
* `encodeForXMLAttribute( value, [canonicalize=false] )` - Encode for XML attribute contexts
* `encodeForXPath( value, [canonicalize=false])` - Encode for XPath contexts

The available contexts for encoding are:

* `CSS`
* `DN`
* `HTML`
* `HTMLAttribute`
* `JavaScript`
* `LDAP`
* `SQL`
* `URL`
* `XML`
* `XMLAttribute`
* `XPath`

> Canonicalize: If set to true, canonicalization happens before encoding. If set to false, the given input string will just be encoded. The default value for canonicalize is false.

### **Examples**

```html
<bx:output>
	<h2>#encodeFor( "HTML", book.title )#</h2>
	<a href="#encodeFor( "HTMLAttribute", book.goodreadsURL )#">Read on Goodreads</a>
</bx:output>

<bx:output>
	<script>
		var user = #encodeFor( "JavaScript", user.name )#;
	</script>
</bx:output>

<bx:output>
	<cfquery name="qBooks" datasource="myDSN">
		SELECT * FROM books WHERE title = #encodeFor( "SQL", form.title )#
	</cfquery>
</bx:output>

<bx:output>
	<a href="search?term=#encodeForURL( form.searchTerm, true )#">Search</a>
</bx:output>
```

## Decoding

This module contributes the following ESAPI decoding BIFs:

* `canonicalize( input, restrictMultiple, restrictMixed, [throwOnError=false])` - Canonicalize or decode the input string. Canonicalization is simply the operation of reducing a possibly encoded string down to its simplest form. This is important, as attackers frequently use encoding to change their input in a way that will bypass validation filters.
  * `input` - The input string to canonicalize
  * `restrictMultiple` - If true, multiple encoding is restricted. This argument can be set to true to restrict the input if multiple or nested encoding is detected. If this argument is set to true, and the given input is multiple or nested encoded using one encoding scheme an error will be thrown
  * `restrictMixed` - If true, mixed encoding is restricted. This argument can be set to true to restrict the input if mixed encoding is detected. If this argument is set to true, and the given input is mixed encoded using multiple encoding schemes an error will be thrown
  * `throwOnError` - If true, an error will be thrown if the input is invalid. If this argument is set to true, and the given input is invalid, an error will be thrown. Default is false.
* `decodeFor( type, value )` - Decode for a specific context: HTML, XML, URL, etc.
* `decodeForBase64( string )` - Decodes a Base64 string
* `decodeForHTML( string )` - Decodes an HTML string
* `decodeForJSON( string )` - Decodes a JSON string
* `decodeFromURL( string )` - Decodes a URL-encoded string

### **Examples**

```html
<bx:output>#canonicalize( "&lt;", false, false )#</bx:output>

<bx:output>
	<h2>#canonicalize( book.title, true, true )#</h2>
</bx:output>

<bx:output>
	<script>
		var user = #decodeFor( "JavaScript", user.name )#;
	</script>
</bx:output>

<bx:output>
	<a href="search?term=#decodeFromURL( form.searchTerm )#">Search</a>
</bx:output>
```

## Antisamy + Sanitization

This module contributes these remaining ESAPI BIFs:

* `getSafeHTML( string, [policy='ebay'], [throwOnError=false], [force=false] )` - Sanitize HTML content using the AntiSamy library
  * `string` - The HTML string to sanitize
  * `policy` - The policy to use for sanitization. Can be a string (built-in policy name or file path) or a struct for programmatic configuration. Default is `'ebay'` (most restrictive). Built-in policies: `anythinggoes`, `ebay`, `myspace`, `slashdot`, `tinymce`
  * `throwOnError` - When `true`, throws an exception if HTML violates policy rules. Default is `false` (silently sanitizes)
  * `force` - When `true` and using a struct policy, evicts the cached compiled policy and rebuilds it. Default is `false`. Useful for dynamic policy configuration or testing
* `isSafeHTML( string, [policy='ebay'], [force=false] )` - Validate HTML content using the AntiSamy library
  * `string` - The HTML string to validate
  * `policy` - The policy to use for validation. Can be a string (built-in policy name or file path) or a struct for programmatic configuration. Default is `'ebay'` (most restrictive)
  * `force` - When `true` and using a struct policy, evicts the cached compiled policy and rebuilds it. Default is `false`
* `sanitizeHTML( string, [policy='ALL'] )` - Sanitizes unsafe HTML to protect against XSS attacks
  * `string` - The HTML string to sanitize
  * `policy` - The policy to use for sanitization. Default is `'ALL'` (most restrictive). Available policies: `BLOCKS`, `FORMATTING`, `IMAGES`, `LINKS`, `STYLES`, `TABLES`. Can also pass a `PolicyFactory` object for custom policies

### Struct-Based Policy Configuration

For advanced use cases, `getSafeHTML()` and `isSafeHTML()` support struct-based policy configuration. This allows you to build custom policies programmatically:

```js
// Custom policy configuration struct
policyConfig = {
    basePolicy: "ebay",              // Start from a built-in policy ("ebay", "myspace", etc.) or "none"
    overrideMode: "merge",           // "merge" or "override" - how to apply overrides
    directives: {
        maxInputSize: 200000         // Custom directive overrides
    },
    allowTags: [ "b", "i", "em", "strong" ],
    tagRules: { ... },               // Custom tag rules
    globalAttributes: { ... },       // Attributes valid on all tags
    cssRules: { ... },               // CSS property rules
    allowedEmptyTags: [ "br", "hr" ],
    requireClosingTags: [ "p", "div" ],
    tagsToEncode: [ "script", "style" ]
};

// Use the custom policy
safeHTML = getSafeHTML( userInput, policyConfig );
isValid = isSafeHTML( userInput, policyConfig );

// Force cache eviction if policy changes frequently
safeHTML = getSafeHTML( userInput, policyConfig, false, true );
```

**Policy Caching:** Struct-based policies are automatically cached for performance. The same policy configuration will be recompiled only once and reused. Use `force=true` to bypass the cache and rebuild the policy on each call (useful for dynamic policies or testing).

### **Examples**

```html
<bx:output>
	#sanitizeHTML( book.description )#
</bx:output>

<bx:if isSafeHTML( form.comment )>
	<bx:output>
		#form.comment#
	</bx:output>
<bx:else>
	<bx:output>
		<p>Comment contains unsafe HTML</p>
	</bx:output>
</bx:if>

<bx:output>
	#sanitizeHTML( "<h1>Hello World</h1><script>alert('XSS')</script>" )#
</bx:output>

<bx:script>
	// Built-in policy
	comment = getSafeHTML( form.comment, "myspace" );
	
	// Custom policy file
	comment = getSafeHTML( form.comment, "C:/path/to/policy.xml" );
	
	// Programmatic struct policy
	comment = getSafeHTML( form.comment, {
	    basePolicy: "ebay",
	    directives: { maxInputSize: 100000 }
	} );
	
	// With error throwing
	try {
	    comment = getSafeHTML( form.comment, "ebay", true );
	} catch ( any e ) {
	    writeln( "Policy violation: " & e.message );
	}
	
	// Force rebuild struct policy (disable caching)
	comment = getSafeHTML( form.comment, policyConfig, false, true );
</bx:script>
```

### GitHub Repository and Reporting Issues <a href="#github-repository-and-reporting-issues" id="github-repository-and-reporting-issues"></a>

Visit the [GitHub repository](https://github.com/ortus-boxlang/bx-esapi) for release notes. You can also file a bug report or improvement suggestion via [Jira](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=13359\&components=27020\&issuetype=1).
