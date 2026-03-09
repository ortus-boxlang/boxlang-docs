# Template Invocations

These events fire during the invocation of BoxLang templates. They are announced on the **global interceptor pool**.

> **Template scope:** `preTemplateInvoke` and `postTemplateInvoke` fire for every template invocation, including `include` calls and nested templates — not just the top-level request template.

| Event Name           | Cancellable | Description                                                                          |
| -------------------- | :---------: | ------------------------------------------------------------------------------------ |
| `preTemplateInvoke`  |     No      | Fired before every template executes.                                                |
| `postTemplateInvoke` |     No      | Fired after every template finishes — always fires, even if an exception was thrown. |

* [`preTemplateInvoke`](template-invocations.md#pretemplateinvoke)
* [`postTemplateInvoke`](template-invocations.md#posttemplateinvoke)

## preTemplateInvoke

Fired immediately before a BoxLang template (`.bx` or `.bxm` file) begins executing. The template has been pushed onto the template stack at this point.

### Data Structure

| Data Key       | Type               | Description                                     |
| -------------- | ------------------ | ----------------------------------------------- |
| `context`      | `IBoxContext`      | The context in which the template is executing. |
| `template`     | `BoxTemplate`      | The template runnable about to be invoked.      |
| `templatePath` | `ResolvedFilePath` | The resolved file path of the template.         |

### Example

```groovy
class myListener{
	function preTemplateInvoke( struct data ){
		// Log execution, inject variables, enforce access control, etc.
		var templatePath = data.templatePath;
	}
}
```

## postTemplateInvoke

Fired after a BoxLang template finishes executing. This is announced inside a `finally` block, so it **always fires** regardless of whether the template threw an exception. The template is still on the stack when this fires and is popped immediately after.

### Data Structure

| Data Key       | Type               | Description                                  |
| -------------- | ------------------ | -------------------------------------------- |
| `context`      | `IBoxContext`      | The context in which the template executed.  |
| `template`     | `BoxTemplate`      | The template runnable that was invoked.      |
| `templatePath` | `ResolvedFilePath` | The resolved file path of the template.      |

### Example

```groovy
class myListener{
	function postTemplateInvoke( struct data ){
		// Collect timing metrics, clean up injected variables, etc.
		var templatePath = data.templatePath;
	}
}
```
