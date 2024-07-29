---
description: Learn how to code with BoxLang and your favorite Chromebook!
---

# Chromebooks

<figure><img src="../../.gitbook/assets/chromebooks.png" alt=""><figcaption></figcaption></figure>

We love Chromebooks, so this guide is for those who want to run and develop BoxLang applications using Intel-based or ARM-based Chromebooks.  We will install all the prerequisites, BoxLang, and VSCode to use the BoxLang IDE and create our first application.

{% embed url="https://www.google.com/chromebook/" %}

<figure><img src="../../.gitbook/assets/CB_Hero_Base.width-1200.format-webp.webp" alt=""><figcaption><p><a href="https://www.google.com/chromebook/">https://www.google.com/chromebook/</a></p></figcaption></figure>

### Requirements

* 4GB RAM Chromebook minimum
* Linux Developer Environment
* JDK 21+

### Linux Environment

Chromebooks are great as they allow you to install a Debian Linux container alongside your OS.  You can do so easily by opening `Settings > Advanced > Developers` and installing the Linux environment.  Go through the wizard, and voila! Debian Linux will be installed alongside your Chrome OS. &#x20;

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-23 19.44.51.png" alt=""><figcaption><p>Install Linux</p></figcaption></figure>

### Terminal

You will be interacting with the Linux installation via the Terminal application.

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-23 19.51.21.png" alt=""><figcaption></figcaption></figure>

Once you open the terminal, you can click on the `Penguin` tab, and it will open the Linux terminal.

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-23 19.45.53 (1).png" alt=""><figcaption></figcaption></figure>

### Installing Pre-Requisites

Let's begin by installing all pre-requisites first:

```bash
# Let's update the OS first
sudo apt-get update
sudo apt-get full-upgrade

# Now, some tooling
sudo apt-get install zip unzip curl git gnome-keyring
```

### Installing Java

{% hint style="warning" %}
Right now, some distros do not have OpenJDK 21 yet.  If not, it would be as easy as `sudo apt install openjdk-21` . However, we will do it manually at the moment.
{% endhint %}

You can download the OpenJDK 21 For your current architecture from here: [https://adoptium.net/temurin/releases/?os=linux](https://adoptium.net/temurin/releases/?os=linux)

* ARM - [https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.3%2B9/OpenJDK21U-jdk\_aarch64\_linux\_hotspot\_21.0.3\_9.tar.gz](https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.3%2B9/OpenJDK21U-jdk\_aarch64\_linux\_hotspot\_21.0.3\_9.tar.gz)
* x64 - [https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.3%2B9/OpenJDK21U-jdk\_x64\_linux\_hotspot\_21.0.3\_9.tar.gz](https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.3%2B9/OpenJDK21U-jdk\_x64\_linux\_hotspot\_21.0.3\_9.tar.gz)

You can use the following in your CLI to do it easier:

```bash
wget {url from above}

# I have an ARM processor
wget 
https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.3%2B9/OpenJDK21U-jdk_aarch64_linux_hotspot_21.0.3_9.tar.gz

# Gunzip it
gunzip OpenJDK21U-jdk_aarch64_linux_hotspot_21.0.3_9.tar.gz
# Untar it
tar -xvf OpenJDK21U-jdk_aarch64_linux_hotspot_21.0.3_9.tar
# Move it to the /usr/lib/jvm folder
mv jdk-21.0.3+9/ /usr/lib/jvm/
```

Now add the `JAVA_HOME` and the path to the jvm in your `PATH` using your bash profile

```bash
edit .bashrc

export JAVA_HOME=/usr/lib/jvm/jdk-11.0.3_9
export PATH=$PATH:/usr/lib/jvm/jdk-11.0.3_9/bin
```

Once you add this to your bash profile, either source your shell or type `bash` or close and startup again

```bash
# Source your shell
$ source .bashrc

$ java -version
openjdk version "17.0.11" 2024-04-16
OpenJDK Runtime Environment (build 17.0.11+9-Debian-1deb12u1)
OpenJDK 64-Bit Server VM (build 17.0.11+9-Debian-1deb12u1, mixed mode, sharing)
```

{% hint style="info" %}
Please note that this will become a one-liner in future distros.  If your distro supports it, you can do `sudo apt install openjdk-21` and be done with this step easily.
{% endhint %}

### Installing BoxLang

This is the easy part, just type the following command:

```bash
sudo /bin/bash -c "$(curl -fsSL https://downloads.ortussolutions.com/ortussolutions/boxlang/install-boxlang.sh)"
```

This will run the BoxLang installer.  Once you are done, just type `boxlang` and boom! We have BoxLang installed!

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

This opens the REPL and you can start coding away, running BoxLang files, starting servers and so much more.

### VSCode BoxLang

Now that we have BoxLang installed, let's get VSCode so you can use this awesome editor for BoxLang coding!

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Choose the debian according to your processor and download the package.  Then double click it and run the installer.  Once done, you will have a new icon in your apps called `Visual Studio Code`. Click it and open it.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

Now go to the Extensions Marketplace and search for `BoxLang`.  Then install the extension

<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

Now we are cooking.  Create a file using the editor and call it `Hello.bx`

```groovy
class{

    function main( args = [] ){
    
        println( "Hello from Chromebook land and BoxLang on #now()#" )
    
    }

}
```

<figure><img src="../../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

Now right-click on the editor and say `BoxLang: Run File`

```
Hello from Chromebook land and BoxLang on {ts '2024-05-23 18:27:33'}
```

You have coded your first BoxLang class and ran it!  Great job!  Let's make it harder now and start a web application.  Create a file and call it `index.bxm` , these are templating files like HTML but spiced up with BoxLang!

```xml
<bx:output>
Hello from Chromebook land #now()#
</bx:output>
```

This uses the `<bx:output>` component to produce output on the website.  Then we reuse the `now()` built-in function to spit out the date.  You can find all about our templating syntax in the language section.  Now let's run our BoxLang MiniServer!  Open a command palette in VSCode and search for `BoxLang`

<figure><img src="../../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>

Now click the `Run Web Server`. You will get the following in the debug console:

```
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

It will open the browser for you as well:

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

You have now created your very first BoxLang web application. Good for you!  Now keep exploring the language syntax and framework so you can now take it to the next level!  Enjoy!

{% hint style="success" %}
This entire guide was written in my awesome Lenovo Duet 5 Chromebook!
{% endhint %}
