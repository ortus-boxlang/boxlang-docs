[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `String`



## String Methods

<details>
<summary><code>toAST(filepath=[string], returnType=[string], sourceType=[string])</code></summary>

Generates the Abstract Syntax Tree (AST) for BoxLang source code or a file.

The AST represents the syntactic structure of the code and can be used for
 code analysis, transformation, or generation.

 ,<p>,
 ,<strong>,Usage Examples:,</strong>,
 ,</p>,

 ,<pre>,
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
 ast = boxAST( source = ",<,bx:output>#now()#,<,/bx:output>", sourceType = "template" );
 ,</pre>,

 ,<p>,
 The returned AST structure contains nodes with the following key properties:
 ,</p>,
 ,<ul>,
 ,<li>,<strong>,ASTType,</strong>, - The type of AST node (e.g., BoxAssignment, BoxFunctionDeclaration, BoxClass),</li>,
 ,<li>,<strong>,ASTPackage,</strong>, - The package name of the AST node class,</li>,
 ,<li>,Additional properties specific to each node type (e.g., name, value, children, etc.),</li>,
 ,</ul>

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `filepath` | `string` | `false` | `null` |
| `returnType` | `string` | `false` | `struct` |
| `sourceType` | `string` | `false` | `script` |

</details>
<details>
<summary><code>jSONDeserialize(strictMapping=[boolean], useCustomSerializer=[string])</code></summary>

Converts a JSON (JavaScript Object Notation) string data representation into data, such as a structure or array.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `strictMapping` | `boolean` | `false` | `true` |
| `useCustomSerializer` | `string` | `false` | `null` |

</details>
<details>
<summary><code>fromJSON(strictMapping=[boolean], useCustomSerializer=[string])</code></summary>

Converts a JSON (JavaScript Object Notation) string data representation into data, such as a structure or array.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `strictMapping` | `boolean` | `false` | `true` |
| `useCustomSerializer` | `string` | `false` | `null` |

</details>


## Examples
