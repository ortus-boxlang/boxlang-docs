[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CreateObject`

Creates a new object representation according to the {@code type} and {@code className} arguments.

<p>
 Available <strong>types</strong> are:
 <ul>
 <li><strong>class/component</strong> - Creates a new instance of a BoxLang class (Default if not used)</li>
 <li><strong>java</strong> - Creates a new instance of a Java class</li>
 <li><strong>{anything}</strong> - Passes the request to the {@code BoxEvent.ON_CREATEOBJECT_REQUEST} event for further processing</li>
 </ul>
 <p>
 If the type requested is not supported, then it passes to an interception call to the {@code BoxEvent.ON_CREATEOBJECT_REQUEST} event,
 so any listeners can contribute to the object creation request (if any). If there are no listeners, an exception is thrown.
 <p>
 You can also target an explicit class from a loaded BoxLang module by using the {@code @moduleName} suffix.
 Example: {@code createObject( 'class', 'class.name.path@module' )}
 <p>
 The <strong>properties</strong> is an optional argument that can be used to pass to the object creation process according to the type.
 <ul>
 <li><strong>class/component</strong> - The properties are not used</li>
 <li><strong>java</strong> - The properties can be a single or an array of absolute path(s) to a directory containing Jars/Classes, or absolute path(s) to specific Jars/Classes to classload</li>
 <li><strong>{anything}</strong> - The properties can be any object that the listener can use to create the object</li>
 </ul>
 <p>
 <strong>IMPORTANT:</strong> This does NOT create an instance of the class, for that you will need to call the {@code init()} method on the returned object.

## Method Signature

```
CreateObject(type=[string], className=[string], properties=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `false` | The type of object to create: java, class (component), or any other type | `class` |
| `className` | `string` | `false` | A fully qualified class name to create an instance of |  |
| `properties` | `any` | `false` | Depending on the type, this can be used to pass additional properties to the object creation process |  |

## Examples

### Create a BX / Component Instance

createObject Component


```java
<bx:script>
	tellTimeClass = createObject( "component", "appResources.components.tellTime" );
	tellTimeClass.getLocalTime();
</bx:script>

```


### Create a SOAP WebService Instance

createObject WebService


```java
<bx:script>
	ws = createObject( "webservice", "http://www.xmethods.net/sd/2001/TemperatureService.wsdl" );
	xlatstring = ws.getTemp( zipcode="55987" );
	writeOutput( "The temperature at 55987 is " & xlatstring );
</bx:script>
      
```


### Create a java class with specified bundle and version

createObject filesystem


```java
POIFSFileSystem = createObject( "java", "org.apache.poi.poifs.filesystem.POIFSFileSystem", "apache.poi", "3.11.0" );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLKc0t0FDISUxKzbFVci5KTSxJ9U%2FKSk0uUcjMU8hKLEtU0lEoSyyyTUaS0lBQgsqAab3SkswcPY%2FE4gzfxAIlBU0FTWuuFJzGlmeWZADNzizR0CTC6JzEvHS94JKizLx0p9K0tNQioPl6EN0gawDE8j51" target="_blank">Run Example</a>

```java
dump( label="CreateObject in java", var=createObject( "java", "java.util.HashMap" ) );
dump( label="CreateObject with init()", var=createObject( "java", "java.lang.StringBuffer" ).init() );

```


```java
dump( var=createObject( "class", "com.my.bx.class" ), expand=false );
// but even "class" is optional for bx
dump( var=createObject( "com.my.bx.class" ), expand=false );
// the modern new Object() syntax is also dynamic
dump( var=new "com.my.bx.class"(), expand=false );
dump( var=new com.my.bx.class(), expand=false );
myClass = "com.my.bx.class";
dump( var=new "#myClass#"(), expand=false );

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
  * [WriteOutput](./WriteOutput.md)
