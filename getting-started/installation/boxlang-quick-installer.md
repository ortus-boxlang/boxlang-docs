---
description: The BoxLang Quick Installer is the fastest way to get started with BoxLang.
icon: poo-storm
---

# BoxLang Quick Installer

<div data-full-width="false"><figure><img src="../../.gitbook/assets/boxlang-quick-installer.jpg" alt=""><figcaption><p>BQI</p></figcaption></figure></div>

The BoxLang Quick Installer provides convenient installation scripts for Mac, Linux, and Windows systems to get BoxLang up and running in minutes. Choose between a single-version installer for simplicity or BVM (BoxLang Version Manager) for advanced version management.

### 🚀 Quick Start

**Mac and Linux:**

```bash
# Single version (simple)
/bin/bash -c "$(curl -fsSL https://install.boxlang.io)"

# Version manager (advanced)
/bin/bash -c "$(curl -fsSL https://install-bvm.boxlang.io)"
```

**Windows:**

```powershell
# Single version (simple)
powershell -NoExit -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://install-windows.boxlang.io'))"
```

#### Verify Installation

```bash
# Check BoxLang version
boxlang --version

# Start BoxLang REPL
boxlang

# Start MiniServer
boxlang-miniserver --port 8080
```

### 📦 Installation Options

#### Option 1: Single-Version Installer (Recommended for Most Users)

**Choose this if you:**

* 📌 Need one BoxLang version system-wide
* 🎯 Want the simplest possible installation
* 🏢 Are setting up production servers
* ⚡ Want the fastest installation with minimal overhead

**Features:**

* ✅ Installs latest stable BoxLang version
* ✅ Sets up BoxLang runtime and MiniServer
* ✅ Includes all helper scripts
* ✅ Automatic PATH configuration
* ✅ User or system-wide installation options

#### Option 2: BVM (BoxLang Version Manager)

**Choose this if you:**

* 🔄 Work on multiple projects needing different BoxLang versions
* 🧪 Want to test code against different BoxLang releases
* 🚀 Need to switch between stable and snapshot versions
* 📦 Want centralized management of BoxLang installations
* 🛠️ Are a BoxLang developer or advanced user

**Features:**

* ✅ Install and manage multiple BoxLang versions
* ✅ Switch between versions with one command
* ✅ List local and remote versions
* ✅ Clean uninstall capabilities
* ✅ Health check and diagnostics

### 🛠️ What Gets Installed

#### Core Components

* **BoxLang Runtime** (`boxlang`, `bx`) - The main BoxLang Runtime Engine
* **BoxLang MiniServer** (`boxlang-miniserver`, `bx-miniserver`) - Lightweight web application server

#### Helper Scripts

* **install-bx-module** - Install modules from ForgeBox
* **install-jre** (Windows) - Install Java Runtime Environment

#### Directory Structure

```
~/.boxlang/           # BoxLang home directory
├── bin/              # Executable binaries
├── lib/              # Core libraries
├── scripts/          # Installed scripts

# System installation locations:
System Wide: /usr/local/bin/       # Binaries (Linux/Mac)
Local User: ~/.local/bin/          # Binaries (Linux/Mac)

C:\BoxLang\  # Installation directory (Windows)
```

### 📋 Prerequisites

#### All Platforms

* **Java 21+** - Required to run BoxLang

#### Mac/Linux Additional Requirements

* **curl** - For downloading releases
* **unzip** - For extracting archives
* **jq** - For JSON parsing (optional, fallback available)

#### Installing Prerequisites

**macOS (with Homebrew):**

```bash
brew install curl unzip jq
```

**Ubuntu/Debian:**

```bash
sudo apt update && sudo apt install curl unzip jq default-jdk
```

**RHEL/CentOS/Fedora:**

```bash
sudo dnf install curl unzip jq java-21-openjdk
```

**Windows:**

