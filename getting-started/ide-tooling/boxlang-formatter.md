---
description: Format BoxLang and CFML code with deterministic, team-wide style enforcement and CI-ready check mode
icon: wand-magic-sparkles
---

# 🎨 BoxLang Formatter

The BoxLang Formatter is the canonical tool for enforcing consistent code style across BoxLang and CFML codebases.

Use this page as your one-stop technical reference for:

- local formatting workflows
- lint-like enforcement in CI/CD pipelines
- formatter configuration precedence
- cfformat migration and conversion strategy

## 🚀 Command Overview

The formatter is exposed as a BoxLang action command:

```bash
boxlang format [OPTIONS]
```

This command routes through the BoxLang runtime action pipeline, so it can be used consistently in local development, pre-commit checks, and CI runners.

### Supported File Types

The formatter can process these extensions:

- `.bx`
- `.bxs`
- `.bxm`
- `.cfm`
- `.cfc`
- `.cfs`

## 📋 CLI Options

{% hint style="info" %}
**BoxLang v1.14+** — The `--source` flag now accepts a comma-delimited list of paths, and the new `--excludes` flag lets you skip specific files or directories during formatting.
{% endhint %}

Use `boxlang format --help` to view the complete option set available in your installed version.

| Option | Description | Typical Usage |
| :--- | :--- | :--- |
| `--help` | Show formatter help and exit | `boxlang format --help` |
| `--source <PATH[,PATH,...]>` | Comma-delimited list of files or directories to process (BoxLang v1.14+) | `boxlang format --source ./src` or `boxlang format --source commands,models,services` |
| `--excludes <PATH[,PATH,...]>` | Comma-delimited list of files or directories to skip (BoxLang v1.14+) | `boxlang format --source . --excludes generated,vendor` |
| `--target <PATH>` | Output path (optional). If omitted, source files are overwritten | `boxlang format --source ./src --target ./formatted` |
| `--check` | Check-only mode; exits non-zero when formatting drift exists | `boxlang format --check --source ./` |
| `--overwrite <BOOL>` | When `false`, write formatted output to stdout instead of rewriting files | `boxlang format --overwrite false --source ./models/User.cfc` |
| `--config <PATH>` | Explicit `.bxformat.json` or `.cfformat.json` path | `boxlang format --config ./.bxformat.json --source ./` |
| `--initConfig` | Create starter formatter config in current workspace | `boxlang format --initConfig` |
| `--convertConfig` | Convert legacy `.cfformat.json` into `.bxformat.json` | `boxlang format --convertConfig --source ./` |

## 🧪 Core Workflows

### Format In Place (Project-Wide)

```bash
boxlang format --source ./
```

Use this as your default command to normalize project style before commit.

### Format a Single File

```bash
boxlang format --source ./models/User.bx
```

Useful for editor tasks, pre-commit hooks, and targeted refactors.

### Print to Stdout (No File Rewrite)

```bash
boxlang format --overwrite false --source ./handlers/MainHandler.cfc
```

This is useful when integrating with custom tooling that captures formatter output.

### CI Gate / Lint-Style Enforcement

```bash
boxlang format --check --source ./
```

In `--check` mode, the command behaves as a lint-style quality gate:

- exits successfully when all files already match formatter rules
- exits non-zero when any file requires formatting

This allows direct integration with CI jobs that should fail on style drift.

## ⚙️ Configuration Model

The formatter auto-discovers configuration using this precedence order:

1. `.bxformat.json`
2. `.cfformat.json` (converted into formatter config model)
3. built-in defaults

This design gives teams a safe migration path:

- BoxLang-native projects can adopt `.bxformat.json`
- mixed/legacy projects can continue using `.cfformat.json` while migrating incrementally

### Bootstrap New Config

```bash
boxlang format --initConfig
```

Use this to generate a baseline `.bxformat.json` in your workspace.

## 🧾 Full Rules Reference (`.bxformat.json`)

This section lists all currently supported formatter configuration keys and how to configure them.

{% hint style="info" %}
Some keys may not appear in the generated `--initConfig` scaffold but are still supported by the formatter config model.
{% endhint %}

### Root-Level Rules

