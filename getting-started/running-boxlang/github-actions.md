---
description: Run BoxLang in your GitHub Actions seamlessly with the official setup action.
icon: github
---

# GitHub Actions

🚀 **Automate your BoxLang setup** - This GitHub Action sets up the BoxLang Dynamic JVM Language runtime for CI/CD workflows with optional CommandBox CLI and module installation ([https://github.com/marketplace/actions/setup-boxlang-cli](https://github.com/marketplace/actions/setup-boxlang-cli))

{% embed url="https://github.com/marketplace/actions/setup-boxlang-cli" %}

## ⌨️ Action Inputs

Configure your BoxLang setup using these input parameters:

<table><thead><tr><th width="184.050537109375">Input</th><th width="88.269775390625">Type</th><th>Default</th><th>Description</th></tr></thead><tbody><tr><td><code>boxlang_home</code></td><td>string</td><td><code>${GITHUB_WORKSPACE}/.boxlang</code></td><td>Custom directory for BoxLang installation. Defaults to a writable directory in the workspace to avoid read-only filesystem issues.</td></tr><tr><td><code>commandbox_version</code></td><td>string</td><td><code>latest</code></td><td>The CommandBox version to install. Only used if <code>with-commandbox</code> is true.</td></tr><tr><td><code>commandbox_modules</code></td><td>string</td><td>---</td><td>If added, a comma-delimited list of CommandBox packages to install. Only used if <code>with-commandbox</code> is true.</td></tr><tr><td><code>forgeboxAPIKey</code></td><td>string</td><td>---</td><td>If added, it will configure the ForgeBox API Key in CommandBox. Only used if <code>with-commandbox</code> is true.</td></tr><tr><td><code>modules</code></td><td>string</td><td>---</td><td>If added, a space-delimited list of modules to install upon installation of the binary for you.</td></tr><tr><td><code>with-commandbox</code></td><td>boolean</td><td><code>false</code></td><td>If true, it will install the latest CommandBox as well.</td></tr><tr><td><code>version</code></td><td>semver</td><td><code>latest</code></td><td>The BoxLang version to install, if not passed we use the latest stable.</td></tr></tbody></table>

{% hint style="info" %}
**Version Options**:

* `latest` - Latest stable release
* `snapshot` - Latest development build
* `1.2.0` - Specific version number
* `1.x` - Latest in major version series
{% endhint %}

## 🔳 Usage Examples

### Simple Setup

```yaml
- name: Setup BoxLang
  uses: ortus-boxlang/setup-boxlang@main
```

### 📦 With BoxLang Modules

```yaml
- name: Setup BoxLang
  uses: ortus-boxlang/setup-boxlang@main
  with:
    modules: bx-ai bx-orm bx-pdf
```

### 🎯 Specific Version

```yaml
- name: Setup BoxLang with specific version
  uses: ortus-boxlang/setup-boxlang@main
  with:
    version: snapshot
```

### 📦 With CommandBox

```yaml
- name: Setup BoxLang with CommandBox
  uses: ortus-boxlang/setup-boxlang@main
  with:
    with-commandbox: true
```

### 🔧 CommandBox with Specific Version

```yaml
- name: Setup BoxLang with specific CommandBox version
  uses: ortus-boxlang/setup-boxlang@main
  with:
    with-commandbox: true
    commandbox_version: 6.0.0
```

### 🛠️ CommandBox with Modules

```yaml
- name: Setup BoxLang with CommandBox and modules
  uses: ortus-boxlang/setup-boxlang@main
  with:
    with-commandbox: true
    commandbox_modules: commandbox-cfconfig,commandbox-dotenv
```

### ⚙️ Full Configuration Example

```yaml
- name: Setup BoxLang with CommandBox (full setup)
  uses: ortus-boxlang/setup-boxlang@main
  with:
    with-commandbox: true
    commandbox_version: 6.0.0
    commandbox_modules: commandbox-cfconfig,commandbox-dotenv,commandbox-fusionreactor
```

### 🔑 With ForgeBox API Key

```yaml
- name: Setup BoxLang with CommandBox and ForgeBox API Key
  uses: ortus-boxlang/setup-boxlang@main
  with:
    with-commandbox: true
    forgeboxAPIKey: ${{ secrets.FORGEBOX_API_KEY }}
```

### 🎯 Specific Version with Modules

```yaml
- name: Setup BoxLang with specific version
  uses: ortus-boxlang/setup-boxlang@main
  with:
    version: 1.2.0
    modules: bx-compat-cfml bx-mail
```

## 📦 Action Outputs

This action provides the following outputs for use in subsequent workflow steps:

* `boxlang-version`: The version of BoxLang that was installed
* `installation-path`: The path where BoxLang was installed

## 🔧 Complete CI/CD Examples

### Quick Start Example

```yaml
name: BoxLang CI/CD

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v6

    - name: Set up BoxLang
      uses: ortus-boxlang/setup-boxlang@main
      with:
        version: latest
        modules: "bx-compat-cfml bx-mail"

    - name: Run BoxLang Tests
      run: boxlang test-runner.bx

    - name: Run BoxLang Application
      run: boxlang app.bx
```

### Web Application Testing

```yaml
name: BoxLang Web App CI

on:
  push:
    branches: [ main, development ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        boxlang-version: [latest, snapshot]

    steps:
    - name: Checkout repository
      uses: actions/checkout@v6

    - name: Setup BoxLang ${{ matrix.boxlang-version }}
      uses: ortus-boxlang/setup-boxlang@main
      with:
        version: ${{ matrix.boxlang-version }}
        modules: "bx-compat-cfml bx-mysql bx-mail bx-esapi"

    - name: Verify BoxLang Installation
      run: |
        boxlang --version
        boxlang --bx-code "println( 'BoxLang is ready!' )"

    - name: Run Unit Tests
      run: boxlang tests/runner.bx

    - name: Run Integration Tests
      run: boxlang tests/integration-suite.bx
      env:
        DB_HOST: localhost
        DB_NAME: testdb
```

### Module Development Workflow

```yaml
name: BoxLang Module Development

on:
  push:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout module source
      uses: actions/checkout@v6

    - name: Setup BoxLang with Development Dependencies
      uses: ortus-boxlang/setup-boxlang@main
      with:
        version: snapshot
        modules: "bx-compat-cfml"

    - name: Install Module Dependencies
      run: |
        # Install any required dependencies for your module
        boxlang install-module.bx

    - name: Run Module Tests
      run: boxlang test-runner.bx

    - name: Verify Module API
      run: boxlang api-tests.bx

    - name: Package Module
      run: boxlang build-module.bx

    - name: Upload Module Artifacts
      uses: actions/upload-artifact@v3
      with:
        name: boxlang-module-${{ github.sha }}
        path: dist/
```

### Multi-Platform Testing

```yaml
name: Cross-Platform BoxLang Testing

on: [push, pull_request]

jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        boxlang-version: [latest, "1.4.0"]

    runs-on: ${{ matrix.os }}

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Setup BoxLang on ${{ matrix.os }}
      uses: ortus-boxlang/setup-boxlang@main
      with:
        version: ${{ matrix.boxlang-version }}
        modules: "bx-compat-cfml bx-mail"

    - name: Run Platform-Specific Tests
      run: boxlang tests/platform-tests.bx
      shell: bash  # Ensures consistent shell across platforms
```

### Enterprise CommandBox Deployment

```yaml
name: Enterprise BoxLang Deployment

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout application
      uses: actions/checkout@v4

    - name: Setup BoxLang with CommandBox
      uses: ortus-boxlang/setup-boxlang@main
      with:
        version: latest
        with-commandbox: true
        modules: "bx-compat-cfml bx-orm bx-mysql bx-redis"

    - name: Verify CommandBox Installation
      run: |
        box version
        boxlang --version

    - name: Build Application Package
      run: |
        box package build
        box server start --dryRun

    - name: Run Application Tests
      run: |
        box testbox run
        boxlang integration-tests.bx
```





## 🐛 Troubleshooting

### Common Issues

**Action fails with Java not found:**

* The action automatically installs OpenJDK 21. If you see Java errors, try updating to the latest action version.

**Module installation timeout:**

* Large modules may take time to install. Consider caching or installing only necessary modules.

**Permission errors on Windows:**

* Ensure your workflow has proper permissions set for the Windows runner.

### Debug Mode

Enable debug output for troubleshooting:

```yaml
- name: Setup BoxLang with Debug
  uses: ortus-boxlang/setup-boxlang@main
  with:
    version: latest
    modules: "bx-compat-cfml"
  env:
    ACTIONS_RUNNER_DEBUG: true
```
