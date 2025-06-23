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
  * [URLEncodedFormat](./URLEncodedFormat.md)
  * [writeDump](./writeDump.md)
  * [WriteLog](./WriteLog.md)
  * [WriteOutput](./WriteOutput.md)
