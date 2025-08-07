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

* `getSafeHTML( string, [policy='ebay'] )` - Sanitize HTML content using the AntiSamy library
  * `string` - The HTML string to sanitize
  * `policy` - The policy to use for sanitization. The default is 'ebay', which is the most restrictive policy. The available policies are: `anythingoes,ebay,myspace,slashdot,tinymce`. However you can pass a custom policy by using an absolute path to the policy file.
* `isSafeHTML( string, [policy='ebay'] )` - Validate HTML content using the AntiSamy library
  * `string` - The HTML string to sanitize
  * `policy` - The policy to use for sanitization. The default is 'ebay', which is the most restrictive policy. The available policies are: `anythingoes,ebay,myspace,slashdot,tinymce`. However you can pass a custom policy by using an absolute path to the policy file.
* `sanitizeHTML( string, [policy='ALL'] )` - Sanitizes unsafe HTML to protect against XSS attacks
  * `string` - The HTML string to sanitize
  * `policy` - The policy to use for sanitization. The default is 'ALL', which is the most restrictive policy. The available policies are: `BLOCKS, FORMATTING, IMAGES, LINKS, STYLES, TABLES`. You can also pass a `PolicyFactory` object to use a custom policy (https://javadoc.io/static/com.googlecode.owasp-java-html-sanitizer/owasp-java-html-sanitizer/20191001.1/org/owasp/html/PolicyFactory.html)

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
	comment = getSafeHTML( form.comment, "myspace" );
	comment = getSafeHTML( form.comment, "C:/path/to/policy.xml" );
</bx:script>
```

### GitHub Repository and Reporting Issues <a href="#github-repository-and-reporting-issues" id="github-repository-and-reporting-issues"></a>

Visit the [GitHub repository](https://github.com/ortus-boxlang/bx-esapi) for release notes. You can also file a bug report or improvement suggestion via [Jira](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=13359\&components=27020\&issuetype=1).