| Key | Type | Default | Allowed / Notes |
| :--- | :--- | :--- | :--- |
| `indentSize` | number | `4` | Indentation width unit |
| `tabIndent` | boolean | `true` | Use tabs instead of spaces |
| `maxLineLength` | number | `115` | Line length target for wrapping decisions |
| `newLine` | string | `"\n"` | `"os"`, `"\n"`, `"\r\n"` |
| `singleQuote` | boolean | `false` | Prefer single quotes for strings/keys |
| `preserveStringQuotes` | boolean | `false` | Preserve original quote style in source |
| `alignConsecutiveAssignments` | boolean | `true` | Vertical align for consecutive assignment-like separators |
| `alignConsecutiveProperties` | boolean | `true` | Vertical align for consecutive `property` declarations |
| `bracketPadding` | boolean | `true` | Global default for array bracket padding |
| `parensPadding` | boolean | `true` | Global default for parentheses padding |
| `binaryOperatorsPadding` | boolean | `true` | Spaces around binary operators |
| `semicolons` | boolean | `true` | Append semicolons where applicable |
| `cfFormatCompatibility` | boolean | `false` | Internal compatibility mode (normally set by cfformat conversion path) |
| `sourceType` | string/null | `null` | `BOXSCRIPT`, `BOXTEMPLATE`, `CFSCRIPT`, `CFTEMPLATE`; `null` = auto-detect |

### `struct` Rules

| Key | Type | Default | Allowed / Notes |
| :--- | :--- | :--- | :--- |
| `struct.padding` | boolean | `true` | Spaces/newlines inside non-empty struct braces |
| `struct.empty_padding` | boolean | `false` | Space in empty structs/ordered markers |
| `struct.quote_keys` | boolean | `false` | Force quoting of struct keys |
| `struct.separator` | string | `" : "` | `":"`, `"="`, `": "`, `" : "`, `"= "`, `" = "` |
| `struct.multiline.element_count` | number | `2` | Break threshold by number of entries |
| `struct.multiline.comma_dangle` | boolean | `false` | Trailing comma when multiline |
| `struct.multiline.leading_comma.enabled` | boolean | `false` | Leading comma style |
| `struct.multiline.leading_comma.padding` | boolean | `true` | Space after leading comma |
| `struct.multiline.min_length` | number | `60` | Break threshold by flattened text length |

### `array` Rules

| Key | Type | Default | Allowed / Notes |
| :--- | :--- | :--- | :--- |
| `array.padding` | boolean | `true` | Spaces/newlines inside non-empty array brackets |
| `array.empty_padding` | boolean | `false` | Space in empty arrays |
| `array.multiline.element_count` | number | `2` | Break threshold by number of elements |
| `array.multiline.comma_dangle` | boolean | `false` | Trailing comma when multiline |
| `array.multiline.leading_comma.enabled` | boolean | `false` | Leading comma style |
| `array.multiline.leading_comma.padding` | boolean | `true` | Space after leading comma |
| `array.multiline.min_length` | number | `50` | Break threshold by flattened text length |

### `property` Rules

| Key | Type | Default | Allowed / Notes |
| :--- | :--- | :--- | :--- |
| `property.multiline.element_count` | number | `3` | Break threshold by number of attributes |
| `property.multiline.comma_dangle` | boolean | `false` | Trailing comma in multiline attribute lists |
| `property.multiline.leading_comma.enabled` | boolean | `false` | Leading comma style |
| `property.multiline.leading_comma.padding` | boolean | `true` | Space after leading comma |
| `property.multiline.min_length` | number | `30` | Break threshold by flattened text length |
| `property.key_value.padding` | boolean | `false` | Spaces around `=` in property attributes |

### `for_loop_semicolons` Rules

| Key | Type | Default | Allowed / Notes |
| :--- | :--- | :--- | :--- |
| `for_loop_semicolons.padding` | boolean | `true` | Space after `;` in `for ( ;; )` header |

### `function` Rules

| Key | Type | Default | Allowed / Notes |
| :--- | :--- | :--- | :--- |
| `function.style` | string | `"preserve"` | Currently preserve-first style control |
| `function.parameters.padding` | boolean | `true` | Spaces in non-empty parameter list |
| `function.parameters.empty_padding` | boolean | `false` | Space in empty parameter list |
| `function.parameters.comma_dangle` | boolean | `false` | Trailing comma in multiline parameters |
| `function.parameters.multiline_count` | number | `3` | Break threshold by parameter count |
| `function.parameters.multiline_length` | number | `50` | Break threshold by flattened length |
| `function.arrow.parens` | string | `"always"` | `"always"` or `"avoid"` |

### `arguments` Rules

| Key | Type | Default | Allowed / Notes |
| :--- | :--- | :--- | :--- |
| `arguments.padding` | boolean | `true` | Spaces in non-empty call argument lists |
| `arguments.empty_padding` | boolean | `false` | Space in empty argument lists |
| `arguments.comma_dangle` | boolean | `false` | Trailing comma in multiline arguments |
| `arguments.multiline_count` | number | `3` | Break threshold by argument count |
| `arguments.multiline_length` | number | `50` | Break threshold by flattened length |

### `braces` Rules

| Key | Type | Default | Allowed / Notes |
| :--- | :--- | :--- | :--- |
| `braces.style` | string | `"same-line"` | `"same-line"`, `"new-line"`, `"preserve"` |
| `braces.require_for_single_statement` | boolean | `true` | Require braces for single statement control blocks |
| `braces.else.style` | string | `"same-line"` | `"same-line"` or `"new-line"` |

