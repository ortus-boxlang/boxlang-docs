---
description: You shall comment ALL your code!
---

# Comments

Comments are necessary and essential for any programming language. BoxLang is no different with helping you add code comments in both script and tag syntax.

## Tag Comments

You can use the `<!---` and `--->` Syntax to comment within a BoxLang template (`.bxm`). This is very similar to HTML comments but adding an extra `-` to demarcate it as a BoxLang comment.

```markup
HTML Comment
<!-- I am an HTML Comment -->

BoxLang Comment
<!---  I am a BoxLang Comment --->
```

## Script Comments

If you are within a class or in a `<bx:script>` block you can use an alternate style for comments. You can leverage `//` for single line comments and the following for multi-line comments:

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

// Single line comment
```

## Script "Javadoc" style comments

A multi-line block can affect the metadata of a `class` or `function` if the opening line contains 2 asterisks. Also, for readability, some people will start each line of the comment with an asterisk. BoxLang will parse out those starting asterisks and they will not appear in the class or the function metadata.

```javascript
    /**
     * This is the hint for the function
     *
     * @param1 This is the hint for the param
     */
    function myFunc( string param1 ){
  }
```

## CFCDoc Style Comments

In the BoxLang world, you can write [JavaDoc](http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html) comments in what we call **CFCDoc** comments. We leverage the [DocBox](https://github.com/Ortus-Solutions/DocBox) library to generate documentation according to object metadata and comments. Please check out the [annotating your code ](https://docbox.ortusbooks.com/getting-started/annotating-your-code)section in the DocBox documentation to get a feel for how to document your code: [https://docbox.ortusbooks.com/getting-started/annotating-your-code](https://docbox.ortusbooks.com/getting-started/annotating-your-code)

{% code title="MyAwesome.bx" %}
```java
/**
 * This is my class
 *
 * @author Luis Majano
 */
class extends="Base" implements="IHello" singleton{

    /**
     * The Settings
     */
    property name="settings";


    /**
     * Constructor
     *
     * @wirebox The Injector
     * @wirebox.inject wirebox
     * @vars The vars I need
     * @vars.generic Array
     *
     * @return MyClass
     * @throws SomethingException
     */
    function init( required wirebox, required vars ){
        variables.wirebox = arguments.wirebox;
        return this;
    }


}
```
{% endcode %}

{% embed url="https://docbox.ortusbooks.com/" %}
Read about DocBox
{% endembed %}

You can see some examples of advanced class documentation here: [https://apidocs.ortussolutions.com/coldbox/current/](https://apidocs.ortussolutions.com/coldbox/current/)

{% hint style="success" %}
**Tip**: VSCode has some great plugins for generating this type of documentation on your classes. We recommend the following extensions:

* **Align** - Helps align everything
* **AutoCloseTag** - Helps close comment and well all tags
* **DocumentThis** - Automatically generates detailed JSDoc, CFCDoc comments in TypeScript and JavaScript files.
{% endhint %}
