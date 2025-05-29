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
