[comment]: # (Note: This documentation is generated dynamically in the build process. To modify the contents, change the javadoc on the component class)

# Component: `<bx:RedisLock>`

Provides a distributed lock around the body of the component using Redis as the locking mechanism. This allows safe concurrent access control across multiple requests or servers using Redis as the coordination backend.

## Supported Actions

This component does not support actions. It operates by wrapping the body content in a distributed lock.

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `name` | `string` | `true` | Lock name. Only one request can execute the code within a lock component with a given name at a time. Cannot be an empty string. |  |
| `cache` | `string` | `true` | The name of the Redis cache (as defined in the application cache settings) to use for the lock. |  |
| `timeout` | `numeric` | `false` | Maximum length of time, in seconds, to wait to obtain a lock. If lock is obtained, tag execution continues. Otherwise, behavior depends on throwOnTimeout attribute value. | 2 |
| `expires` | `numeric` | `false` | The length of time, in seconds, before the lock automatically expires. | 60 |
| `throwOnTimeout` | `boolean` | `false` | True: if lock is not obtained within the timeout period, a runtime exception is thrown. False: if lock is not obtained, the body of the component is skipped and execution continues without running the statements in the component. | true |
| `bypass` | `boolean` | `false` | If true, the lock is bypassed and the body is executed immediately without acquiring a lock. | false |

## Examples



## Related
