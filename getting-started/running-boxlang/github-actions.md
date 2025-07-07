---
description: Run BoxLang in your GitHub actions seamlessly.
icon: github
---

# GitHub Actions

To run BoxLang in your GitHub Actions workflow, you need to add a step to your workflow file to set up and execute BoxLang. Below is an example of how you can use the action to run BoxLang with default settings:

```yaml
name: Run BoxLang

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up BoxLang
      uses: ortus-boxlang/setup-boxlang@1.0.0
      with:
        version: latest # or specify a version like '1.2.3'
        modules: "module1 module2" # optional: specify modules to install

    - name: Run BoxLang Script
      run: boxlangyour_script.bx
```

This setup installs BoxLang, optionally installs modules, and runs a BoxLang script within your repository. Adjust the `version` and `modules` as needed.

### Inputs

The following are all the different input variables you can use with the action, allowing you to set up BoxLang in your GitHub Actions workflow.

<table><thead><tr><th>Input</th><th width="115.16839599609375">Type</th><th>Default</th><th>Description</th></tr></thead><tbody><tr><td><code>modules</code></td><td>string</td><td>---</td><td>If added, a space-delimited list of modules to install upon installation of the binary for you.</td></tr><tr><td><code>version</code></td><td>semver</td><td><code>latest</code></td><td>The BoxLang version to install, if not passed we use the latest stable.</td></tr></tbody></table>

{% hint style="success" %}
**Tip:** You can use `snapshot` version to install the latest bleeding-edge version.
{% endhint %}

### Usage Examples

Simple usage:

```yaml
- name: Setup BoxLang
  uses: ortus-boxlang/setup-boxlang@1.0.0
```

With Specific Modules:

```yaml
- name: Setup BoxLang
  uses: ortus-boxlang/setup-boxlang@1.0.0
  with:
    modules: bx-ai bx-orm bx-pdf
```

Install a specific version of BoxLang:

```yaml
- name: Setup BoxLang with specific version
  uses: ortus-boxlang/setup-boxlang@1.0.0
  with:
    version: snapshot
```

Here is another one:

```yaml
- name: Setup BoxLang with specific version
  uses: ortus-boxlang/setup-boxlang@1.0.0
  with:
    version: 1.1.0
```

### System Requirements

This action will automatically install the following system packages if they are not already available:

* `openjdk-21-jre` (or equivalent) - Java Runtime Environment for BoxLang
