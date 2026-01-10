[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `WriteOutput`

Print a message with line break to the buffer

## Method Signature

```
WriteOutput(message=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `message` | `any` | `true` | The message to print |  |

## Examples

### Output the literal string "Hello World"



<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQUPJIzcnJVwjPL8pJUVLQtOYCAKyDbxm%3D" target="_blank">Run Example</a>

```java
writeOutput( "Hello World" );

```


### Output the equivalent string as a variable



<a href="https://try.boxlang.io/?code=eJxLL0pNLcnMS1ewVVDySM3JyVcIzy%2FKSVGy5iovyixJ9S8tKSgt0VBIhynTtOYCAM6DEV8%3D" target="_blank">Run Example</a>

```java
greeting = "Hello World";
writeOutput( greeting );

```


### Using the encodeFor argument

CF2016+ Passing in `html` to the `encodeFor` argument wraps the result with a call to encodeForHTML.

<a href="https://try.boxlang.io/?code=eJzLS8xNVbBVUApILUlVsuYqL8osSfUvLSkoLdFQUPJIzcnJV1BSUFPIAyrTUVDKKMnNUVLQtOYCAOVaEGw%3D" target="_blank">Run Example</a>

```java
name = "Pete";
writeOutput( "Hello " & name, "html" );

```

Result: Hello Pete

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxVUEFOxDAMvPMKqwcEB9o72620dyQOIK6rbOo2hjQOjtNqeT0JixZx9IxnPGOniz9GI2YWEx3soenj8OoQnrJFhCj8jlaBEngc4XQGvXKHlNiSUeJwG04p7l420i8Ub8IIBgKHhyKfSC9sb8AJTvumcaoxPXYdhnajD4o4kmlZ5q5OXXFJ6fiGghSaZkh1BPN3q%2B%2FM0MIBZuGNwnyNuDmyrga1vCykWuIq%2F8RN2VosJjwB6YXPgfRc64zoaUWpRp%2FZ%2BIomnnQzgvDbI4vmunCpUcGUY2TRIgQMKwmHBYPCxFL8VvQcUVK9PmN5XVjZrzi2fReHZnezCSk%2BZ41Z78D9f%2F%2F97uYbebiSmQ%3D%3D" target="_blank">Run Example</a>

```java
html_paragraph = "<p>The Boxlang project is led by the Boxlang Association&nbsp;Switzerland a non-profit&nbsp;<a href=""https://en.wikipedia.org/wiki/Swiss_Verein"">swiss association</a>. A growing project which is committed to the success of its community by delivering quality software and a nurturing&nbsp;and supportive environment for developers to get involved.</p>";
writeOutput( html_paragraph );

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
  * [URLEncodedFormat](./URLEncodedFormat.md)
  * [writeDump](./writeDump.md)
  * [WriteLog](./WriteLog.md)
