---
icon: plug-circle-bolt
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

By default, once you execute a `boxlang` binary it will look for a `BOXLANG_HOME` environment variable so it can be used as the home for the OS runtime.  If you don't provide one, then by default, it will use the currently logged-in user's home folder + `.boxlang`

{% tabs %}
{% tab title="Mac" %}
```javascript
/Users/username/.boxlang
```
{% endtab %}

{% tab title="Linux" %}
```bash
/home/username/.boxlang
```
{% endtab %}

{% tab title="Windows" %}
```python
c:/Windows/users/myuser/.boxlang
```
{% endtab %}
{% endtabs %}

This is important because inside of the home folder, you can have several folders and files by convention that will be used for the runtime execution.

{% hint style="danger" %}
Please note that each runtime can have a different location for the BoxLang home.  So make sure you read each of the runtime's docs to see where each goes.
{% endhint %}

<table><thead><tr><th width="257">Folder/FIle</th><th>Description</th></tr></thead><tbody><tr><td><code>/classes</code></td><td>Where all the compiled classes will be stored</td></tr><tr><td><code>/config</code></td><td>Where configuration files are stored for the runtime</td></tr><tr><td><code>/config/boxlang.json</code></td><td>The <a href="../configuration.md">runtime configuration file</a>.  Here is where you can configure all the settings, caches, datasources, compiler information, and so much more.</td></tr><tr><td><code>/global</code></td><td>Where global BoxLang classes and component templates can be stored for the entire runtime</td></tr><tr><td><code>/lib</code></td><td>You can place any *.jar files here, and they will be loaded into the runtime at startup. This is a great place to put third-party jars that will be available at runtime.</td></tr><tr><td><code>/logs</code></td><td>All log files will be stored here</td></tr><tr><td><code>/modules</code></td><td>Here is where the BoxLang modules are installed and will be available for the entire operating system binary.</td></tr><tr><td><code>version.properties</code></td><td>The version information of the installed runtime.</td></tr></tbody></table>

### Start the REPL  <a href="#start-the-repl-8" id="start-the-repl-8"></a>

The first thing you can do is start up the BoxLang REPL, make sure the insaller has added your installation directory to the `PATH` system variable.

{% tabs %}
{% tab title="Mac/*nix" %}
```javascript
boxlang
```
{% endtab %}

{% tab title="Windows" %}
```ruby
boxlang.bat
```
{% endtab %}

{% tab title="Jar" %}
```
java -jar path/to/boxlang-1.0.0-all.jar
```
{% endtab %}
{% endtabs %}

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

You can run one-off expressions from the REPL like so:

```shell
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

{% hint style="success" %}
Press Ctrl-C to exit the REPL or type `exit` or `quit`
{% endhint %}

Please note that the REPL remembers state, so you can use the variables you declare and build a mini-program with it.

### Executing a File <a href="#execute-a-file-9" id="execute-a-file-9"></a>

You can also use the `boxlang` binary to execute BoxLang or even CFML code.  You can pass a second argument to the binary and it can be a relative (to the current directory you are on) or an absolute path to a file that you wish to execute.

{% hint style="info" %}
Allowed files are:

* `*.bx -` A BoxLang class with a `main( args=[] )` method
* \*.bxs -  A BoxLang script file
* \*.bxm - A Boxlang markup template file

If you are using the `bx-compat-cfml` module for CFML Support:

* \*.cfs - A CFML script file
* \*.cfm - A CFML markup template file
{% endhint %}

Modify the same command you run above to execute the REPL but add a file path to the end. It can be absolute or relative to the current working directory.

{% tabs %}
{% tab title="Mac / *Unix" %}
```bash
boxlang task.bx
boxlang myscript.bxs
boxlang mytemplate.bxm

boxlang /full/path/to/test.bxs
boxlang /full/path/to/Task.bx
```
{% endtab %}

{% tab title="Windows" %}
```powershell
boxlang.bat task.bx
boxlang.bat myscript.bxs
boxlang.bat mytemplate.bxm
```
{% endtab %}

{% tab title="Jar" %}
```ruby
java -jar boxlang-1.0.0-all.jar task.bx
java -jar boxlang-1.0.0-all.jar /full/path/to/test.bxs
```
{% endtab %}
{% endtabs %}

#### Producing Output

As you navigate all the built-in functions and capabilities of BoxLang, let's learn how to produce output to the system console.

* `printLn()` - Print with a line break
* `print()` - Print with no line break
* `writeOUtput()` - Writes to the output buffer (Each runtime decides what it's buffer is.  The CLI is the system output, the Web is the HTML response buffer, etc)

```groovy
println( "Time is #now()#" )
```

I get the output:

```bash
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

So, to give a quiet example of the `--bx-code` flag here’s running some one-off code.

```bash
boxlang --bx-code "2+2"
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

### Command Line Arguments <a href="#other-command-line-args-10" id="other-command-line-args-10"></a>

If you interact with the `boxlang` binary then you will be executing the `BoxRunner` class in BoxLang.  You can use several options and positional arguments to our runtime.  Let's explore them.

#### Options

* `--bx-code "code here"`—This is used to pass ad-hoc code to execute. Provide code in the next argument, quoted.
* `--bx-config` - Pass a path to a JSON file for BoxLang configuration. See [Runtime Configuration](../configuration.md) for more information.
* `--bx-debug` - Enable debug mode (more debug logs!)
* `--bx-home` - Pass a path to a custom runtime home directory for storing modules, configuration, and more. See [Runtime Home Directory](../configuration.md#runtime-home-directory) for more information.
* `--bx-printAST` - Prints out BoxLang AST in JSON format for code provided via the `-c` flag (for debugging)
* `--bx-transpile` - Prints out transpiled Java source that would be compiled to create the bytecode for the passed template path. (for debugging)
* `--version` - Output  the current runtime's version information

#### Positionals

* `script_path | class_path` - The template, class, or script to execute
  * If it's a class, it must have a `main( args )` method.
* `module:{name}` - The executable module to execute.  This will execute a Modules' `ModuleConfig.main( args )` method.
* `{actionCommand: compile,featureAudit, cftranspile}` - If you send any of those action commands, we will execute those CLI tools

### Using 3rd Party Jars <a href="#using-3rd-party-jars-14" id="using-3rd-party-jars-14"></a>

You can load custom third-party JARs at runtime by adding all your `*.jar` to the `BOXLANG_HOME/lib` folder. This will be loaded at runtime and available to use and integrate.

### Environment Variables

The `boxlang` binary will also scan for several environment variables as overrides to the execution process.

| Env Variable                  | Purpose                      |
| ----------------------------- | ---------------------------- |
| `BOXLANG_CONFIG` = PATH       | Override the `boxlang.json`  |
| `BOXLANG_DEBUG = BOOLEAN`     | Enable or disable debug mode |
| `BOXLANG_HOME = DIRECTORY`    | Override the HOME directory  |
| `BOXLANG_PRINTAST = BOOLEAN`  | Print the AST                |
| `BOXLANG_TRANSPILE = BOOLEAN` | Tranpile the code            |

At this point, you are done getting running with BoxLang.  It's now your turn to write some code and get it running.
