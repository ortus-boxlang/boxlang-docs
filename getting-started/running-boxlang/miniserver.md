---
description: BoxLang includes a lightning fast web server powered by Undertow!
---

# MiniServer

<figure><img src="../../.gitbook/assets/miniserver.png" alt=""><figcaption></figcaption></figure>

The BoxLang MiniServer runtime, a symbol of flexibility, is a lightweight and lightning-fast web server powered by Undertow. It's ideal for non-mission-critical applications, lightweight traffic, or development. For those who desire a more robust server, we offer our [CommandBox server](commandbox.md) and [CommandBox PRO](https://boxlang.io/plans) with a BoxLang Subscription.

### Starting a BoxLang MiniServer <a href="#starting-a-web-server-12" id="starting-a-web-server-12"></a>

The BoxLang core, on its own, doesn't have knowledge about a web application. Our web support runtime provides this functionality, a crucial part of the MiniServer and the Servlet (JEE, Jakarta, CommandBox) runtime.  This runtime enhances the core boxlang runtime, making it multi-runtime and web deployable.

**There is no servlet container;** the web server is just a simple, fast, and pure Java Undertow server.  Let's start a default server:

```bash
# Mac / *unix
boxlang-miniserver

# Windows
boxlang-miniserver.bat

# Full Jar approach
java -jar /usr/local/lib/boxlang-miniserver-1.0.0-all.jar
```

This will:

* Use the current **working dir** as the web root
* Bind to `localhost:8080`
* Configures a VERY simple web server with some default welcome files, and any CFML or BoxLang extensions will get processed by BoxLang.

{% hint style="warning" %}
**ALERT:** The BoxLang Core knows nothing of web or HTTP, so the `form`, `url`, `cookie`, and `cgi` scopes will only exist when running the BoxLang web server (but not in the REPL, etc).
{% endhint %}

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

\\
