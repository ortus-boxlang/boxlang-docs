# BoxAnnounce

Announce a BoxLang event to a specific interceptor pool.

By default, the event is announced to the global interception service. Available pools are "global" and "request". The request pool is tied to the application listener and is only available during the request lifecycle.

Example:

```
 // Announce globally
 boxAnnounce( "onRequestStart", { request = request } )

 // Announce to the application request
 boxAnnounce( "myRequestEvent", { data : myData }, "request" )
 
```

## Method Signature

```
BoxAnnounce(state=[string], data=[struct], poolname=[string])
```

### Arguments

| Argument   | Type     | Required | Description                                                                                                                 | Default  |
| ---------- | -------- | -------- | --------------------------------------------------------------------------------------------------------------------------- | -------- |
| `state`    | `string` | `true`   | The interceptor event to announce: Ex: "onRequestStart", "onRequestEnd", "onError"                                          |          |
| `data`     | `struct` | `false`  | The data struct to send with the event                                                                                      | `{}`     |
| `poolname` | `string` | `false`  | The name of the interceptor pool to announce the event to. Default is "global". Available pools are "global" and "request". | `global` |

## Examples

## Related

* [ApplicationRestart](ApplicationRestart.md)
* [ApplicationStartTime](ApplicationStartTime.md)
* [ApplicationStop](ApplicationStop.md)
* [BoxAnnounceAsync](BoxAnnounceAsync.md)
* [BoxRegisterInterceptionPoints](BoxRegisterInterceptionPoints.md)
* [BoxRegisterInterceptor](BoxRegisterInterceptor.md)
* [BoxRegisterRequestInterceptor](BoxRegisterRequestInterceptor.md)
* [CallStackGet](CallStackGet.md)
* [CreateGUID](CreateGUID.md)
* [CreateObject](CreateObject.md)
* [CreateUUID](CreateUUID.md)
* [DE](DE.md)
* [DebugBoxContexts](DebugBoxContexts.md)
* [Dump](Dump.md)
* [Duplicate](Duplicate.md)
* [echo](echo.md)
* [EncodeForHTML](EncodeForHTML.md)
* [GetApplicationMetadata](GetApplicationMetadata.md)
* [GetBaseTagData](GetBaseTagData.md)
* [GetBaseTagList](GetBaseTagList.md)
* [GetBaseTemplatePath](GetBaseTemplatePath.md)
* [GetBoxContext](GetBoxContext.md)
* [GetBoxRuntime](GetBoxRuntime.md)
* [GetBoxVersionInfo](GetBoxVersionInfo.md)
* [GetClassMetadata](GetClassMetadata.md)
* [GetComponentList](GetComponentList.md)
* [GetContextRoot](GetContextRoot.md)
* [GetCurrentTemplatePath](GetCurrentTemplatePath.md)
* [GetFileFromPath](GetFileFromPath.md)
* [GetFunctionCalledName](GetFunctionCalledName.md)
* [GetFunctionList](GetFunctionList.md)
* [GetModuleInfo](GetModuleInfo.md)
* [GetModuleList](GetModuleList.md)
* [GetRequestClassLoader](GetRequestClassLoader.md)
* [GetSemver](GetSemver.md)
* [GetSystemSetting](GetSystemSetting.md)
* [GetTempDirectory](GetTempDirectory.md)
* [GetTickCount](GetTickCount.md)
* [htmlEditFormat](htmlEditFormat.md)
* [IIF](IIF.md)
* [Invoke](Invoke.md)
* [IsInstanceOf](IsInstanceOf.md)
* [JavaCast](JavaCast.md)
* [ObjectDeserialize](ObjectDeserialize.md)
* [ObjectSerialize](ObjectSerialize.md)
* [PagePoolClear](PagePoolClear.md)
* [Print](Print.md)
* [Println](Println.md)
* [RunThreadInContext](RunThreadInContext.md)
* [SessionInvalidate](SessionInvalidate.md)
* [SessionRotate](SessionRotate.md)
* [SessionStartTime](SessionStartTime.md)
* [Sleep](Sleep.md)
* [SystemCacheClear](SystemCacheClear.md)
* [SystemExecute](SystemExecute.md)
* [SystemOutput](SystemOutput.md)
* [Throw](Throw.md)
* [Trace](Trace.md)
* [URLDecode](URLDecode.md)
* [URLEncodedFormat](URLEncodedFormat.md)
* [writeDump](writeDump.md)
* [WriteLog](WriteLog.md)
* [WriteOutput](WriteOutput.md)
