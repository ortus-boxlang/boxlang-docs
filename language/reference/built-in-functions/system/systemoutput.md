[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SystemOutput`

Writes the given object to the output stream

## Method Signature
```
SystemOutput(obj=[any], addNewLine=[boolean], doErrorStream=[boolean])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `obj` | `any` | `true` | The object to write to the output stream |  |
| `addNewLine` | `boolean` | `true` | If true, a new line will be added to the output stream | `false` |
| `doErrorStream` | `boolean` | `false` | If true, the object will be written to the error stream | `false` |

## Examples

```
SystemOutput(obj=[any], addNewLine=[boolean], doErrorStream=[boolean])
```

## Related
  * [ApplicationRestart](ApplicationRestart.md)
  * [ApplicationStartTime](ApplicationStartTime.md)
  * [ApplicationStop](ApplicationStop.md)
  * [BoxAnnounce](BoxAnnounce.md)
  * [BoxAnnounceAsync](BoxAnnounceAsync.md)
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
  * [GetBaseTemplatePath](GetBaseTemplatePath.md)
  * [GetBoxContext](GetBoxContext.md)
  * [GetBoxRuntime](GetBoxRuntime.md)
  * [GetBoxVersionInfo](GetBoxVersionInfo.md)
  * [GetComponentList](GetComponentList.md)
  * [GetComponentMetadata](GetComponentMetadata.md)
  * [GetContextRoot](GetContextRoot.md)
  * [GetCurrentTemplatePath](GetCurrentTemplatePath.md)
  * [GetFileFromPath](GetFileFromPath.md)
  * [GetFunctionCalledName](GetFunctionCalledName.md)
  * [GetFunctionList](GetFunctionList.md)
  * [GetSystemSetting](GetSystemSetting.md)
  * [GetTempDirectory](GetTempDirectory.md)
  * [GetTickCount](GetTickCount.md)
  * [htmlEditFormat](htmlEditFormat.md)
  * [IIF](IIF.md)
  * [Invoke](Invoke.md)
  * [IsInstanceOf](IsInstanceOf.md)
  * [JavaCast](JavaCast.md)
  * [PagePoolClear](PagePoolClear.md)
  * [Print](Print.md)
  * [Println](Println.md)
  * [RunThreadInContext](RunThreadInContext.md)
  * [SessionInvalidate](SessionInvalidate.md)
  * [SessionRotate](SessionRotate.md)
  * [SessionStartTime](SessionStartTime.md)
  * [Sleep](Sleep.md)
  * [SystemExecute](SystemExecute.md)
  * [Test](Test.md)
  * [Throw](Throw.md)
  * [URLDecode](URLDecode.md)
  * [URLEncodedFormat](URLEncodedFormat.md)
  * [writeDump](writeDump.md)
  * [WriteLog](WriteLog.md)
  * [WriteOutput](WriteOutput.md)
