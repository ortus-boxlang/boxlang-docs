---
description: Discover if your application is compatible with BoxLang.
---

# CFML Feature Audit

the The BoxLang CFML Feature audit tool is a CLI tool that will scan your source code and give you a compatibility report.  This will allow you to see if your CFML code will run natively in BoxLang or if any BIFs or Components are required.   Like the other tools, this is based on our BL AST (BoxLang Abstract Syntax Tree), so it should be accurate and not require anything like regex. It’s using the actual BL ANTLR parsers.  **Before you run the tool, install the appropriate BoxLang modules so our tell can also account for those module collaborations.**

{% hint style="info" %}
Remember, as you read below, tags are now called “components” in BoxLang. This tool will parse tag-based and script-based code alike.
{% endhint %}

This CLI tool will scan

* a single file
* or a folder of files recursively (in parallel)

and will track:

* what BIFs you are using
* What Components (Tags) you are using

including the

* file name where it is used
* line number it was used on
* The module that BIF/component is from
* Whether or not that feature is missing from BoxLang currently (true/false)

Data tracked can be

* Every occurrence of a component or BIF
* aggregate of what BIFs/components were used per file
* aggregate summary of what BIFs/components were used across all files

and can be

* printed to console
* and/or written to CSV report file

### Usage <a href="#usage-1" id="usage-1"></a>

Like the other CLI tools, this is implemented as a separate Main class.  Pretty wrappers are coming soon.

The main syntax for calling the feature audit tool is

```bash
java -cp boxlang-1.0.0-all.jar ortus.boxlang.compiler.FeatureAudit  <options here>
```

### CLI Options

* `--source` - Defaults to working directory. If supplied, it must be followed by an absolute path or a path relative to the working directory.
* `--missing` - Filter results to only show BIFs and Components which are missing from BoxLang
* `--aggregate` - Instead of showing every usage instance, roll-up counts at the file level by default.
* `--aggregate summary` - If the arg “summary” is passed after the aggregate flag, we will roll the results up even further to include all files processed. In “summary” mode, the total number of files processed will also be output to the console, along with a breakdown of the number of file extensions encountered.
* `--quiet` - Do not output the details of what was found on the console. Use in conjunction with the report path arg if you want to write out a report file. Even in quiet mode, each file processed will be output.
* `--reportFile` - An absolute or relative (to the working dir) file path to write the data matching your filters and aggregate settings in a CSV format. Intermediate folders will be created. If the filename does not end with `.csv`, it will be appended.
  * The CSV columns, when not aggregating the data, will be `File,Name,Type,Module,Missing,Line`
  * The CSV columns, when aggregating data at a per-file level, will be: `File,Name,Type,Module,Missing,Count`
  * The CSV columns, when aggregating data at a summary level, will be: `Name,Type,Module,Missing,Count`

### Examples

Get a full report of all BIFs and Components used in a file

```bash
java -cp boxlang-1.0.0-all.jar ortus.boxlang.compiler.FeatureAudit --source includes/myFile.cfm
```

Scan all your models for missing BIFs and Components

```bash
java -cp boxlang-1.0.0-all.jar ortus.boxlang.compiler.FeatureAudit --source ./models/ --missing
```

Same as above, but aggregate results per file and write results to a CSV report

```css
java -cp boxlang-1.0.0-all.jar ortus.boxlang.compiler.FeatureAudit --source ./models/ --missing --aggregate --quiet --reportFile /path/to/models-missing-features.csv
```

Get a summary level aggregate report of all missing features in ColdBox output to the console

```css
java -cp boxlang-1.0.0-all.jar ortus.boxlang.compiler.FeatureAudit --source ./coldbox/ --missing --aggregate summary 
```
