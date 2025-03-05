[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `WriteLog`

Writes a log message out

## Method Signature

```
WriteLog(text=[string], type=[string], application=[boolean], log=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `text` | `string` | `true` | The text of the log message |  |
| `type` | `string` | `false` | The log level of the entry. One of "Information", "Warning", "Error", "Debug", "Trace" | `info` |
| `application` | `boolean` | `false` | If true, it logs the application name alongside the message. Default is true. | `true` |
| `log` | `string` | `false` | The destination logger to use. If not passed, we use the default logger (application.log).<br>               If the logger is a file appender and it doesn't exist it will create it for you.<br>               If the value is an absolue path, it will create a file appender for you at that location. |  |

## Examples



## Related

  * [ApplicationRestart](./ApplicationRestart.md)
  * [ApplicationStartTime](./ApplicationStartTime.md)
  * [ApplicationStop](./ApplicationStop.md)
  * [BoxAnnounce](./BoxAnnounce.md)
  * [BoxAnnounceAsync](./BoxAnnounceAsync.md)
  * [BoxRegisterInterceptionPoints](./BoxRegisterInterceptionPoints.md)
  * [BoxRegisterInterceptor](./BoxRegisterInterceptor.md)
  * [BoxRegisterRequestInterceptor](./BoxRegisterRequestInterceptor.md)
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
  * [SystemExecute](./SystemExecute.md)
  * [SystemOutput](./SystemOutput.md)
  * [Throw](./Throw.md)
  * [Trace](./Trace.md)
  * [URLDecode](./URLDecode.md)
  * [URLEncodedFormat](./URLEncodedFormat.md)
  * [writeDump](./writeDump.md)
  * [WriteOutput](./WriteOutput.md)