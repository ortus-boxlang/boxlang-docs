# CallStackGet

Returns an array of structs by default of the current tag context.

Each struct contains template name, line number, and function name (if applicable).\
This is a snapshot of all function calls or invocations.

## Method Signature

```
CallStackGet(maxFrames=[integer])
```

### Arguments

| Argument    | Type      | Required | Description | Default |
| ----------- | --------- | -------- | ----------- | ------- |
| `maxFrames` | `integer` | `false`  |             | `-1`    |

## Examples

### Tag Syntax

This example the factorial of a number is computed.

```java
<!--- callfact.bxm --->
<bx:try>
    <bx:include template="fact.bxm">

<bx:catch type="any">
    <bx:output>
        #bxcatch.MESSAGE#
        <br>#bxcatch.DETAIL#<br>
    </bx:output>
</bx:catch></bx:try>
```

### Script Syntax

This example the factorial of a number is computed.

```java
<!--- fact.bxm --->
<bx:script>

	numeric function factorial( Any n ) {
		if( n == 1 ) {
			writeDump( callStackGet() );
			writeOutput( "<br>" );
			return 1;
		}
		 else {
			writeDump( callStackGet() );
			writeOutput( "<br>" );
			return n * factorial( n - 1 );
		}
	}
	factorial( 5 );
</bx:script>

```

### Additional Examples

```java
dump( var=CallStackGet( type="json" ), label="json " );
dump( var=CallStackGet( type="json", offset=2 ), label="json with offset" );
dump( var=CallStackGet( type="json", maxframes=2 ), label="json with maxFrames" );
dump( var=CallStackGet( "string" ), label="string" );
dump( var=CallStackGet( "array" ), label="array" );
dump( var=CallStackGet( "html" ), label="html" );

```

## Related

* [ApplicationRestart](ApplicationRestart.md)
* [ApplicationStartTime](ApplicationStartTime.md)
* [ApplicationStop](ApplicationStop.md)
* [BoxAnnounce](BoxAnnounce.md)
* [BoxAnnounceAsync](BoxAnnounceAsync.md)
* [BoxModuleReload](BoxModuleReload.md)
* [BoxRegisterInterceptionPoints](BoxRegisterInterceptionPoints.md)
* [BoxRegisterInterceptor](BoxRegisterInterceptor.md)
* [BoxRegisterRequestInterceptor](BoxRegisterRequestInterceptor.md)
* [BoxUnregisterInterceptor](BoxUnregisterInterceptor.md)
* [BoxUnregisterRequestInterceptor](BoxUnregisterRequestInterceptor.md)
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
* [GetBaseTagData](GetBaseTagData.md)
* [GetBaseTagList](GetBaseTagList.md)
* [GetBaseTemplatePath](GetBaseTemplatePath.md)
* [GetBoxContext](GetBoxContext.md)
* [GetBoxRuntime](GetBoxRuntime.md)
* [GetBoxVersionInfo](GetBoxVersionInfo.md)
* [GetClassMetadata](GetClassMetadata.md)
* [GetComponentList](GetComponentList.md)
* [GetContextRoot](GetContextRoot.md)
* [GetCurrentTemplatePath](GetCurrentTemplatePath.md)
* [GetFileFromPath](GetFileFromPath.md)
* [GetFunctionCalledName](GetFunctionCalledName.md)
* [GetFunctionList](GetFunctionList.md)
* [GetModuleInfo](GetModuleInfo.md)
* [GetModuleList](GetModuleList.md)
* [GetRequestClassLoader](GetRequestClassLoader.md)
* [GetSemver](GetSemver.md)
* [GetSystemSetting](GetSystemSetting.md)
* [GetTempDirectory](GetTempDirectory.md)
* [GetTickCount](GetTickCount.md)
* [htmlEditFormat](htmlEditFormat.md)
* [IIF](IIF.md)
* [Invoke](Invoke.md)
* [IsInstanceOf](IsInstanceOf.md)
* [JavaCast](JavaCast.md)
* [ObjectDeserialize](ObjectDeserialize.md)
* [ObjectSerialize](ObjectSerialize.md)
* [PagePoolClear](PagePoolClear.md)
* [Print](Print.md)
* [Println](Println.md)
* [RunThreadInContext](RunThreadInContext.md)
* [SessionInvalidate](SessionInvalidate.md)
* [SessionRotate](SessionRotate.md)
* [SessionStartTime](SessionStartTime.md)
* [Sleep](Sleep.md)
* [SystemCacheClear](SystemCacheClear.md)
* [SystemExecute](SystemExecute.md)
* [SystemOutput](SystemOutput.md)
* [Throw](Throw.md)
* [Trace](Trace.md)
* [URLDecode](URLDecode.md)
* [URLEncodedFormat](URLEncodedFormat.md)
* [writeDump](writeDump.md)
* [WriteLog](WriteLog.md)
* [WriteOutput](WriteOutput.md)
