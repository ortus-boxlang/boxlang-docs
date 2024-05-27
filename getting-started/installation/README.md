---
description: Getting started with BoxLang is easy!  Choose your path wisely!
---

# Installation

{% hint style="danger" %}
PLEASE NOTE THAT WE ARE STILL IN OPEN BETA. ANYTHING CAN CHANGE
{% endhint %}

## Requirements <a href="#requirements-7" id="requirements-7"></a>

* JDK 21+

{% hint style="warning" %}
BoxLang is currently compiling Java source on the fly for debugging purposes, so it requires a JDK, not a JRE, to run! Eventually, we’ll be generating bytecode directly, but for now, we have a dependency on the JDK’s Java Compiler classes.
{% endhint %}

You should be able to grab the Java 21 JDK for your OS and CPU arch here: [Download Java 21 JDK 4](https://adoptium.net/temurin/releases/?package=jdk\&version=21)

{% tabs %}
{% tab title="Mac" %}
To get started in a Mac with the BoxLang requirements, we recommend you use [homebrew](https://brew.sh/). If not, you will have to download the requirements separaterly from the link above.

```bash
# Install the latest openjdk 21 and utilities
brew install curl zip unzip openjdk
```
{% endtab %}

{% tab title="*Unix" %}
Leverage your system‘s package manager to install the needed requirements.

### APT

```bash
# Update OS first
sudo apt-get update
sudo apt-get full-upgrade

# Install requirements
sudo apt-get install curl zip unzip openjdk-21
```

### Yum

```bash
# Update OS first
sudo yum update
sudo yum upgrade

# Install requirements
sudo yum install curl zip unzip java-21-openjdk

```
{% endtab %}
{% endtabs %}

## Mac/\*Unix Quick Installer

BoxLang has been designed to run on multiple runtimes and adapt itself and the code you write to enhance itself.  Once your requirements are installed, then If you are on Mac or Unix, you can use our handy quick installer by running the following command:

```bash
# If you don’t require sudo
/bin/bash -c "$(curl -fsSL https://downloads.ortussolutions.com/ortussolutions/boxlang/install-boxlang.sh)"

# If you require sudo (Chromebooks, etc)
sudo /bin/bash -c "$(curl -fsSL https://downloads.ortussolutions.com/ortussolutions/boxlang/install-boxlang.sh)"
```

{% hint style="success" %}
The quick installer requires the following:

* Bash
* JDK21+
* `curl, unzip` installed
* Permission to copy files to `/usr/local/bin and /usr/local/lib`
{% endhint %}

The quick installer will install the OS binary and the MiniServer for you In the directories mentioned above.  The following scripts will be installed for you

* `boxlang` - Our BoxLang binary, [learn more](../running-boxlang/)
* `boxlang-miniserver` - Our BoxLang MiniServer binary, [learn more](../running-boxlang/miniserver.md)

Just run `boxlang` and you are ready to rock in our REPL or execute scripts.

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
To upgrade your installation, just re-run the quick installer and the new binaries will install.
{% endhint %}

## Binaries

We have a collection of different binaries for the different runtimes we support.  Enjoy!

### Operating System Binaries

Here you can find the installers and binaries for all Operating Systems:

* Windows Installer: \
  [https://downloads.ortussolutions.com/ortussolutions/boxlang/boxlang-snapshot-installer.exe](https://downloads.ortussolutions.com/ortussolutions/boxlang/boxlang-snapshot-installer.exe)
* Zip (All OSs): \
  [https://downloads.ortussolutions.com/ortussolutions/boxlang/1.0.0/boxlang-1.0.0.zip](https://downloads.ortussolutions.com/ortussolutions/boxlang/1.0.0/boxlang-1.0.0.zip)
* Jar: \
  [https://downloads.ortussolutions.com/ortussolutions/boxlang/1.0.0/boxlang-1.0.0-all.jar](https://downloads.ortussolutions.com/ortussolutions/boxlang/1.0.0/boxlang-1.0.0-all.jar)

### MiniServer Binaries

The BoxLang MiniServer includes the BoxLang OS runtime with the addition of our super fast and lightweight web server. &#x20;

* All OSs:\
  [https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-miniserver/1.0.0/boxlang-miniserver-1.0.0.zip](https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-miniserver/1.0.0/boxlang-miniserver-1.0.0.zip)

### AWS Lambda Binaries

BoxLang can also run on AWS Lambdas. It even powers our entry playground at [https://try.boxlang.io](https://try.boxlang.io/). &#x20;

* Runtime: \
  [https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-aws-lambda/1.0.0/boxlang-aws-lambda-1.0.0.zip](https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-aws-lambda/1.0.0/boxlang-aws-lambda-1.0.0.zip)
* Template\
  [https://github.com/ortus-boxlang/bx-aws-lambda-template](https://github.com/ortus-boxlang/bx-aws-lambda-template)

### CommandBox BoxLang Server

<div align="left">

<figure><img src="../../.gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure>

</div>

BoxLang can also be deployed using [CommandBox](https://www.ortussolutions.com/products/commandbox).  This is our preferred way to deploy web applications using BoxLang.  BoxLang +/++ Subscribers even get access to [CommandBox Pro](https://www.ortussolutions.com/products/commandbox-pro).

```bash
box install commandbox-boxlang
box server start cfengine=boxlang javaVersion=openjdk21_jdk
```

Learn more in our [CommandBox guide.](../running-boxlang/commandbox.md)

### Servlet EE Binaries

This is the servlet edition of BoxLang that you can deploy on any servlet container (Jetty, Tomcat, JBoss, etc)

* WAR: \
  [https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-servlet/1.0.0/boxlang-servlet-1.0.0.war](https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-servlet/1.0.0/boxlang-servlet-1.0.0.war)
* JAR:\
  [https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-servlet/1.0.0/boxlang-servlet-1.0.0-all.jar](https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-servlet/1.0.0/boxlang-servlet-1.0.0-all.jar)

### Docker

We have a full [Docker guide you can follow here.](../running-boxlang/docker.md)

## BoxLang IDE

<div align="left">

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption><p>BoxLang IDE</p></figcaption></figure>

</div>

The BoxLang IDE is a collection of modules for VSCode. You can find it here:

{% embed url="https://marketplace.visualstudio.com/items?itemName=ortus-solutions.vscode-boxlang" %}
Install Now
{% endembed %}

## Core Modules

The BoxLang core is lightweight and fast.  Everything that extends the core comes in the form of modules.  We have a collection of core modules that the BoxLang team maintains and curates.  We also have several enterprise modules for our BoxLang +,++ subscribers and the community also can create and share modules in our cloud package manager [FORGEBOX](https://forgebox.io).

We recommend you use CommandBox, Our CLI and Package Manager, to interact, install, and work with any package in BoxLang.

{% content-ref url="modules.md" %}
[modules.md](modules.md)
{% endcontent-ref %}

## BoxLang+, ++ Modules

Our [BoxLang+, and ++](https://boxlang.io/plans) subscribers not only get customized support but also new features, and modules.  You can find out more about our subscriptions here: [https://boxlang.io/plans](https://boxlang.io/plans).  Here are the collection of modules that you will get with your subscription.

<table><thead><tr><th width="160">Module</th><th width="424">Description</th><th width="158">Status<select><option value="7PvmwHzSW7tN" label="In Development" color="blue"></option><option value="KAAYVEqj9HUs" label="Done" color="blue"></option><option value="LZpOL7kx2Gyb" label="In Planning" color="blue"></option></select></th></tr></thead><tbody><tr><td>bx-redis</td><td>Native Redis integration for caching, session distribution, and publish-subcribe events.</td><td><span data-option="7PvmwHzSW7tN">In Development</span></td></tr><tr><td>bx-mongo</td><td>Native MongoDB integration for caching, session distribution and advanced MongoDB operations.</td><td><span data-option="7PvmwHzSW7tN">In Development</span></td></tr><tr><td>bx-couchbase</td><td>Native Couchbase integration for caching, NoSQL, session distribution and advanced Couchbase usage.</td><td><span data-option="7PvmwHzSW7tN">In Development</span></td></tr><tr><td>bx-pdftools</td><td>Our collection of enhanced PDF tooling.  Includes the ability to extract PDF forms, fill out PDF forms, squash, merge and more.</td><td><span data-option="7PvmwHzSW7tN">In Development</span></td></tr></tbody></table>

{% hint style="danger" %}
Please note that these modules are still under development, we will publish their status as we complete them.
{% endhint %}



