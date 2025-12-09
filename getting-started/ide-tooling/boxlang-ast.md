---
description: Access BoxLang's Abstract Syntax Tree (AST) for building code analysis tools, linters, formatters, and migration utilities
icon: code-branch
---

# BoxLang AST

**New in BoxLang 1.7.0** - The `BoxAST()` BIF provides programmatic access to BoxLang's Abstract Syntax Tree (AST), enabling developers to build sophisticated code analysis tools, formatters, linters, and migration utilities. The AST represents the parsed structure of BoxLang code in a format that's easy to analyze and manipulate programmatically.

## 🌳 What is an AST?

An Abstract Syntax Tree (AST) is a tree representation of the syntactic structure of source code. Each node in the tree represents a construct occurring in the source code. The AST abstracts away concrete syntax details (like parentheses, semicolons, and whitespace) while preserving the semantic structure of the code.

For example, the code `x = 1 + 2;` would be represented as an AST with:

* An assignment node with target `x`
* A binary operation node for addition
* Literal nodes for values `1` and `2`

## 📋 Table of Contents

- [What is an AST?](#what-is-an-ast)
- [BoxAST() BIF](#boxast-bif)
- [Output Formats](#output-formats)
- [Node Types](#node-types)
- [Common Use Cases](#common-use-cases)
- [AST Analysis Examples](#ast-analysis-examples)
- [Best Practices](#best-practices)

## 📋 BoxAST() BIF

The `BoxAST()` function parses BoxLang or CFML source code and returns its AST representation.

### Syntax

```js
BoxAST(
    source: string,
    returnType: string = "struct",
    sourceType: string = "script"
)

BoxAST(
    filepath: string,
    returnType: string = "struct",
    sourceType: string = "script"
)
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `source` | string | Yes* | - | BoxLang/CFML source code to parse |
| `filepath` | string | Yes* | - | Path to file to parse (alternative to `source`) |
| `returnType` | string | No | `"struct"` | Output format: `"struct"`, `"json"`, or `"text"` |
| `sourceType` | string | No | `"script"` | Syntax type: `"script"`, `"template"`, `"cfscript"`, or `"cftemplate"` |

\* Either `source` or `filepath` must be provided, but not both.

### Return Types

#### struct (default)

Returns the AST as a BoxLang struct with full node hierarchy and properties. This is the most useful format for programmatic analysis.

```js
ast = BoxAST( source: "x = 1 + 2;" );
// Returns: struct with nodes, positions, types, etc.
```

#### json

Returns the AST as a JSON string, perfect for passing to external tools or storing for later analysis.

```js
astJson = BoxAST(
    source: "function hello() { return 'world'; }",
    returnType: "json"
);
// Returns: JSON string representation of the AST
```

#### text

Returns a human-readable text representation of the AST structure, useful for debugging and visualization.

```js
astText = BoxAST(
    source: "x = 1 + 2;",
    returnType: "text"
);
// Returns: Pretty-printed text tree structure
```

### Source Types

#### script (default)

Parse BoxLang script syntax (`.bx`, `.bxs` files).

```js
ast = BoxAST(
    source: "function hello() { return 'world'; }",
    sourceType: "script"
);
```

#### template

Parse BoxLang template syntax (`.bxm` files with `<bx:>` tags).

```js
ast = BoxAST(
    source: "<bx:output>#now()#</bx:output>",
    sourceType: "template"
);
```

#### cfscript

Parse CFML/ColdFusion script syntax for migration and compatibility tools.

```js
ast = BoxAST(
    source: "cfset x = 1; cfloop from='1' to='10' index='i' { writeOutput(i); }",
    sourceType: "cfscript"
);
```

#### cftemplate

Parse CFML/ColdFusion template syntax (`.cfm` files with `<cf>` tags) for migration tools.

```js
ast = BoxAST(
    source: "<cfset x = 1><cfoutput>#x#</cfoutput>",
    sourceType: "cftemplate"
);
```

## 💡 Usage Examples

### Basic AST Generation

```js
// Parse simple BoxLang code
code = "x = 1 + 2; y = x * 3;";
ast = BoxAST( source: code );

// Inspect the AST structure
println( ast.toString() );
```

### Using String Member Method

BoxLang strings have a convenient `toAST()` member method:

```js
// Parse using member method
code = "function hello() { return 'world'; }";
ast = code.toAST();

// With parameters
astJson = "x = 1 + 2;".toAST( returnType: "json" );

// Parse template syntax
templateCode = "<bx:output>#now()#</bx:output>";
ast = templateCode.toAST( sourceType: "template" );
```

### Parsing Files

```js
// Parse a BoxLang script file
ast = BoxAST( filepath: "/path/to/myScript.bx" );

// Parse a template file
ast = BoxAST(
    filepath: "/path/to/myTemplate.bxm",
    sourceType: "template"
);

// Parse a CFML file for migration
ast = BoxAST(
    filepath: "/legacy/code/myComponent.cfc",
    sourceType: "cfscript"
);
```

### JSON Export for External Tools

```js
// Generate AST as JSON for external processing
astJson = BoxAST(
    filepath: "myComponent.bx",
    returnType: "json"
);

// Send to external analysis tool
httpPost(
    url: "https://analysis-service.com/analyze",
    body: astJson,
    contentType: "application/json"
);

// Or save to file
fileWrite( "ast-output.json", astJson );
```

### Text Visualization

```js
// Get human-readable AST representation
astText = BoxAST(
    source: "function calculate( a, b ) { return a + b; }",
    returnType: "text"
);

println( astText );
// Outputs formatted tree structure showing nodes and relationships
```

## 🎯 Use Cases

### Code Analysis Tools

Build custom linters and static analysis tools to enforce coding standards:

```js
// Analyze code for patterns
code = fileRead( "myFile.bx" );
ast = code.toAST();

// Walk the AST to find specific patterns
// Example: Find all function declarations
functions = findFunctionNodes( ast );
```

### Code Formatters

Create custom code formatting utilities:

```js
// Parse unformatted code
uglyCode = "function test(){x=1;y=2;return x+y;}";
ast = uglyCode.toAST();

// Traverse AST and reformat based on rules
formattedCode = astToFormattedCode( ast );
```

### Documentation Generators

Extract function signatures, parameters, and documentation comments:

```js
// Parse component file
componentCode = fileRead( "MyComponent.bx" );
ast = componentCode.toAST();

// Extract all functions with their metadata
docs = extractFunctionDocumentation( ast );

// Generate API documentation
generateMarkdownDocs( docs );
```

### Migration Tools

Parse and analyze CFML code for BoxLang migration:

```js
// Parse legacy CFML file
cfmlCode = fileRead( "legacy.cfm" );
ast = BoxAST(
    source: cfmlCode,
    sourceType: "cftemplate"
);

// Analyze CFML features used
features = analyzeCFMLFeatures( ast );

// Generate migration report
generateMigrationReport( features );
```

### Refactoring Tools

Analyze and transform code structures:

```js
// Parse code to refactor
code = fileRead( "needsRefactoring.bx" );
ast = code.toAST();

// Find and replace deprecated patterns
transformedAst = replaceDeprecatedPatterns( ast );

// Generate updated code
newCode = astToCode( transformedAst );
fileWrite( "refactored.bx", newCode );
```

### IDE Tooling

Power syntax highlighting, code intelligence, and autocomplete features:

```js
// Parse current file for IDE features
currentCode = editor.getCurrentCode();
ast = currentCode.toAST();

// Provide intelligent autocomplete based on AST analysis
suggestions = getAutocompleteSuggestions( ast, cursorPosition );
```

## 🔍 AST Structure

The AST returned by `BoxAST()` contains detailed information about the code structure:

### Node Properties

Each AST node includes detailed metadata about the code structure:

* **ASTType** - The kind of node (e.g., "BoxScript", "BoxAssignment", "BoxBinaryOperation", "BoxIntegerLiteral")
* **ASTPackage** - The Java package containing the node class
* **sourceText** - Original source code for this node
* **position** - Source location with start/end line and column numbers
* **comments** - Associated comments
* **Additional Properties** - Node-specific data (name, value, operator, statements, etc.)

### Example AST Structure

For code: `x = 1 + 2`

```js
{
    "ASTType": "BoxScript",
    "ASTPackage": "ortus.boxlang.compiler.ast",
    "sourceText": "x = 1 + 2",
    "position": {
        "start": { "line": 1, "column": 0 },
        "end": { "line": 1, "column": 9 }
    },
    "comments": [],
    "statements": [
        {
            "ASTType": "BoxExpressionStatement",
            "ASTPackage": "ortus.boxlang.compiler.ast.statement",
            "sourceText": "x = 1 + 2",
            "position": {
                "start": { "line": 1, "column": 0 },
                "end": { "line": 1, "column": 9 }
            },
            "comments": [],
            "expression": {
                "ASTType": "BoxAssignment",
                "ASTPackage": "ortus.boxlang.compiler.ast.expression",
                "sourceText": "x = 1 + 2",
                "position": {
                    "start": { "line": 1, "column": 0 },
                    "end": { "line": 1, "column": 9 }
                },
                "comments": [],
                "modifiers": [],
                "left": {
                    "ASTType": "BoxIdentifier",
                    "ASTPackage": "ortus.boxlang.compiler.ast.expression",
                    "sourceText": "x",
                    "position": {
                        "start": { "line": 1, "column": 0 },
                        "end": { "line": 1, "column": 1 }
                    },
                    "comments": [],
                    "name": "x"
                },
                "op": {
                    "ASTType": "BoxAssignment",
                    "ASTPackage": "ortus.boxlang.compiler.ast.expression",
                    "sourceText": "Equal"
                },
                "right": {
                    "ASTType": "BoxBinaryOperation",
                    "ASTPackage": "ortus.boxlang.compiler.ast.expression",
                    "sourceText": "1 + 2",
                    "position": {
                        "start": { "line": 1, "column": 4 },
                        "end": { "line": 1, "column": 9 }
                    },
                    "comments": [],
                    "left": {
                        "ASTType": "BoxIntegerLiteral",
                        "ASTPackage": "ortus.boxlang.compiler.ast.expression",
                        "sourceText": "1",
                        "position": {
                            "start": { "line": 1, "column": 4 },
                            "end": { "line": 1, "column": 5 }
                        },
                        "comments": [],
                        "value": 1
                    },
                    "operator": {
                        "ASTType": "BoxBinaryOperation",
                        "ASTPackage": "ortus.boxlang.compiler.ast.expression",
                        "sourceText": "Plus"
                    },
                    "right": {
                        "ASTType": "BoxIntegerLiteral",
                        "ASTPackage": "ortus.boxlang.compiler.ast.expression",
                        "sourceText": "2",
                        "position": {
                            "start": { "line": 1, "column": 8 },
                            "end": { "line": 1, "column": 9 }
                        },
                        "comments": [],
                        "value": 2
                    }
                }
            }
        }
    ]
}
```

## 📊 Best Practices

{% hint style="success" %}
**When to Use BoxAST():**

* Building code analysis and quality tools
* Creating custom formatters and linters
* Developing migration utilities from CFML to BoxLang
* Generating documentation from source code
* Implementing refactoring tools
* Powering IDE features and code intelligence
{% endhint %}

{% hint style="info" %}
**Performance Tips:**

* Use `filepath` parameter for large files instead of reading into memory first
* Cache AST results for files that don't change frequently
* Use `returnType: "json"` when passing to external tools
* Consider using `returnType: "text"` only for debugging and development
* Parse incrementally for large codebases rather than all at once
{% endhint %}

{% hint style="warning" %}
**Important Considerations:**

* **Parsing Errors**: Invalid syntax will throw an exception - wrap in try/catch
* **Large Files**: Parsing very large files can consume significant memory
* **Source Type**: Ensure you specify the correct `sourceType` for CFML vs BoxLang
* **AST Changes**: AST structure may evolve between BoxLang versions
* **Read-Only**: The returned AST is for analysis - use code generation to create new code
{% endhint %}

## 🔗 Related Resources

* [BoxLang Compiler](boxlang-compiler.md)
* [CFML Transpiler](cfml-to-boxlang-transpiler.md)
* [BoxLang IDE](boxlang-ide.md)
* [Release Notes 1.7.0](../../readme/release-history/1.7.0.md)
* [BoxLang Language Reference](../../boxlang-language/)

## 🛠️ Building Tools with BoxAST()

The `BoxAST()` BIF opens up powerful possibilities for the BoxLang ecosystem:

### Example: Simple Linter

```js
function lintCode( code ) {
    ast = code.toAST();
    issues = [];

    // Check for var declarations (prefer local scope)
    if ( findVarDeclarations( ast ).len() > 0 ) {
        issues.append( "Use 'local' scope instead of 'var'" );
    }

    // Check for missing return statements
    functions = findFunctionNodes( ast );
    functions.each( ( func ) => {
        if ( !hasReturnStatement( func ) ) {
            issues.append( "Function '#func.name#' missing return statement" );
        }
    } );

    return issues;
}
```

### Example: Function Extractor

```js
function extractFunctions( filepath ) {
    ast = BoxAST( filepath: filepath );
    functions = [];

    walkAST( ast, ( node ) => {
        if ( node.type == "FunctionDeclaration" ) {
            functions.append( {
                "name": node.name,
                "parameters": node.parameters,
                "returnType": node.returnType ?: "any",
                "line": node.position.line
            } );
        }
    } );

    return functions;
}
```

The possibilities are endless - from simple code metrics to sophisticated refactoring tools, `BoxAST()` provides the foundation for building powerful development tools in the BoxLang ecosystem.
