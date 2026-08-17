---
description: Validate BoxLang and CFML source files for syntax errors without executing them.
icon: square-check
---

# ✅ BoxLang Syntax Check

The BoxLang Syntax Check tool (`check`) is a CLI action command that parses one or more source files and reports syntax errors, **without executing the code or compiling it to bytecode**. It's the BoxLang equivalent of `bash -n script.sh` or `node --check file.js` — a fast way to validate that your code is well-formed before you run it, commit it, or ship it.

This makes it a great fit for:

* Pre-commit and git hooks
* CI pipelines, as a fast fail-early step before running the full test suite
* Editor/IDE tooling integrations (via `--format json`)

Like the other BoxLang CLI tools, syntax checking is based on our BL AST (BoxLang Abstract Syntax Tree) and the actual BL ANTLR parsers, so results are accurate for both BoxLang and CFML source.

## Usage

Make sure you have installed the OS version of [BoxLang](../installation/) so you get all the tools installed as well. Please note that the action command funnels through the `boxlang` binary, so you can use all the [CLI arguments](../running-boxlang/#other-command-line-args-10) for the `boxlang` runner.

```bash
// Using the script
boxlang check [OPTIONS] [FILE...]

// Using the full path to the jar
java -cp boxlang-1.0.0.jar ortus.boxlang.compiler.SyntaxCheck [OPTIONS] [FILE...]
```

You can pass one or more explicit file paths, a `--source` directory to scan recursively, or both.

### Supported Source Files

`.cfm` `.cfc` `.cfs` `.bx` `.bxs` `.bxm`

### CLI Options

* `-h, --help` - Show the help message and exit.
* `--source <PATH>` - Path to a source directory or file to check. When a directory is given, it is walked recursively and every supported file extension is checked.
* `--format <text|json>` - Output format. Defaults to `text`. Use `json` for machine-readable output suited to editor/CI tooling integration.
* `-q, --quiet` - Suppress the per-file success output and summary line. Failures are always reported, even in quiet mode.

You can also pass one or more file paths directly as positional arguments, instead of (or in addition to) `--source`.

### Exit Codes

* `0` - Every checked file is syntactically valid.
* `1` - One or more files have syntax errors, or a usage error occurred (e.g. a missing `--source` path).

## Examples

Check one or more specific files:

```bash
// Using the script
boxlang check myapp.bx myComponent.cfc

// Using the full path to the jar
java -cp boxlang-1.0.0.jar ortus.boxlang.compiler.SyntaxCheck myapp.bx myComponent.cfc
```

Check an entire directory recursively, e.g. in CI or a git hook:

```bash
// Using the script
boxlang check --source ./src

// Using the full path to the jar
java -cp boxlang-1.0.0.jar ortus.boxlang.compiler.SyntaxCheck --source ./src
```

Get machine-readable output for editor/CI tooling:

```bash
// Using the script
boxlang check --source ./src --format json
```

### Sample Output

A valid file produces minimal output and exits `0`:

```
$ boxlang check good.bxs
✅ good.bxs

───────────────────────────────
✅ 1 valid   ❌ 0 invalid   (1 files checked)
```

An invalid file reports the file, line, column, and message, and exits `1`:

```
$ boxlang check bad.bxs
❌ bad.bxs
   bad.bxs: Line: 1 Col: 3 - Unclosed parenthesis [(] on line 1
if ( true {
   ^

───────────────────────────────
✅ 0 valid   ❌ 1 invalid   (1 files checked)
```

Checking a directory reports every file that was scanned, with a combined summary:

```
$ boxlang check --source ./demo
❌ /path/to/demo/bad.bxs
   /path/to/demo/bad.bxs: Line: 1 Col: 3 - Unclosed parenthesis [(] on line 1
if ( true {
   ^
✅ /path/to/demo/good.bxs

───────────────────────────────
✅ 1 valid   ❌ 1 invalid   (2 files checked)
```

`--format json` returns an array of `{file, valid, issues}` records, one per checked file:

```json
[ {
  "file" : "/path/to/demo/bad.bxs",
  "valid" : false,
  "issues" : [ {
    "message" : "Unclosed parenthesis [(] on line 1\nif ( true {\n   ^",
    "line" : 1,
    "column" : 3
  } ]
}, {
  "file" : "/path/to/demo/good.bxs",
  "valid" : true,
  "issues" : [ ]
} ]
```
