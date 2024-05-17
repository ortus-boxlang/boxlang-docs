# RunThreadInContext

Executes the code in the callback with a speciec parent context so a specific application name is visible and an optional sessionID, or a specific context can be provided from another request.

## Method Signature

```
RunThreadInContext(applicationName=[string], sessionId=[string], context=[any], callback=[function])
```

### Arguments

| Argument          | Type       | Required   | Description                                                                                    | Default   |
| ----------------- | ---------- | ---------- | ---------------------------------------------------------------------------------------------- | --------- |
| `applicationName` | `string`   | `false`    | The application name to use run the code in.                                                   |           |
| `sessionId`       | `string`   | `false`    | The sessionID to use to run the code in (requires application name).                           |           |
| `context`         | `any`      | `false`    | The context to use to run the code in. Mututally exclusive with applicationName and sessionId. |           |
| `callback`        | `function` | `true`     | The function to run in the new context.                                                        |           |
| ----------        | ------     | ---------- | -------------                                                                                  | --------- |

## Examples

```
RunThreadInContext(applicationName=[string], sessionId=[string], context=[any], callback=[function])
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
