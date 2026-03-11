# Logging Events

These events are announced when messages are logged inside the BoxLang runtime. They are announced on the **global interceptor pool**.

| Event Name   | Cancellable | Description                                                                                     |
| ------------ | :---------: | ----------------------------------------------------------------------------------------------- |
| `logMessage` |     No      | Fired by `bx:log` and `writeLog()` for every log entry. The actual log writing is handled by interceptors listening to this event. |

* [`logMessage`](logging-events.md#logmessage)

## logMessage

Fired by both the `bx:log` component and the `writeLog()` BIF for every log call. The event data struct is passed **directly** from the caller's attributes/arguments — the actual writing to log files is performed by interceptors that listen to this event (including the built-in logging interceptor). This means you can intercept, suppress, enrich, or redirect any log message in the system.

If `application=true` and an application context is active, an `applicationName` key is automatically added to the data before the event fires.

### Data Structure

| Data Key          | Type      | Description                                                                                           |
| ----------------- | --------- | ----------------------------------------------------------------------------------------------------- |
| `text`            | `String`  | The message text to log.                                                                              |
| `type`            | `String`  | The log level. One of `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`. Defaults to the runtime default level. |
| `log`             | `String`  | The target logger name or absolute file path. Defaults to `application` (the application log).        |
| `application`     | `Boolean` | Whether to include the application name alongside the message. Defaults to `true`.                   |
| `applicationName` | `String`  | The current application name. Added automatically when `application=true` and an app context exists.  |
| `file`            | `String`  | _(Compat only — use `log` instead.)_ Legacy file destination.                                        |

### Example

```groovy
class myListener{
	function logMessage( struct data ){
		var text            = data.text;
		var type            = data.type;
		var log             = data.log;
		var applicationName = data.applicationName ?: "";
		// Route, enrich, suppress, or forward log messages
	}
}
```
