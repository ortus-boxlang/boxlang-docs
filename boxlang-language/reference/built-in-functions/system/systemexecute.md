[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SystemExecute`

Executes a system process/command on the underlying OS.

## Method Signature
```
SystemExecute(name=[string], arguments=[any], timeout=[long], terminateOnTimeout=[boolean], directory=[string], output=[string], error=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The process name or binary path ( e.g. bash or /bin/sh ) |  |
| `arguments` | `any` | `false` | The process arguments ( e.g. for `java --version` this would be `--version` ) |  |
| `timeout` | `long` | `false` | The timeout to wait for the command, in seconds ( default unlimited ) |  |
| `terminateOnTimeout` | `boolean` | `false` | Whether to terminate the process/command if a timeout is reached | `false` |
| `directory` | `string` | `false` | A working directory to execute the command from |  |
| `output` | `string` | `false` |  |  |
| `error` | `string` | `false` | An optional file path to write errors to |  |

## Examples

```
SystemExecute(name=[string], arguments=[any], timeout=[long], terminateOnTimeout=[boolean], directory=[string], output=[string], error=[string])
```

## Related
  * [ApplicationRestart](boxlang-language/reference/built-in-functions/ApplicationRestart.md)
  * [ApplicationStartTime](boxlang-language/reference/built-in-functions/ApplicationStartTime.md)
  * [ApplicationStop](boxlang-language/reference/built-in-functions/ApplicationStop.md)
  * [BoxAnnounce](boxlang-language/reference/built-in-functions/BoxAnnounce.md)
  * [BoxAnnounceAsync](boxlang-language/reference/built-in-functions/BoxAnnounceAsync.md)
  * [CallStackGet](boxlang-language/reference/built-in-functions/CallStackGet.md)
  * [CreateGUID](boxlang-language/reference/built-in-functions/CreateGUID.md)
  * [CreateObject](boxlang-language/reference/built-in-functions/CreateObject.md)
  * [CreateUUID](boxlang-language/reference/built-in-functions/CreateUUID.md)
  * [DE](boxlang-language/reference/built-in-functions/DE.md)
  * [DebugBoxContexts](boxlang-language/reference/built-in-functions/DebugBoxContexts.md)
  * [Dump](boxlang-language/reference/built-in-functions/Dump.md)
  * [Duplicate](boxlang-language/reference/built-in-functions/Duplicate.md)
  * [echo](boxlang-language/reference/built-in-functions/echo.md)
  * [EncodeForHTML](boxlang-language/reference/built-in-functions/EncodeForHTML.md)
  * [GetApplicationMetadata](boxlang-language/reference/built-in-functions/GetApplicationMetadata.md)
  * [GetBaseTemplatePath](boxlang-language/reference/built-in-functions/GetBaseTemplatePath.md)
  * [GetBoxContext](boxlang-language/reference/built-in-functions/GetBoxContext.md)
  * [GetBoxRuntime](boxlang-language/reference/built-in-functions/GetBoxRuntime.md)
  * [GetBoxVersionInfo](boxlang-language/reference/built-in-functions/GetBoxVersionInfo.md)
  * [GetComponentList](boxlang-language/reference/built-in-functions/GetComponentList.md)
  * [GetComponentMetadata](boxlang-language/reference/built-in-functions/GetComponentMetadata.md)
  * [GetContextRoot](boxlang-language/reference/built-in-functions/GetContextRoot.md)
  * [GetCurrentTemplatePath](boxlang-language/reference/built-in-functions/GetCurrentTemplatePath.md)
  * [GetFileFromPath](boxlang-language/reference/built-in-functions/GetFileFromPath.md)
  * [GetFunctionCalledName](boxlang-language/reference/built-in-functions/GetFunctionCalledName.md)
  * [GetFunctionList](boxlang-language/reference/built-in-functions/GetFunctionList.md)
  * [GetSystemSetting](boxlang-language/reference/built-in-functions/GetSystemSetting.md)
  * [GetTempDirectory](boxlang-language/reference/built-in-functions/GetTempDirectory.md)
  * [GetTickCount](boxlang-language/reference/built-in-functions/GetTickCount.md)
  * [htmlEditFormat](boxlang-language/reference/built-in-functions/htmlEditFormat.md)
  * [IIF](boxlang-language/reference/built-in-functions/IIF.md)
  * [Invoke](boxlang-language/reference/built-in-functions/Invoke.md)
  * [IsInstanceOf](boxlang-language/reference/built-in-functions/IsInstanceOf.md)
  * [JavaCast](boxlang-language/reference/built-in-functions/JavaCast.md)
  * [PagePoolClear](boxlang-language/reference/built-in-functions/PagePoolClear.md)
  * [Print](boxlang-language/reference/built-in-functions/Print.md)
  * [Println](boxlang-language/reference/built-in-functions/Println.md)
  * [RunThreadInContext](boxlang-language/reference/built-in-functions/RunThreadInContext.md)
  * [SessionInvalidate](boxlang-language/reference/built-in-functions/SessionInvalidate.md)
  * [SessionRotate](boxlang-language/reference/built-in-functions/SessionRotate.md)
  * [SessionStartTime](boxlang-language/reference/built-in-functions/SessionStartTime.md)
  * [Sleep](boxlang-language/reference/built-in-functions/Sleep.md)
  * [SystemOutput](boxlang-language/reference/built-in-functions/SystemOutput.md)
  * [Test](boxlang-language/reference/built-in-functions/Test.md)
  * [Throw](boxlang-language/reference/built-in-functions/Throw.md)
  * [URLDecode](boxlang-language/reference/built-in-functions/URLDecode.md)
  * [URLEncodedFormat](boxlang-language/reference/built-in-functions/URLEncodedFormat.md)
  * [writeDump](boxlang-language/reference/built-in-functions/writeDump.md)
  * [WriteLog](boxlang-language/reference/built-in-functions/WriteLog.md)
  * [WriteOutput](boxlang-language/reference/built-in-functions/WriteOutput.md)
