---
description: Getting started with BoxLang is easy!  Choose your path wisely!
---

# Installation

{% hint style="danger" %}
PLEASE NOTE THAT WE ARE STILL IN OPEN BETA. ANYTHING CAN CHANGE
{% endhint %}

### Requirements <a href="#requirements-7" id="requirements-7"></a>

BoxLang is explicitly compiled for Java 17+ right now (it will be 21 soon as our standard). We’re exploring how far back to support, but please download Java 17+ for now.&#x20;

BoxLang is currently compiling Java source on the fly, so it requires a JDK, not a JRE, to run! Eventually, we’ll be generating bytecode directly, but for now, we have a dependency on the JDK’s Java Compiler classes.

You should be able to grab the Java 17 JDK for your OS and CPU arch here: [Download Java 17 JDK 5](https://adoptium.net/temurin/releases/?package=jdk\&version=17)

You should be able to grab the Java 21 JDK for your OS and CPU arch here: [Download Java 21 JDK 4](https://adoptium.net/temurin/releases/?package=jdk\&version=21)

### **Runtime Binaries**

BoxLang has been designed to run on multiple runtimes and adapt itself and the code you write to enhance itself.   If you are on Mac or Unix, you can use our handy quick installer by running the following command:

```bash
/bin/bash -c "$(curl -fsSL https://downloads.ortussolutions.com/ortussolutions/boxlang/install-boxlang.sh)"
```

{% hint style="success" %}
The quick installer requires the following:

* Bash or ZSH or SH
* Any JDK21+
* `curl, unzip` installed
* Permission to copy files to `/usr/local/bin and /usr/local/lib`
{% endhint %}

Below are the available runtimes:

* Any OS
* MiniServer
* AWS Lambda
* CommandBox
* Servlet Containers
* Docker

<details>

<summary><img src="../../.gitbook/assets/image (2) (1).png" alt=""></summary>

This installation is for any operating system (Windows, Unix, Mac OS)

* Windows Installer: [https://downloads.ortussolutions.com/ortussolutions/boxlang/boxlang-snapshot-installer.exe](https://downloads.ortussolutions.com/ortussolutions/boxlang/boxlang-snapshot-installer.exe)
* Zip (All OSs): [https://downloads.ortussolutions.com/ortussolutions/boxlang/1.0.0/boxlang-1.0.0.zip](https://downloads.ortussolutions.com/ortussolutions/boxlang/1.0.0/boxlang-1.0.0.zip)
* Jar: \
  [https://downloads.ortussolutions.com/ortussolutions/boxlang/1.0.0/boxlang-1.0.0-all.jar](https://downloads.ortussolutions.com/ortussolutions/boxlang/1.0.0/boxlang-1.0.0-all.jar)

</details>

<details>

<summary><img src="../../.gitbook/assets/image (3) (1).png" alt=""></summary>

The BoxLang MiniServer includes the BoxLang OS runtime with the addition of our super fast and lightweight web server. &#x20;

* All OSs:\
  [https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-miniserver/1.0.0/boxlang-miniserver-1.0.0.zip](https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-miniserver/1.0.0/boxlang-miniserver-1.0.0.zip)

</details>

<details>

<summary><img src="../../.gitbook/assets/image (4) (1).png" alt=""></summary>

BoxLang can also run on AWS Lambdas. It even powers our entry playground at https://try.boxlang.io. &#x20;

* Runtime: \
  [https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-aws-lambda/1.0.0/boxlang-aws-lambda-1.0.0.zip](https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-aws-lambda/1.0.0/boxlang-aws-lambda-1.0.0.zip)
* Template\
  [https://github.com/ortus-boxlang/bx-aws-lambda-template](https://github.com/ortus-boxlang/bx-aws-lambda-template)

</details>

<details>

<summary><img src="../../.gitbook/assets/image (6) (1).png" alt="" data-size="original"></summary>

BoxLang can also be deployed using [CommandBox](https://www.ortussolutions.com/products/commandbox).  This is our preferred way to deploy web applications using BoxLang.  BoxLang +/++ Subscribers even get access to [CommandBox Pro](https://www.ortussolutions.com/products/commandbox-pro).

```bash
box install commandbox-boxlang
box server start cfengine=boxlang javaVersion=openjdk21_jdk
```

</details>

<details>

<summary>Java/Jakarta EE (Servlet) Runtime</summary>

This is the servlet edition of BoxLang that you can deploy on any servlet container (Jetty, Tomcat, JBoss, etc)

* WAR: \
  [https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-servlet/1.0.0/boxlang-servlet-1.0.0.war](https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-servlet/1.0.0/boxlang-servlet-1.0.0.war)
* JAR:\
  [https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-servlet/1.0.0/boxlang-servlet-1.0.0-all.jar](https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-servlet/1.0.0/boxlang-servlet-1.0.0-all.jar)

</details>

{% content-ref url="../running-boxlang/docker.md" %}
[docker.md](../running-boxlang/docker.md)
{% endcontent-ref %}

{% hint style="success" %}
CommandBox is a standalone, native tool for Windows, Mac, and Linux that will provide you with a Command Line Interface (CLI) for developer productivity, tool interaction, package management, embedded Java/Web server, application scaffolding, and some sweet ASCII art.

It seamlessly integrates to work with any of our \*Box products but it is also open for extensibility for any BoxLang project as it is also written in BoxLang using our concepts of CommandBox Commands. It tightly integrates with our contribution community; [ForgeBox](https://www.forgebox.io/), so developers can share modules world-wide.

[https://www.ortussolutions.com/products/commandbox](https://www.ortussolutions.com/products/commandbox)
{% endhint %}

### BoxLang IDE

<div align="left">

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption><p>BoxLang IDE</p></figcaption></figure>

</div>

We have also created an IDE for you to code using Microsoft VSCode.  You can find it here:

{% embed url="https://marketplace.visualstudio.com/items?itemName=ortus-solutions.vscode-boxlang" %}
Install Now
{% endembed %}

### Core Modules

BoxLang offers a plethora of modules to enhance itself.  In the following page you will find the core mo, ForgeBox, so d[ebox.io](https://forgebox.io)  to browse core and third-party modules.

We recommend you use CommandBox, Our CLI and Package Manager, to interact, install, and work with any package in BoxLang.

{% content-ref url="modules.md" %}
[modules.md](modules.md)
{% endcontent-ref %}

### BoxLang+, ++ Modules

Our BoxLang+, and ++ subscribers not only get customized support but also new features, and modules.  You can find out more about our subscriptions here: [https://boxlang.io/plans](https://boxlang.io/plans)

<table><thead><tr><th width="220">Module</th><th>Description</th></tr></thead><tbody><tr><td>bx-redis</td><td>Native Redis integration for caching, session distribution, and publish-subcribe events.</td></tr><tr><td>bx-mongo</td><td>Native MongoDB integration for caching, session distribution and advanced MongoDB operations.</td></tr><tr><td>bx-couchbase</td><td>Native Couchbase integration for caching, NoSQL, session distribution and advanced Couchbase usage.</td></tr><tr><td>bx-pdftools</td><td>Our collection of enhanced PDF tooling.  Includes the ability to extract PDF forms, fill out PDF forms, squash, merge and more.</td></tr></tbody></table>





