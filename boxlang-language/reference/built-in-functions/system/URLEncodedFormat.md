[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `URLEncodedFormat`

Generates a URL-encoded string.

For example, it replaces spaces with `%20`, and non-alphanumeric characters with equivalent hexadecimal escape
 sequences. Passes arbitrary strings within a URL.

## Method Signature

```
URLEncodedFormat(string=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `any` | `true` | String to encode for usage within a URL. |  |

## Examples

### Simple urlEncodedFormat Example

It returns url encoded string.

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQCA3ycc1Lzk9JTXHLL8pNBIoohWRkFisAUaJCcUlRZl66QnlmSYZCcUFqcmZijkJyRmJRYnJJapGekoKmgqY1FwB4fhsa" target="_blank">Run Example</a>

```java
writeOutput( URLEncodedFormat( "This is a string with special character." ) );

```

Result: This%20is%20string%20with%20special%20character%2E

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxFjcsKwjAQRff5iqEQaBfpSBQXFhdCm5UrwbVIEmqhbUo60d93DAVhHnA5nJvi%2BFgpDnMPZyheRMt6QnT%2BXY%2FJel%2BH2CPhx482TF5RUDlWDKDeHQ9FI1yalhLut2s32%2BC8MyFOTyoh%2Fc0VVI0ARMh%2Bub9IbXhYInWXhfy5iTPi3dqkbinw2YA24%2BbXKr7VkDpv" target="_blank">Run Example</a>

```java
url_string = "https://dev.boxlang.org/t/welcome-to-boxlang-dev/2064";
dump( URLEncodedFormat( url_string ) );
 // https%3A%2F%2Fdev%2Eboxlang%2Eorg%2Ft%2Fwelcome%2Dto%2Dboxlang%2Ddev%2F2064

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
  * [URLDecode](./URLDecode.md)
  * [writeDump](./writeDump.md)
  * [WriteLog](./WriteLog.md)
  * [WriteOutput](./WriteOutput.md)
