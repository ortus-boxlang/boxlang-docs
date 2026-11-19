[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SystemExecute`

Executes a system process/command on the underlying OS.

Returns a struct with the following keys:

 {
 output : [ the command output ]
 error : [ any errors emitted by the command ]
 timeout : [ boolean value as to whether a timeout was reached ]
 terminated : [ boolean value as to whether the process was terminated ]
 pid : the PID of the process
 exitCode : the exit code, when the process exited or was terminated
 cancelled : [ boolean value as to whether isCancelled() ended the process ]
 }

Pass `onLine` to receive each output line while the process runs, `isCancelled` to stop it on demand, and `mergeErrors` to fold stderr into stdout. See [Live Output and Cancellation](../../../../boxlang-framework/os-integration.md#live-output-and-cancellation). Added in 1.20.0.

## Method Signature

```
SystemExecute(name=[string], arguments=[any], timeout=[long], terminateOnTimeout=[boolean], directory=[string], output=[string], error=[string], inheritEnvironment=[boolean], environment=[struct], onLine=[function], isCancelled=[function], mergeErrors=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The process name or binary path ( e.g. bash or /bin/sh ) |  |
| `arguments` | `any` | `false` | The process arguments ( e.g. for `java --version` this would be `--version` ) |  |
| `timeout` | `long` | `false` | The timeout to wait for the command, in seconds ( default unlimited ) |  |
| `terminateOnTimeout` | `boolean` | `false` | Whether to terminate the process/command if a timeout is reached | `false` |
| `directory` | `string` | `false` | A working directory to execute the command from |  |
| `output` | `string` | `false` | An optional file path to write the command output to |  |
| `error` | `string` | `false` | An optional file path to write errors to |  |
| `inheritEnvironment` | `boolean` | `false` | Whether to inherit the parent process environment variables. Defaults to true. | `true` |
| `environment` | `struct` | `false` | A struct of environment variables to pass to the process. Merged in after the inherit decision. | `{}` |
| `onLine` | `function` | `false` | An optional function called as each output line arrives, before the process exits: `onLine( line, stream )`, where stream is `"stdout"` or `"stderr"`. It runs on the calling thread. Output is still captured in the result. A stream redirected to a file gets no callbacks. If the function throws, the process is killed and the error is rethrown. |  |
| `isCancelled` | `function` | `false` | An optional function polled while the process runs. When it returns true the process tree is terminated and the output captured so far is returned with `cancelled = true` and `terminated = true`. A cancellation is not a timeout. Lines still queued when the process is killed are not delivered to `onLine`, but remain in the captured output. |  |
| `mergeErrors` | `boolean` | `false` | When true, stderr is combined into stdout, so there is a single stream and every line is reported as `"stdout"`. When false the streams stay separate. Cannot be combined with the `error` argument. | `false` |

## Examples

### Execute a system command

```java
result = systemExecute( "echo hello" );
writeOutput( result.output.contains( "hello" ) );

```

Result: true

### Execute with working directory

```java
result = systemExecute( "pwd", getCanonicalPath( "." ) );
writeOutput( isStruct( result ) );

```

Result: true

### Stream output as it arrives

```java
lines = []
result = systemExecute(
    name = "sh",
    arguments = [ "-c", "echo first; sleep 2; echo second" ],
    onLine = ( line, stream ) => lines.append( line )
)
writeOutput( lines.len() )

```

Result: 2

### Cancel a running process

```java
start = getTickCount()
result = systemExecute(
    name = "sleep",
    arguments = "30",
    isCancelled = () => getTickCount() - start > 500
)
writeOutput( result.cancelled )

```

Result: true

### Merge stderr into stdout

```java
result = systemExecute(
    name = "sh",
    arguments = [ "-c", "echo out; echo err >&2" ],
    mergeErrors = true
)
writeOutput( result.output.contains( "err" ) )

```

Result: true

## Related

  * [ApplicationRestart](./ApplicationRestart.md)
  * [ApplicationStartTime](./ApplicationStartTime.md)
  * [ApplicationStop](./ApplicationStop.md)
  * [BoxAnnounce](./BoxAnnounce.md)
  * [BoxAnnounceAsync](./BoxAnnounceAsync.md)
  * [BoxAST](./BoxAST.md)
  * [BoxModuleReload](./BoxModuleReload.md)
  * [BoxRegisterInterceptionPoints](./BoxRegisterInterceptionPoints.md)
  * [BoxRegisterInterceptor](./BoxRegisterInterceptor.md)
  * [BoxRegisterRequestInterceptor](./BoxRegisterRequestInterceptor.md)
  * [BoxUnregisterInterceptor](./BoxUnregisterInterceptor.md)
  * [BoxUnregisterRequestInterceptor](./BoxUnregisterRequestInterceptor.md)
  * [CallStackGet](./CallStackGet.md)
  * [CreateGUID](./CreateGUID.md)
  * [CreateObject](./CreateObject.md)
  * [CreateUUID](./CreateUUID.md)
  * [DE](./DE.md)
  * [DebugBoxContexts](./DebugBoxContexts.md)
  * [Dump](./Dump.md)
  * [Duplicate](./Duplicate.md)
  * [echo](./echo.md)
  * [EncodeForHTML](./EncodeForHTML.md)
  * [GetApplicationMetadata](./GetApplicationMetadata.md)
  * [GetBaseTagData](./GetBaseTagData.md)
  * [GetBaseTagList](./GetBaseTagList.md)
  * [GetBaseTemplatePath](./GetBaseTemplatePath.md)
  * [GetBoxContext](./GetBoxContext.md)
  * [GetBoxRuntime](./GetBoxRuntime.md)
  * [GetBoxVersionInfo](./GetBoxVersionInfo.md)
  * [GetClassMetadata](./GetClassMetadata.md)
  * [GetComponentList](./GetComponentList.md)
  * [GetContextRoot](./GetContextRoot.md)
  * [GetCurrentTemplatePath](./GetCurrentTemplatePath.md)
  * [GetFileFromPath](./GetFileFromPath.md)
  * [GetFunctionCalledName](./GetFunctionCalledName.md)
  * [GetFunctionList](./GetFunctionList.md)
  * [GetModuleInfo](./GetModuleInfo.md)
  * [GetModuleList](./GetModuleList.md)
  * [GetModuleTree](./GetModuleTree.md)
  * [GetRequestClassLoader](./GetRequestClassLoader.md)
  * [GetSemver](./GetSemver.md)
  * [GetSystemSetting](./GetSystemSetting.md)
  * [GetTempDirectory](./GetTempDirectory.md)
  * [GetTickCount](./GetTickCount.md)
  * [htmlEditFormat](./htmlEditFormat.md)
  * [IIF](./IIF.md)
  * [Invoke](./Invoke.md)
  * [IsInstanceOf](./IsInstanceOf.md)
  * [JavaCast](./JavaCast.md)
  * [ObjectDeserialize](./ObjectDeserialize.md)
  * [ObjectSerialize](./ObjectSerialize.md)
  * [PagePoolClear](./PagePoolClear.md)
  * [Print](./Print.md)
  * [Println](./Println.md)
  * [RunThreadInContext](./RunThreadInContext.md)
  * [SessionInvalidate](./SessionInvalidate.md)
  * [SessionRotate](./SessionRotate.md)
  * [SessionStartTime](./SessionStartTime.md)
  * [Sleep](./Sleep.md)
  * [SystemCacheClear](./SystemCacheClear.md)
  * [SystemOutput](./SystemOutput.md)
  * [Throw](./Throw.md)
  * [Trace](./Trace.md)
  * [URLDecode](./URLDecode.md)
  * [URLEncodedFormat](./URLEncodedFormat.md)
  * [writeDump](./writeDump.md)
  * [WriteLog](./WriteLog.md)
  * [WriteOutput](./WriteOutput.md)
