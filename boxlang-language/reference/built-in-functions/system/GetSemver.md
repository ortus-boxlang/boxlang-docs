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

 var version = GetSemver().withMajor( 1 ).withMinor( 2 ).withPatch( 3 ).withPreRelease( "alpha" ).build();
 var versionString = GetSemver().withMajor( 1 ).withMinor( 2 ).withPatch( 3 ).withPreRelease( "alpha" ).build();
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
