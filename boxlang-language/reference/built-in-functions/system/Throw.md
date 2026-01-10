[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Throw`

Throws a developer-specified exception, which can be caught with a catch block.

## Method Signature

```
Throw(message=[any], type=[String], detail=[String], errorcode=[String], extendedinfo=[any], object=[Throwable])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `message` | `any` | `false` | Message that describes exception event |  |
| `type` | `String` | `false` | The type of the exception |  |
| `detail` | `String` | `false` | Description of the event |  |
| `errorcode` | `String` | `false` | A custom error code that you supply |  |
| `extendedinfo` | `any` | `false` | Additional custom error data that you supply |  |
| `object` | `Throwable` | `false` | An instance of an exception object. If there is no message provided, this object will be thrown directly. If there is a message, a<br>                  CustomException will be thrown and this object will be used as the cause. |  |

## Examples

### Throw a custom exception

Use the throw function to throw a custom application exception.


```java
<bx:script>
	throw( type="MyCustomError", message="A custom error has been thrown!" );
</bx:script>

```


### Throw a custom http response exception

Use the throw function to throw a custom exception when the http response is invalid.


```java
if( !isJSON( httpResponse.FILECONTENT ) ) {
	throw( type="InvalidHTTPResponse", message="The http response was not valid JSON" );
}

```


### Additional Examples


```java
// thrown as a statement example
try {
	throw "thrown";
} catch ( e) {
	dump( var=bxcatch, label="single argument keyword" );
}

try {
	throw message = "thrown";
	detail = "deets";
	errorCode = "403";
	type = "Test";
} catch ( e) {
	dump( var=bxcatch, label="additional arguments are ignored" );
}
// use this syntax instead
try {
	throw( message="thrown", detail="deets", errorCode="403", type="Test" );
} catch ( e) {
	dump( var=bxcatch, label="script throw with arguments" );
}

```



## Related

  * [ApplicationRestart](./ApplicationRestart.md)
  * [ApplicationStartTime](./ApplicationStartTime.md)
  * [ApplicationStop](./ApplicationStop.md)
  * [BoxAnnounce](./BoxAnnounce.md)
  * [BoxAnnounceAsync](./BoxAnnounceAsync.md)
  * [BoxAST](./BoxAST.md)
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
  * [GetApplicationMetadata](./GetApplicationMetadata.md)
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
  * [Trace](./Trace.md)
  * [URLDecode](./URLDecode.md)
  * [URLEncodedFormat](./URLEncodedFormat.md)
  * [writeDump](./writeDump.md)
  * [WriteLog](./WriteLog.md)
  * [WriteOutput](./WriteOutput.md)
