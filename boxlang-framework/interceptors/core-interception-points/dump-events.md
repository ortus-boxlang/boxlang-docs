# Dump Events

These events occur when BoxLang's native dumping or introspection operations are performed. They are announced on the **global interceptor pool**.

| Event Name            | Cancellable | Description                                                                                     |
| --------------------- | :---------: | ----------------------------------------------------------------------------------------------- |
| `onBXDump`            |     No      | Fired on every `bx:dump` / `dump()` call, before output is written.                            |
| `onMissingDumpOutput` |     No      | Fired when the `output` parameter of a dump is not a built-in destination. Use this to implement custom dump output targets. |

* [`onBXDump`](dump-events.md#onbxdump)
* [`onMissingDumpOutput`](dump-events.md#onmissingdumpoutput)

## onBXDump

Fired on every `bx:dump` or `dump()` call, immediately after the output parameters are resolved and before any output is written. Use this to intercept dumps for debugging tools, testing assertions, or suppressing dump output in production.

The `output` value is already normalised at this point:
- `"console"` — output to stdout
- `"buffer"` — output to the request buffer
- `"___file___"` — output to a file (path is in `dumpFilePath`)
- Any other string — triggers `onMissingDumpOutput` after the dump is rendered

### Data Structure

| Data Key       | Type          | Description                                                                              |
| -------------- | ------------- | ---------------------------------------------------------------------------------------- |
| `context`      | `IBoxContext` | The context in which the dump was called.                                                |
| `target`       | `Object`      | The value being dumped.                                                                  |
| `label`        | `String`      | Optional label to display above the dump output.                                         |
| `top`          | `Integer`     | Maximum nesting depth to render. `null` means unlimited.                                 |
| `expand`       | `Boolean`     | Whether to render the dump in expanded state.                                            |
| `abort`        | `Boolean`     | Whether to abort the request after dumping.                                              |
| `output`       | `String`      | The resolved output destination (`"console"`, `"buffer"`, `"___file___"`, or custom).   |
| `format`       | `String`      | The resolved output format: `"html"` or `"text"`.                                       |
| `dumpFilePath` | `Path`        | The resolved file path when `output` is `"___file___"`. `null` otherwise.               |
| `showUDFs`     | `Boolean`     | Whether to include UDF/function members in the dump output.                              |

### Example

```groovy
class myListener{
	function onBXDump( struct data ){
		var target = data.target;
		var output = data.output;
		var format = data.format;
		// Capture dump output for test assertions, suppress in production, etc.
	}
}
```

## onMissingDumpOutput

Fired when the `output` parameter of a dump call is a custom string that is not one of the built-in destinations (`console`, `buffer`, or a file path). This is the primary extension point for modules to implement custom dump output targets such as a browser debug panel, a remote inspector, or a log aggregator.

By the time this fires, the dump has already been fully rendered into `dumpOutput` (HTML or text). The event data includes all the same fields as `onBXDump` plus the rendered output string.

### Data Structure

| Data Key       | Type          | Description                                                                                 |
| -------------- | ------------- | ------------------------------------------------------------------------------------------- |
| `context`      | `IBoxContext` | The context in which the dump was called.                                                   |
| `target`       | `Object`      | The value that was dumped.                                                                  |
| `label`        | `String`      | Optional label that was passed to the dump call.                                            |
| `top`          | `Integer`     | Maximum nesting depth that was used. `null` means unlimited.                                |
| `expand`       | `Boolean`     | Whether the dump was rendered in expanded state.                                            |
| `abort`        | `Boolean`     | Whether the request will be aborted after the dump.                                         |
| `output`       | `String`      | The custom output destination string that triggered this event.                             |
| `format`       | `String`      | The format used to render the dump: `"html"` or `"text"`.                                  |
| `dumpFilePath` | `Path`        | Always `null` for this event (a file path would have been handled natively).               |
| `showUDFs`     | `Boolean`     | Whether UDF/function members were included in the dump output.                              |
| `dumpOutput`   | `String`      | The fully rendered dump output string (HTML or plain text) ready to be sent to the target. |

### Example

```groovy
class myListener{
	function onMissingDumpOutput( struct data ){
		var output     = data.output;
		var dumpOutput = data.dumpOutput;

		if ( output == "debugpanel" ) {
			// Send dumpOutput to a custom debug panel, WebSocket, etc.
			myDebugPanel.append( dumpOutput );
		}
	}
}
```
