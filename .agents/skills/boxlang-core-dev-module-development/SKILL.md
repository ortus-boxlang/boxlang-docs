---
name: boxlang-core-dev-module-development
description: "Use this skill when creating a BoxLang module: ModuleConfig.bx structure, lifecycle methods (configure/onLoad/onUnload), module metadata, registering interceptors and BIFs, Gradle build setup, publishing to ForgeBox, or using the official module template."
---

# BoxLang Module Development

## Overview

A BoxLang module is a packaged unit of functionality that extends the runtime
with new built-in functions (BIFs), components, interceptors, and Java libraries.
Modules are auto-discovered by the runtime on startup and managed through the
`ModuleService`. The [official module template](https://github.com/ortus-boxlang/boxlang-module-template)
is the recommended starting point.

## Module Directory Structure

```
my-module/
├── ModuleConfig.bx          # Required: module descriptor and lifecycle
├── box.json                 # CommandBox/ForgeBox package manifest
├── build.gradle             # Gradle build configuration
├── gradle/
│   └── wrapper/
├── bifs/                    # Custom built-in functions
│   ├── MyFunction.bx        # BoxLang BIF
│   └── MyJavaFunction.java  # Java BIF
├── components/              # Custom tags/components
│   └── MyComponent.bx
├── interceptors/            # Event listeners
│   └── MyInterceptor.bx
├── models/                  # Supporting classes and services
│   └── MyService.bx
├── libs/                    # JAR dependencies (module-scoped)
│   └── some-library.jar
├── src/
│   ├── main/
│   │   ├── bx/              # BoxLang source (mirrored into module root)
│   │   └── java/            # Java source
│   └── test/
│       ├── bx/              # BoxLang tests
│       └── java/            # Java unit tests
└── settings.gradle
```

## `ModuleConfig.bx`

The heart of every module. Must exist (can be empty, but lifecycle methods are recommended):

```boxlang
// ModuleConfig.bx
class {

    // --- Module Metadata ---
    // These are read by the ModuleService
    this.title       = "My Awesome Module"
    this.author      = "Your Name <you@example.com>"
    this.description = "Does amazing things for BoxLang"
    this.version     = "1.0.0"
    this.boxlangVersion = ">=1.10.0"

    // Module settings with defaults (overridden by boxlang.json)
    this.settings = {
        apiKey      : "",
        baseUrl     : "https://api.example.com",
        timeout     : 30,
        retryCount  : 3,
        debugMode   : false
    }

    // Interceptors to auto-register on module load
    this.interceptors = [
        {
            class      : "#moduleRecord.invocationPath#.interceptors.RequestLogger",
            properties : { logLevel: "INFO" }
        }
    ]

    // Component paths to register
    this.componentPaths = [
        "#moduleRecord.physicalPath#/components"
    ]

    // --- Lifecycle Methods ---

    /**
     * Called first. Set up default settings, validate config, etc.
     * The `settings` struct is already merged with user overrides by this point.
     */
    function configure() {
        // Validate required settings
        if ( !len( settings.apiKey ) ) {
            throw(
                message = "bx-mymodule: apiKey setting is required",
                type    = "bx-mymodule.ConfigurationError"
            )
        }

        // Set computed settings
        settings.baseUrlWithVersion = settings.baseUrl & "/v1"

        // Register custom datasource, cache, etc.
    }

    /**
     * Called after the module is fully loaded and registered.
     * Use for resource initialization, warm-up, service registration.
     */
    function onLoad() {
        // Register a service in the BoxRuntime IOC container
        // boxRuntime.registerService( "MyService", new models.MyService( settings ) )

        // Log startup
        log.info( "bx-mymodule loaded successfully. Version: #this.version#" )
    }

    /**
     * Called when the module is unloaded (server shutdown, hot-reload).
     * Use for cleanup, closing connections, flushing buffers.
     */
    function onUnload() {
        // Close connections, cleanup resources
        log.info( "bx-mymodule unloaded." )
    }

}
```

## Available Injection Variables in ModuleConfig

BoxLang injects these variables into `ModuleConfig.bx` automatically:

| Variable | Type | Description |
|---|---|---|
| `settings` | Struct | Merged module settings (defaults + user overrides) |
| `moduleRecord` | Struct | Module metadata: `name`, `version`, `physicalPath`, `invocationPath` |
| `boxRuntime` | BoxRuntime | The BoxLang runtime instance |
| `log` | Logger | Module-specific logger |
| `interceptorService` | InterceptorService | To register interceptors programmatically |
| `moduleService` | ModuleService | To interact with other modules |
| `wirebox` | WireBox | IOC container (if bx-wirebox is installed) |

## `box.json` — Package Manifest

```json
{
    "name": "bx-mymodule",
    "version": "1.0.0",
    "author": "Your Name",
    "description": "Does amazing things for BoxLang",
    "homepage": "https://github.com/you/bx-mymodule",
    "keywords": ["boxlang", "module"],
    "license": "Apache-2.0",
    "repository": {
        "type": "git",
        "url": "https://github.com/you/bx-mymodule"
    },
    "dependencies": {},
    "devDependencies": {
        "testbox": "^5.0.0"
    },
    "type": "boxlang-module",
    "boxlangVersion": ">=1.10.0"
}
```

## Gradle Build Setup

Based on the [official module template](https://github.com/ortus-boxlang/boxlang-module-template):

```groovy
// build.gradle
plugins {
    id "java"
    id "com.diffplug.spotless" version "6.25.0"
}

repositories {
    mavenCentral()
    maven { url "https://downloads.ortussolutions.com/maven" }
}

dependencies {
    // BoxLang runtime (downloaded by downloadBoxLang task)
    compileOnly files( "libs/boxlang-1.0.0-all.jar" )
    testImplementation files( "libs/boxlang-1.0.0-all.jar" )

    // Your dependencies
    implementation "com.example:my-library:1.2.3"
}

// Key Gradle tasks:
// ./gradlew downloadBoxLang  - Download the BoxLang binary (run first!)
// ./gradlew build            - Compile and package
// ./gradlew test             - Run all tests
// ./gradlew jar              - Package into JAR only
// ./gradlew clean            - Remove build artifacts
```

### Running Gradle Tasks

```bash
# Initial setup — download BoxLang runtime
./gradlew downloadBoxLang

# Full build
./gradlew build

# Run tests
./gradlew test

# Package for distribution
./gradlew jar

# Check code formatting
./gradlew spotlessCheck

# Auto-fix formatting
./gradlew spotlessApply
```

## Module Settings — User Configuration

Users configure module settings in their `boxlang.json`:

```json
{
    "modules": {
        "bx-mymodule": {
            "enabled": true,
            "settings": {
                "apiKey"    : "user-api-key-here",
                "timeout"   : 60,
                "debugMode" : false
            }
        }
    }
}
```

Access settings in `ModuleConfig.bx` or BIFs via the `settings` struct.

## Accessing Settings From BIFs and Interceptors

```boxlang
// In any BIF or interceptor inside your module
class {

    function invoke() {
        // Get the module settings
        var moduleSettings = boxRuntime
            .getModuleService()
            .getModuleRecord( "bx-mymodule" )
            .settings

        var apiKey = moduleSettings.apiKey
        // ...
    }

}
```

## Publishing to ForgeBox

```bash
# Login to ForgeBox
box forgebox login

# Publish
box forgebox publish

# Or bump version then publish
box bump --minor
box forgebox publish
```

## Hot Reload During Development

```bash
# Reload a module without restarting the server
box server reload
# or via CommandBox shell:
box> reload
```

## Module Integration Test Pattern

```boxlang
// tests/specs/MyModuleTest.bx
class extends="testbox.system.BaseSpec" {

    function beforeAll() {
        // Load the module into a test runtime
        setup()
    }

    function run() {
        describe( "My Module BIFs", function() {

            it( "should call myFunction and return the expected result", function() {
                var result = myFunction( "test" )
                expect( result ).toBe( "expected" )
            })

        })
    }

}
```

```bash
# Run tests
box testbox run
```

## References

- [BoxLang Module Template](https://github.com/ortus-boxlang/boxlang-module-template)
- [Modularity Docs](https://boxlang.ortusbooks.com/boxlang-framework/modularity)
- [Module Configuration](https://boxlang.ortusbooks.com/getting-started/configuration#modules)
- [ForgeBox](https://forgebox.io)
- [BoxLang Source](https://github.com/ortus-boxlang/BoxLang)
