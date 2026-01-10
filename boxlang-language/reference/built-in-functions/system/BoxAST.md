[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BoxAST`

Generates the Abstract Syntax Tree (AST) for BoxLang source code or a file.

The AST represents the syntactic structure of the code and can be used for
 code analysis, transformation, or generation.

 <p>
 <strong>Usage Examples:</strong>
 </p>

 <pre>
 // Parse source code and return as struct (default)
 ast = boxAST( source = "x = 1 + 2" );
 println( ast.ASTType ); // Outputs: BoxAssignment

 // Parse source code and return as JSON
 json = boxAST( source = "function add(a, b) { return a + b; }", returnType = "json" );
 println( json ); // Outputs: JSON representation of the AST

 // Parse source code and return as text
 text = boxAST( source = "if (x > 5) { println('yes'); }", returnType = "text" );
 println( text ); // Outputs: Human-readable text representation

 // Parse a file
 ast = boxAST( filepath = "src/MyClass.bx" );

 // Use as a member function on a string
 source = "a = [1, 2, 3]";
 ast = source.toAST(); // Returns AST as struct
 ast = source.toAST( returnType = "json" ); // Returns AST as JSON string

 // Parse CFML/ColdFusion syntax
 ast = boxAST( source = "cfset x = 1", sourceType = "cfscript" );

 // Parse template syntax
 ast = boxAST( source = "<bx:output>#now()#</bx:output>", sourceType = "template" );
 </pre>

 <p>
 The returned AST structure contains nodes with the following key properties:
 </p>
 <ul>
 <li><strong>ASTType</strong> - The type of AST node (e.g., BoxAssignment, BoxFunctionDeclaration, BoxClass)</li>
 <li><strong>ASTPackage</strong> - The package name of the AST node class</li>
 <li>Additional properties specific to each node type (e.g., name, value, children, etc.)</li>
 </ul>

## Method Signature

```
BoxAST(source=[string], filepath=[string], returnType=[string], sourceType=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `source` | `string` | `false` | The BoxLang source code to parse. Either source or filepath must be provided.<br>                  When used as a member function, this is automatically set to the string value. |  |
| `filepath` | `string` | `false` | The path to a BoxLang file to parse. Either source or filepath must be provided.<br>                    Can be relative (to the current working directory) or absolute. |  |
| `returnType` | `string` | `false` | The format of the returned AST. Valid values are "struct" (default), "json", or "text".<br>                      <ul><br>                      <li><strong>struct</strong> - Returns a nested structure (Map) representing the AST hierarchy</li><br>                      <li><strong>json</strong> - Returns a JSON string representation of the AST</li><br>                      <li><strong>text</strong> - Returns a human-readable text representation of the AST</li><br>                      </ul> | `struct` |
| `sourceType` | `string` | `false` | The type of source code being parsed. Valid values are "script" (default), "template", "cfscript", or "cftemplate".<br>                      <ul><br>                      <li><strong>script</strong> - BoxLang script syntax (BOXSCRIPT)</li><br>                      <li><strong>template</strong> - BoxLang template syntax (BOXTEMPLATE)</li><br>                      <li><strong>cfscript</strong> - ColdFusion script syntax (CFSCRIPT)</li><br>                      <li><strong>cftemplate</strong> - ColdFusion template syntax (CFTEMPLATE)</li><br>                      </ul> | `script` |

## Examples



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
