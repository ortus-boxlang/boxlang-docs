# Throw

Throws a developer-specified exception, which can be caught with a catch block.

## Method Signature

```
Throw(message=[String], type=[String], detail=[String], errorcode=[String], extendedinfo=[any], object=[any])
```

### Arguments

| Argument       | Type     | Required | Description                                                                                                                        | Default |
| -------------- | -------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `message`      | `String` | `false`  | Message that describes exception event                                                                                             |         |
| `type`         | `String` | `false`  | The type of the exception                                                                                                          |         |
| `detail`       | `String` | `false`  | Description of the event                                                                                                           |         |
| `errorcode`    | `String` | `false`  | A custom error code that you supply                                                                                                |         |
| `extendedinfo` | `any`    | `false`  | Additional custom error data that you supply                                                                                       |         |
| `object`       | `any`    | `false`  | An instance of an exception object. If there is no message provided, this object will be thrown directly. If there is a message, a |         |

```
              CustomException will be thrown and this object will be used as the cause. | |
```

\|----------|------|----------|-------------|---------|

## Examples

```
Throw(message=[String], type=[String], detail=[String], errorcode=[String], extendedinfo=[any], object=[any])
```

## Related

* [ApplicationRestart](applicationrestart.md)
* [ApplicationStartTime](applicationstarttime.md)
* [ApplicationStop](applicationstop.md)
* [BoxAnnounce](boxannounce.md)
* [BoxAnnounceAsync](boxannounceasync.md)
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
* [GetBaseTemplatePath](getbasetemplatepath.md)
* [GetBoxContext](getboxcontext.md)
* [GetBoxRuntime](getboxruntime.md)
* [GetBoxVersionInfo](getboxversioninfo.md)
* [GetComponentMetadata](getcomponentmetadata.md)
* [GetContextRoot](getcontextroot.md)
* [GetCurrentTemplatePath](getcurrenttemplatepath.md)
* [GetFileFromPath](getfilefrompath.md)
* [GetFunctionCalledName](getfunctioncalledname.md)
* [GetFunctionList](getfunctionlist.md)
* [GetSystemSetting](getsystemsetting.md)
* [GetTempDirectory](gettempdirectory.md)
* [GetTickCount](gettickcount.md)
* [htmlEditFormat](htmleditformat.md)
* [IIF](iif.md)
* [Invoke](invoke.md)
* [IsInstanceOf](isinstanceof.md)
* [JavaCast](javacast.md)
* [PagePoolClear](pagepoolclear.md)
* [Print](print.md)
* [Println](println.md)
* [RunThreadInContext](runthreadincontext.md)
* [SessionInvalidate](sessioninvalidate.md)
* [SessionRotate](sessionrotate.md)
* [SessionStartTime](sessionstarttime.md)
* [Sleep](sleep.md)
* [SystemExecute](systemexecute.md)
* [SystemOutput](systemoutput.md)
* [Test](test.md)
* [URLDecode](urldecode.md)
* [URLEncodedFormat](urlencodedformat.md)
* [writeDump](writedump.md)
* [WriteLog](writelog.md)
* [WriteOutput](writeoutput.md)
