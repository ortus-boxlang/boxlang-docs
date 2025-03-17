# CreateObject

Creates a new object representation according to the {@code type} and {@code className} arguments.

Available **types** are:

* **class/component** - Creates a new instance of a BoxLang class (Default if not used)
* **java** - Creates a new instance of a Java class
* **{anything}** - Passes the request to the {@code BoxEvent.ON\_CREATEOBJECT\_REQUEST} event for further processing

If the type requested is not supported, then it passes to an interception call to the {@code BoxEvent.ON\_CREATEOBJECT\_REQUEST} event, so any listeners can contribute to the object creation request (if any). If there are no listeners, an exception is thrown.

You can also target an explicit class from a loaded BoxLang module by using the {@code @moduleName} suffix. Example: {@code createObject( 'class', 'class.name.path@module' )}

The **properties** is an optional argument that can be used to pass to the object creation process according to the type.

* **class/component** - The properties are not used
* **java** - The properties can be a single or an array of absolute path(s) to a directory containing Jars/Classes, or absolute path(s) to specific Jars/Classes to classload
* **{anything}** - The properties can be any object that the listener can use to create the object

**IMPORTANT:** This does NOT create an instance of the class, for that you will need to call the {@code init()} method on the returned object.

## Method Signature

```
CreateObject(type=[string], className=[string], properties=[any])
```

### Arguments

| Argument     | Type     | Required | Description                                                                                          | Default |
| ------------ | -------- | -------- | ---------------------------------------------------------------------------------------------------- | ------- |
| `type`       | `string` | `false`  | The type of object to create: java, class (component), or any other type                             | `class` |
| `className`  | `string` | `false`  | A fully qualified class name to create an instance of                                                |         |
| `properties` | `any`    | `false`  | Depending on the type, this can be used to pass additional properties to the object creation process |         |

## Examples

## Related

* [ApplicationRestart](ApplicationRestart.md)
* [ApplicationStartTime](ApplicationStartTime.md)
* [ApplicationStop](ApplicationStop.md)
* [BoxAnnounce](BoxAnnounce.md)
* [BoxAnnounceAsync](BoxAnnounceAsync.md)
* [BoxRegisterInterceptionPoints](BoxRegisterInterceptionPoints.md)
* [BoxRegisterInterceptor](BoxRegisterInterceptor.md)
* [BoxRegisterRequestInterceptor](BoxRegisterRequestInterceptor.md)
* [CallStackGet](CallStackGet.md)
* [CreateGUID](CreateGUID.md)
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
