---
description: >-
  Comprehensive BoxLang language support for Sublime Text 4 — syntax
  highlighting, intelligent completions (825+ BIFs, 81+ tags), inline
  documentation, code formatting, type inference, and build tools.
icon: pen-nib
---

# BoxLang Sublime Text Package

[![Tests](https://github.com/ortus-boxlang/sublimetext-boxlang/actions/workflows/tests.yml/badge.svg)](https://github.com/ortus-boxlang/sublimetext-boxlang/actions/workflows/tests.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Comprehensive BoxLang language support for **Sublime Text 4**. The package provides syntax highlighting, intelligent completions with 825+ built-in functions, inline documentation, code formatting, type inference, and a full build system — all powered by the BoxLang CLI.

{% @github-files/github-code-block url="https://github.com/ortus-boxlang/sublimetext-boxlang" %}

***

## 📋 Requirements

| Dependency    | Version        | Notes                                               |
| ------------- | -------------- | --------------------------------------------------- |
| Sublime Text  | 4 (Build 4180+) | Editor platform                                    |
| BoxLang CLI   | 1.13.0+        | Required for parsing, formatting, and compilation   |
| Python        | 3.11+          | Plugin runtime (bundled with Sublime Text 4)        |

> **Note:** Syntax highlighting works without BoxLang installed. The full feature set (completions, formatting, build system) requires the `boxlang` CLI available in your `PATH`.

***

## ⚡ Installation

### Via Package Control (Recommended)

1. Open the Command Palette (`Cmd+Shift+P` on macOS / `Ctrl+Shift+P` on Windows/Linux)
2. Select **Package Control: Install Package**
3. Search for `BoxLang` and press Enter
4. Restart Sublime Text when prompted

### Manual Installation

Clone the repository directly into your Sublime Text `Packages` directory:

```bash
# macOS
git clone https://github.com/ortus-boxlang/sublimetext-boxlang.git \
  ~/Library/Application\ Support/Sublime\ Text/Packages/BoxLang

# Linux
git clone https://github.com/ortus-boxlang/sublimetext-boxlang.git \
  ~/.config/sublime-text/Packages/BoxLang

# Windows
git clone https://github.com/ortus-boxlang/sublimetext-boxlang.git \
  "%APPDATA%\Sublime Text\Packages\BoxLang"
```

Restart Sublime Text after cloning.

### Optional: Enhanced File Icons

Install **A File Icon** from Package Control to display BoxLang-branded per-extension icons (`.bx`, `.bxs`, `.bxm`) in the sidebar. Without it, Sublime Text still uses native scope-based fallback icons configured by the package.

***

## 🧙 First Run & Setup Wizard

On first launch, the **BoxLang Setup Wizard** will automatically run to configure the package:

1. **Detect BoxLang** — Checks if the `boxlang` CLI is available in your `PATH` and shows the detected version
2. **Configure CFML Support** — Optionally enable `.cfc`/`.cfm`/`.cfs` file handling (disabled by default, and auto-disabled if the CFML package is already installed)
3. **Quick Tips** — Displays essential keyboard shortcuts to get you started

You can re-run the wizard at any time from the Command Palette: **BoxLang: Run Setup Wizard**

***

## ✨ Features

### 🎨 Syntax Highlighting

Full syntax highlighting for all BoxLang file types:

| Extension | Type                        | Description                                      |
| --------- | --------------------------- | ------------------------------------------------ |
| `.bx`     | Script class                | OOP classes with full BoxLang script syntax      |
| `.bxs`    | Script-only file            | Executable BoxLang scripts                       |
| `.bxm`    | Markup template             | HTML templates with embedded `<bx:script>` blocks |

The script syntax (`source.boxlang`) supports:

* **Modern keywords** — `class`, `interface`, `abstract`, `final`, `static`, `assert`
* **Control flow** — `if`/`else`, `for`/`while`/`do`, `switch`/`case`, `try`/`catch`/`finally`
* **Functions** — Named, anonymous, arrow (`=>`), and lambda (`->`) expressions
* **Operators** — Standard, comparison, strict equality (`===`, `!==`), spread, rest, ternary
* **Literals** — Strings with `#expression#` interpolation, arrays, structs, booleans, null, hex numbers
* **Scopes** — `variables`, `this`, `arguments`, `request`, `session`, `application`, `server`, `cgi`, and more
* **Annotations** — `@name(...)` with full parameter support
* **Imports** — `import` statements with dot-path resolution
* **Destructuring** — Array and struct destructuring bindings

The markup syntax (`embedding.boxlang.markup`) delegates embedded `<bx:script>` and `<bx:function>` blocks to the full script highlighter.

### 🤖 Intelligent Completions

The package ships with a rich completion engine driven by JSON data extracted from BoxLang sources:

| Category                     | Count | Details                                                  |
| ---------------------------- | ----- | -------------------------------------------------------- |
| Built-In Functions (BIFs)    | 825+  | 563 core + 262 module (compat-cfml, image, JWT, Redis…)  |
| BoxLang Tags (`bx:`)         | 81+   | 49 core + 32 module, with attribute completions          |
| Member Functions             | 229   | Per native type: string, array, struct, query, datetime  |
| Dot-Path Completions         | —     | `import`, `new`, `createObject()` dot-path navigation    |
| Type-Aware Completions       | —     | Inferred-type member method suggestions                  |
| Component Index Completions  | —     | Project-wide class scanning with inheritance resolution  |

Completion style is configurable per setting (see [Settings](#️-settings)):

* **`basic`** — Function name only
* **`required`** (default) — Name + required parameters as snippet
* **`full`** — Name + all parameters as snippet

### 📚 Inline Documentation

| Feature             | Trigger             | Description                                               |
| ------------------- | ------------------- | --------------------------------------------------------- |
| F1 Popup            | `F1`                | Full documentation popup with parameter reference table   |
| Hover Docs          | Mouse hover         | Quick info popup when hovering over a symbol              |
| Completion Docs     | During auto-complete | Parameter hints visible alongside completion suggestions  |
| Go to Docs          | Via popup link      | Opens [boxlang.ortusbooks.com](https://boxlang.ortusbooks.com) to the relevant page |

### 🛠️ Developer Tools

* **Code Formatting** — Format the current file with `boxlang format` via `Shift+Alt+F` or **BoxLang: Format Code** in the Command Palette. Optionally enable `boxlang_format_on_save` to format automatically.
* **Go to Definition** — `Ctrl/Cmd+Click` on any class or function reference to jump to its definition file.
* **Error Panel** — Parse errors are displayed in an output panel with inline region highlighting. Navigate between errors with `F4` (next) and `Shift+F4` (previous).
* **Status Bar** — Shows BoxLang CLI version, indexing progress, and error counts directly in the Sublime Text status bar.
* **DI Property Injection** — `Shift+Alt+D` inserts a dependency injection property template (configurable via `boxlang_di_property` setting).
* **Controller/View Toggle** — `Ctrl+F1` toggles between controller and view files based on configured folder names.

***

## ⌨️ Key Bindings

| Action                        | macOS                  | Linux / Windows       |
| ----------------------------- | ---------------------- | --------------------- |
| Show inline documentation     | `F1`                   | `F1`                  |
| Toggle controller/view        | `Ctrl+F1`              | `Ctrl+F1`             |
| Format code                   | `Shift+Option+F`       | `Shift+Alt+F`         |
| Inject DI property            | `Shift+Option+D`       | `Shift+Alt+D`         |
| Insert `writeDump()`          | `Ctrl+Option+D`        | `Ctrl+Alt+D`          |
| Insert `writeOutput()`        | `Ctrl+Shift+O`         | `Ctrl+Shift+O`        |
| Insert `abort;`               | `Ctrl+Option+A`        | `Ctrl+Alt+A`          |
| Wrap selection in `##`        | `#` (with selection)   | `#` (with selection)  |
| Go to definition              | `Cmd+Click`            | `Ctrl+Click`          |
| Next parse error              | `F4`                   | `F4`                  |
| Previous parse error          | `Shift+F4`             | `Shift+F4`            |
| Build & run current file      | `Cmd+B`                | `Ctrl+B`              |

> **Tip:** On macOS, if `F1` / `F4` trigger media keys, hold `Fn` first or remap them in System Preferences.

***

## 🔨 Build System

The package registers a **BoxLang** build system with six variants, selectable from **Tools → Build System** or the build variant picker:

| Variant              | Command                                                        | Use Case                        |
| -------------------- | -------------------------------------------------------------- | ------------------------------- |
| **Run**              | `boxlang "$file"`                                              | Execute the current file        |
| **Run with Arguments** | `boxlang "$file" ${args}`                                    | Execute with custom CLI args    |
| **Run with Debug**   | `boxlang --bx-debug "$file"`                                   | Run with debug output           |
| **Compile File**     | `boxlang compile --source "$file" --target "./bin"`            | Compile single file to bytecode |
| **Compile Project**  | `boxlang compile --source "$file_path" --target "./bin"`       | Compile entire project          |
| **Feature Audit**    | `boxlang featureaudit --source "$file_path"`                   | Audit CFML→BoxLang compatibility|

***

## ⚙️ Settings

Open settings via the Command Palette: **BoxLang: Settings**

### Key Settings

| Setting                                 | Default       | Description                                                       |
| --------------------------------------- | ------------- | ----------------------------------------------------------------- |
| `boxlang_executable_path`               | `null`        | Custom path to the BoxLang CLI executable                         |
| `boxlang_enable_cfml_fallback`          | `false`       | Enable `.cfc`/`.cfm`/`.cfs` file handling                         |
| `boxlang_bif_completions`               | `"required"`  | BIF completion style: `basic`, `required`, or `full`              |
| `boxlang_class_completions`             | `"required"`  | Component completion style: `basic`, `required`, or `full`        |
| `boxlang_class_completion_names`        | `"basic"`     | Include return type in completion name: `basic` or `full`         |
| `boxlang_instantiated_component_completions` | `true`   | Enable variable-to-component member completions                   |
| `boxlang_hover_docs`                    | `true`        | Show documentation popup on mouse hover                           |
| `boxlang_completion_docs`              | `true`        | Show parameter hints alongside auto-complete suggestions           |
| `boxlang_inline_doc_regions_highlight`  | `true`        | Highlight documentation regions in the editor                     |
| `boxlang_format_on_save`               | `false`       | Auto-format current file on save                                  |
| `boxlang_auto_compile_on_save`          | `false`       | Auto-compile to `./bin` on save                                   |
| `boxlang_compile_target`               | `"./bin"`     | Compilation target directory for auto-compile                     |
| `boxlang_testbox_enabled`              | `true`        | Enable TestBox integration                                        |
| `boxlang_status_bar_enabled`           | `true`        | Show BoxLang information in the status bar                        |

### Project Configuration

Add BoxLang-specific settings to your `.sublime-project` file to enable project-wide component indexing and dot-path resolution:

```json
{
  "settings": {
    "boxlang_class_folders": [
      {
        "path": "model",
        "variable_names": ["{class}", "{class_folder_singularized}"],
        "accessors": true
      }
    ]
  },
  "mappings": [
    { "path": "/absolute/path/to/project", "mapping": "/" }
  ]
}
```

* **`boxlang_class_folders`** — Folders to index for component completions. `variable_names` controls which variable name patterns map to indexed components; `accessors` enables getter/setter completions for component properties.
* **`mappings`** — Maps absolute file system paths to logical dot-path roots, enabling `createObject()` and `import` resolution across the project.

Trigger a manual re-index via the Command Palette: **BoxLang: Index Active Project**

***

## 📝 Code Snippets

The package includes 10 built-in snippets activated by their trigger word followed by `Tab`:

| Trigger       | Description                        |
| ------------- | ---------------------------------- |
| `bxclass`     | Class declaration with `extends`   |
| `bxinterface` | Interface declaration              |
| `bxcomponent` | Component declaration              |
| `bxfunc`      | Function declaration               |
| `bxtest`      | Test block (`describe`/`it`)       |
| `bxtry`       | Try/catch block                    |
| `bxfor`       | For loop                           |
| `bxforeach`   | For-in loop                        |
| `bxif`        | If statement                       |
| `bxscript`    | `<bx:script>` block                |

***

## 🔧 CFML Support

By default, CFML file types (`.cfc`, `.cfm`, `.cfs`) are **not** handled by the BoxLang package to avoid conflicts with the dedicated CFML package. To enable CFML fallback support, set the following in **BoxLang: Settings**:

```json
{
  "boxlang_enable_cfml_fallback": true
}
```

When enabled, the BoxLang syntax and completion engine will also apply to CFML files. The setup wizard automatically disables this option if it detects the CFML package is already installed.

***

## ⚠️ Known Limitations

1. **AST for `.bxm`** — `boxlang --bx-printast` does not yet support markup template files; the package uses a flexible tag tokenizer instead of the AST parser for `.bxm` files.
2. **AST class parsing** — BoxLang v1.13.0 represents `class` declarations as `BoxIdentifier` expressions rather than `BoxClassDeclaration` nodes, requiring sequential statement pattern matching.
3. **Java introspection** — `createObject("java", "...")` calls resolve to the generic `"any"` type; per-class Java method completions are deferred to a future phase.
4. **In-memory index** — The component index is not persisted to disk and is rebuilt fresh each Sublime Text session.
5. **MCP server** — The BoxLang MCP server integration is available but deferred to a future phase.

***

## 🤝 Contributing

Contributions are welcome! The package includes a comprehensive test suite with **236 tests** using pytest and TestBox-style assertions.

```bash
# Clone the repository
git clone https://github.com/ortus-boxlang/sublimetext-boxlang.git

# Run the full test suite
python -m pytest tests/

# Or use make shortcuts
make test          # All tests
make test-unit     # Unit tests only
make test-coverage # With coverage report
```

Please review the [Contributing Guidelines](https://github.com/ortus-boxlang/sublimetext-boxlang/blob/main/CONTRIBUTING.md) before submitting a pull request.

***

Built by [Ortus Solutions](https://www.ortussolutions.com) for the BoxLang community. Architecture inspired by the [sublimetext-cfml](https://github.com/jcberquist/sublimetext-cfml) package, reimagined from the ground up for BoxLang.
