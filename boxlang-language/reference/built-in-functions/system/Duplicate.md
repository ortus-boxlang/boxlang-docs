[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Duplicate`

Duplicates an object - either shallow or deep

## Method Signature

```
Duplicate(object=[any], deep=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `object` | `any` | `true` | Any object to duplicate |  |
| `deep` | `boolean` | `false` | Whether to deep copy the object or make a shallow copy (e.g. only the top level keys in a struct) | `true` |

## Examples

### Changing a struct compared to changing its copy

`myNewStruct` holds a reference to `myStruct` so if you change `myNewStruct`, `myStruct` is changed accordingly as well, because they are the same struct just assigned to two variables.
In comparison `myOtherNewStruct` is a copy so if you change `myOtherNewStruct`, `myStruct` stays untouched because with the duplicate, a new, unique structure with the same key-value pairs is created thus they do not share the same reference

<a href="https://try.boxlang.io/?code=eJzLrQwuKSpNLlGwVahW4OJUSsvPV1KwUlDyyS9KzVXILCguzVXSAYonJRaBxZMSq5S4aq25civ9UsvhWnOhpoDE%2FUsyUouQJVNKC3IykxNLUjXg6hQ0UUzQc%2FP3BypUSszITS1RKC7NU8I0CKYmJT8nv0ihOLMEqKa8KLMk1b%2B0pKC0BGE2WKGagpLCo7ZJQFJNAd0iVDkstgAdBwDc31vf" target="_blank">Run Example</a>

```java
myStruct = { 
	"foo" : "Lorem ipsum",
	"bar" : "baz"
};
myNewStruct = myStruct;
myOtherNewStruct = duplicate( myStruct );
myNewStruct.FOO = "ahmet sun";
myOtherNewStruct.FOO = "dolor sit";
writeOutput( myStruct.FOO & " → " & myNewStruct.FOO & " → " & myOtherNewStruct.FOO );

```

Result: ahmet sun → ahmet sun → dolor sit

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrSC0qzs9TsFWoVuDidPMMCg5RsFJQckpMSlXS4eL0cYTwg0pLMpS4aq25UkpzCzQUCiCaNK0V9PUVQGoVQAq4knPy81KBRqWUFuRkJieWpCKphOqEKEHXCFGlB7bNVkEpODcTaB1uy8DyaAZyoZoIAKLOP%2BU%3D" target="_blank">Run Example</a>

```java
person = { 
	FIRST : "Babe",
	LAST : "Ruth"
};
dump( person ); // Babe Ruth
clone = duplicate( person );
dump( clone ); // Babe Ruth
person.LAST = "Smith";
dump( person ); // Babe Smith
dump( clone );
 // Babe Ruth

```



## Related

  * [Throw](./Throw.md)
  * [GetBaseTemplatePath](./GetBaseTemplatePath.md)
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
