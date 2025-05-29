
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


