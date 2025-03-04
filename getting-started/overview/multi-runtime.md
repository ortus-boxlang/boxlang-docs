---
icon: starfighter-twin-ion-engine
description: BoxLang can be deployed to multiple runtimes
---

# Multi-Runtime

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

BoxLang has been designed with a lightweight, fast, and modular core.  The operating system binary is a whopping **8MB** in size.  This allows us to build on this binary according to the deployed runtime of choice.  Check out our [installation methods.](../installation/)

### Available Runtimes

The currently available and in-development runtimes are the following:

<table><thead><tr><th width="176">Runtime</th><th width="420">Description</th><th>Status<select><option value="cMUAhLvVhult" label="Done" color="blue"></option><option value="TMVEyyxmm5bg" label="In Progress" color="blue"></option><option value="J7HvD8eZZTpl" label="In Planning" color="blue"></option></select></th></tr></thead><tbody><tr><td><a href="../running-boxlang/"><strong>OS</strong></a></td><td>Bare metal runtime for any OS Java runs in</td><td><span data-option="cMUAhLvVhult">Done</span></td></tr><tr><td><a href="../running-boxlang/jsr-223-scripting.md"><strong>JSR-223</strong></a></td><td>Java scripting interfaces</td><td><span data-option="cMUAhLvVhult">Done</span></td></tr><tr><td><a href="../running-boxlang/miniserver.md"><strong>MiniServer</strong></a></td><td>A pure Java webserver built with BoxLang</td><td><span data-option="cMUAhLvVhult">Done</span></td></tr><tr><td><strong>Servlet WAR</strong></td><td>A servlet capable <code>war</code></td><td><span data-option="cMUAhLvVhult">Done</span></td></tr><tr><td><a href="../running-boxlang/commandbox.md"><strong>CommandBox</strong></a></td><td>A BoxLang engine for CommandBox</td><td><span data-option="cMUAhLvVhult">Done</span></td></tr><tr><td><a href="../running-boxlang/aws-lambda.md"><strong>AWS Lambda</strong></a></td><td>Ability to run BoxLang with AWS Lambda</td><td><span data-option="cMUAhLvVhult">Done</span></td></tr><tr><td><a href="../running-boxlang/docker.md"><strong>Docker</strong></a></td><td>BoxLang CLI, MIniServer and CommandBox images</td><td><span data-option="cMUAhLvVhult">Done</span></td></tr><tr><td><strong>Azure Functions</strong></td><td>Ability to run BoxLang with Microsoft Functions</td><td><span data-option="TMVEyyxmm5bg">In Progress</span></td></tr><tr><td><strong>Google Cloud Functions</strong></td><td>Ability to run BoxLang with Google Cloud Functions</td><td><span data-option="TMVEyyxmm5bg">In Progress</span></td></tr><tr><td><strong>Android</strong></td><td>Ability to run BoxLang in Android Devices</td><td><span data-option="J7HvD8eZZTpl">In Planning</span></td></tr><tr><td><strong>iOS</strong></td><td>Ability to run BoxLang in iOS Devices</td><td><span data-option="J7HvD8eZZTpl">In Planning</span></td></tr><tr><td><strong>WebAssembly</strong></td><td>Ability to run BoxLang as WebAssembly compiled code</td><td><span data-option="J7HvD8eZZTpl">In Planning</span></td></tr></tbody></table>

The core impetus of BoxLang is to grow in a hierarchical approach to target specific runtimes with specific behavior for particular runtimes.  For example, the concept of a FORM, URL scope, or web functions and components are only available to those runtimes that offer web support.

**Just because a runtime is not listed here doesn't mean BoxLang can't run there.  These are just a collection of officially supported runtimes.  You can use the core runtime and make it run ANYWHERE the JVM can be run.  You can embed it now in Android, Azure, OpenWhisk, and more.  However, once we have official runtimes, we will post them here.**

{% hint style="success" %}
All of our runtime source code can be found in our organization: [https://github.com/ortus-boxlang](https://github.com/ortus-boxlang)
{% endhint %}



### Third-Party Runtimes

We love our community, and if you have created custom runtimes for BoxLang, please let us know, and we will add them here.

