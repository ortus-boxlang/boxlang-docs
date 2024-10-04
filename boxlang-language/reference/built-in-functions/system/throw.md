# Throw

Throws a developer-specified exception, which can be caught with a catch block.

## Method Signature

```
Throw(message=[String], type=[String], detail=[String], errorcode=[String], extendedinfo=[any], object=[Throwable])
```

### Arguments

| Argument       | Type        | Required | Description                                                                                                                                                                                                            | Default |
| -------------- | ----------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `message`      | `String`    | `false`  | Message that describes exception event                                                                                                                                                                                 |         |
| `type`         | `String`    | `false`  | The type of the exception                                                                                                                                                                                              |         |
| `detail`       | `String`    | `false`  | Description of the event                                                                                                                                                                                               |         |
| `errorcode`    | `String`    | `false`  | A custom error code that you supply                                                                                                                                                                                    |         |
| `extendedinfo` | `any`       | `false`  | Additional custom error data that you supply                                                                                                                                                                           |         |
| `object`       | `Throwable` | `false`  | <p>An instance of an exception object. If there is no message provided, this object will be thrown directly. If there is a message, a<br>CustomException will be thrown and this object will be used as the cause.</p> |         |

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
* [GetSystemSetting](getsystemsetting.md)
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
* [URLDecode](urldecode.md)
* [URLEncodedFormat](urlencodedformat.md)
* [writeDump](writedump.md)
* [WriteLog](writelog.md)
* [WriteOutput](writeoutput.md)
