---
description: You shall comment ALL your code!
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

```javascript
/**
 * This is my class hint
 *
 * @author Luis Majano
 * @version 1.0.0
 */
class extends="Base" implements="IHello" singleton{

     /**
      * This is the hint for the function
      *
      * @param1 This is the hint for the param
      * @data The incoming data
      *
      * @throws InvalidException - If the exception is invalid
      * 
      * @return A string of data
      */
     function myFunc( string param1, data ){
     }
     
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
