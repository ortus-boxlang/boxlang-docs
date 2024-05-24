---
description: Running a BoxLang server with CommandBox
---

# CommandBox

<figure><img src="../../.gitbook/assets/commandbox.png" alt=""><figcaption></figcaption></figure>

CommandBox is a standalone, native tool for Windows, Mac, and Linux that will provide you with a Command Line Interface (CLI) for developer productivity, tool interaction, package management, embedded JEE server, application scaffolding, and sweet ASCII art.&#x20;

It seamlessly integrates to work with any of [Ortus Solutions](http://www.ortussolutions.com/products) \*Box products, but it is also open for extensibility for any BoxLang or ColdFusion (CFML) project.

{% hint style="success" %}
The steps below will become unnecessary once CommandBox has been fully ported to BoxLang.
{% endhint %}

### Install the Module <a href="#versioning" id="versioning"></a>

CommandBox neds (for the moment) the `commandbox-boxlang` module in order to start BoxLang servers.  So let's go ahead and install it:

```bash
install commandbox-boxlang
```

This will add the right file types and handlers to CommandBox for BoxLang.

### Start up a Server

This guide is short and sweet.  The hard part has been done.  Now you can startup a BoxLang server just like any other CommandBox server.  So just go to your webroot of your choosing and run:

```bash
server start cfengine=boxlang javaVersion=openjdk21_jdk
```

Enjoy your server!

### Server Home

Like any other CommandBox server, the servers will be stored in the CommandBox Home of your setup.  The `boxlang.json` , class folders, modules, will all be installed here.

### Installing BoxLang Modules

Just like with any server, you can also install modules into the BoxLang server.

```bash
install bx-mysql, bx-derby
```

That's it. CommandBox knows where to put them and manage them.

### Server.json

You acn also make your CommandBox server portable with a `server.json` file:

```json
{
    "app":{
        "cfengine":"boxlang",
        "serverHomeDirectory":".engine/boxlang"
    },
    "name":"myServer",
    "openBrowser":true,
    "web":{
        "rewrites":{
            "enable":true
        },
    },
    "cfconfig":{
        "file":".cfconfig.json"
    },
    "env":{
    },
    "scripts" : {
 	"onServerInitialInstall":"install bx-mail,bx-mysql,bx-derby,bx-compat"
   }
}

```
