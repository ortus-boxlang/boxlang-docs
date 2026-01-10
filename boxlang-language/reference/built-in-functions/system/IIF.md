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
  * [GetRequestClassLoader](./GetRequestClassLoader.md)
  * [GetSemver](./GetSemver.md)
  * [GetSystemSetting](./GetSystemSetting.md)
  * [GetTempDirectory](./GetTempDirectory.md)
  * [GetTickCount](./GetTickCount.md)
  * [htmlEditFormat](./htmlEditFormat.md)
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
  * [SystemExecute](./SystemExecute.md)
  * [SystemOutput](./SystemOutput.md)
  * [Throw](./Throw.md)
  * [Trace](./Trace.md)
  * [URLDecode](./URLDecode.md)
  * [URLEncodedFormat](./URLEncodedFormat.md)
  * [writeDump](./writeDump.md)
  * [WriteLog](./WriteLog.md)
  * [WriteOutput](./WriteOutput.md)
