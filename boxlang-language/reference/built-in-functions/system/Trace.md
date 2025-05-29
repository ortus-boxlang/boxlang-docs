[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Trace`

Traces messages into the tracing facilites so they can be display by the running runtime either in console, or debug
 output or whatever the runtime is configured to do.

<p>
 It will track from where the trace call was made and the message will be logged with the category, type and text provided.
 <p>
 All tracers will be sent to the {@code trace.log} file in the logs directory of the runtime as well.
 <p>
 If the {@code abort} attribute is set to true, the current request will be aborted after the trace call.
 <p>
 Tracers will <strong>only</strong> be displayed if the runtime is in <strong>debug mode.</strong>. However, all
 traces will be logged regardless of the debug mode flag.
 <p>
 The {@code extraInfo} attribute is optional and can be any simple or complex object. We will convert it to string for logging
 using the {@code toString()} method on the object. You can also use the alias of {@code var} for this attribute as well.

## Method Signature

```
Trace(text=[string], category=[String], type=[string], extrainfo=[any], abort=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `text` | `string` | `true` | The text of the trace message. Required. |  |
| `category` | `String` | `false` | The category of the trace message. Default is an empty string. |  |
| `type` | `string` | `false` | The type of the trace message. Default is "Information". | `Information` |
| `extrainfo` | `any` | `false` | Any extra information to be logged with the trace message. This can be simple or a complex object. We will convert it to string for logging. |  |
| `abort` | `boolean` | `false` | If true, the current request will be aborted after the trace call. Default is false. | `false` |

## Examples



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
  * [IIF](./IIF.md)
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
  * [GetBaseTagList](./GetBaseTagList.md)
  * [ObjectDeserialize](./ObjectDeserialize.md)
  * [DebugBoxContexts](./DebugBoxContexts.md)
  * [Dump](./Dump.md)
  * [writeDump](./writeDump.md)
  * [BoxUnregisterInterceptor](./BoxUnregisterInterceptor.md)
  * [CallStackGet](./CallStackGet.md)
