[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetSemver`

Parses and returns a Semver object version of the passed version string or if you do not pass
 in a version, we will return to you a Semver builder {@link Semver#of()} object, so you can programmaticaly build
 a version object.

<p>
 Semver is a tool that provides useful methods to manipulate versions that follow the "semantic versioning"
 specification (see <a href="http://semver.org">semver.org</a> and <a href="https://github.com/semver4j/semver4j">github</a>).
 <p>
 Some of the methods provided by Semver are:
 <ul>
 <li>{@link Semver#compareTo(Semver)}: Compares two versions and returns -1, 0, or 1 if the first version is less than,
 equal to, or greater than the second version, respectively.</li>
 <li>{@link Semver#satisfies(String)}: Checks if the version satisfies the given range.</li>
 <li>{@link Semver#isValid(String)}: Checks if the version is valid.</li>
 <li>{@link Semver#nextMajor()}: Increments the major version.</li>
 <li>{@link Semver#nextMinor()}: Increments the minor version.</li>
 <li>{@link Semver#nextPatch()}: Increments the patch version.</li>
 <li>{@link Semver#withBuild(String)}: Set the build version.</li>
 <li>{@link Semver#withPreRelease(String)}: Set the pre-release version.</li>
 <li>{@link Semver#isStable()}: Checks if the version is stable.</li>
 </ul>
 <p>
 Here are some examples of how to parse and manipulate versions using Semver:

 <pre>

 var version = GetSemver( "1.2.3-alpha+20151212" );
 var version = GetSemver( "1.2.3-alpha" );
 var version = GetSemver( "1.2.3" );
 var version = GetSemver( "1.2.3+20151212" );
 var version = GetSemver( "1.2.3-alpha.1" );
 var version = GetSemver( "1.2.3-alpha.beta" );
 </pre>

 Here are some examples of comparing versions using Semver:

 <pre>
 var version1 = GetSemver( "1.2.3" );
 var version2 = GetSemver( "1.2.4" );
 var version3 = GetSemver( "1.3.0" );

 version1.compare( version2 ); // -1
 version1.compare( version3 ); // -1
 version2.compare( version3 ); // -1
 </pre>

 <p>
 To use the builder you can do something like this:

 <pre>

 var version = GetSemver().withMajor( 1 ).withMinor( 2 ).withPatch( 3 ).withPreRelease( "alpha" ).toSemver();
 var versionString = GetSemver().withMajor( 1 ).withMinor( 2 ).withPatch( 3 ).withPreRelease( "alpha" ).toString();
 </pre>

## Method Signature

```
GetSemver(version=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `version` | `string` | `false` | The version string to parse. |  |

## Examples



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
