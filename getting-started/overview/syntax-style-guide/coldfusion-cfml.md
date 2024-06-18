---
description: A quick guide on key differences and issues when migrating from CFML
---

# Migrating From ColdFusion/CFML

{% hint style="danger" %}
Please note that our CFML Compatibility is still in progress. Please keep this page bookmarked as we progress to our stable release.
{% endhint %}

BoxLang is a new language with a dual parser to support the ColdFusion/CFML ecosystem.  It also has a compatibility module (`bx-compat`) that will allow the BoxLang runtime to behave like an Adobe ColdFusion or Lucee Server.  We also recommend you read the [Quick Syntax Style Guide](./) to give you an understanding of all the new features of BoxLang.

### File Types

BoxLang can parse and run all of the traditional ColdFusion/CFML file types

* `.cfc` - Components
* `.cfs` - Scripts
* `.cfm` - Templates

### Components are Classes

ColdFusion Components (CFCs) are now called BoxLang classes, like any other language. You can also use the `class` declaration for them.  You can continue to write components if you like, but if you use our `.bx` extensions, they are now classes.

```java
class{
    
    property name=¨firstName¨

}
```

### Tags are Components

Since BoxLang is not a tag-based language but a dynamic language offering a templating language. There are no concepts of tags but of BoxLang components that can be accessed via our templating language or script.  In CFML the templating language uses a `<cf` prefix, in BoxLang we use a `<bx:` prefix.

```xml
<bx:if expression>

<bx:else>

</bx:if>
```

### Default assignment scope

In CFML, the default assignment scope is always `variables`, but in BL it can differ based on the context. For Functions, it will be `local`. The BoxLang runtime will toggle this behavior based on the type of the compiled source code. So for `.cfm` or `.cfc` source files, the default assignment scope in functions will remain `variables` but for code compiled from `.bx`, `.bxs` or `.bxm` files, the default assignment scope in functions will be `local`.

### CastAs operator

BoxLang has a new `castAs` binary operator that you can use instead of the `javaCast()` bif.

```jsx
expression castAs "type"
```

No transpilation changes are needed since this is a BL-only feature.

### Multiple catch types

BoxLang supports

```jsx
catch( foo.com | brad | com.luis.majano e ) {}
```

No transpilation changes are needed since this is a BL-only feature.

### Annotations

BoxLang will allow for proper annotations before UDF declarations, properties, and classes. The annotation's value can be a string, struct literal, or array literal. You can also use multi-spaced or indentation.

```jsx
@foo
@bar "value"
@output true
function myFunc() {
}
```

No transpilation changes are needed since this is a BL-only feature.

### Documentation Comments (Javadoc style)

BL will support documentation comments like CF, but will NOT allow them to actually influence the function’s behavior. When transpiling CFML to BL, any annotations set in a doc comment modifying the function or any arguments need to be moved to proper annotations in BL.

So the CFML

```jsx
/**
* My function hint
*
* @output false
* @brad wood
*
* @myService my hint here for the arg
* @myService.inject 
*/
function foo( required any myService ) {}
```

would turn into this BoxLang

```jsx
/**
* My function hint
* 
* @myService my hint here for the arg
*/
@output false
@brad wood
@myService.inject 
function foo( required any myService ) {}
```

### Function output defaults to false

The `output` of functions will be false in BL. The BoxLang runtime will toggle this behavior based on the type of the compiled source code. So for `.cfm` or `.cfc` source files, default value of the `output` annotation on classes and functions will remain `true` but for code compiled from `.bx`, `.bxs` or `.bxm` files, the default value of the `output` annotation on classes and functions will be `false`.

Note, if your `Application.cfc` and `onRequestStart()` method do not specify

```html
@output true
```

you will get a blank page with no output!

### Import keyword

CFML has the cfimport tag, but there doesn’t seem to be any special script version of it, ours looks like this:

```jsx
import taglib="/relative/path/customTags" prefix="tags";
```

```jsx
import package.Class as alias;
```

### Import Aliases

You can also import classes from any resolver and attach an alias to remove any ambiguity.

```julia
import java:org.apache.User as jUser;
import models.User;

var oUser = new jUser()
var testUser = new User()
```

### Object Resolvers

Any `import` or `new` can be prefixed with an object resolvers prefix. A resolver adheres to our resolver interface to provide access into any type of object or filesystem. By default we ship with two resolvers:

1. `java` : Java classes
2. `bx` : BoxLang classes

This allows you to import or easily create classes from any source.

```julia
// Default resolver is bx : boxlang
import models.User;
// Same as
import bx:models.User;

// Java resolver
import java:java.util.ConcurrentHashMap;

// Custom Resolver
import cborm:entity
```

This will allow us to modularly provide object resolvers for any type of integrations. You will also be able to use the resolvers for `extends` and `implements`

