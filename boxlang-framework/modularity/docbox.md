---
description: >-
  DocBox is a JavaDoc-style documentation generator for your BoxLang and CFML
  Applications.
icon: file-lines
---

# DocBox

## 📚 DocBox - API Documentation Generator

DocBox is a **JavaDoc-style documentation generator** for BoxLang codebases, featuring modern HTML themes, JSON output, and UML diagram generation.

You can check out the API Docs for DocBox itself here: [https://s3.amazonaws.com/apidocs.ortussolutions.com/docbox/5.0.0/index.html](https://s3.amazonaws.com/apidocs.ortussolutions.com/docbox/5.0.0/index.html)

<figure><img src="../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

### ✨ Features

* 🎨 **Modern HTML Documentation** - Two professional themes with dark mode support
* 🔍 **Real-time Search** - Live method filtering with keyboard navigation
* 📋 **Multiple Output Formats** - HTML, JSON, and XMI/UML diagrams
* 🦤 **BoxLang Native** - First-class BoxLang runtime and CLI support
* 📝 **JavaDoc Compatible** - Standard JavaDoc comment block parsing
* ⚡ **Alpine.js SPA** - Fast, modern single-page application interface
* 🌓 **Dark Mode** - System preference detection with manual toggle



<figure><img src="../../.gitbook/assets/image (46).png" alt=""><figcaption></figcaption></figure>

### 🚀 Quick Start

#### BoxLang Module (Recommended)

Install DocBox as a BoxLang module for CLI access:

```bash
# CommandBox web runtimes
box install bx-docbox

# BoxLang OS runtime
install-bx-module bx-docbox
```

Generate documentation from the command line:

```bash
boxlang module:docbox --source=/path/to/code \
                       --mapping=myapp \
                       --output-dir=/docs \
                       --project-title="My API"
```

#### BoxLang Apps

Install as a development dependency in your BoxLang project:

```bash
box install docbox --saveDev
```

Use programmatically in your build scripts:

```js
new docbox.DocBox()
    .addStrategy( "HTML", {
        projectTitle : "My API Docs",
        outputDir    : expandPath( "./docs" ),
        theme        : "default"  // or "frames"
    })
    .generate(
        source   = expandPath( "./models" ),
        mapping  = "models",
        excludes = "(tests|build)"
    );
```

***

### 📦 Installation Options

<table><thead><tr><th width="205.48870849609375">Method</th><th>Command</th><th>Use Case</th></tr></thead><tbody><tr><td><strong>BoxLang Module</strong></td><td><code>box install bx-docbox</code></td><td>CLI usage, BoxLang projects</td></tr><tr><td><strong>BoxLang Apps</strong></td><td><code>box install docbox --saveDev</code></td><td>Programmatic use, build scripts</td></tr><tr><td><strong>CommandBox Module</strong></td><td><code>box install commandbox-docbox</code></td><td>Task runner, automated builds</td></tr></tbody></table>

***

### 🎨 Modern Themes

#### Default Theme (Alpine.js SPA)

* ⚡ Client-side routing and dynamic filtering
* 🌓 Dark mode with localStorage persistence
* 🔍 Real-time method search
* 📑 Method tabs (All/Public/Private/Static/Abstract)
* 💜 Modern purple gradient design

#### Frames Theme (Traditional)

* 🗂️ Classic frameset layout
* 📚 jstree navigation sidebar
* 🎯 Bootstrap 5 styling
* 📱 Mobile-friendly design

***

### 💻 System Requirements

* **BoxLang 1.8+**
* **CommandBox** (for installation and CLI usage)

***

### 📚 Output Formats

<table><thead><tr><th width="143.29681396484375">Format</th><th>Description</th><th>Use Case</th></tr></thead><tbody><tr><td><strong>HTML</strong></td><td>Modern browsable documentation</td><td>Developer reference, public API docs</td></tr><tr><td><strong>JSON</strong></td><td>Machine-readable structured data</td><td>Integration with other tools, custom processing</td></tr><tr><td><strong>XMI</strong></td><td>UML diagram generation</td><td>Architecture diagrams, visual documentation</td></tr></tbody></table>

***

### 🛠️ CLI Examples

#### BoxLang Module CLI

```bash
# Basic usage
boxlang module:docbox --source=/src --mapping=app --output-dir=/docs

# Multiple source mappings
boxlang module:docbox --mappings:v1=/src/v1 --mappings:v2=/src/v2 -o=/docs

# With theme selection
boxlang module:docbox --source=/src --mapping=app --theme=frames -o=/docs

# Show help
boxlang module:docbox --help
```

#### CommandBox Task Runner

Install the [commandbox-docbox](https://github.com/Ortus-Solutions/commandbox-docbox) module:

```bash
box install commandbox-docbox
```

Generate documentation using CommandBox commands:

```bash
# Generate HTML docs
box docbox generate source=/path/to/code mapping=myapp outputDir=/docs

# Generate with excludes
box docbox generate source=/src mapping=app outputDir=/docs excludes=(tests|build)

# Generate JSON docs
box docbox generate source=/src mapping=app outputDir=/docs strategy=JSON

# Show help
box docbox generate help
```

Use in a `task.cfc` for automated builds:

```js
component {
    function run() {
        command( "docbox generate" )
            .params(
                source    = getCWD() & "/models",
                mapping   = "models",
                outputDir = getCWD() & "/docs",
                excludes  = "tests"
            )
            .run();
    }
}
```

***

### 📖 Documentation

Complete documentation is available at [**docbox.ortusbooks.com**](https://docbox.ortusbooks.com/)

* [Getting Started](https://docbox.ortusbooks.com/getting-started/getting-started-with-docbox)
* [BoxLang CLI Tool](https://docbox.ortusbooks.com/getting-started/boxlang-cli)
* [Configuration](https://docbox.ortusbooks.com/getting-started/configuration)
* [Annotating Your Code](https://docbox.ortusbooks.com/getting-started/annotating-your-code)
* [HTML Output](https://docbox.ortusbooks.com/output-formats/html-output)
* [JSON Output](https://docbox.ortusbooks.com/output-formats/json-output)

***

### 🔗 Related Projects

* [**commandbox-docbox**](https://github.com/Ortus-Solutions/commandbox-docbox) - CommandBox module for task runner integration
* [**bx-docbox**](https://forgebox.io/view/bx-docbox) - BoxLang native module with CLI
