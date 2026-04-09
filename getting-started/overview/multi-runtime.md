---
description: BoxLang can be deployed to multiple runtimes
icon: starfighter-twin-ion-engine
---

# Multi-Runtime

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

BoxLang has been designed with a lightweight, fast, and modular core. The operating system binary is a whopping **8MB** in size. This allows us to build on this binary according to the deployed runtime of choice. Check out our [installation methods.](../installation/)

### Available Runtimes

The currently available and in-development runtimes are the following:

| Runtime | Description | Status |
| :--- | :--- | :--- |
| **Android** | Ability to run BoxLang in Android Devices | *In Planning* |
| [**AWS Lambda**](../running-boxlang/aws-lambda.md) | Ability to run BoxLang with AWS Lambda | **Done** |
| **Azure Functions** | Ability to run BoxLang with Microsoft Functions | *In Progress* |
| [**CommandBox**](../running-boxlang/commandbox.md) | A BoxLang engine for CommandBox | **Done** |
| [**Docker**](../running-boxlang/docker.md) | BoxLang CLI, MiniServer and CommandBox images | **Done** |
| **Desktop** | BoxLang native Desktop Applications | *In Progress* |
| [**DigitalOcean App Platform**](../running-boxlang/digitalocean-app.md) | DigitalOcean App Platform applications | **Done** |
| **iOS** | Ability to run BoxLang in iOS Devices | *In Planning* |
| [**Google Cloud Functions**](../running-boxlang/google-cloud-functions.md) | Ability to run BoxLang with Google Cloud Functions | **Done** |
| [**JSR-223**](../running-boxlang/jsr-223-scripting.md) | Java scripting interfaces | **Done** |
| [**MiniServer**](../running-boxlang/miniserver.md) | A pure Java webserver built with BoxLang | **Done** |
| [**Spring Boot**](../running-boxlang/spring-boot.md) | A Spring Boot starter and auto configurator | **Done** |
| **Servlet WAR** | A servlet capable `war` | **Done** |
| [**OS**](../running-boxlang/) | Bare metal runtime for any OS Java runs in | **Done** |
| **WebAssembly** | Ability to run BoxLang as WebAssembly compiled code | *In Progress* |

The core impetus of BoxLang is to grow through a hierarchical approach, targeting specific runtimes with specific behaviors. For example, the concepts of FORM, URL scope, web functions, and components are available only to runtimes that support web.

**Just because a runtime isn't listed here doesn't mean BoxLang can't run on it. These are just a collection of officially supported runtimes. You can use the core runtime and run it anywhere the JVM can run. You can embed it now in Android, Azure, OpenWhisk, and more. However, once we have official runtimes, we will post them here.**

{% hint style="success" %}
All of our runtime source code can be found in our organization: [https://github.com/ortus-boxlang](https://github.com/ortus-boxlang)
{% endhint %}

### Third-Party Runtimes

We love our community. If you have created custom runtimes for BoxLang, please let us know, and we will add them here.
