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

  * [Throw](./Throw.md)
  * [GetBaseTemplatePath](./GetBaseTemplatePath.md)
  * [Duplicate](./Duplicate.md)
  * [WriteLog](./WriteLog.md)
  * [BoxAnnounceAsync](./BoxAnnounceAsync.md)
  * [SessionRotate](./SessionRotate.md)
  * [IsInstanceOf](./IsInstanceOf.md)
  * [GetApplicationMetadata](./GetApplicationMetadata.md)
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
