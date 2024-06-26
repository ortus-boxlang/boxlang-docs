---
description: JSON all things!
---

# JSON

BoxLang supports native JSON support via several key functions and some member functions.

## Serialize

BoxLang gives us the `jsonSerialize()` function to convert any piece of data to its JSON representation ([https://cfdocs.org/serializejson](https://cfdocs.org/serializejson))

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

By default BoxLang will convert the keys in a struct to uppercase in the result JSON document:

```javascript
person = { name = "Luis Majano", company = "Ortus Solutions", year = 2006};
writeOutput( jsonSerialize( person ) );

// Will become
{ "NAME" : "Luis Majano", "COMPANY" : "Ortus Solutions", "YEAR" : 2006 }
```

If you want to preserve the key casing then wrap them in double/single quotes and define the case:

```javascript
person = {
    'Name' = "Luis Majano",
    'company' = "Ortus Solutions",
    'year' = 2006
};

// Will become
{ "Name" : "Luis Majano", "company" : "Ortus Solutions", "year" : 2006 }
```

### Possible Casting Issues

BoxLang may incorrectly serialize some strings if they can be automatically converted into other types, like numbers or booleans. One workaround is to use a class with [cfproperty](https://cfdocs.org/cfproperty) to specify types. Another workaround is to prepend `Chr(2)` to the value and it will be forced to a string, however, that is an unofficial/undocumented workaround. A more formal workaround is to call `setMetadata()` as a member function on a `struct` to force a type:

```javascript
myStruct = { "zip"="00123" };
myStruct.setMetadata( { "zip": "string" } );
writeOutput( jsonSerialize(myStruct) );
```

## Deserialize

The inverse of serialization is deserialization ([https://cfdocs.org/deserializejson](https://cfdocs.org/deserializejson)). BoxLang gives you the `jsonDeserialize()` function that will take a JSON document and produce native BoxLang data structures for you.

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

BoxLang has a function to test if the incoming string is valid JSON ([https://cfdocs.org/isjson](https://cfdocs.org/isjson)) or not: `isJSON()`

```javascript
isJSON( "[ 1, 2, 3 ]" )
```
