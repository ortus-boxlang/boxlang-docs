# GetSystemSetting

Retrieve a Java System property or environment value by name.

It looks at properties first then environment variables second.

You can also pass a default value to return if the property or environment variable is not found.

## Method Signature

```
GetSystemSetting(key=[String], defaultValue=[String])
```

### Arguments

| Argument       | Type     | Required | Description                                                                      | Default |
| -------------- | -------- | -------- | -------------------------------------------------------------------------------- | ------- |
| `key`          | `String` | `true`   | The name of the system property or environment variable to retrieve              |         |
| `defaultValue` | `String` | `false`  | The default value to return if the property or environment variable is not found |         |

## Examples

## Related

* [ApplicationRestart](applicationrestart.md)
* [ApplicationStartTime](applicationstarttime.md)
* [ApplicationStop](applicationstop.md)
* [BoxAnnounce](boxannounce.md)
* [BoxAnnounceAsync](boxannounceasync.md)
* [BoxRegisterInterceptor](boxregisterinterceptor.md)
* [BoxRegisterRequestInterceptor](boxregisterrequestinterceptor.md)
* [CallStackGet](callstackget.md)
* [CreateGUID](createguid.md)
* [CreateObject](createobject.md)
* [CreateUUID](createuuid.md)
* [DE](de.md)
* [DebugBoxContexts](debugboxcontexts.md)
* [Dump](dump.md)
* [Duplicate](duplicate.md)
* [echo](echo.md)
* [EncodeForHTML](encodeforhtml.md)
* [GetApplicationMetadata](getapplicationmetadata.md)
* [GetBaseTagData](getbasetagdata.md)
* [GetBaseTagList](getbasetaglist.md)
* [GetBaseTemplatePath](getbasetemplatepath.md)
* [GetBoxContext](getboxcontext.md)
* [GetBoxRuntime](getboxruntime.md)
* [GetBoxVersionInfo](getboxversioninfo.md)
* [GetClassMetadata](getclassmetadata.md)
* [GetComponentList](getcomponentlist.md)
* [GetContextRoot](getcontextroot.md)
* [GetCurrentTemplatePath](getcurrenttemplatepath.md)
* [GetFileFromPath](getfilefrompath.md)
* [GetFunctionCalledName](getfunctioncalledname.md)
* [GetFunctionList](getfunctionlist.md)
* [GetModuleInfo](getmoduleinfo.md)
* [GetModuleList](getmodulelist.md)
* [GetTempDirectory](gettempdirectory.md)
* [GetTickCount](gettickcount.md)
* [htmlEditFormat](htmleditformat.md)
* [IIF](iif.md)
* [Invoke](invoke.md)
* [IsInstanceOf](isinstanceof.md)
* [JavaCast](javacast.md)
* [ObjectDeserialize](objectdeserialize.md)
* [ObjectSerialize](objectserialize.md)
* [PagePoolClear](pagepoolclear.md)
* [Print](print.md)
* [Println](println.md)
* [RunThreadInContext](runthreadincontext.md)
* [SessionInvalidate](sessioninvalidate.md)
* [SessionRotate](sessionrotate.md)
* [SessionStartTime](sessionstarttime.md)
* [Sleep](sleep.md)
* [SystemCacheClear](systemcacheclear.md)
* [SystemExecute](systemexecute.md)
* [SystemOutput](systemoutput.md)
* [Throw](throw.md)
* [URLDecode](urldecode.md)
* [URLEncodedFormat](urlencodedformat.md)
* [writeDump](writedump.md)
* [WriteLog](writelog.md)
* [WriteOutput](writeoutput.md)
