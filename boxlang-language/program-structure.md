---
description: This section covers the basics of the program structures of BoxLang
---

# Program Structure

## File Types

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

BoxLang can be written in 3 types of files:

1. Scripts (\*.bxs, or in compat mode \*.cfs)
2. Templates (\*.bxm, or in compat mode \*.cfm)
3. Classes (\*.bx or in compat mode \*.cfc)

Each of these files follow the same program structure with different syntaxes.  The only one of these that you will write using our templating language is the `templates (*.bxm)`.

## Scripts/Templates

Scripts and templates in BoxLang do not require a class definition and can be executed via the CLI binary directly: `boxlang {script|template|` or ran by the MiniServer/CommandBox/Servlet/Etc.

Templates will use the templating language but can also use scripts via opening and closing `<bx:script></bx:script>` tags.

Scripts are in script notation, but you can also use the templating language by using opening and closing tag island notations: ` ``` `

````java
println( "I am a script" )

```
<!--- Now I can do templating --->
<bx:output>
    <h1>hello</h1>
</bx:output>
```

// Now I am back in scripts
println( "scripts again" )
````

## Classes

Classes have a `.bx` extension and can be executed via the CLI if they have a `main()` method by convention.  Unlike Java or other languages, the `main()` method does NOT have to be static, it can be an instance method or a static method, you chose.

```java
class{

    function main( args = [] ){
        println( "BoxLang Rulez!" )
    }

}
```

## Package Names

Package names are not necessary for these types of files as BoxLang will automatically create them for you.  You will refer to these scripts or templates by path location or via mappings.

## Path Imports

BoxLang allows you to access any BoxLang class or script/template by location convention first with no need of imports explicitly.  The following approaches can be used via path imports:

* `new class_path()`
* `createObject( "class", path )`
* `include template="path"`
* `Any BIF that requires a path`

{% hint style="info" %}
The discovery is done by looking at your global, application mappings and then relative pathing.
{% endhint %}

```
script.bxs
  + models
    + User.bx
  + scripts
    + data.bxs
```

Then we can do so my location reference:

{% code title="script.bxs" %}
```javascript
// Create a new user
user = new models.User( "luis", "majano" )
println( user.getFullName() )

// Now I need to include another script here
include template="scripts/data/bxs"
```
{% endcode %}

These work great but the caveat is that when searching for those files and templates, BoxLang will try to discover them:

* Is there a location mapping (globally or in the application)
* does the file exist
* use it

Works great, but yes, some lookup is done, but cached.

## Simple Imports

Another approach in BoxLang is to use the `import` statement or the `<bx:import>` template statement if you are in templates.  This allows you to fully define the location of a class or template explicitly.  This is also used not only for BoxLang classes but for any Java class:

```java
import java.math.BigInteger
import models.User
import ortus.boxlang.runtime.scopes.Key

a = BigInteger.valueOf( 54 )
result = a.add( 444 )

user = new User()

caseInsensitiveKey = new Key( "luis" )
```

From the example above I made no distinction on what was a Java class or what was a Boxlang class.  By convention BoxLang will auto-discover the class for you according to it's package path.  However, you can also use object resolver notation to disambiguiate the location and define it explicitly.&#x20;

{% hint style="info" %}
The implicit resolver is `bx` meaning a Boxlang class.  You don't need to use it if you don't want to.
{% endhint %}

### Object Resolver Imports

BoxLang ships with two object resolver prefixes:

* `java:` - To demarcate a Java class path
* `bx:` - To demarcate a BoxLang class path

This is useful to disambiguiate paths and make them explicit.  You can use it in the import or in the `new() or createObject()` syntax.

```java
import java:java.math.BigInteger
import java:ortus.boxlang.runtime.scopes.Key

import models.User


a = BigInteger.valueOf( 54 )
result = a.add( 444 )

user = new User()

caseInsensitiveKey = new java:Key( "luis" )
```

### Location of Imports

In box templates and scripts you can add the `import/<bx:import>` statements ANYWHERE in the file.  We will collect them internally for you.

```java
import java:java.math.BigInteger
a = BigInteger.valueOf( 54 )
result = a.add( 444 )

import models.User
user = new User()

import java:ortus.boxlang.runtime.scopes.Key
caseInsensitiveKey = new java:Key( "luis" )
```

## Star Imports

Boxlang, like Java, allows you to import all classes from a package using the `*` after the last package path.  All classes within that package/folder will be available for shorthand usage and reserved.

```java
 // Without star imports
 import java.util.ArrayList
 import java.util.HashMap
 
 myList = new ArrayList()
 myList.add( "apple" )
 myList.add( "pear" )
 
 myJavaMap = new HashMap()
 myJavaMap.put( "name", "boxlang" )
```

Now let's use start imports

```java
 // Without star imports
 import java.util.*
 
 myList = new ArrayList()
 myList.add( "apple" )
 myList.add( "pear" )
 
 myJavaMap = new HashMap()
 myJavaMap.put( "name", "boxlang" )
```

This can be for both Java and BoxLang class paths.

## Import Aliases

BoxLang allows you to alias your imports in order to break ambiguity and to be able to import classes with the same name but with different aliases.

```java
import java.math.BigInteger as jBigInt
import models.User as BXUser
import models.util.Key
import ortus.boxlang.runtime.scopes.Key as jKey

a = jBigInt.valueOf( 54 )
result = a.add( 444 )

user = new BXUser()

caseInsensitiveKey = new Key( "luis" )
javaKey = new jKey( "java" )
```

Here is another example:

```java
import java.util.Date
import java.sql.Date as SQLDate

d1 = new Date( 1000 )
d2 = new SQLDate( 1000 )

assert d1 instanceof "java.util.Date"
assert d2 instanceof "java.sql.Date"
```
