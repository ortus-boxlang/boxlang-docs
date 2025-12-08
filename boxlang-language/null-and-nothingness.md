---
description: null does mean something!
icon: helmet-battle
---

# Null & Nothingness

What is nothingness? Is there nothingness only in outer space? If a tree falls in the forest and nobody listens, does it make a sound? Starting to see the point? Does nothing really mean nothing? To be or not to be? OK, I think we are going on a philosophical tangent, so let's get back to our geekiness:

`null` is Java's way to refer to "nothingness.", something that does not exist and has no value.

## Full-Null Support

Full null support is the default in BoxLang, meaning you can use the `null` keyword and get real `null` values from databases or external services. Note that `null` is a reserved word so can't be used for variable names.

Note that if you are using the compat module then full null support is disabled unless you change the module settings for compat to enable it. You can do this programmatically via the `Application.bx` file, which can be used when building web applications. You can learn more [about it here](../boxlang-framework/applicationbx.md). In reality, you still could simulate `null` without full null support, and sometimes you get an empty string, sometimes a full Java `null`. So basically, the nonfull null support is a partial null support, which makes it hard for developers. **So as a rule of thumb, we always recommend checking for nullness no matter WHAT!**

{% code title="Application.bx" %}
```java
class{
    this.nullSupport = true;
}
```
{% endcode %}

## Checking For Nullness

Use the `isNull()` or `isDefined()` methods to evaluate for nothingness.

```javascript
r = getMaybeData()
if( isNull( r ) ){
  // do something because r doesn't exist
}

if( isDefined( "r" ) ){

}
```

Also, remember that you can use the [Elvis operator](operators.md#elvis-operator-null-coalescing) to test for null and an operator and expression.

```javascript
results = getMaybeData() ?: "default value"
```

## Safe Navigation Operator

The [safe navigation operator](operators.md#safe-navigation-operator) (`?.`) is your best friend when dealing with potentially null values in object chains. It prevents null pointer exceptions by returning `null` instead of throwing an error when accessing properties or methods on null objects.

```javascript
// Without safe navigation - may throw error
salary = user.getProfile().getSalary()

// With safe navigation - returns null safely
salary = user?.getProfile()?.getSalary()

// Works with structs too
name = userData?.profile?.name ?: "Unknown"

// Combine with Elvis operator for defaults
displayName = user?.getName() ?: "Anonymous"
```

<a href="https://try.boxlang.io" target="_blank">Try safe navigation on try.boxlang.io</a>

{% hint style="info" %}
We would recommend that you use `isNull()` as it expresses coherently its purpose. Since `isDefined()` can also evaluate expressions.
{% endhint %}

## Elvis Operator - Null Coalescing

The [Elvis operator](operators.md#elvis-operator-null-coalescing) (`?:`) provides a concise way to handle null values by providing a default value when the left operand is null. It's named after Elvis Presley because `?:` looks like Elvis's hairstyle when viewed sideways.

```javascript
// Basic usage - use default if null
displayName = userName ?: "Anonymous"

// With function calls
data = fetchData() ?: []

// Chaining with safe navigation
result = user?.profile?.email ?: "no-email@example.com"

// Multiple levels
config = getConfig() ?: getDefaultConfig() ?: {}

// In function parameters
function greet( name ) {
    println( "Hello, #arguments.name ?: 'Guest'#!" )
}
```

{% hint style="success" %}
The Elvis operator is your go-to solution for providing default values when dealing with potentially null data. It's more concise than ternary operators or if-else statements.
{% endhint %}

<a href="https://try.boxlang.io" target="_blank">Try the Elvis operator on try.boxlang.io</a>

## Creating Nulls

You can create nulls in different ways in BoxLang. Let's explore these:

| Approach | Full Null | Description |
|----------|:---------:|-------------|
| `null` keyword | ✅ | `r = null` |
| Non returning function call | ❌ | If a function returns nothing, its assignment will produce a null.<br>`function getNull(){}`<br>`r = getNull()` |
| `nullValue()` | ❌ | `r = nullValue()` |
| `javaCast( "null", "" )` | ❌ | `r = javaCast( "null", "" )` |

## In Practice

If you have three eggs and eat three eggs, then you might think you have "nothing," but in terms of eggs, you have "0". Zero is something, it’s a number, and it’s not nothing.

If you’re working with words and have a string like "hello" then delete the "h", "e", "l"s, and "o" you might think you’d end up with nothing, but you have "" which is an empty string. It’s still something.

Null in BoxLang is usually encountered when you ask for something that doesn’t exist. When looking at arrays, for instance, we created a list with five elements then asked BoxLang to give us the sixth element of that list. There is no sixth element, so BoxLang gave us null. It isn’t that there’s a blank in that sixth spot (""), it’s not a number 0, it’s nothingness – null.

**Examples**

```java
function getData( filter ){

    if( isNull( arguments.filter ) ){
      // then do this
    } else {
      // use the filter
    }

}

function returnsNull(){
  if( key.exists( "invalid" ) ){
    return key[ "invalid" ];
  }
}

results = returnsNull();

writeOutput( isNull( results ) );
```

Also note that if a function returns **nothing,** it will be the same as returning `null`.
