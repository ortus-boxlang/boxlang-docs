---
description: Getting started with BoxLang is easy!  Choose your path wisely!
icon: sign-posts-wrench
---

# Installation

BoxLang can be deployed on multiple runtimes, and each runtime can be set up differently.  We recommend you leverage the "Running BoxLang" section for those specific runtimes.  We recommend getting started by installing BoxLang at the global operating system level first.  This is what this guide does! &#x20;

**You can choose to either install a single version of BoxLang (Quick Installer) or our BoxLang Version Manager (BVM), so you can manage multiple versions of BoxLang on your operating system.**

## Requirements <a href="#requirements-7" id="requirements-7"></a>

BoxLang is a JVM language, so we need a JVM.  You should be able to grab the Java 21 JRE for your OS and CPU arch here: [Download Java 21 JRE](https://adoptium.net/temurin/releases/?package=jre\&version=21). Alternatively, see the tabs below for instructions on how to automate it.

{% hint style="warning" %}
To use our BoxLang/CFML to Java transpiler, you must have the JDK installed, not the JRE.
{% endhint %}

{% tabs %}
{% tab title="🍎 Mac" %}
We recommend using [homebrew](https://brew.sh/) to get started on a Mac with the **BoxLang** requirements. If not, you must download the requirements separately from the link above.

```bash
brew install openjdk@21
```

Once the requirements are installed, move down to the quick installer.
{% endtab %}

{% tab title="🐧 *Unix/Linux" %}
Leverage your system‘s package manager to install the needed requirements.

**APT**

```bash
# Update OS first
sudo apt-get update
sudo apt-get full-upgrade

# Install requirements
sudo apt-get install openjdk-21-jre
```

**Yum**

```bash
# Update OS first
sudo yum update
sudo yum upgrade

# Install requirements
sudo yum install java-21-openjdk

```

Note that you may need to tell the system to use the correct JDK version. This can be done via `update-alternatives --config java` (sudo may be required).

**XBPS (Voidlinux)**

```bash
# Update OS first
sudo xbps-install -Su

# Install requirements
sudo xbps-install openjdk21

```

Note that you may need to tell the system to use the correct JDK version. This can be done via `sudo xbps-alternatives -g jdk -s openjdk21`

**Arch Linux Variants**

```bash
# Update OS first
sudo pacman -Syu

# Install requirements
sudo pacman -S jre21-openjdk

```

Note that you may need to tell the system to use the correct JDK version. This can be done via `sudo archlinux-java set java-21-openjdk`
{% endtab %}

{% tab title="🪟 Windows" %}


Use the following PowerShell script to install the JRE 21. \
**HOWEVER, MAKE SURE YOU RUN THIS AS AN ADMINISTRATOR.**

```powershell
powershell -NoExit -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://downloads.ortussolutions.com/ortussolutions/boxlang-quick-installer/helpers/install-jre.ps1'))"
```

* Once this runs, the JRE will be installed in your `C:\Program Files\Java\jre{version}`
* A `JAVA_HOME` will be created for you

{% hint style="danger" %}
Ensure you restart any terminal windows for the changes to take effect.
{% endhint %}
{% endtab %}
{% endtabs %}

## Quick Installer

Once the requirements above are installed, to get started quickly with BoxLang, use our **BoxLang Quick Installer** for Mac, Linux,\* Nix, or Windows.  This will allow you to execute the script in your favorite terminal application.  Please note that some OS will require you to run it as an `administrator` or with `sudo` capabilities.

You can see the full documentation for the quick installer in the link below:

{% content-ref url="boxlang-quick-installer.md" %}
[boxlang-quick-installer.md](boxlang-quick-installer.md)
{% endcontent-ref %}

Let's get started:

{% tabs %}
{% tab title="Bash / ZSH" %}
Just copy the following into your terminal to install by default for your user.

```bash
/bin/bash -c "$(curl -fsSL https://install.boxlang.io)"
```

If you want a system-wide installation, then prefix it with `sudo`:

```bash
sudo /bin/bash -c "$(curl -fsSL https://install.boxlang.io)"
```

Please make sure you use the `--help` on our scripts to see everything you can do with them.
{% endtab %}

{% tab title="SH" %}
Just copy the following into your terminal to install be default for your user.

```bash
/bin/sh -c "$(curl -fsSL https://install.boxlang.io)"
```

If you want a system-wide installation then prefix it with `sudo`:

```bash
sudo /bin/sh -c "$(curl -fsSL https://install.boxlang.io)"
```

Please make sure you use the `--help` on our scripts to see everything you can do with them.
{% endtab %}

{% tab title="Windows PowerShell" %}
Just copy this into a Powershell Terminal.\
**HOWEVER, MAKE SURE YOU RUN THIS AS AN ADMINISTRATOR.**

```powershell
powershell -NoExit -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://install-windows.boxlang.io'))"
```

Please make sure you use the `--help` on our scripts to see everything you can do with them.
{% endtab %}
{% endtabs %}

{% hint style="danger" %}
If your system requires admin privileges (Like Chromebooks or Linux distros), make sure you use `sudo` or make sure the `/usr/local` folder is yours as the owner.
{% endhint %}

The quick installer will install the latest stable **BoxLang** **OS** binary and the **MiniServer** in the above directories. It will also install the following scripts for you:

* `boxlang` - Our BoxLang binary runner, [learn more](../running-boxlang/)
* `boxlang-miniserver` - Our BoxLang MiniServer binary runner, [learn more](../running-boxlang/miniserver.md)
* `install-boxlang` - The quick installer so you can reuse it to upgrade your installations or install the `snapshot` version of BoxLang.  Run `install-boxlang --help` for more commands.
* `install-bx-module` - A module installer. Just pass in the slug of the module, an optional version or a list of modules.  Run `install-bx-module` for more commands.

```bash
# Test BoxLang works:
boxlang --version

# Get Help
install-boxlang --help

# Upgrade your installation
install-boxlang

# Uninstall
install-boxlang --uninstall

# Install a single module
install-bx-module bx-compat-cfml

# Install a specific version of a module
install-bx-module bx-compat-cfml@1.11.0

# Install multiple async modules
install-bx-module bx-compat-cfml bx-esapi bx-pdf

# Remove a module
install-bx-module --remove bx-esapi

# List your modules
install-bx-module --list

# Get all the help
install-bx-module --help
```

### Upgrading Your Install

The `install-boxlang` script will allow you to upgrade your OS installation easily. If you call it without arguments, it will install the **latest stable** release and override the local install. You can also pass a specific version to install as the second argument, or the word `snapshot`to install the bleeding edge release.  You can find all the latest artifacts here: [https://downloads.ortussolutions.com/#/ortussolutions/boxlang/](https://downloads.ortussolutions.com/#/ortussolutions/boxlang/)

```bash
# Upgrade to the latest stable version
install-boxlang

# Upgrade or Downgrade to a specific version
install-boxlang 1.0.0

# Use the latest snapshot
install-boxlang snapshot
```

{% hint style="success" %}
You can get the version of the current BoxLang Runtime by running `boxlang --version`
{% endhint %}

### Installing Modules

You can use the `install-bx-module` binary to install modules into your boxlang home. Just pass in the name of the slug you want. You can use the `install bx-modules`to install multiple modules at once as well.

{% hint style="info" %}
All our modules are available in the cloud software directory [FORGEBOX](https://forgebox.io/type/boxlang-modules). You can also register and collaborate with modules of your own :person\_raising\_hand:.
{% endhint %}

#### Install to the BoxLang Home

```bash
# install individual modules
install-bx-module bx-compat-cfml
install-bx-module bx-esapi

# install multiple modules
install-bx-module bx-compat-cfml bx-esapi
```

#### Install Locally

You can also install modules to the running application (CLI, web) by using the `--local`option in the command. This will create a `boxlang_modules`folder from which you ran the command and install the modules locally.

```bash
# install individual modules
install-bx-module bx-compat-cfml --local
install-bx-module bx-esapi --local

# install multiple modules
install-bx-module bx-compat-cfml bx-esapi --local
```

## BoxLang Version Manager (BVM)

BVM is a simple version manager for BoxLang, similar to jenv or nvm. It allows you to easily install, manage, and switch between different versions of BoxLang.  Read the full documentation at the link below:

{% content-ref url="boxlang-version-manager-bvm.md" %}
[boxlang-version-manager-bvm.md](boxlang-version-manager-bvm.md)
{% endcontent-ref %}

To get started easily just follow the instructions:

```bash
# Install BVM
curl -fsSL https://install-bvm.boxlang.io/ | bash

# Or download and run locally
wget --content-disposition https://install-bvm.boxlang.io/
chmod +x install-bvm.sh
./install-bvm.sh
```

## R.E.P.L.

**Read, Evaluate, Print Loop**

A REPL, or Read-Evaluate-Print Loop, is an interactive programming environment that takes single-user inputs, executes them, and returns the result to the user. This is particularly useful for testing code snippets and debugging in real time. In the context of BoxLang, running `boxlang` will start the REPL, allowing you to write and test code quickly within the BoxLang environment.

The REPL will also remember state, so you can define variables and use them in your testing and explorations. Code away :rocket:

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

## Binaries

The quick installer is the best and easiest way to get installed on Mac or \*Nix. However, below, you can find a collection of all our installers and binaries for running BoxLang and each Runtime.

### Operating System Binaries

Here, you can find the installers and binaries for all Operating Systems:

* Windows Installer:\
  [https://downloads.ortussolutions.com/ortussolutions/boxlang/boxlang-installer.exe](https://downloads.ortussolutions.com/ortussolutions/boxlang/boxlang-installer.exe)
* Zip (All OSs):\
  [https://downloads.ortussolutions.com/ortussolutions/boxlang/boxlang-latest.zip](https://downloads.ortussolutions.com/ortussolutions/boxlang/boxlang-latest.zip)
* Jar:\
  [https://downloads.ortussolutions.com/ortussolutions/boxlang/boxlang-latest-all.jar](https://downloads.ortussolutions.com/ortussolutions/boxlang/boxlang-latest-all.jar)
* Quick Installer (Mac/\*nix)\
  [https://downloads.ortussolutions.com/ortussolutions/boxlang/install-boxlang.sh](https://downloads.ortussolutions.com/ortussolutions/boxlang/install-boxlang.sh)

### MiniServer Binaries

The BoxLang MiniServer includes the BoxLang OS runtime with the addition of our super-fast and lightweight web server.

* All OSs:\
  [https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-miniserver/boxlang-miniserver-latest.zip](https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-miniserver/boxlang-miniserver-latest.zip)

### AWS Lambda Binaries

BoxLang can also run on AWS Lambdas. It even powers our entry playground at [https://try.boxlang.io](https://try.boxlang.io/).

* Runtime:\
  [https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-aws-lambda/boxlang-aws-lambda-latest-all.jar](https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-aws-lambda/boxlang-aws-lambda-latest-all.jar)
* Template\
  [https://github.com/ortus-boxlang/boxlang-starter-aws-lambda](https://github.com/ortus-boxlang/boxlang-starter-aws-lambda)

### CommandBox BoxLang Server

BoxLang can also be deployed using [CommandBox](https://www.ortussolutions.com/products/commandbox). This is our preferred way to deploy web applications using BoxLang. BoxLang +/++ Subscribers even get access to [CommandBox Pro](https://www.ortussolutions.com/products/commandbox-pro). Note: This installation method is typically tailored for a specific web application and is not typically accessible by other applications.

```bash
box install commandbox-boxlang
box server start cfengine=boxlang javaVersion=openjdk21_jdk
```

Learn more in our [CommandBox guide.](../running-boxlang/commandbox.md)

### Servlet EE Binaries

This is the servlet edition of BoxLang that you can deploy on any servlet container (Jetty, Tomcat, JBoss, etc)

* WAR:\
  [https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-servlet/boxlang-servlet-latest.war](https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-servlet/boxlang-servlet-latest.war)
* JAR:\
  [https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-servlet/boxlang-servlet-latest-all.jar](https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-servlet/boxlang-servlet-latest-all.jar)

### Docker

We have a full [Docker guide you can follow here.](../running-boxlang/docker.md)

## BoxLang IDE

<div align="left"><figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption><p>BoxLang IDE</p></figcaption></figure></div>

The BoxLang IDE is a collection of modules for VSCode that will give you a line debugger, LSP (Language Server Protocol), highlighting, introspection, generation, and much more. You can find it here:

{% embed url="https://marketplace.visualstudio.com/items?itemName=ortus-solutions.vscode-boxlang" %}
Install Now
{% endembed %}

## Core Modules

The BoxLang core is lightweight and fast. Everything that extends the core comes as modules or individual runtimes. We have a collection of core modules that the BoxLang team maintains and curates. We also have several enterprise modules for our **BoxLang +, ++** subscribers, and the community can create and share modules in our cloud package manager [FORGEBOX](https://forgebox.io).

{% content-ref url="modules.md" %}
[modules.md](modules.md)
{% endcontent-ref %}

## BoxLang+, ++ Modules

Our [BoxLang+, and ++](https://boxlang.io/plans) subscribers not only get professional/customized support but also new features, and modules. You can find out more about our subscriptions here: [https://boxlang.io/plans](https://boxlang.io/plans). Here is the collection of modules that you will get with your subscription which are not part of the open source edition.

<table><thead><tr><th width="160">Module</th><th width="424">Description</th><th width="158">Status<select><option value="7PvmwHzSW7tN" label="In Development" color="blue"></option><option value="KAAYVEqj9HUs" label="Done" color="blue"></option><option value="LZpOL7kx2Gyb" label="In Planning" color="blue"></option></select></th></tr></thead><tbody><tr><td><strong>bx-redis</strong></td><td>Native Redis integration is used for caching, session distribution, and publish-subscribe events.<br><br><code>install-bx-module bx-redis</code></td><td><span data-option="KAAYVEqj9HUs">Done</span></td></tr><tr><td><strong>bx-mongo</strong></td><td>Native MongoDB integration for caching, session distribution and advanced MongoDB operations.</td><td><span data-option="7PvmwHzSW7tN">In Development</span></td></tr><tr><td><strong>bx-couchbase</strong></td><td>Native Couchbase integration for caching, NoSQL, session distribution and advanced Couchbase usage.</td><td><span data-option="7PvmwHzSW7tN">In Development</span></td></tr><tr><td><strong>bx-pdftools</strong></td><td>Our collection of enhanced PDF tooling. Includes the ability to extract PDF forms, fill out PDF forms, squash, merge and more.</td><td><span data-option="7PvmwHzSW7tN">In Development</span></td></tr></tbody></table>