### `operators` Rules

| Key | Type | Default | Allowed / Notes |
| :--- | :--- | :--- | :--- |
| `operators.position` | string | `"end"` | Binary operator position on wrapped expressions: `"end"` or `"start"` |
| `operators.comparison_style` | string | `"symbols"` | `"symbols"`, `"keywords"`, or `"preserve"` |
| `operators.ternary.style` | string | `"flat"` | `"flat"`, `"always-multiline"`, or `"preserve"` |
| `operators.ternary.question_position` | string | `"start"` | `"start"` or `"end"` |

### `chain` Rules

| Key | Type | Default | Allowed / Notes |
| :--- | :--- | :--- | :--- |
| `chain.break_count` | number | `3` | Break chain when call count reaches threshold |
| `chain.break_length` | number | `60` | Break chain when flattened length reaches threshold |

### `template` Rules

| Key | Type | Default | Allowed / Notes |
| :--- | :--- | :--- | :--- |
| `template.component_prefix` | string | `"bx"` | Commonly `"bx"` or `"cf"` |
| `template.indent_content` | boolean | `true` | Indent tag body content |
| `template.single_attribute_per_line` | boolean | `false` | One attribute per line in tags |
| `template.self_closing` | boolean | `true` | Use `/>` for self-closing tags |

### `import` Rules

| Key | Type | Default | Allowed / Notes |
| :--- | :--- | :--- | :--- |
| `import.sort` | boolean | `false` | Sort imports alphabetically |
| `import.group` | boolean | `false` | Group imports by package with blank lines |

### `comments` Rules

| Key | Type | Default | Allowed / Notes |
| :--- | :--- | :--- | :--- |
| `comments.preserve_blank_lines` | boolean | `true` | Keep blank lines around comments |
| `comments.wrap` | boolean | `false` | Wrap long comments based on `maxLineLength` |

### `class` Rules

| Key | Type | Default | Allowed / Notes |
| :--- | :--- | :--- | :--- |
| `class.member_order` | string | `"preserve"` | Member ordering strategy |
| `class.member_spacing` | number | `1` | Blank lines between members |
| `class.property_order` | string | `"preserve"` | `"preserve"`, `"alphabetical"`, `"length"`, `"type"` |
| `class.method_order` | string | `"preserve"` | `"preserve"` or `"alphabetical"` |
| `class.method_grouping` | boolean | `false` | Group methods by modifier/type before ordering |

### `sql` Rules

| Key | Type | Default | Allowed / Notes |
| :--- | :--- | :--- | :--- |
| `sql.uppercase_keywords` | boolean | `true` | Uppercase SQL keywords |
| `sql.indent_clauses` | boolean | `true` | Indent SQL clauses in query blocks |

## 🛠️ Configuration Examples

### Minimal Starter

```json
{
	"maxLineLength": 120,
	"tabIndent": true,
	"parensPadding": true,
	"arguments": {
		"multiline_count": 3,
		"multiline_length": 40
	}
}
```

### Strict CI-Friendly Layout

```json
{
	"maxLineLength": 100,
	"semicolons": true,
	"braces": {
		"style": "same-line",
		"require_for_single_statement": true,
		"else": {
			"style": "same-line"
		}
	},
	"operators": {
		"position": "end",
		"comparison_style": "symbols",
		"ternary": {
			"style": "always-multiline",
			"question_position": "start"
		}
	},
	"comments": {
		"preserve_blank_lines": true,
		"wrap": true
	}
}
```

## 🔄 Migration from cfformat

If your team currently relies on cfformat conventions, migrate with a controlled two-phase approach.

### Phase 1: Convert Existing Config

```bash
boxlang format --convertConfig --source ./
```

This creates a BoxLang formatter config from legacy cfformat configuration so existing style intent is preserved as much as possible.

### Phase 2: Validate with Check Mode

```bash
boxlang format --check --source ./
```

Run this in CI to detect any unexpected drift while your team validates behavior.

### Recommended Migration Strategy

1. Convert config using `--convertConfig`.
2. Run formatter once in a dedicated normalization commit.
3. Enable `--check` in CI to prevent future drift.
4. Refine `.bxformat.json` as project standards evolve.

{% hint style="info" %}
Compatibility mode for `.cfformat.json` is designed for migration safety. For long-term BoxLang-first teams, prefer `.bxformat.json` as the canonical source of formatting policy.
{% endhint %}

## 🧷 CI/CD Integration Patterns

### Minimal CI Step

```bash
boxlang format --check --source ./
```

### Recommended Team Policy

