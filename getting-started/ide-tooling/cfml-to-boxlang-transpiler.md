---
description: Transpile your CFML code to BoxLang.
---

# CFML to BoxLang Transpiler

This CLI tool will allow you to transpile your CFML code into BoxLang native code.  This is a great way to move forward and leverage BoxLang for your future projects.  It will also transpile your Tag-based CFCs into the script.

### Usage

Make sure you have installed the OS version of [BoxLang](../installation/) so you get all the tools installed as well.  Please note that the action command funnels through the `boxlang` binary, so you can use all the [CLI arguments](../running-boxlang/#other-command-line-args-10) for `boxlang` runner.

You can call the tool using our script or the full path to the jar.

```bash
// Using the script
boxlang cftranspile <options here>

// Using the full path to the jar
java -cp boxlang-1.0.0-all.jar ortus.boxlang.compiler.CFTranspiler  <options here>
```

### Examples

```bash
// Using the script
boxlang cftranspile 
    --source /path/to/file.cfc 
    --target /path/to/file.bx

// Using the full path
java -cp boxlang-1.0.0-all.jar ortus.boxlang.compiler.CFTranspiler 
--source /path/to/file.cfc 
--target /path/to/file.bx
```

(If you leave off the target file extension, the tool will automatically append the correct one based on the source file type).  You can also convert an entire folder like so:

```bash
// Using the script
boxlang cftranspile
    --source /path/to/CF/code 
    --target /path/to/BL/code 
    --stopOnError

// Using the full path
java -cp boxlang-1.0.0-all.jar ortus.boxlang.compiler.CFTranspiler 
--source /path/to/CF/code 
--target /path/to/BL/code 
--stopOnError
```

#### Known issues right now are

* It may not have the same whitespace you had in the original source. Since our Abstract Syntax Tree (AST) doesn’t store whitespace from script-based code, you’ll get whatever formatting the tool applies. That said, we do plan to make some of that configurable in regards to tabs v, spaces, etc.
* ALL function and class annotations are converted to the new `@foo bar` syntax, but we’ll update that eventually to keep inline annotations as inline and only move CF “JavaDoc” style annotations to pre-annotations.
* All CFCs will be converted to script. This is designed as BoxLang plans to enforce classes to only be written in script.

### CLI Options

* `--source path` A file or directory to transpile to BoxLang
* `--target path` The target file or directory to store the new BoxLang source. Extension not required.
* `--stopOnError or --stopOnError boolean` Stop execution if an error is encountered or continue processing. Defaults to `false`
