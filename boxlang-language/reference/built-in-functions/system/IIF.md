[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IIF`

A boolean condition or value is passed into the first argument.

If the condition is true the second argument is evaluated and returned, if false
 the third argument is evaluated and returned.

## Method Signature

```
IIF(condition=[boolean], expression1=[string], expression2=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `condition` | `boolean` | `true` | The condition to evaluate |  |
| `expression1` | `string` | `true` | The expression to evaluate if the condition is true |  |
| `expression2` | `string` | `true` | The expression to evaluate if the condition is false |  |

## Examples

### Simple iIf Example



<a href="https://try.boxlang.io/?code=eJzL9EzTUChOLSpLLdLzD9bzc%2FR1VbC1VVBySkzOz1PSUUhJ1VBQCirNy8vMS1cACyr4ByspaEJl%2FPJLFLDIKmhacwEAwp8Z9w%3D%3D" target="_blank">Run Example</a>

```java
iIf( server.OS.NAME == "Bacon", de( "Running Bacon OS" ), de( "Not Running Bacon OS" ) );
```

Result: Not Running Bacon OS

### Simple Example using Ternary Operator Instead

Instead of using iif, you should use the ternary operator

<a href="https://try.boxlang.io/?code=eJzT0ChOLSpLLdLzD9bzc%2FR1VbC1VVBySkzOz1PSVLBXUAoqzcvLzEtXAAsp%2BAcrKVgpKPnllyhgSGhacwEAduEWnQ%3D%3D" target="_blank">Run Example</a>

```java
((server.OS.NAME == "Bacon") ? "Running Bacon OS" : "Not Running Bacon OS");

```

Result: Not Running Bacon OS


## Related

  * [Throw](./Throw.md)
  * [GetBaseTemplatePath](./GetBaseTemplatePath.md)
  * [Duplicate](./Duplicate.md)
  * [WriteLog](./WriteLog.md)
  * [BoxAnnounceAsync](./BoxAnnounceAsync.md)
  * [SessionRotate](./SessionRotate.md)
  * [IsInstanceOf](./IsInstanceOf.md)
  * [GetApplicationMetadata](./GetApplicationMetadata.md)
  * [URLDecode](./URLDecode.md)
  * [GetFunctionList](./GetFunctionList.md)
  * [URLEncodedFormat](./URLEncodedFormat.md)
  * [ApplicationRestart](./ApplicationRestart.md)
  * [Invoke](./Invoke.md)
  * [GetModuleInfo](./GetModuleInfo.md)
  * [CreateUUID](./CreateUUID.md)
  * [GetTempDirectory](./GetTempDirectory.md)
  * [GetSemver](./GetSemver.md)
  * [GetModuleList](./GetModuleList.md)
  * [ApplicationStop](./ApplicationStop.md)
  * [SystemExecute](./SystemExecute.md)
  * [BoxModuleReload](./BoxModuleReload.md)
  * [GetRequestClassLoader](./GetRequestClassLoader.md)
  * [GetFunctionCalledName](./GetFunctionCalledName.md)
  * [WriteOutput](./WriteOutput.md)
  * [echo](./echo.md)
  * [Print](./Print.md)
  * [BoxRegisterRequestInterceptor](./BoxRegisterRequestInterceptor.md)
  * [ApplicationStartTime](./ApplicationStartTime.md)
  * [GetBoxContext](./GetBoxContext.md)
  * [CreateObject](./CreateObject.md)
  * [GetComponentList](./GetComponentList.md)
  * [ObjectSerialize](./ObjectSerialize.md)
  * [SessionInvalidate](./SessionInvalidate.md)
  * [SessionStartTime](./SessionStartTime.md)
  * [BoxUnregisterRequestInterceptor](./BoxUnregisterRequestInterceptor.md)
  * [GetFileFromPath](./GetFileFromPath.md)
  * [EncodeForHTML](./EncodeForHTML.md)
  * [htmlEditFormat](./htmlEditFormat.md)
  * [GetClassMetadata](./GetClassMetadata.md)
  * [SystemOutput](./SystemOutput.md)
  * [JavaCast](./JavaCast.md)
  * [GetContextRoot](./GetContextRoot.md)
  * [GetTickCount](./GetTickCount.md)
  * [CreateGUID](./CreateGUID.md)
  * [Sleep](./Sleep.md)
  * [DE](./DE.md)
  * [GetBoxRuntime](./GetBoxRuntime.md)
  * [PagePoolClear](./PagePoolClear.md)
  * [GetCurrentTemplatePath](./GetCurrentTemplatePath.md)
  * [Println](./Println.md)
  * [SystemCacheClear](./SystemCacheClear.md)
  * [GetSystemSetting](./GetSystemSetting.md)
  * [RunThreadInContext](./RunThreadInContext.md)
  * [GetBaseTagData](./GetBaseTagData.md)
  * [BoxAnnounce](./BoxAnnounce.md)
  * [BoxRegisterInterceptor](./BoxRegisterInterceptor.md)
  * [BoxRegisterInterceptionPoints](./BoxRegisterInterceptionPoints.md)
  * [GetBoxVersionInfo](./GetBoxVersionInfo.md)
  * [Trace](./Trace.md)
  * [GetBaseTagList](./GetBaseTagList.md)
  * [ObjectDeserialize](./ObjectDeserialize.md)
  * [DebugBoxContexts](./DebugBoxContexts.md)
  * [Dump](./Dump.md)
  * [writeDump](./writeDump.md)
  * [BoxUnregisterInterceptor](./BoxUnregisterInterceptor.md)
  * [CallStackGet](./CallStackGet.md)
