[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `URLDecode`

Decodes a URL-encoded string.

## Method Signature

```
URLDecode(string=[any], charset=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `any` | `true` | The URL-encoded string to decode. |  |
| `charset` | `string` | `false` | The charset to use when decoding the string. Defaults to UTF-8. | `UTF-8` |

## Examples

### Simple urlDecode() example

Shows how it takes an input of: %21 and returns: !

<a href="https://try.boxlang.io/?code=eJwrLcpxSU3OT0nVUFBSNTJUUtC05gIAQ8QFOg%3D%3D" target="_blank">Run Example</a>

```java
urlDecode( "%21" );

```

Result: !

### Basic urlDecode() usage

In this example we demonstrate taking a URL encoded message passed on the request context and displaying it decoded.


```java
if( len( rc.MSG ) ) {
	writeOutput( encodeForHTML( urlDecode( rc.MSG ) ) );
}

```


### urlDecode() in obfuscation

In this example we demonstrate url encoding a password before it is encrypted, and then decoding it after it is decrypted.

<a href="https://try.boxlang.io/?code=eJwrKE9RsFUoLcpxzUvOT0lNccsvyk0s0VBQUjG0UEmLU4nICUk1MVRS0LTmKi%2FKLEn1Ly0pKAXKFwD1qSkoKVgpgOUKwMak5iUXVRZAZHUUlMyjLPLT9NO9wwsKiyv0y8z8TSs9grwT84oiigssjZ1MKjw9wizNq9IsLAJtlYDqnXz8w908gz30nZ2c9QO8nYNNAxJTUjLz0kGSHq4RBF2RkpoMcQiQQV%2BHQG3G5hZg2LqkgsIWrgqHZqAwAG7SeBo%3D" target="_blank">Run Example</a>

```java
pwd = urlEncodedFormat( "$18$f^$XlTe41" );
writeOutput( pwd & " : " );
pwd = encrypt( pwd, "7Z8of/gKWpqsx/v6O5yHRKanrXsp93B4xIHV97zf88Q=", "BLOWFISH/CBC/PKCS5Padding", "HEX" );
writeOutput( pwd & " : " );
decpwd = decrypt( pwd, "7Z8of/gKWpqsx/v6O5yHRKanrXsp93B4xIHV97zf88Q=", "BLOWFISH/CBC/PKCS5Padding", "HEX" );
writeOutput( decpwd & " : " );
decpwd = urlDecode( decpwd );
writeOutput( decpwd );

```

Result: %2418%24f%5E%24XlTe41 : <some encrypted value> : %2418%24f%5E%24XlTe41 : $18$f^$XlTe41

### urlDecode() usage as a member function

In this example we demonstrate taking a URL encoded message passed on the request context and displaying it decoded using the urlDecode() member function.


```java
if( len( rc.MSG ) ) {
	writeOutput( encodeForHTML( rc.MSG.urlDecode() ) );
}

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLzUvOT0lNiS8uKcrMS1ewVVDKKCkpKFY1dlQ1cgOilNQyVSPXnNLk1FQgnV%2BUDhQrAeLy1Jzk%2FFygmEtJPpCAKnABK3czMjAzUbLmSinNLdBQCA3ycUkFWaKhkIpqmaaCpjWXgr6%2BAthKK319oG49sEl6QIv0S%2FShluiW5OuChXWBCvRBhnMBACK4OpY%3D" target="_blank">Run Example</a>

```java
encoded_string = "https%3A%2F%2Fdev%2Eboxlang%2Eorg%2Ft%2Fwelcome%2Dto%2Dboxlang%2Ddev%2F2064";
dump( URLDecode( encoded_string ) );

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
  * [Throw](./Throw.md)
  * [Trace](./Trace.md)
  * [URLEncodedFormat](./URLEncodedFormat.md)
  * [writeDump](./writeDump.md)
  * [WriteLog](./WriteLog.md)
  * [WriteOutput](./WriteOutput.md)
