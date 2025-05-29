[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetApplicationMetadata`

Print a message with line break to the console

## Method Signature

```
GetApplicationMetadata()
```

### Arguments

This function does not accept any arguments

## Examples

### Simple Example

Prints the statements using application meta data.

<a href="https://try.boxlang.io/?code=eJx9j8tugzAQRfd8xciLCjZh36e8cKosDJUgHzCBCYyEHYQH9feL2%2BZBpHYzkud47tHNc9iSND3gOA7coPDJgyNBaFEwiQNeoCPRV24XHEGaPSV5Dh8Te1nde3SUfE4sVM4yzpKC0ncYOICCB0hj0KbQ1mwG8p30aQZvcFnCI6jZh5EaPjK1KltO1PNhelVwKw8UQkwWdnSa5c5drelZ%2FS2pTFXtyqLeWVPu6%2F%2FTHXrsyJH%2FS3D9sK73K7G60O%2FGmqJeKiryeBiWSrFiy%2BHnkUXxFylogwQ%3D" target="_blank">Run Example</a>

```java
// Fetch application meta data
data = getApplicationMetadata();
// Print application name
writeOutput( "Application name is " & (data.NAME.length() ? data.NAME : "unspecified") & "<br>" );
// Print session timeout
writeOutput( "Session timeout is " & data.SESSIONTIMEOUT & "<br>" );
// Print session management
writeOutput( "Session management is " & (data.SESSIONMANAGEMENT ? "enabled" : "disabled") );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJzLTS1JVLBVSE8tcSwoyMlMTizJzM%2FzBQq6JJYkamhac6WU5hZoKOSClAF5AI%2FJD6M%3D" target="_blank">Run Example</a>

```java
meta = getApplicationMetaData();
dump( meta );

```



## Related

  * [Throw](./Throw.md)
  * [GetBaseTemplatePath](./GetBaseTemplatePath.md)
  * [Duplicate](./Duplicate.md)
  * [WriteLog](./WriteLog.md)
  * [BoxAnnounceAsync](./BoxAnnounceAsync.md)
  * [SessionRotate](./SessionRotate.md)
  * [IsInstanceOf](./IsInstanceOf.md)
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
  * [GetFileFromPath](./GetFileFromPath.md)
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
