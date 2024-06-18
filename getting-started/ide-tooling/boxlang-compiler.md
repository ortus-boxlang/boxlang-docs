---
description: Sourceless deployments for all
---

# BoxLang Compiler

BoxLang ships with many CLI tools.  The BoxLang Compiler is one of them.  This tool allows you to compile a file or a directory of files into Java Bytecode.  This will allow you to do sourceless deployments.

{% hint style="warning" %}
&#x20;The compiler still has some issues we need to iron out, mostly around apps using mappings that provide more than one Class/CFC path to reference a single physical file on the disk.
{% endhint %}

This tool will compile and place (by default) your BoxLang files into Java bytecode so you can do sourceless deployments.  When BoxLang goes to compile a file, it will check to see if the file has bytecode in it and proceed with loading the class directly, skipping the parsing and compilation step.

## Usage

### A single file:

```css
java -cp boxlang-1.0.0-all.jar ortus.boxlang.compiler.BXCompiler 
--source /path/to/webroot/index.cfm 
--target /path/to/compiled-webroot/index.cfm 
--basePath /path/to/webroot
```

Note, for the code to run, the compiled file needs to have the exact same path on disk as the original file. That means you’ll either need to copy the pre-compiled files back over to the original location or just point the source and target at the same place. **BE WARNED: this will overwrite the source code! So pay attention.**

### **Directory**

And an entire directory like so:

```css
java -cp boxlang-1.0.0-all.jar ortus.boxlang.compiler.BXCompiler 
--source /path/to/webroot/ 
--target /path/to/compiled-webroot/ 
--basePath /path/to/webroot
```

Also note, when pre-compiling an entire directory, the tool doesn’t touch non-code files, so if your target is a separate folder, that new folder won’t contain images, js files, etc. The typical use case for this would be in a CI build or similar, where you would override the code files in place.

### CLI Options

* `--basePath path`  The path to use for all base operations that require relative paths.
* `--mapping dot_notation` If there is a mapping name to the source folder, then add it here
* `--source file/directory`  A file or directory to compile.
* `--stopOnError`  or `--stopOnError boolean` to stop execution if an error occurs. Otherwise, it ignores it, logs it, and continues compiling.
* `--target path` Optional; if not passed, it will be compiled and put in the same location as the source.  This is a directory where the compiled files will be placed.
