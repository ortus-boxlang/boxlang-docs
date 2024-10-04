# SystemExecute

Executes a system process/command on the underlying OS.

Returns a struct with the following keys:

{ output : \[ the command output ] error : \[ any errors emitted by the command ] timeout : \[ boolean value as to whether a timeout was reached ] terminated : \[ boolean value as to whether the process was terminated ] pid : the PID of the process }

## Method Signature

```
SystemExecute(name=[string], arguments=[any], timeout=[long], terminateOnTimeout=[boolean], directory=[string], output=[string], error=[string])
```

### Arguments

| Argument             | Type      | Required | Description                                                                   | Default |
| -------------------- | --------- | -------- | ----------------------------------------------------------------------------- | ------- |
| `name`               | `string`  | `true`   | The process name or binary path ( e.g. bash or /bin/sh )                      |         |
| `arguments`          | `any`     | `false`  | The process arguments ( e.g. for `java --version` this would be `--version` ) |         |
| `timeout`            | `long`    | `false`  | The timeout to wait for the command, in seconds ( default unlimited )         |         |
| `terminateOnTimeout` | `boolean` | `false`  | Whether to terminate the process/command if a timeout is reached              | `false` |
| `directory`          | `string`  | `false`  | A working directory to execute the command from                               |         |
| `output`             | `string`  | `false`  |                                                                               |         |
| `error`              | `string`  | `false`  | An optional file path to write errors to                                      |         |

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
* [SystemOutput](systemoutput.md)
* [Throw](throw.md)
* [URLDecode](urldecode.md)
* [URLEncodedFormat](urlencodedformat.md)
* [writeDump](writedump.md)
* [WriteLog](writelog.md)
* [WriteOutput](writeoutput.md)
