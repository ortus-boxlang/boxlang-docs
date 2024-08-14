---
description: JSON all things!
---

# JSON

BoxLang supports native JSON support via several key functions and some member functions.

## Serialize

BoxLang gives us the `jsonSerialize()` function to convert any piece of data to its JSON representation ([https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/conversion/jsonserialize](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/conversion/jsonserialize))

```javascript
jsonSerialize(
 var
 [, serializeQueryByColumns = false ]
 [, useSecureJSONPrefix = false ]
 [, useCustomSerializer = false ]
)
```

Pass in any complex or simple variable to the `var` argument and JSON will be produced:

```javascript
person = { name = "Luis Majano", company = "Ortus Solutions", year = 2006};
writeOutput( jsonSerialize( person ) );
```

You can even use the `toJSON()` member function:

```javascript
person = { name = "Luis Majano", company = "Ortus Solutions", year = 2006};
writeOutput( person.toJSON() );
```

### Key Casing

By default BoxLang will keep the keys in a struct in their original casing in the resulting JSON document:

```javascript
person = { name = "Luis Majano", company = "Ortus Solutions", year = 2006};
writeOutput( jsonSerialize( person ) );

// Will become
{ "name" : "Luis Majano", "company" : "Ortus Solutions", "year" : 2006 }
```

### Possible Casting Issues

BoxLang may incorrectly serialize some strings if they can be automatically converted into other types, like numbers or booleans. One workaround is to use a class with [property](https://boxlang.ortusbooks.com/boxlang-language/classes/properties) to specify types. Another workaround is to prepend `Chr(2)` to the value and it will be forced to a string, however, that is an unofficial/undocumented workaround. A more formal workaround is to call `setMetadata()` as a member function on a `struct` to force a type:

```javascript
myStruct = { "zip"="00123" };
myStruct.setMetadata( { "zip": "string" } );
writeOutput( jsonSerialize(myStruct) );
```

## Deserialize

The inverse of serialization is deserialization ([https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/conversion/jsondeserialize](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/conversion/jsondeserialize)). BoxLang gives you the `jsonDeserialize()` function that will take a JSON document and produce native BoxLang data structures for you.

```javascript
jsonDeserialize(
 json
 [, strictMapping = true ]
 [, useCustomSerializer = false ]
)
```

Just pass a JSON document, and off we go with native structs/arrays/dates/strings and booleans.

```java
if( isJson( mydata ) ){
    return jsonDeserialize( data );
}

person = jsonDeserialize( '{"company":"Ortus","name":"Mr OrtusMan"}' );
writeOutput( person.company );
```

This function can also be used as a member function in any string literal:

```java
var deserializedData = myjsonString.jsonDeserialize();
var data = '[]'.jsonDeserialize();
```

## Is this JSON?

BoxLang has a function to test if the incoming string is valid JSON ([https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/decision/isjson](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/decision/isjson)) or not: `isJSON()`

```javascript
isJSON( "[ 1, 2, 3 ]" )
```
