---
description: Easily install BoxLang or our BoxLang Version Manager (BVM) with Homebrew!
icon: beer-mug
---

# Homebrew

**🥊 The official Homebrew tap for the BoxLang JVM Language!**

Make sure you have Homebrew installed: [https://brew.sh/](https://brew.sh/)

{% embed url="https://brew.sh/" %}

### Installation

First, add this tap to Homebrew:

```bash
brew tap ortus-boxlang/boxlang
```

***

### Formulas

#### `bvm` — BoxLang Version Manager

Installs [BVM](https://boxlang.ortusbooks.com/getting-started/installation/boxlang-version-manager-bvm), the BoxLang Version Manager, which lets you install and switch between multiple BoxLang versions.

```bash
brew install ortus-boxlang/boxlang/bvm
```

After installation, install and activate BoxLang:

```bash
bvm install latest
bvm use latest
boxlang --version
```

Common BVM commands:

```bash
bvm install latest    # Install the latest stable BoxLang
bvm install snapshot  # Install the latest snapshot
bvm use latest        # Switch to the latest version
bvm list              # List locally installed versions
bvm current           # Show the active version
bvm help              # Show all available commands
```

***

#### `boxlang` — BoxLang Quick Installer

Installs the [BoxLang Quick Installer](https://boxlang.ortusbooks.com/getting-started/installation/boxlang-quick-installer), which sets up BoxLang (runtime and MiniServer) in a single step.

```bash
brew install ortus-boxlang/boxlang/boxlang
```

After installation, run the installer to set up BoxLang:

```bash
install-boxlang
```

Additional options:

```bash
install-boxlang --with-jre     # Auto-install Java 21 JRE if not found
install-boxlang --yes          # Accept all defaults (non-interactive)
sudo install-boxlang --system  # Install system-wide (all users)
```

After the installer completes, add the following to your shell profile (`~/.zshrc` or `~/.bashrc`) and restart your terminal:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

You can then run BoxLang:

```bash
boxlang               # Start the BoxLang REPL
boxlang --version     # Check the installed version
boxlang-miniserver    # Start the BoxLang MiniServer
```

***

### Prerequisites

Both formulas automatically pull in the following dependencies via Homebrew:

* `curl`
* `unzip`
* `jq`
* `openjdk@21`

***

### Auto-updates

This tap ships with a GitHub Actions workflow (`.github/workflows/update-formulas.yml`) that keeps the formulas up to date automatically:

* **Scheduled**: runs daily at 06:00 UTC.
* **Manual**: trigger the _Update Homebrew Formulas_ workflow from the Actions tab at any time.
* **On release**: the `ortus-boxlang/boxlang-quick-installer` repository can trigger an update immediately after publishing a new release by dispatching a `repository_dispatch` event of type `installer-released` to this repository.

When a new version of the [BoxLang Quick Installer](https://github.com/ortus-boxlang/boxlang-quick-installer) is published the workflow updates both formulas and commits the change automatically. Once the tap formula is updated, users running `brew upgrade` will receive the latest installer version.

> **Note on BoxLang runtime versions**: the formulas install the _installer tool_, not a pinned BoxLang runtime. After upgrading the formula you can get the latest BoxLang runtime with `bvm install latest && bvm use latest` or by re-running `install-boxlang`.
