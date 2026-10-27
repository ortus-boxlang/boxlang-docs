---
description: The Officially supported BoxLang modules
icon: atom-simple
---

# Modules

Our official modules can be found in the BoxLang Software Directory: **FORGEBOX**: [www.forgebox.io](https://www.forgebox.io).

{% hint style="success" %}
Every runtime can use modules, and the installation process can differ. So, make sure you review each of the sections on Running BoxLang and adapt your installation process accordingly.
{% endhint %}

For web runtimes running on CommandBox, our servlet server, use the `box` CommandBox CLI for installation and `server.json` for tracking dependencies. For our operating system runtime, use the `bx-module` command.

## 🧰 The `bx-module` Command

`bx-module` is the BoxLang module manager. It is installed by the [Quick Installer](boxlang-quick-installer.md) and by [BVM](boxlang-version-manager-bvm.md), and it installs, removes, lists, and updates modules from [FORGEBOX](https://www.forgebox.io).

{% hint style="warning" %}
**`install-bx-module` is deprecated** (since installer `1.37.0`). It still works as a thin alias that prints a deprecation notice and forwards to `bx-module`, so existing scripts keep running. Use `bx-module` for all new work. See [Migrating from `install-bx-module`](modules.md#migrating-from-install-bx-module).
{% endhint %}

```
bx-module <command> [arguments] [options]
```

### Commands

| Command | Purpose |
| --- | --- |
| `bx-module install [<module>[@<version>] ...]` | Install one or more modules. With no module names, installs the `dependencies` of the `box.json` in the current directory. |
| `bx-module remove <module> [<module> ...]` | Remove one or more modules, their nested dependencies, and any launchers they installed. |
| `bx-module list` | Show installed modules, with nested dependencies indented under their parent. |
| `bx-module outdated` | Compare installed versions against FORGEBOX and report which are outdated. |
| `bx-module update [<module> ...]` | Update all outdated modules, or only the ones you name. |
| `bx-module help [<command>]` | Show general help, or help for one command. |

### Options

Options follow the command.

| Option | Applies to | Purpose |
| --- | --- | --- |
| `--local` | all commands | Work with the `./boxlang_modules` folder instead of BoxLang HOME (`~/.boxlang/modules`). |
| `--force` | `remove`, `update` | Skip the confirmation prompt, useful for unattended scripts and CI. |
| `--help`, `-h` | all commands | Show help. |

{% hint style="info" %}
Module names can be separated by spaces or commas: `bx-module install bx-orm bx-ai` and `bx-module install bx-orm,bx-ai` are equivalent. If no version is given, the latest FORGEBOX version is installed. `bx-module` requires `curl` and `jq`.
{% endhint %}

### Operating System Modules

By default, modules are installed into BoxLang HOME and are available to every BoxLang application on the machine.

{% code title="Operating System" %}
```bash
# Install os-wide modules
bx-module install bx-compat-cfml

# Install the free-to-use proprietary BoxLang MCP module and its dependency
bx-module install bx-ai bx-mcp

# Install os-wide modules with a specific version
bx-module install bx-compat-cfml@1.0.0

# Install multiple modules
bx-module install bx-compat-cfml bx-esapi bx-orm

# Remove a module (add --force to skip the confirmation)
bx-module remove bx-esapi

# List installed modules
bx-module list

# Check for outdated modules
bx-module outdated

# Update everything, or only specific modules
bx-module update
bx-module update bx-orm bx-esapi

# Update without confirmation
bx-module update --force

# Get help, or help for one command
bx-module help
bx-module help update
```
{% endcode %}

### Local CLI Application Modules

BoxLang also supports the concept of local loading. Meaning, if you have a `boxlang_modules` folder in the root of where you run your CLI applications, then BoxLang will load those modules first and then fall back to the user's home directory for the operating system.

{% hint style="info" %}
A module can also ship modules of its own, in a `modules` folder inside it, loaded before the module itself. A `.jar` dropped into any modules folder is a module too. See [Module Inception](../../boxlang-framework/module-development/module-inception.md).
{% endhint %}

{% code title="myAppDirectory" %}
```bash
# Install locally
bx-module install bx-compat-cfml --local

# Install a specific version locally
bx-module install bx-compat-cfml@1.0.0 --local

# Install multiple modules locally
bx-module install bx-compat-cfml bx-esapi bx-orm --local

# Manage the local folder
bx-module list --local
bx-module outdated --local
bx-module update --force --local
```
{% endcode %}

### Installing a Project's Dependencies

Run `bx-module install` with no module names and it reads the `dependencies` of the `box.json` in the current directory, much like `npm install`. Without `--local` they go to BoxLang HOME, and with `--local` they go to `./boxlang_modules`. If there is no `box.json`, the usage help is shown instead.

```bash
# Install ./box.json dependencies into BoxLang HOME
bx-module install

# Install ./box.json dependencies into ./boxlang_modules
bx-module install --local
```

### Dependency Manifest

Installs are tracked in a `box.json` dependency manifest. Global modules use `~/.boxlang/modules/box.json`, while `--local` modules use `./boxlang_modules/box.json`. Installing and removing modules keeps the manifest current, and `bx-module list` can generate a missing manifest for modules that were installed before manifest tracking existed.

### Module Dependencies and Nested Modules

When a module's own `box.json` declares `dependencies`, `bx-module` installs them automatically. A version of `"*"` (or empty) installs the latest FORGEBOX version, and any other value (an exact version, `be`, or `snapshot`) is installed as specified. Circular chains are detected and skipped.

Dependencies are installed as **nested modules** inside the parent's own `modules/` folder, which the runtime loads before the parent. For example, installing `bx-sites` produces:

```
~/.boxlang/modules/
  box.json                  # manifest: top-level modules only (bx-sites)
  bx-sites/
    box.json
    modules/
      bx-markdown/
      bx-esapi/
```

* Nesting is recursive: a dependency's own dependencies nest inside it.
* Each module is self-contained, so a shared dependency is nested again under every module that needs it. A warning is printed when a nested dependency is also installed elsewhere.
* Nested modules are not added to the shared manifest. Their parent's `box.json` declares them.
* `list`, `outdated`, and `update` show nested modules indented under their parent, and `update` reinstalls outdated nested modules in place.
* `remove` deletes a module together with its nested dependencies.
* Dependencies that are not plain FORGEBOX slugs (Maven, URL, or git style entries) are skipped with a warning.

### Migrating from `install-bx-module`

`install-bx-module` was the previous name of this tool and is **deprecated**. It translates its old flags into the matching `bx-module` command, prints a deprecation notice (to stderr in bash, as a warning in PowerShell), and forwards the call. It is shipped for Bash, PowerShell, and the Windows `.bat` launchers.

| Previous (deprecated) | Now |
| --- | --- |
| `install-bx-module bx-orm --local` | `bx-module install bx-orm --local` |
| `install-bx-module` (reads `./box.json`) | `bx-module install` |
| `install-bx-module --list` | `bx-module list` |
| `install-bx-module --outdated` | `bx-module outdated` |
| `install-bx-module --update [--force]` | `bx-module update [--force]` |
| `install-bx-module --remove bx-orm [--force]` | `bx-module remove bx-orm [--force]` |
| `install-bx-module --help` | `bx-module help` |

`bx-module` itself does not accept the old flag style. Running `bx-module --list` or `bx-module bx-orm` fails with a hint naming the right command.

### CommandBox Runtimes

The CommandBox CLI installs BoxLang modules into web runtimes.

{% hint style="warning" %}
Eventually, CommandBox will be the de-facto standard of installation once it's migrated to BoxLang.
{% endhint %}

{% code title="CommandBox" %}
```bash
box install bx-compat-cfml,bx-esapi

# Install the free-to-use proprietary BoxLang MCP module and its dependency
box install bx-ai,bx-mcp
```
{% endcode %}

{% hint style="info" %}
The `bx-mcp` module is free to use but proprietary. It requires `bx-ai`; no `bx-plus` subscription is needed. See the [bx-mcp module guide](../../boxlang-framework/modularity/bx-mcp/README.md).
{% endhint %}

### Configuration

You can customize the boxlang module directory by changing the `runtime.modulesDirectory` setting in your `config/boxlang.json` file:

{% code title="boxlang.json" %}
```json
{

    // A collection of BoxLang module directories, they must be absolute paths
    "modulesDirectory": [
      "${boxlang-home}/modules"
    ],

}
```
{% endcode %}



## Core Modules

Visit the [Modules](../../boxlang-framework/modularity/) section of our docs for the most up to date listing of our supported modules.

## CLI Executables and Bash Completions

When you install a module with `bx-module`, it can also come with its own CLI wrapper executable(s) and a bash completion script, both wired up automatically. Removing the module (`bx-module remove`) deletes them again, unless another copy of the module is still installed. See [CLI Executables and Completions](../../boxlang-framework/module-development/module-descriptor.md#cli-executables-and-completions) in the module authoring docs for how a module declares these in its `box.json`.
