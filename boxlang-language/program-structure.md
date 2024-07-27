---
description: This section covers the basics of the program structures of BoxLang
---

# Program Structure

As we saw in the [syntax](syntax.md) section, BoxLang can be written in 3 types of files:

1. Scripts (\*.bxs, or in compat mode \*.cfs)
2. Templates (\*.bxm, or in compat mode \*.cfm)
3. Classes (\*.bx or in compat mode \*.cfc)

Each of these files follow the same program structure with different syntaxes.

## Package Names

Package names are not necessary for these types of files as BoxLang will automatically create them for you.  You will refer to these scripts or templates by path location.

## Path Imports

BoxLang allows you to access any BoxLang class or script/template by location convention first with no need of imports explicitly.  The following approaches can be used via path imports:

* `new class_path()`
* `createObject( "class", path )`
* `include template="path"`
* `Any BIF that requires a path`

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

* Is there a location mapping
* does the file exist
* use it

Works great, but yes, some lookup is done, but cached.

## Simple Imports

Another approach in BoxLang is to use the `import` statement or the `<bx:import>` template statement if you are in templates.  This allows you to fully define the location of a class or template.  This is also used not only for BoxLang classes but for any Java class:

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

### Star Imports

Boxlang, like Java, allows you to import all classes from a package using the `*` after the last package path.  All classes within that package/folder will be available for shorthand usage.

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

