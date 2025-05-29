[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetFunctionCalledName`

Get the name of the function that is being called.

If no function is being called, an empty string is returned.

## Method Signature

```
GetFunctionCalledName()
```

### Arguments

This function does not accept any arguments

## Examples

### getFunctionCalledName Basic Example

Show results of calling a function directly versus by reference

<a href="https://try.boxlang.io/?code=eJydjrEOgjAQhmf7FBdYYHJxkspi4qiLL3CWA5rUlpQrDMZ3V1A0Jp0c77%2Fv%2F%2FKLwekK6mAVa2cBFQc0h%2Fd5xCtlOdzEavSa6RS4C5xBEqVG7EGhMVQB9ltIG%2BKF2M%2Fxi0vlxZcJ5IW4i1%2BrbH0p20050do20S1y%2FQTmduxb%2FGGEQSN4qsmTVfT1f6KzWwqwixii5DTlAWJed%2FI%3D" target="_blank">Run Example</a>

```java

void function actualFunctionName() {
	writeOutput( "actualFunctionName() was called as: #getFunctionCalledName()#<br>" );
}
writeOutput( "<hr><h4>Calling actualFunctionName()</h4>" );
actualFunctionName();
writeOutput( "<hr><h4>Calling actualFunctionName() via reference</h4>" );
referenceToFunction = actualFunctionName;
referenceToFunction();

```


### Getters and Setters Example

Example of using getFunctionCalledName to create dynamic getters and setters


```java
//callednamedemo.bx
component
{
    variables.x1 = 1;
    variables.y1 = 2;

    function init() {
        return this;
    }

    function get() {
        var name = getFunctionCalledName();
        return variables[mid(name,4,len(name)-3)];
    }

    function set(value) {
        var name = getFunctionCalledName();
        variables[mid(name,4,len(name)-3)] = value;
    }

    this.getX1 = get;
    this.getY1 = get;
    this.setX1 = set;
    this.setY1 = set;
}

<!--- calledname.bxm --->

<bx:script>

	function test() {
		return getFunctionCalledName();
	}
	writeOutput( test() & "<br>" ); // test
	a = test;
	writeOutput( variables.a() & "<br>" ); // a
	o = new callednamedemo();
	// shows *real* methods get(), SetX1() and getY1(), etc.
	writeDump( o );
	o.setX1( 10 );
	o.setY1( 20 );
	writeOutput( o.getX1() & "<br>" ); // 10
	writeOutput( o.getY1() & "<br>" );
</bx:script>
 <!--- 20 --->
```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJxljs0KwjAQhM%2FNUww5pSD0AUIEETz6Dmua1kJ%2BSn%2BUIL67SVpB8LTszDc7G421UBA4%2BQhPzqCGOuLFKqPvQeySZFW7ulHgQZPqzXJZvV6G4M9krWmviRH1AZZuxir%2BNfGkGboQoJnnK2%2FJYioU4HkUaaaY%2BvMq0TTQYYzo9gvZTGxGuik4lEDcPk7ifwDU0%2BB%2FO7Zggkv2A8H8Sts%3D" target="_blank">Run Example</a>

```java
yell = ( Any name ) => {
	echo( name );
	dump( var=getFunctionCalledName(), label="Function was called as" );
};
yell( "yell" );
say = yell; // copy function
say( "say from " );
yell = say; // copy function again
yell( "yell from say" );

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
