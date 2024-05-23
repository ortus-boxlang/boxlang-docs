# Syntax Style Guide

This guide provides a quick overview of BoxLang syntax styles, operators, and features. It aims to assist developers from other languages in their BoxLang development journey.

### Dynamic & Loose Typing

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

```cfscript
function add( required numeric a, required numeric b, boolean print = false ){

}
```

As you can see not only can we make arguments required or not, but we can add default values to arguments.  We can also do type promotions and auto-casting from types that can be castable to other types.  So if we called our function like this:

```groovy
// we auto cast 1 to numeric, "true" to boolean
add( "1", 345, "true" )
```

This is handy as we really really try to match your incoming data to functional arguments.

### `Any` by default

All arguments are of `any` type if not specifically typed.  This means that they will be inferred at runtime.

### `Public` by default

All functions and classes are public by default, so there is no need to add the `public` identifier if you don't want to.  This creates a very nice and low-verbosity approach to function declaration:

```cfscript
function hello(){

}

private function getData(){

}

protected function bindData(){

}
```

### Non-required arguments by default

All arguments are NOT required by default and will be defaulted to `null` if not passed.  You can use the `required` identifier to mark them as required.

### Default Arguments

You can create defaults for arguments which can be literals or actual expressions

```java
function save( transactional = true, data = {}, scope = "#expression#" )
```

### Expression Interpolation

BoxLang can interpret ANYTHING within `#` as an expression. This can be used for output, assignments and much more.

### No Semicolons

Semicolons, as you can see, are completely optional.  We prefer no semi-colons unless you really really need to demarcate a beginning and an end.
