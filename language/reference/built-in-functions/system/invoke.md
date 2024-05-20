# Invoke

Invokes an object method and returns the result of the invoked method.

## Method Signature

```
Invoke(instance=[any], methodname=[string], arguments=[any])
```

### Arguments

| Argument   | Type  | Required | Description                                                                                                                  | Default |
| ---------- | ----- | -------- | ---------------------------------------------------------------------------------------------------------------------------- | ------- |
| `instance` | `any` | `true`   | Instance of a Box Class or name of one to instantiate. If an empty string is provided, the method will be invoked within the |         |

```
                same template or Box Class. | |
```

\| `methodname` | `string` | `true` | The name of the method to invoke | |

| `arguments` | `any` | `false` | An array of positional arguments or a struct of named arguments to pass into the method. |   |
| ----------- | ----- | ------- | ---------------------------------------------------------------------------------------- | - |

## Examples

```
Invoke(instance=[any], methodname=[string], arguments=[any])
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
* [Throw](throw.md)
* [URLDecode](urldecode.md)
* [URLEncodedFormat](urlencodedformat.md)
* [writeDump](writedump.md)
* [WriteLog](writelog.md)
* [WriteOutput](writeoutput.md)
