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
