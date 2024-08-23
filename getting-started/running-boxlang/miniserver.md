---
description: BoxLang includes a lightning fast web server powered by Undertow!
icon: jet-fighter-up
---

# MiniServer

<figure><img src="../../.gitbook/assets/miniserver.png" alt=""><figcaption></figcaption></figure>

The BoxLang MiniServer runtime, a symbol of flexibility, is a lightweight and lightning-fast web server powered by Undertow. It's ideal for non-mission-critical applications, lightweight traffic, embedded web servers, and development. For those who desire a more robust server implementation, we offer our [CommandBox server](commandbox.md) and [CommandBox PRO](https://boxlang.io/plans) with a BoxLang Subscription.

### Starting a BoxLang MiniServer <a href="#starting-a-web-server-12" id="starting-a-web-server-12"></a>

The BoxLang core, on its own, doesn't have knowledge about a web application. Our web support runtime provides this functionality, which is a crucial part of the MiniServer and the Servlet (JEE, Jakarta, CommandBox) runtime.  This runtime enhances the core boxlang runtime, making it multi-runtime and web deployable.

**There is no servlet container;** the web server is just a simple, fast, and pure Java Undertow server.  We will use the `boxlang-miniserver` binary to start servers.



{% tabs %}
{% tab title="Mac/Unix" %}
```bash
# Mac / *unix
boxlang-miniserver
```
{% endtab %}

{% tab title="Windows" %}
```powershell
# Windows
boxlang-miniserver.bat
```
{% endtab %}

{% tab title="JAR Execution" %}
```bash
java -jar /usr/local/lib/boxlang-miniserver-1.0.0-all.jar
```
{% endtab %}
{% endtabs %}

Once you run the command, the following output will appear in your console:

```bash
+ Starting BoxLang Server...
- Web Root: /home/lmajano/Sites/temp
- Host: localhost
- Port: 8080
- Debug: false
- Config Path: null
- Server Home: null
+ Starting BoxLang Runtime...
+ Runtime Started in 2043ms
+ BoxLang MiniServer started in 2135ms
+ BoxLang MiniServer started at: http://localhost:8080
Press Ctrl+C to stop the server.
```

As you can see from the output, this is the result of the command:

* Use the current **working dir** as the web root.
* Bind to `localhost:8080`
* This configures a very simple web server with some default welcome files. BoxLang will process any CFML or BoxLang extensions.
* Seed the `BOXLANG_HOME` to `${HOME}/.boxlang` if not set via env

{% hint style="warning" %}
**ALERT:** The BoxLang Core knows nothing of web or HTTP, so the `form`, `url`, `cookie`, and `cgi` scopes will only exist when running the BoxLang web server (but not in the REPL, etc).
{% endhint %}

That's practically it.  This is a very lightweight server that can get the job done.  You can also startup servers using our VSCode IDE by opening the command palette and clicking on startup a BoxLang web server.

<figure><img src="../../.gitbook/assets/ide-tooling-context-minserver.png" alt=""><figcaption></figcaption></figure>

### Arguments <a href="#web-server-args-13" id="web-server-args-13"></a>

Here is the collection of arguments you can pass into the binary.

<table><thead><tr><th width="351">Argument</th><th>Value</th></tr></thead><tbody><tr><td><code>--configPath path/boxlang.json</code><br><code>-c path/boxlang.json</code></td><td>Relative/Absolute location of the <code>boxlang.json</code> to use. By default it uses the <code>~/.boxlang/boxlang.json</code></td></tr><tr><td><code>--debug</code><br><code>-d</code></td><td>Put the runtime into debug mode. By default we use <code>false</code></td></tr><tr><td><code>--host ip|domain</code><br><code>-h ip|domain</code></td><td>Bind the hostname to the mini server. By default we use <code>localhost</code></td></tr><tr><td><code>--port 8080</code><br><code>-p 8080</code></td><td>The port to bind the mini server to. By default we use port <code>8080</code></td></tr><tr><td><code>--serverHome path/</code><br><code>-s path/</code></td><td>The location of the BoxLang home for the miniserver.  This is where it will look for the boxlang.json, place the log files, the compiled classes, load modules and much more.  By default we use the OS home via the <code>BOXLANG_HOME</code> env variable which usually points to the user's home: <code>~/.boxlang/</code></td></tr><tr><td><code>--webroot path/</code><br><code>-w path/</code></td><td>The webserver root.  By default, we use the directory from where you started the command.</td></tr></tbody></table>

```bash
# Custom port and webroot
boxlang-miniserver --port 80 --webroot /var/www

# Custom port and server home
boxlang-miniserver --port 80 --serverHome /var/www/servers/myServer
```

### Environment Variables

The `boxlang-miniserver` binary will also scan for several environment variables as overrides to the execution process.

| Env Variable                           | Purpose                                                             |
| -------------------------------------- | ------------------------------------------------------------------- |
| `BOXLANG_CONFIG` = PATH                | Override the `boxlang.json`                                         |
| `BOXLANG_DEBUG = BOOLEAN`              | Enable or disable debug mode                                        |
| `BOXLANG_HOME = DIRECTORY`             | Override the server HOME directory                                  |
| `BOXLANG_HOST = ip or domain`          | Override the `localhost` default to whatever IP or domain you like. |
| `BOXLANG_PORT = 8080`                  | Override the default port                                           |
| `BOXLANG_WEBROOT = path`               | Override the location of the web root                               |
| `BOXLANG_MINISERVER_OPTS = jvmOptions` | A list of Java options to pass to the startup command               |

**Environment variables are scanned first, then the command arguments.  Thus the command arguments take precedence.**

### Using 3rd Party Jars <a href="#using-3rd-party-jars-14" id="using-3rd-party-jars-14"></a>

You can load up custom third-party JARs into the runtime in two manners

1. `BOXLANG_HOME/lib` - You can place all the jars the runtime will load in this location
   1. Remember you can use the `--serverHome` to chose this.
2. Add via the classpath to your runner.

Please note that if you use the `-cp` approach, then you need to use a full `java -cp` syntax or you can customize the `boxlang-miniserver` shell scripts to do your bidding.

If you want to test 3rd part libs with the web server, you’ll need to use a different syntax that uses the `-cp` (classpath) JVM arg and specifies both the boxlang jar AND a semi-colon delimited list of the jars you want to use. It’s a little annoying, but this is how java works.

```bash
# Format
java -cp {jarpath;jarpath2} ortus.boxlang.web.MiniServer


# Example
java -cp boxlang-miniserver-1.0.0-all.jar;/path/to/my.jar;/path/to/another.jar ortus.boxlang.web.MiniServer
```

### Modules

If you would like to use modules for the MiniServer, then you must install them using CommandBox, our Docker image or manually into the `BOXLANG_HOME/modules` folder.  You can ad `debug` true to the arguments or env, so you can see which modules got loaded on startup.

### JVM Options

You can use the `BOXLANG_MINISERVER_OPTS` env variable to seed the Java arguments the miniserver will start with.

```bash
BOXLANG_MINISERVER_OPTS="-Xmx512m"
boxlang-miniserver
```

### Runtime Source Code

The runtime source code can be found here: [https://github.com/ortus-boxlang/boxlang-miniserver](https://github.com/ortus-boxlang/boxlang-miniserver)

We welcome any pull requests, testing, docs, etc.
