# ColdFusion/CFML

When comparing BoxLang to CFML, here are some of the differences between them.

### Components are Classes

ColdFusion Components (CFCs) are now called BoxLang classes, like any other language. You can also use the `class` declaration for them.

### Tags are Components

Since BoxLang is not a tag-based language but a dynamic language offering a templating language. There are no concepts of tags but of BoxLang components that can be accessed via our templating language or script.

### Default assignment scope

In CFML, the default assignment scope is always `variables`, but in BL it can differ based on the context. For Functions, it will be `local`. The BoxLang runtime will toggle this behavior based on the type of the compiled source code. So for `.cfm` or `.cfc` source files, the default assignment scope in functions will remain `variables` but for code compiled from `.bx`, `.bxs` or `.bxm` files, the default assignment scope in functions will be `local`.

### CastAs operator

BL has a new `castAs` binary operator

```jsx
expression castAs "type"
```

No transpilation changes are needed since this is a BL-only feature.

### Multiple catch types

BL supports

```jsx
catch( foo.com | brad | com.luis.majano e ) {}
```

No transpilation changes are needed since this is a BL-only feature.

### Annotations

BL will allow for actual proper annotations before UDF declarations, properties and classes. The value of the annotation can be a string, struct literals or array literals. You can also use multi-spaced or indentation.

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

## JDBC Query Parameter SQL Types

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