[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `EncodeForHTML`

Encodes the input string for safe output in the body of a HTML tag.

The encoding in meant to mitigate Cross Site Scripting (XSS) attacks. This
 function can provide more protection from XSS than the HTMLEditFormat or XMLFormat functions do.

## Method Signature

```
EncodeForHTML(string=[string], canonicalize=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The string to encode. |  |
| `canonicalize` | `boolean` | `true` | If set to true, canonicalization happens before encoding. If set to false, the given input string will just be encoded. | `false` |

## Examples

### Escapes the HTML characters



<a href="https://try.boxlang.io/?code=eJw1ikEOgkAQBO%2B%2BopcD0TdAvMmZgx8YZOJOWHaTnRZ9PmhiUqeqilzTbTYOpa7CM5p7NMeBgOpEC%2F5FLoxa0f8O6odfa%2FkIz6SYqjwWpV8xVt2svBzJsuItjilJXkIIDS7daQf35Ca6" target="_blank">Run Example</a>

```java
htmlEditFormat( "This is a test & this is another <This text is in angle brackets> Previous line was blank!!!" );

```

Result: This is a test &amp; this is another &lt;This text is in angle brackets&gt; Previous line was blank!!!

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrSS0uCS4pysxLV7BVUPJIzcnJV1BUVOSyCcnILFYoSa0oUQDSmXnFmSmpCvlpCol56TmpCklFicnZqSXFdlwoyvJLS7CrAxmpZM1VXpRZkgpUVFBaogHUBLdZE01KySbD1M4jxNfHNSWzxC2%2FKDexxEYfKKSkoKaAKoxqDMggADvORjk%3D" target="_blank">Run Example</a>

```java
testString = "Hello !!!
<This text is inside of angle brackets>
This text is outside of angle brackets !!!";
writeoutput( testString );
writeoutput( "<h5>HTMLEditFormat</h5>" & HTMLEditFormat( testString ) );

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
  * [Throw](./Throw.md)
  * [Trace](./Trace.md)
  * [URLDecode](./URLDecode.md)
  * [URLEncodedFormat](./URLEncodedFormat.md)
  * [writeDump](./writeDump.md)
  * [WriteLog](./WriteLog.md)
  * [WriteOutput](./WriteOutput.md)
