[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CreateDynamicProxy`

Creates a dynamic proxy of the Box Class that is passed to a Java library.

Dynamic proxy lets you pass Box Classes to Java objects.

 Java objects can work with the Box Class seamlessly as if they are native
 Java objects.

## Method Signature

```
CreateDynamicProxy(class=[any], interfaces=[any], classLoader=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `class` | `any` | `true` | The Box Class to create a dynamic proxy of. |  |
| `interfaces` | `any` | `true` | The interfaces that the dynamic proxy should implement. |  |
| `classLoader` | `any` | `false` | **New in 1.7.0** - Optional Java ClassLoader to use for loading the interfaces. Useful when working with custom ClassLoaders or when interfaces are loaded from non-standard locations. |  |

## Examples

### Tag Syntax

```java
<bx:set instance = new cfc.helloWorld() >
 <bx:set dynInstnace = createDynamicProxy( instance, [
	"MyInterface"
	] ) >
 <bx:set x = createObject( "java", "InvokeHelloProxy" ).init( dynInstnace ) >
 <bx:set y = x.invokeHello() >
 <bx:output>#y#</bx:output>
```

### Script Syntax with Custom ClassLoader (New in 1.7.0)

```javascript
// Create instance of Box Class
instance = new cfc.helloWorld();

// Get custom ClassLoader if needed
customClassLoader = createObject( "java", "java.lang.Thread" )
    .currentThread()
    .getContextClassLoader();

// Create dynamic proxy with custom ClassLoader
dynInstance = createDynamicProxy(
    instance,
    [ "MyInterface" ],
    customClassLoader
);

// Pass to Java library
x = createObject( "java", "InvokeHelloProxy" ).init( dynInstance );
y = x.invokeHello();
echo( y );
```



## Related
