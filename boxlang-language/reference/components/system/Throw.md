
# Component: `Throw`

Throws a developer-specified exception, which can be caught with a catch block.

## Component Signature

```
<bx:Throw message=[any]
type=[String]
detail=[String]
errorcode=[String]
extendedinfo=[any]
object=[Throwable] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `message` | `any` | `false` | Message that describes exception event |  |
| `type` | `String` | `false` | The type of the exception |  |
| `detail` | `String` | `false` | Description of the event |  |
| `errorcode` | `String` | `false` | A custom error code that you supply |  |
| `extendedinfo` | `any` | `false` | Additional custom error data that you supply |  |
| `object` | `Throwable` | `false` | An instance of an exception object. If there is no message provided, this object will be thrown directly. If there is a message, a<br>                   CustomException will be thrown and this object will be used as the cause. |  |

## Examples

### Throw a custom exception

Raises a developer-defined exception that can be caught by a try/catch block.

```java
<bx:throw type="ValidationException" message="Email is required">

```

### Throw with detail and error code

```java
<bx:throw
    type="DatabaseError"
    message="Failed to save record"
    detail="Constraint violation on users.email column"
    errorCode="DB_001"
>

```

### Throw with extended info

```java
<bx:throw
    type="AuthException"
    message="Invalid token"
    extendedInfo="#{ userId: 42, token: 'abc123' }#"
>

```

### Rethrow an existing exception object

```java
try {
    riskyOperation();
} catch ( any e ) {
    <bx:throw object="#e#" message="Wrapped: #e.message#">
}

```
