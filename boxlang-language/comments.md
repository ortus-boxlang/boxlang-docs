---
description: You shall comment ALL your code!
icon: comment
---

# Comments

Comments are necessary for any programming language. BoxLang is no different in helping you add code comments in both script and tag syntax.  The syntax is the same if you are a Java/Kotlin developer.

## Tag Comments

You can use the `<!---` and `--->` Syntax to comment within a BoxLang template (`.bxm`). This is similar to HTML comments but adds an extra `-` to demarcate it as a BoxLang comment.

```markup
HTML Comment
<!-- I am an HTML Comment -->

BoxLang Comment
<!---  I am a BoxLang Comment --->
```

### Nested Tag Comments

BoxLang supports **nested tag comments**, which is useful when you need to comment out a block of code that already contains comments. The parser tracks the nesting depth and only closes the outer comment when all nested levels are properly terminated.

```markup
<!---
    This is an outer comment
    <bx:set fruit = "apple">

    <!--- This is a nested comment inside --->

    <bx:output>#fruit#</bx:output>
--->
```

This feature is particularly helpful during development when you want to temporarily disable a section of code without removing existing comments.

{% hint style="info" %}
**Note**: Script-style comments (`/* */` and `//`) follow standard Java/C conventions and do **not** support nesting. Attempting to nest `/* */` comments will result in the first `*/` closing the comment block.
{% endhint %}

## Script Comments

If you are within a class, scripting or in a `<bx:script>` block, you can use an alternate style for comments. You can leverage `//` for single-line comments and the following for multi-line comments:

```java
/**
 * Multi-line Javadoc style comment
 *
 * @COLDBOX_CONFIG_FILE The override location of the config file
 * @COLDBOX_APP_ROOT_PATH The location of the app on disk
 * @COLDBOX_APP_KEY The key used in application scope for this application
 * @COLDBOX_APP_MAPPING The application mapping override, only used for Flex/SOAP apps, this is auto-calculated
 * @COLDBOX_FAIL_FAST By default if an app is reiniting and a request hits it, we will fail fast with a message. This can be a boolean indicator or a closure.
 */


/*
  Multi
  Line
  Comments
  are
  great!
*/

// Single-line comment
```

## BxDoc: "Javadoc" style comments

A multi-line block can affect the metadata of a `class` or `function` if the opening line contains 2 asterisks. Also, for readability, some people will start each line of the comment with an asterisk. BoxLang will parse out those starting asterisks, but they will not appear in the class or the function metadata.

You can use all the JavaDoc style comments; however, when doing parameters, we omit the verbosity of the `@param {name} hint` and use the `@{name} hint`.

### Documentation Metadata vs Standalone Annotations

It's important to understand the difference between **documentation annotations** (using `@` inside BxDoc comments) and **standalone annotations** (using `@` before declarations):

- **Documentation annotations** (`@something` inside `/** */` comments) become part of the `documentation` metadata struct
- **Standalone annotations** (`@something` before a class/function/property) become direct metadata properties

**Documentation Annotations Example:**

```js
/**
 * This is a function comment
 *
 * @see Luis Majano
 * @version 1.0.0
 * @another { name: 123, age: 123 }
 */
function test() {
}
```

When you call `getMetadata( test )`, the documentation annotations are available in the `documentation` struct:

```js
{
  documentation : {
    hint : "This is a function comment",
    see : "Luis Majano",
    version : "1.0.0",
    another : "{ name: 123, age: 123 }"
  }
}
```

**Standalone Annotations Example:**

```js
@cached
@timeout( 60 )
function getData() {
}
```

These become direct annotations struct in the metadata:

```js
{
    annotations : {
        cached : true,
        timeout : 60
    }
}
```

{% hint style="warning" %}
**CRITICAL DISTINCTION**: Documentation annotations (`@something` inside `/** */` comments) are **for documentation purposes only** and do NOT affect runtime behavior. They exist purely to provide metadata for documentation generators and human readers.

If you need an annotation that **alters code runtime behavior** (such as dependency injection, caching, validation, security, etc.), you MUST use **standalone annotations** (`@something` before the class/function/property declaration).
{% endhint %}

{% hint style="info" %}
**Best Practice**: Use documentation annotations (`@see`, `@version`, `@author`, `@return`, etc.) for human-readable documentation that tools like DocBox can process. Use standalone annotations for framework-level metadata that affects runtime behavior (dependency injection, caching, validation, etc.).
{% endhint %}

### Flexible Annotation Syntax

BoxLang's documentation metadata system is **open and flexible**. You can use any `@name` annotation inside BxDoc comments - there are no reserved keywords or restrictions. This allows you to create custom documentation annotations tailored to your application or framework needs.

{% hint style="danger" %}
**Important**: Documentation annotations inside BxDoc comments (`/** @annotation */`) are **metadata only** and do NOT change runtime behavior. They are stored in the `documentation` metadata struct for documentation tools to read.

If you want an annotation that **changes how your code executes** (like `@inject`, `@cached`, `@transactional`), you must use **first-class standalone annotations** placed before the class, property, or function declaration.
{% endhint %}

**Common Documentation Annotations:**

```js
/**
 * User authentication service
 *
 * @author Luis Majano
 * @version 2.1.0
 * @since 1.0.0
 * @see UserRepository
 * @deprecated Use AuthenticationService instead
 * @throws AuthenticationException When credentials are invalid
 * @return User object on successful authentication
 */
function authenticateUser( string username, string password ) {
}
```

**Custom Documentation Annotations:**

You can create your own annotations for any purpose:

```js
/**
 * Process customer order
 *
 * @apiEndpoint POST /api/orders
 * @rateLimit 100 requests per minute
 * @cacheStrategy redis
 * @monitoring enable
 * @team payments-team
 * @jiraTicket PROJ-1234
 */
function processOrder( struct orderData ) {
}
```

All `@name` annotations become entries in the `documentation` metadata struct, accessible via `getMetadata()`:

```js
{
  documentation : {
    hint : "Process customer order",
    apiEndpoint : "POST /api/orders",
    rateLimit : "100 requests per minute",
    cacheStrategy : "redis",
    monitoring : "enable",
    team : "payments-team",
    jiraTicket : "PROJ-1234"
  }
}
```

**Simplified Parameter Documentation:**

Unlike traditional JavaDoc's verbose `@param name description` syntax, BoxLang uses a simplified approach where you can directly use `@parameterName` followed by the description:

```js
/**
 * Calculate user discount
 *
 * @userId The unique identifier for the user
 * @purchaseAmount Total purchase amount before discount
 * @couponCode Optional promotional code
 * @return The final discounted amount
 */
function calculateDiscount( required numeric userId, required numeric purchaseAmount, string couponCode ) {
}
```

### DocBox

We have a tool call [DocBox](https://github.com/Ortus-Solutions/DocBox) that can generate the documentation off your BoxLang classes, much like JavaDoc.

Please check out the [annotating your code ](https://docbox.ortusbooks.com/getting-started/annotating-your-code)section in the DocBox documentation to get a feel for how to document your code: [https://docbox.ortusbooks.com/getting-started/annotating-your-code](https://docbox.ortusbooks.com/getting-started/annotating-your-code)

{% embed url="https://docbox.ortusbooks.com/" %}
Read about DocBox
{% endembed %}

{% hint style="success" %}
**Tip**: VSCode has some great plugins for generating this type of documentation in your classes. We recommend the following extensions:

* **Align** - Helps align everything
* **AutoCloseTag** - Helps close comments as well all tags
* **DocumentThis** - Automatically generates detailed JSDoc BoxLangDocs comments in TypeScript and JavaScript files.
{% endhint %}
