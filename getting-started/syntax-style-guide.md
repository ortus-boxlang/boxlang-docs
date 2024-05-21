# Syntax Style Guide

This guide provides a quick overview of BoxLang syntax styles, operators, and features. It aims to assist developers from other languages in their BoxLang development journey.

### Dynamic

BoxLang variables are dynamic and type-inferred.  We try our best to infer which type you are trying to set for variables at compile-time, but they can completely change at runtime.  You use the `var` keyword to specify a variable within functions, or just declare if you are in a `bxs` or `bxm` script file.

```groovy
// string infered
name = "boxlang"
// double infered
age = 1 
// boolean inferred
isActive = false 

function test(){
  var name = "hello"
}

```

You can also add types to arguments within functions or omit it and it will default to `any` which means, well, anything:

```
function add( required numeric a, required numeric b, boolean print = false ){

}
```

### No Semicolons

Semicolons, as you can see, are completely optional.  We prefer no semi-colons unless you really really need to demarcate a beginning and an end.
