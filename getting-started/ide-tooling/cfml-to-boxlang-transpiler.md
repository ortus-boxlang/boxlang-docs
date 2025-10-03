---
description: Transpile your CFML code to BoxLang.
icon: swap-arrows
---

# 🔄 CFML to BoxLang Transpiler

This CLI tool will allow you to transpile your CFML code into BoxLang native code. This is a great way to move forward and leverage BoxLang for your future projects. It will also transpile your Tag-based CFCs into script.

## 🚀 Usage

Make sure you have installed the OS version of [BoxLang](../installation/) so you get all the tools installed as well. Please note that the action command funnels through the `boxlang` binary, so you can use all the [CLI arguments](../running-boxlang/#other-command-line-args-10) for the `boxlang` runner.

You can call the tool using our script or the full path to the JAR:

```bash
# Using the OS binary
boxlang cftranspile [OPTIONS]

# Using the full path to the JAR
java -jar boxlang-1.6.0.jar ortus.boxlang.compiler.CFTranspiler [OPTIONS]
```

### Getting Help

```bash
# Display comprehensive help
boxlang cftranspile --help
boxlang cftranspile -h
```

## 📋 CLI Options

| Option | Short | Description | Default |
| :--- | :--- | :--- | :--- |
| `--help` | `-h` | Show help message and exit | - |
| `--verbose` | `-v` | Enable verbose output with detailed progress information | `false` |
| `--source <PATH>` | - | Path to source directory or file to transpile | Current directory (`.`) |
| `--target <PATH>` | - | Path to target directory or file (**required**) | - |
| `--stopOnError [BOOL]` | - | Stop processing on first error | `false` |

{% hint style="info" %}
**New in 1.6.0**: The `--verbose` / `-v` flag provides detailed transpilation progress, showing file-by-file status, parsing issues, and directory creation operations.
{% endhint %}

## 🔄 File Extension Mapping

The transpiler automatically converts ColdFusion file extensions to their BoxLang equivalents:

| ColdFusion | BoxLang | Description |
| :--- | :--- | :--- |
| `.cfm` | `.bxm` | ColdFusion markup → BoxLang markup |
| `.cfc` | `.bx` | ColdFusion component → BoxLang class |
| `.cfs` | `.bxs` | ColdFusion script → BoxLang script |

## 💡 Examples

### Transpile Current Directory

```bash
# Transpile all ColdFusion files in current directory
boxlang cftranspile --target ./boxlang-output
```

### Transpile Specific Directory

```bash
# Convert an entire project with directory structure preserved
boxlang cftranspile \
    --source ./coldfusion-code \
    --target ./boxlang-code
```

### Transpile Single File

```bash
# Convert a single file (extension auto-detected)
boxlang cftranspile \
    --source app.cfm \
    --target app.bxm
```

### Verbose Mode (New in 1.6.0)

```bash
# See detailed progress information during transpilation
boxlang cftranspile \
    --source ./cf-app \
    --target ./bx-app \
    --verbose
```

The verbose output will show:

* 🚀 Transpiler initialization
* 📂 Directory scanning progress
* 🔄 File-by-file transpilation status
* ⚙️ Parsing operations
* 📁 Directory creation
* ✅ Success confirmations
* ❌ Detailed error messages with parsing issues

### Stop on Error

```bash
# Stop transpilation on first error encountered
boxlang cftranspile \
    --source ./cf-app \
    --target ./bx-app \
    --stopOnError
```

### Complete Example with All Options

```bash
# Full-featured transpilation with verbose output
boxlang cftranspile \
    --source /path/to/cf/project \
    --target /path/to/bx/project \
    --verbose \
    --stopOnError
```

## 📂 Behavior

* **Directory Transpilation**: Preserves folder structure from source to target
* **Single File Transpilation**: Allows custom target naming
* **Auto Directory Creation**: Missing target directories are created automatically
* **Error Handling**: Parsing errors are logged; processing continues unless `--stopOnError` is used
* **Parallel Processing**: Directory mode processes files in parallel for better performance
* **Extension Auto-Mapping**: Target extensions are automatically determined based on source type

## 🔧 Supported Source Files

The transpiler supports the following ColdFusion file types:

* `.cfm` - ColdFusion markup pages
* `.cfc` - ColdFusion components
* `.cfs` - ColdFusion script files

## ⚠️ Known Limitations

{% hint style="warning" %}
The transpiler has some current limitations to be aware of:
{% endhint %}

* **Whitespace**: May not preserve the exact whitespace from the original source. Since the Abstract Syntax Tree (AST) doesn't store whitespace from script-based code, you'll get whatever formatting the tool applies. We plan to make some of this configurable (tabs vs. spaces, etc.)
* **Annotations**: ALL function and class annotations are converted to the new `@foo bar` syntax. We'll update this eventually to keep inline annotations as inline and only move CF "JavaDoc" style annotations to pre-annotations
* **Script Conversion**: All CFCs will be converted to script. This is by design as BoxLang enforces classes to only be written in script

## 📖 Additional Resources

* [BoxLang Documentation](https://boxlang.ortusbooks.com/)
* [Community Forums](https://community.ortussolutions.com/c/boxlang/42)
* [GitHub Repository](https://github.com/ortus-boxlang)
