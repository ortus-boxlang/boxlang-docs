[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Invoke`

Invokes an object method and returns the result of the invoked method.

## Method Signature

```
Invoke(object=[any], method=[string], arguments=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `object` | `any` | `true` |  |  |
| `method` | `string` | `false` | The name of the method to invoke |  |
| `arguments` | `any` | `false` | An array of positional arguments or a struct of named arguments to pass into the method. |  |

## Examples

### Invoke a Java Method

Invokes the size method on a new HashMap object, which should return 0


```java
invoke( createObject( "java", "java.util.HashMap" ), "size" );

```

Result: 0

### Invoke a method on a component

Invokes the method named 'test' on the component Test.bx with one parameter


```java
obj = createObject( "component", "Test" );
invoke( obj, "test", {
	PARAMETER : "Test Data"
} );

```


### Invoke a method on a webservice with one argument

Invokes the method named 'test' on the webservice Test.bx with one argument


```java
obj = createObject( "webservice", "https://example.com/test.bx?wsdl" );
invoke( obj, "test", {
	ARGUMENT1 : "Test Data"
} );

```


### Invoke a method on a webservice with multiple arguments

Invokes the method named 'test' on the webservice Test.bx with multiple arguments


```java
obj = createObject( "webservice", "https://example.com/test.bx?wsdl" );
invoke( obj, "test", {
	ARGUMENT1 : "Test Data",
	ARGUMENT2 : "More Data",
	ARGUMENT3 : "Still More Data"
} );

```


### Additional Examples


```java
<bx:script>
	writeDump( label="structure with invoke()", var=invoke( variables, "myStruct", {
		A : "First"
	} ) );

	private function myStruct() {
		return "myStruct:" & JSONSerialize( arguments );
	}
	writeDump( label="Adding numbers with invoke()", var=invoke( variables, "calc", {
		A : 3,
		B : 2
	} ) );

	private function calc( numeric a, numeric b ) {
		return a + b;
	}
</bx:script>

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
