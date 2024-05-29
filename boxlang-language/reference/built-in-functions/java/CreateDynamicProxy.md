[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CreateDynamicProxy`

Creates a dynamic proxy of the Box Class that is passed to a Java library.

Dynamic proxy lets you pass Box Classes to Java objects.
 
 Java objects can work with the Box Class seamlessly as if they are native
 Java objects.

## Method Signature

```
CreateDynamicProxy(class=[any], interfaces=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `class` | `any` | `true` | The Box Class to create a dynamic proxy of. |  |
| `interfaces` | `any` | `true` | The interfaces that the dynamic proxy should implement. |  |

## Examples

```
CreateDynamicProxy(class=[any], interfaces=[any])
```

## Related


