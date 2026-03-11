# Request Context Events

These events occur during request context setup and configuration. They are announced on the **global interceptor pool**.

| Event Name               | Cancellable | Description                                                         |
| ------------------------ | :---------: | ------------------------------------------------------------------- |
| `onRequestContextConfig` |     No      | Fired when the request context configuration is being assembled.    |

## onRequestContextConfig

Fired when the request context is assembling its runtime configuration (mappings, security settings, datasources, etc.). Modules can use this to inject or override configuration values for a specific request.

### Data Structure

| Data Key  | Type          | Description                                                                    |
| --------- | ------------- | ------------------------------------------------------------------------------ |
| `context` | `IBoxContext` | The request box context being configured.                                      |
| `config`  | `IStruct`     | The configuration struct being assembled. Mutate this to override settings.    |

### Example

```groovy
class myListener{
	function onRequestContextConfig( struct data ){
		// Inject or override request-level configuration
		data.config[ "myCustomSetting" ] = "value";
	}
}
```
