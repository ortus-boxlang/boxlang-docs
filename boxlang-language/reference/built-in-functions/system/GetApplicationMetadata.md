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

  * [ApplicationRestart](./ApplicationRestart.md)
  * [ApplicationStartTime](./ApplicationStartTime.md)
  * [ApplicationStop](./ApplicationStop.md)
  * [BoxAnnounce](./BoxAnnounce.md)
  * [BoxAnnounceAsync](./BoxAnnounceAsync.md)
  * [BoxModuleReload](./BoxModuleReload.md)
  * [BoxRegisterInterceptionPoints](./BoxRegisterInterceptionPoints.md)
  * [BoxRegisterInterceptor](./BoxRegisterInterceptor.md)
  * [BoxRegisterRequestInterceptor](./BoxRegisterRequestInterceptor.md)
  * [BoxUnregisterInterceptor](./BoxUnregisterInterceptor.md)
  * [BoxUnregisterRequestInterceptor](./BoxUnregisterRequestInterceptor.md)
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
  * [WriteLog](./WriteLog.md)
  * [WriteOutput](./WriteOutput.md)