* Java 21+ from [Oracle](https://www.oracle.com/java/technologies/downloads/) or [OpenJDK](https://openjdk.org/)
* PowerShell 5.1+ (included with Windows 10+)

### 🎯 Detailed Usage

#### Single-Version Installer Commands

```bash
# Install latest stable version
install-boxlang

# Install specific version
install-boxlang --version 1.2.0

# Install snapshot version
install-boxlang --snapshot

# System-wide installation (requires sudo)
sudo install-boxlang --system

# Uninstall BoxLang
install-boxlang --uninstall

# Get help
install-boxlang --help
```

#### Module Management

```bash
# Install a module globally
install-bx-module bx-orm

# Install multiple modules
install-bx-module bx-orm,bx-mail,bx-db

# Install to specific directory
install-bx-module bx-orm --directory ./modules

# Install specific version
install-bx-module bx-orm@1.0.0

# Get help
install-bx-module --help
```

### 🌐 Running Applications

#### BoxLang Runtime

```bash
# Start REPL
boxlang

# Run a class
boxlang Task.bx

# Run a script
boxlang myscript.bxs

# Execute inline code
boxlang -c "println('Hello BoxLang!')"

# Compile to bytecode
boxlang compile myscript.bx

# Show version
boxlang --version
```

#### BoxLang MiniServer

```bash
# Start with default settings
boxlang-miniserver

# Specify port
boxlang-miniserver --port 8080

# Set web root
boxlang-miniserver --webroot ./public

# Enable development mode
boxlang-miniserver --dev

# Show all options
boxlang-miniserver --help
```

### 🔧 Configuration

#### Environment Variables

```bash
# BoxLang home directory
export BOXLANG_HOME=~/.boxlang

# Java options for BoxLang
export BOXLANG_OPTS="-Xmx2g -Xms512m"

# Module search paths
export BOXLANG_MODULES_PATH="./modules:~/.boxlang/modules"
```

### 🐛 Troubleshooting

#### Common Issues

**BoxLang not found after installation:**

```bash
# Restart terminal or reload profile
source ~/.bashrc  # or ~/.zshrc

# Check PATH
echo $PATH | grep boxlang
```

**Java not found:**

```bash
# Check Java installation
java -version

# Install Java 21 (Ubuntu/Debian)
sudo apt install default-jdk

# Install Java 21 (macOS)
brew install openjdk@21
```

**Permission denied errors:**

```bash
# Fix permissions for user installation
chmod +x ~/.boxlang/bin/*

# Or use system installation
sudo install-boxlang --system
```

**Module installation fails:**

```bash
# Check network connectivity
curl -I https://forgebox.io

# Clear module cache
rm -rf ~/.boxlang/modules/.cache

# Install with verbose output
install-bx-module bx-orm --verbose
```

#### Getting Help

```bash
# Command-specific help
install-boxlang --help
install-bx-module --help
bvm help

# Health check (BVM only)
bvm doctor

# Verbose output for debugging
install-boxlang --verbose
install-bx-module --verbose
```

### 📚 Resources

#### Documentation

* 📖 [Official Documentation](https://boxlang.io/docs)
* 🚀 [Getting Started Guide](https://boxlang.io/docs/getting-started)
* 📋 [Language Reference](https://boxlang.io/docs/reference)
* 🔧 [Module Development](https://boxlang.io/docs/modules)

#### Community

* 💬 [Discord Community](https://boxlang.io/discord)
* 📧 [Mailing List](https://boxlang.io/mailing-list)
* 🐛 [Issue Tracker](https://github.com/ortus-boxlang/boxlang/issues)
* 💡 [Feature Requests](https://github.com/ortus-boxlang/boxlang/discussions)

#### Examples

* 🧑‍💻 [Interactive Playground](https://try.boxlang.io)
* 📁 [Sample Applications](https://github.com/ortus-boxlang/bx-demos)
* 🎓 [Tutorials](https://learn.boxlang.io)

### 🤝 Contributing

We welcome contributions! Here's how you can help:

#### Reporting Issues

1. Check existing [issues](https://ortussolutions.atlassian.net/browse/BLINSTALL)
2. Create a detailed bug report with:
   * Operating system and version
   * BoxLang version
   * Steps to reproduce
   * Expected vs actual behavior

#### Contributing Code

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Add tests if applicable
5. Update documentation
6. Submit a pull request

#### Testing

Help test new features and releases:

```bash
# Install snapshot for testing
bvm install snapshot
bvm use snapshot

# Report any issues found
```

### 📄 License

This project is licensed under the Apache License, Version 2.0.

### 🆘 Support

#### Community Support (Free)

* 🌐 Website: https://boxlang.io
* 📖 Documentation: https://boxlang.ortusbooks.com
* 💾 GitHub: https://github.com/ortus-boxlang/boxlang
* 💬 Community: https://community.ortussolutions.com/
* 🧑‍💻 Try: https://try.boxlang.io
* 📧 Mailing List: https://newsletter.boxlang.io

#### Professional Support

* 🫶 Enterprise Support: https://boxlang.io/plans
* 🎓 Training: https://learn.boxlang.io
* 🔧 Consulting: https://www.ortussolutions.com/services/development
* 📞 Priority Support: [Available with enterprise plans](https://boxlang.io/plans)

***

Made with ♥️ in USA 🇺🇸, El Salvador 🇸🇻 and Spain 🇪🇸
