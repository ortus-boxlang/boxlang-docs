---
description: BoxLang and the Multiverse!
---

# Running BoxLang

{% hint style="warning" %}
Please check out our [installation page ](../installation/)to make sure you install the right runtime you want to deploy on.  We are assuming you have it installed and `boxlang` and `boxlang-miniserver` are in your machine's path.
{% endhint %}

{% hint style="info" %}
The script for \*nix/Mac is `boxlang`

The script for Windows is `boxlang.bat`
{% endhint %}

### BoxLang Home <a href="#start-the-repl-8" id="start-the-repl-8"></a>

By default, once you execute a `boxlang` binary it will look for a `BOXLANG_HOME` environment variable so it can be used as the home for the OS runtime.  If you don't provide one, then by default it will use the currently logged-in user's home folder + `.boxlang`

```
/Users/myuser/.boxlang
c:/Windows/users/myuser/.boxlang
```

This is important because inside of the home folder, you can have several folders and files by convention that will be used for the runtime execution.

<table><thead><tr><th width="177">Folder/FIle</th><th>Description</th></tr></thead><tbody><tr><td><code>/classes</code></td><td>Where all the compiled classes will be stored</td></tr><tr><td><code>/lib</code></td><td>You can place any *.jar files here, and they will be loaded into the runtime at startup. This is a great place to put third-party jars that will be available at runtime.</td></tr><tr><td><code>/logs</code></td><td>All log files will be stored here</td></tr><tr><td><code>/modules</code></td><td>Here is where the BoxLang modules are installed and will be available for the entire operating system binary.</td></tr><tr><td><code>boxlang.json</code></td><td>The <a href="../configuration.md">runtime configuration file</a>.  Here is where you can configure all the settings, caches, datasources, compiler information, and so much more.</td></tr></tbody></table>

### Start the REPL  <a href="#start-the-repl-8" id="start-the-repl-8"></a>

The first thing you can do is start up the BoxLang REPL.

```bash
# Execute our scripts
$ boxlang

# Execute directly the jar
java -jar boxlang-1.0.0-all.jar
```

Feel free to specify a full path to the `Java` binary if the one in your default path does not point to your Java JDK.

```bash
/full/path/to/bin/java -jar boxlang-1.0.0-all.jar
```

You can run one-off expressions from the REPL like so:

```shell
██████   ██████  ██   ██ ██       █████  ███    ██  ██████
██   ██ ██    ██  ██ ██  ██      ██   ██ ████   ██ ██
██████  ██    ██   ███   ██      ███████ ██ ██  ██ ██   ███
██   ██ ██    ██  ██ ██  ██      ██   ██ ██  ██ ██ ██    ██
██████   ██████  ██   ██ ███████ ██   ██ ██   ████  ██████

Enter an expression, then hit enter.
Press Ctrl-C to exit.

BoxLang> 2+2
4

BoxLang> dateFormat( now(), "full" )
Wednesday, March 13, 2024

BoxLang> "brad".ucase().reverse()
DARB

BoxLang> a=3
3

BoxLang> b=5
5

BoxLang> a*b
15

BoxLang> ["luis","gavin","jorge"].map( name->name.ucFirst() )
[Luis, Gavin, Jorge]

```

{% hint style="info" %}
Press Ctrl-C to exit the REPL.
{% endhint %}

Please note that the REPL remembers state, so you can use the variables you declare and build a mini-program with it.

### Execute a File <a href="#execute-a-file-9" id="execute-a-file-9"></a>

You can also use the `boxlang` binary to execute BoxLang or even CFML code.  You can pass a second argument to the binary and it can be a relative (to the current directory you are on) or an absolute path to a file.

{% hint style="info" %}
Allowed files are:

* `*.bx -` A BoxLang class with a `main( args=[] )` method
* \*.bxs -  A BoxLang script file
* \*.bxm - A Boxlang markup template file
* \*.cfs - A CFML script file
* \*.cfm - A CFML markup template file
{% endhint %}

Modify the same command you run above to execute the REPL but add a file path to the end. It can be absolute or relative to the current working directory.

```bash
# binary
boxlang task.bx
boxlang myscript.bxs
boxlang mytemplate.bxm

# jar
java -jar boxlang-1.0.0-all.jar task.bx

```

or

```bash
# binary
boxlang /full/path/to/test.bxs
boxlang /full/path/to/Task.bx

# jar
java -jar boxlang-1.0.0-all.jar /full/path/to/test.bxs

```

Any output written to the buffer with `echo()`, or `writeOutput()` will be output in the console as well as any text printed to the console with `println() or print()`.   So with the example file `test.bxs` containing

```groovy
println( "Time is #now()#" )
```

I get the output:

```python
╰─ boxlang test.bxs
Time is {ts '2024-05-22 22:09:56'}
```

Hooray!  You have executed your first script using BoxLang.  Now let's build a class with a `main( args=[] )` convention.  This is simliar to Java or Groovy.

```groovy
class{

        function main( args=[] ){

                println( "Task called with " & arguments.toString() )

        }

}
```

You can now call it with zero or more arguments!

```bash
╰─ boxlang Task.bx
Task called with {ARGS=[]}

╰─ boxlang Task.bx boxlang rocks
Task called with {ARGS=[boxlang, rocks]}
```

### One Off Code Execution

So, to give a quiet example of the `-c` flag here’s running some one-off code.

```bash
boxlang -c "2+2"
```

{% hint style="warning" %}
This assumes script, not templating tags.
{% endhint %}

### Piping code <a href="#piping-code-11" id="piping-code-11"></a>

You can also pipe statements into the BoxLang binary for execution as well. This assumes script, not tags.

```bash
echo "2+2" | java -jar boxlang-1.0.0-all.jar
echo "2+2" | boxlang
```

or

```bash
# on *nix
cat test.cfs | java -jar boxlang-1.0.0-all.jar
cat test.cfs | boxlang

# on Windows
type test.cfs | java -jar boxlang-1.0.0-all.jar
type test.cfs | boxlang.bat
```

### Other Command Line Arguments <a href="#other-command-line-args-10" id="other-command-line-args-10"></a>

We also support the following command line args right now.

* `-c "code here"`—This is used to pass ad-hoc code to execute. Provide code in the next argument, quoted.
* `--config` - Pass a path to a JSON file for BoxLang configuration. See [Runtime Configuration](../configuration.md) for more information.
* `--debug` - Enable debug mode (more debug logs!)
* `--home` - Pass a path to a custom runtime home directory for storing modules, configuration, and more. See [Runtime Home Directory](../configuration.md#runtime-home-directory) for more information.
* `--printAST` - Prints out BoxLang AST in JSON format for code provided via the `-c` flag (for debugging)
* `--transpile` - Prints out transpiled Java source that would be compiled to create the bytecode for the passed template path. (for debugging)
* `--version` - Output  the current runtime's version information
* `path` - The template, class, or script to execute
* `module:{name}` - The executable module to execute.  This will execute a Modules' `ModuleConfig.main()` method.

### Environment Variables

The `boxlang` binary will also scan for several environment variables as overrides to the execution process.

| Env Variable                  | Purpose                      |
| ----------------------------- | ---------------------------- |
| `BOXLANG_CONFIG` = PATH       | Override the `boxlang.json`  |
| `BOXLANG_DEBUG = BOOLEAN`     | Enable or disable debug mode |
| `BOXLANG_HOME = DIRECTORY`    | Override the HOME directory  |
| `BOXLANG_PRINTAST = BOOLEAN`  | Print the AST                |
| `BOXLANG_TRANSPILE = BOOLEAN` | Tranpile the code            |