1. Developers run `boxlang format --source ./` before pushing changes.
2. CI enforces `boxlang format --check --source ./`.
3. Pull requests that fail check mode must be reformatted before merge.

This gives deterministic formatting without requiring a separate linter for stylistic concerns.

## 🧠 IDE Auto-Formatting (VS Code / BoxLang IDE)

For editor-on-save workflows and IDE formatter setup, the BoxLang LSP supports experimental formatting. Because this feature is still in beta, you need to explicitly enable it with a few steps.

### Enabling Experimental Formatting in VS Code

1. **Enable formatting in `.bxlint.json`** — Add the following to your project's `.bxlint.json`:

   ```json
   {
       "formatting": {
           "experimental": {
               "enabled": true
           }
       }
   }
   ```

2. **Enable format-on-save in VS Code** — Add this override to your VS Code `settings.json` (Workspace or User):

   ```json
   {
       "[boxlang]": {
           "editor.formatOnSave": true
       },
       "[boxlang-template]": {
           "editor.formatOnSave": true
       }
   }
   ```

3. **Update BoxLang & LSP versions** — Open the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`) and run:
   - `BoxLang: Select BoxLang Version` — choose the latest available version
   - `BoxLang: Select LSP Version` — choose the latest available version
   - `Developer: Reload Window` — to pick up the changes

Once these steps are completed, the formatter will run automatically when you save `.bx`, `.bxs`, `.bxm`, `.cfc`, `.cfm`, or `.cfs` files.

### Recommended Split of Responsibilities

- IDE format-on-save for fast local feedback
- CLI `--check` mode for authoritative CI enforcement

## 🧩 Complete `.bxformat.json` Schema Template

Copy this file to your project root as `.bxformat.json` and remove or adjust only the keys you want to override. All values shown are the Ortus gold-standard defaults.

{% hint style="info" %}
Run `boxlang format --initConfig` to generate this file automatically in your current directory instead of copy-pasting.
{% endhint %}

```json
{
  "indentSize": 4,
  "tabIndent": true,
  "maxLineLength": 120,
  "newLine": "os",
  "singleQuote": false,
  "preserveStringQuotes": false,
  "alignConsecutiveAssignments": true,
  "alignConsecutiveProperties": true,
  "bracketPadding": true,
  "parensPadding": true,
  "binaryOperatorsPadding": true,
  "semicolons": true,
  "cfFormatCompatibility": false,
  "sourceType": null,

  "struct": {
    "padding": true,
    "empty_padding": false,
    "quote_keys": false,
    "separator": ": ",
    "multiline": {
      "element_count": 2,
      "comma_dangle": false,
      "leading_comma": { "enabled": false, "padding": true },
      "min_length": 40
    }
  },

  "array": {
    "padding": true,
    "empty_padding": false,
    "multiline": {
      "element_count": 2,
      "comma_dangle": false,
      "leading_comma": { "enabled": false, "padding": true },
      "min_length": 40
    }
  },

  "property": {
    "multiline": {
      "element_count": 4,
      "comma_dangle": false,
      "leading_comma": { "enabled": false, "padding": true },
      "min_length": 40
    },
    "key_value": { "padding": false }
  },

  "for_loop_semicolons": { "padding": true },

  "function": {
    "style": "preserve",
    "parameters": {
      "padding": true,
      "empty_padding": false,
      "comma_dangle": false,
      "multiline_count": 3,
      "multiline_length": 40
    },
    "arrow": { "parens": "always" }
  },

  "arguments": {
    "padding": true,
    "empty_padding": false,
    "comma_dangle": false,
    "multiline_count": 3,
    "multiline_length": 40
  },

  "braces": {
    "style": "same-line",
    "require_for_single_statement": true,
    "else": { "style": "same-line" }
  },

  "operators": {
    "position": "end",
    "comparison_style": "symbols",
    "ternary": {
      "style": "flat",
      "question_position": "start"
    }
  },

  "chain": {
    "break_count": 3,
    "break_length": 60
  },

  "template": {
    "component_prefix": "bx",
    "indent_content": true,
    "single_attribute_per_line": false,
    "self_closing": true
  },

  "import": {
    "sort": false,
    "group": false
  },

  "comments": {
    "preserve_blank_lines": true,
    "wrap": false
  },

  "class": {
    "member_order": "preserve",
    "member_spacing": 1,
    "property_order": "preserve",
    "method_order": "preserve",
    "method_grouping": false
  },

  "sql": {
    "uppercase_keywords": true,
    "indent_clauses": true
  }
}
```

## 📚 Related Tooling

- [BoxLang Compiler](boxlang-compiler.md)
- [BoxLang AST](boxlang-ast.md)
- [CFML Transpiler](cfml-to-boxlang-transpiler.md)
- [CLI Scripting](../running-boxlang/cli-scripting.md)
