---
description: Run BoxLang in your GitHub Actions seamlessly with the official setup action.
icon: github
---

# GitHub Actions

Integrate BoxLang into your CI/CD workflows with the official **setup-boxlang** GitHub Action. This action provides comprehensive BoxLang runtime setup, module installation, and optional CommandBox integration for your GitHub Actions workflows.

## 🚀 Quick Start

To run BoxLang in your GitHub Actions workflow, add the setup step to your workflow file. Here's a basic example:

```yaml
name: BoxLang CI/CD

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up BoxLang
      uses: ortus-boxlang/setup-boxlang@1.1.0
      with:
        version: latest # or specify a version like '1.5.0'
        modules: "bx-compat-cfml bx-mail" # optional: install modules

    - name: Run BoxLang Tests
      run: boxlang test-runner.bx

    - name: Run BoxLang Application
      run: boxlang app.bx
```

## 📋 Action Inputs

The following input parameters allow you to customize the BoxLang setup for your specific needs:

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| `version` | semver | `latest` | BoxLang version to install. Use `latest` for stable, `snapshot` for bleeding-edge, or specific version like `1.5.0` |
| `modules` | string | --- | Space-delimited list of BoxLang modules to install automatically |
| `with-commandbox` | boolean | `false` | When `true`, installs CommandBox alongside BoxLang for enterprise features |

{% hint style="info" %}
**Version Options**:

- `latest` - Latest stable release
- `snapshot` - Latest development build
- `1.5.0` - Specific version number
- `1.x` - Latest in major version series

{% endhint %}

## 💡 Usage Examples

### Basic Setup

Minimal setup with latest BoxLang version:

```yaml
- name: Setup BoxLang
  uses: ortus-boxlang/setup-boxlang@1.1.0
```

### With Specific Version

Install a specific BoxLang version:

```yaml
- name: Setup BoxLang 1.5.0
  uses: ortus-boxlang/setup-boxlang@1.1.0
  with:
    version: "1.5.0"
```

### With Snapshot/Development Version

Use the latest development version:

```yaml
- name: Setup BoxLang Snapshot
  uses: ortus-boxlang/setup-boxlang@1.1.0
  with:
    version: snapshot
```

### With BoxLang Modules

Install BoxLang with commonly used modules:

```yaml
- name: Setup BoxLang with Modules
  uses: ortus-boxlang/setup-boxlang@1.1.0
  with:
    version: latest
    modules: "bx-compat-cfml bx-mail bx-mysql bx-redis bx-esapi"
```

### With CommandBox Integration

Enable CommandBox for enterprise servlet deployments:

```yaml
- name: Setup BoxLang with CommandBox
  uses: ortus-boxlang/setup-boxlang@1.1.0
  with:
    version: latest
    with-commandbox: true
    modules: "bx-compat-cfml bx-orm"
```

## 🔧 Complete CI/CD Examples

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
      uses: actions/checkout@v4

    - name: Setup BoxLang ${{ matrix.boxlang-version }}
      uses: ortus-boxlang/setup-boxlang@1.1.0
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
      uses: actions/checkout@v4

    - name: Setup BoxLang with Development Dependencies
      uses: ortus-boxlang/setup-boxlang@1.1.0
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
      uses: ortus-boxlang/setup-boxlang@1.1.0
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
      uses: ortus-boxlang/setup-boxlang@1.1.0
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

## 🔍 System Requirements

The action automatically installs required dependencies:

- **Java Runtime**: OpenJDK 21 (or equivalent JRE)
- **System packages**: curl, unzip, and other utilities as needed
- **BoxLang Runtime**: Complete BoxLang installation
- **CommandBox** (optional): When `with-commandbox: true`

{% hint style="success" %}
**Automatic Dependency Management**: The action handles all system requirements automatically. No manual Java or system package installation needed!
{% endhint %}

## 📦 Popular Module Combinations

### Web Development Stack

```yaml
modules: "bx-compat-cfml bx-orm bx-mysql bx-redis bx-mail bx-esapi"
```

### API Development

```yaml
modules: "bx-mysql bx-redis bx-mail bx-compat-cfml"
```

### Data Processing Pipeline

```yaml
modules: "bx-mysql bx-derby bx-excel bx-pdf bx-mail"
```

### Enterprise Integration

```yaml
modules: "bx-compat-cfml bx-orm bx-mysql bx-redis bx-elasticsearch bx-mail bx-esapi"
```

## 🐛 Troubleshooting

### Common Issues

**Action fails with Java not found:**

- The action automatically installs OpenJDK 21. If you see Java errors, try updating to the latest action version.

**Module installation timeout:**

- Large modules may take time to install. Consider caching or installing only necessary modules.

**Permission errors on Windows:**

- Ensure your workflow has proper permissions set for the Windows runner.

### Debug Mode

Enable debug output for troubleshooting:

```yaml
- name: Setup BoxLang with Debug
  uses: ortus-boxlang/setup-boxlang@1.1.0
  with:
    version: latest
    modules: "bx-compat-cfml"
  env:
    ACTIONS_RUNNER_DEBUG: true
```

## 🔗 Additional Resources

- **Action Repository**: [https://github.com/ortus-boxlang/setup-boxlang](https://github.com/ortus-boxlang/setup-boxlang)
- **BoxLang Documentation**: [https://boxlang.ortusbooks.com](https://boxlang.ortusbooks.com)
- **GitHub Actions Marketplace**: [setup-boxlang action](https://github.com/marketplace/actions/setup-boxlang)
- **BoxLang Community**: [https://community.ortussolutions.com](https://community.ortussolutions.com)

{% hint style="info" %}
**Professional Support**: BoxLang+ and BoxLang++ subscribers receive priority support for CI/CD integration and GitHub Actions workflows. Visit [boxlang.io/plans](https://boxlang.io/plans) for more information.
{% endhint %}
