---
icon: square-terminal
description: CommandBox is the package manager, CLI and enterprise servlet server for BoxLang, now available in pure BoxLang as the bx-cli module
---

# CommandBox CLI

<div align="center">

<figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

</div>

[**CommandBox**](https://commandbox.ortusbooks.com) is our package manager, CLI and enterprise servlet server. It is now available in pure BoxLang as the **`bx-cli`** module, so it runs on BoxLang itself. You get:

* A **package manager** with [ForgeBox](https://www.forgebox.io) integration
* A **CLI and REPL** to run commands, recipes, tasks and workflows
* An **enterprise servlet server** with rewrites, SSL and more

It is still CommandBox and still the same `box` command you already know, now powered by BoxLang instead of Lucee.

{% hint style="info" %}
**Coming soon to BoxLang itself.** This November, bx-cli will ship as part of BoxLang. Until then, install it as a module as shown below. The module is at version 7 release candidate stage, so report any issues you find in the [CommandBox repository](https://github.com/Ortus-Solutions/commandbox).
{% endhint %}

## Features

* Operating system integration for executing commands
* Create and execute commands built with BoxLang and CFML
* ForgeBox integration for cloud package management and installation
* ColdBox Platform, TestBox and ContentBox CMS integrations
* Integrated servlet server with rewrite capabilities
* Command recipes and execution
* Interactive workflows and installers via the CLI
* Workflows and tasks

## Requirements

* BoxLang `1.17.0` or newer
* JRE/JDK 21+
* 256MB+ RAM and 250MB+ free disk space

## Install

{% stepper %}
{% step %}
### Install BoxLang

Use the [quick installer](../installation/boxlang-quick-installer.md), [BVM](../installation/boxlang-version-manager-bvm.md) or [Homebrew](../installation/homebrew.md).
{% endstep %}

{% step %}
### Install the module

```bash
install-bx-module bx-cli
```

Or with the module manager:

```bash
bx-module install bx-cli
```
{% endstep %}

{% step %}
### Make sure the `bin` folder is on your PATH

The module registers the `box` executable in the `bin` folder of your BoxLang home, usually `~/.boxlang/bin`. Add it to your `PATH` if your installer has not already done so.
{% endstep %}

{% step %}
### Verify

```bash
box version
```
{% endstep %}
{% endstepper %}

{% hint style="info" %}
You can also launch it through the runtime without the `box` executable:

```bash
boxlang cli
```
{% endhint %}

## Use

Start the interactive shell by running `box` with no arguments, or run a command directly.

{% tabs %}
{% tab title="Packages" %}
```bash
# Install a package from ForgeBox
box install coldbox

# Install everything in box.json
box install

# Search ForgeBox
box forgebox search term
```
{% endtab %}

{% tab title="Servers" %}
```bash
# Start a server from the current folder
box server start

# Check and stop it
box server list
box server stop
```
{% endtab %}

{% tab title="Scaffolding" %}
```bash
# Create a ColdBox application
coldbox create app skeleton=cbgenesis

# Run tests with TestBox
box testbox run
```
{% endtab %}

{% tab title="Run code" %}
```bash
# Open the REPL
box repl

# Run a task or a script
box task run
```
{% endtab %}
{% endtabs %}

Every command, flag and server option is covered in the [CommandBox documentation](https://commandbox.ortusbooks.com), and the same commands work in bx-cli.

## Your Existing CommandBox Home

bx-cli reuses your previous CommandBox home, so you keep:

* Modules
* Servers and server JREs
* Artifacts
* Configuration
* History

You can even share one CommandBox home between a CommandBox 6.x installation and bx-cli (7.x) at the same time.

## bx-cli and Lucee-Based CommandBox

{% hint style="warning" %}
Lucee-based CommandBox 6.x continues to be supported for **security patches only**. New features land in bx-cli. Plan to move to bx-cli.
{% endhint %}

Because bx-cli runs on BoxLang, anything that depends on Lucee-specific code will not work. Known examples:

* The CFLint module uses a Lucee-specific OSGi helper
* Task runners with Lucee-specific code

Many popular modules load without errors, including `testbox-cli`, `coldbox-cli`, `commandbox-cfconfig`, `commandbox-dotenv`, `commandbox-docbox`, `commandbox-cfformat`, `wheels-cli` and `contentbox-cli`.

## BoxLang in CI

Install the module in GitHub Actions with the [setup-boxlang](https://github.com/ortus-boxlang/setup-boxlang) action:

```yaml
- uses: ortus-boxlang/setup-boxlang@1.6.0
  with:
    modules: bx-cli
```

## Learn More

* [CommandBox documentation](https://commandbox.ortusbooks.com)
* [ForgeBox](https://www.forgebox.io)
* [Running BoxLang with CommandBox](../running-boxlang/commandbox.md)
* [Community forum](https://community.ortussolutions.com/c/communities/commandbox/14)
