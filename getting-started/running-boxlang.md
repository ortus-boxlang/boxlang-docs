# Running BoxLang

We don’t have installers built yet, so for now, it’s just a single jar that you run via Java directly.

BoxLang doesn’t “unpack” anything to your hard drive like you may be used to Lucee or CF doing. It will use your Java temp dir to write out class files for disk caching and JSON and Java files for debugging. If you are unsure where Java’s temp dir is, run

```lua
java -XshowSettings:properties --version
```

and look in the output for the `java.io.tmpdir` line. When updating to a newer BoxLang jar, you may need to manually wipe the contents of this folder or just run it with the `--debug` flag and it will auto-wipe.

### Requirements <a href="#requirements-7" id="requirements-7"></a>

BoxLang is explicitly compiled for Java 17+ right now (it will be 21 soon as our standard). We’re exploring how far back to support, but please download Java 17+ for now. BoxLang is currently compiling Java source on the fly, so it requires a JDK, not a JRE, to run! Eventually, we’ll be generating bytecode directly, but for now, we have a dependency on the JDK’s Java Compiler classes.

You should be able to grab the Java 17 JDK for your OS and CPU arch here: [Download Java 17 JDK 5](https://adoptium.net/temurin/releases/?package=jdk\&version=17)

You should be able to grab the Java 21 JDK for your OS and CPU arch here: [Download Java 21 JDK 4](https://adoptium.net/temurin/releases/?package=jdk\&version=21)

You don’t necessarily have to set it as your `java_home` since, for now, the commands I’ll show you can allow you to specify a full path to the `java` binary if you want.

### Start the REPL <a href="#start-the-repl-8" id="start-the-repl-8"></a>

The first thing you can do is start up the BoxLang REPL. Run the jar directly with no arguments for this

```bash
# Execute directly
java -jar boxlang-1.0.0-all.jar

# Using the distribution version you can execute the bash or bat script
bin/boxlang.bat
bin/boxlang
```

Feel free to specify a full path to the `java` binary if the one in your default path does not point to your Java JDK.

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

Press Ctrl-C to exit the REPL.\
Not all BIFs are supported in the language. We’ll get some documentation what is and isn’t supported soon.

### Execute a file <a href="#execute-a-file-9" id="execute-a-file-9"></a>

We’re focusing on CF compat at the moment, so the BoxLang parser isn’t finsihed yet. Therefore, I recommend using CF extensions for now (`.cfm`, `.cfs`). You can use BL extensions (`.bxm`, `.bxs`) but since those parsers aren’t finished yet, they will just use the CF parser for now.

Modify the same command you run above to execute the REPL but add a file path to the end. It can be absolute or relative to the current working directory.

```bash
java -jar boxlang-1.0.0-all.jar test.cfm
bin/boxlang test.cfm
bin/boxlang.bat test.cfm
```

or

```bash
java -jar boxlang-1.0.0-all.jar /full/path/to/test.cfm
bin/boxlang /full/path/to/test.cfm
bin/boxlang.bat /full/path/to/test.cfm
```

Any output written to the buffer with `echo()`, or `writeOutput()` will be output in the console as well as any text printed to the console with `println()` or `systemOutput()`. You’ll have to scroll past the console logging for now. We’ll get that moved to a file eventually.

So with the example file `test.cfm` containing

```html
<cfoutput>
	Time is: #now()#
</cfoutput>
```

I get the output:

```python
C:\>java -jar boxlang-1.0.0-all.jar test.cfm
2024-03-13 02:12:03,075 BoxRuntime [INFO]  + Starting up BoxLang Runtime
... snip ...
        Time is: {ts '2024-03-13 02:12:04'}
... snip ...
2024-03-13 02:12:04,588 BoxRuntime [INFO]  + BoxLang Runtime has been shutdown
```

There may be a short delay on the first run while the code is JIT compiled, but it should run very fast on subsequent runs, which includes loading up the entire runtime and shutting it down again!

### Other Command line args <a href="#other-command-line-args-10" id="other-command-line-args-10"></a>

We also support the following command line args right now.

* `--debug` - Enable debug mode (moar debug logs!)
* `--debugger` - Enable debugger (need more info)
* `-c "code here"`—This is used to pass ad-hoc code to execute. Provide code in the next argument, quoted.
* `--printAST` - Prints out BoxLang AST in JSON format for code provided via the `-c` flag (for debugging)
* `--transpile` - Prints out transpiled Java source that would be compiled to create the bytecode for the passed template path. (for debugging)
* `--config` - Pass a path to a JSON file for BoxLang configuration. Documentation on this file format is coming soon. For now, you can look inside the BoxLang jar at the `config/boxlang.json` file for an example.

So, to give a quiet example of the `-c` flag, here’s running some one-off code.

```bash
java -jar boxlang-1.0.0-all.jar -c "2+2"
bin/boxlang -c "2+2"
bin/boxlang.bat -c "2+2"
```

This assumes script, not tags.

### Piping code <a href="#piping-code-11" id="piping-code-11"></a>

You can also pipe statements into the BoxLang jar for execution as well. This assumes script, not tags.

```bash
echo "2+2" | java -jar boxlang-1.0.0-all.jar
```

or

```bash
# on *nix
cat test.cfs | java -jar boxlang-1.0.0-all.jar

# on Windows
type test.cfs | java -jar boxlang-1.0.0-all.jar
```

### Starting a web server <a href="#starting-a-web-server-12" id="starting-a-web-server-12"></a>

The web server is currently bundled in the core, but it will soon be broken into a separate project, so the BoxLang Core has no web knowledge. There is no servlet container at all; the web server is just a simple proof of concept using a pure Java Undertow server. Our separate main Java class handles this, so the call will look a little different.

Go to a folder that you want to be the web root and run:

```undefined
java -jar boxlang-1.0.0-web.jar
```

This will

* Use the current working dir as the web root
* Bind to `localhost:8080`
* Configures a VERY simple web server with some default welcome files and any CF or BoxLang extensions will get processed by BoxLang.

The BoxLang Core knows nothing of web or HTTP, so the `form`, `url`, `cookie`, and `cgi` scopes will only exist when running the BoxLang web server (but not in the REPL, etc).

#### Web server args <a href="#web-server-args-13" id="web-server-args-13"></a>

There are a few JVM args you can pass to the web server right now:

* `--port 80` - to change the port. You cannot change the host nor the protocol (HTTP) right now
* `--webroot /var/www` - to specify the web root. This can be absolute or relative to the working dir.
* `--debug` - to enable debug mode

```bash
java -jar boxlang-1.0.0-web.jar --port 80 --webroot /var/www
```

### Using 3rd party jars <a href="#using-3rd-party-jars-14" id="using-3rd-party-jars-14"></a>

If you want to test 3rd part libs with the web server, you’ll need to use a different syntax that uses the `-cp` (classpath) JVM arg and specifies both the boxlang jar AND a semi-colon delimited list of the jars you want to use. It’s a little annoying, but this is how java works. Soon we’ll have BL running inside of CommandBox and this will all go away.

```javascript
java -cp boxlang-1.0.0-all.jar;/path/to/my.jar;/path/to/another.jar ortus.boxlang.web.Server
```

\
