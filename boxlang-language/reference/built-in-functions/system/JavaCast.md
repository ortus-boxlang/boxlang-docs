[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `JavaCast`

Cast a variable to a specified Java type

## Method Signature

```
JavaCast(type=[string], variable=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `true` | The name of a Java primitive or a Java class name. |  |
| `variable` | `any` | `true` | The variable, Java object, or array to cast. |  |

## Examples

### Convert a Boxlang Number to a Java double primitive

Converts the number 180.0 degrees to radians using Java method: Math.toRadians(double degrees)

<a href="https://try.boxlang.io/?code=eJxLLkpNLEn1T8pKTS7RUFDKSixLVNKB0Ho5iXnper6JJRlKCpp6JflBiSmZiXnFGgogSefEYpD6lPzSpJxUoA5DCwM9AwVNBU1rLgCAgBlm" target="_blank">Run Example</a>

```java
createObject( "java", "java.lang.Math" ).toRadians( javaCast( "double", 180.0 ) );

```

Result: 3.141592653589793

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxNjsEKgzAMQO9%2BRfCkMKq7je244WGwDfYH0Qat2Fba1P3%2BWipj5JCQ5L2kaeBqzUaOAWO1yC54ZQ08g%2B7JAdvYvuOGIG3oF4LVKa1YbVQ0P9IDTwQmE8dTK1qQNDoin3iHUqHxEL1mzC5NPFl5hgfyJNi%2B80a1n9jZuvg4xXQLeq1gcIRMr36mgSso52gpDzmLBc0okqqE%2Bs8GaTigT%2FvZHIn8XZ3iUnwBDBpUJw%3D%3D" target="_blank">Run Example</a>

```java
// Convert a Boxlang Number to a Java double primitive
// Converts the number 180.0 degrees to radians using Java method: Math.toRadians(double degrees)
writeDump( createObject( "java", "java.lang.Math" ).toRadians( javacast( "double", 180.0 ) ) );

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
  * [GetFileFromPath](./GetFileFromPath.md)
  * [EncodeForHTML](./EncodeForHTML.md)
  * [htmlEditFormat](./htmlEditFormat.md)
  * [GetClassMetadata](./GetClassMetadata.md)
  * [SystemOutput](./SystemOutput.md)
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
