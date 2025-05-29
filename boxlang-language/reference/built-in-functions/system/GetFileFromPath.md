[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetFileFromPath`

Extracts a filename from an absolute path.

## Method Signature

```
GetFileFromPath(path=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `path` | `string` | `true` | The absolute path to extract the filename from |  |

## Examples

### Basic Example



<a href="https://try.boxlang.io/?code=eJxLTy1xy8xJdSvKzw1ILMnQUFBytoopSc0tiEkDCuuVVJQoKWhacwEAF8wNFQ%3D%3D" target="_blank">Run Example</a>

```java
getFileFromPath( "C:\temp\file.txt" );

```

Result: file.txt

### Additional Examples

<a href="https://try.boxlang.io/?code=eJzLrYxPy8xJVbBVSE8tcQOy3IrycwMSSzI0FJRAEgVAZgyIoZdaUaKkoGnNlVKaW6ChkAvVBxRQ0NdXgKngAgBihRpe" target="_blank">Run Example</a>

```java
my_file = getFileFromPath( "filepath\file.ext" );
dump( my_file );
 // file.ext

```



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
  * [Trace](./Trace.md)
  * [GetBaseTagList](./GetBaseTagList.md)
  * [ObjectDeserialize](./ObjectDeserialize.md)
  * [DebugBoxContexts](./DebugBoxContexts.md)
  * [Dump](./Dump.md)
  * [writeDump](./writeDump.md)
  * [BoxUnregisterInterceptor](./BoxUnregisterInterceptor.md)
  * [CallStackGet](./CallStackGet.md)