```julia
class implements="java:java.util.List" {

}

class extends="java:ortus.boxlang.runtime.types.Struct"{

}
```

## Auto-casting argument and return value types

In CF an argument or return value of Numeric will allow a String through untouched so long as that string can be cast to a number. In BoxLang, we are actively casting the value to a “real” number. In theory, this is seamless, but could affect if you are checking the underlying Java type or passing to a Java method. There is no transpilation that can undo this, unless we add some setting or runtime configuration to disable the “feature”.

### GetCurrentTemplatePath() and relative includes

Both Adobe and Lucee do not agree with each other and are inconsistent even within themselves regarding

* The return value of the `getCurrentTemplatePath()` BIF
* The lookup of relative templates being included
* The lookup of relative CFC paths for object instantiation

Here is some documentation on their differences:

* Given a method that's originally part of a CFC
  * getCurrentTemplatePath() returns the original CFC (**Adobe** and **Lucee** agree here)
  * `new RelativeCFC()` find CFCs in the same folder as the original CFC (**Adobe** and **Lucee** agree here)
  * `include "relativePath.cfm";` find CFCs in the same folder as the original CFC (**Adobe** and **Lucee** agree here)
* Given a UDF defined in a file in a different directory that's injected into another CFC
  * getCurrentTemplatePath()
    * returns the original birthplace of the UDF source in **Lucee**
    * returns the new CFC the UDF was injected into in **Adobe**
  * Relative CFC path resolution
    * finds the CFC relative to the original birthplace of the UDF source in **Lucee**
    * finds the CFC relative to the NEW CFC's path in **Adobe**
  * Relative cfinclude path resolution
    * finds the CFC relative to the original birthplace of the UDF source in **Lucee**
    * finds the CFC relative to the original birthplace of the UDF source in **Adobe**
* Given a UDF defined in a file in a different directory that's passed into a UDF in another CFC for invocation
  * getCurrentTemplatePath()
    * returns the new CFC the UDF was injected into in **Lucee**
    * returns the new CFC the UDF was injected into in **Adobe**
  * Relative CFC path resolution
    * finds the CFC relative to the original birthplace of the UDF source in **Lucee**
    * finds the CFC relative to the NEW CFC's path in **Adobe**
  * Relative cfinclude path resolution
    * finds the CFC relative to the original birthplace of the UDF source in **Lucee**
    * finds the CFC relative to the original birthplace of the UDF source in **Adobe**

In BoxLang, this is being simplified and made consistent across the board. In ALL cases the “current template path” and relative lookup directory will tie to the original source path on disk of the file that contains the currently executing code. So, whether it’s an include, a UDF, an injected UDF from another location, or a closure defined elsewhere - whatever original source file for the code in question is what determines the “current template path” and relative lookups.

## BIF Renaming

Some bifs have been renamed in BoxLang.

| CFML                 | BoxLang          |
| -------------------- | ---------------- |
| serializeJSON        | jsonSerialize    |
| deserializeJSON      | jsonDeserialize  |
| chr                  | char             |
| asc                  | ascii            |
| getComponentMetadata | getClassMetadata |

## CreateObject Types

The `component` type for create object becomes `class` in BoxLang

```
createObject( ¨class¨, path )
```

## JDBC Queries

### Parameter SQL Types

Both Adobe ColdFusion and Lucee Server utilize a `cfsqltype` key on query parameters to denote the type of the value being used in a prepared statement or query:

```js
queryExecute(
  "select quantity, item from cupboard where item_id = :itemID"
  { itemID : { value : arguments.itemID, cfsqltype : "cf_sql_numeric" } }
);
```

In BoxLang, you'll need to replace `cfsqltype` with just `sqltype`. In addition, we'd prefer to see all usage of the `cf_sql_`/`CF_SQL` prefixes stripped:

```js
queryExecute(
  "select quantity, item from cupboard where item_id = :itemID"
  { itemID : { value : arguments.itemID, sqltype : "numeric" } }
);
```

Here's a full breakdown of the various syntaxes:

* `sqltype:"numeric"` - The preferred syntax.
* `cfsqltype:"cf_sql_numeric"` - will throw an error in BoxLang core. In CFML syntax files, is transpiled to `sqltype:"cf_sql_numeric"`.
* `sqltype:"cf_sql_numeric"` - is silently treated as `sqltype:"numeric"`.

### BlockFactor Query Option

The `blockfactor` query option in Adobe CF and Lucee Server is used to set a custom batch size when selecting large numbers of rows:

```js
queryExecute( "Select * FROM myBigTable", {}, { blockfactor : 100 } ); 
```

In BoxLang, this is renamed to `fetchSize`:

```js
queryExecute( "Select * FROM myBigTable", {}, { fetchSize : 100 } ); 
```

You can use the `blockfactor` nomenclature by installing the `bx-compat` module.
