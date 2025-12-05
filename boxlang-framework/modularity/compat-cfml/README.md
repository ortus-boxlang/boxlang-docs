---
description: >-
  This module allows your BoxLang engine to simulate an Adobe ColdFusion or
  Lucee CFML server for seamless migration with zero code changes
icon: bolt
---

# Compat CFML

## Welcome to the BoxLang Compatibility Module For CFML

The **BoxLang CFML Compatibility Module** (`bx-compat-cfml`) transforms BoxLang's runtime behavior to match Adobe ColdFusion or Lucee CFML servers, enabling **zero-code migration** (HOPEFULLY, this is not guaranteed) of existing CFML applications to BoxLang. This comprehensive compatibility layer ensures your legacy CFML applications run identically under BoxLang without modification.

### 🎯 Purpose

This module bridges the behavioral differences between BoxLang's modern runtime and traditional CFML engines by:

* **Runtime Behavior Simulation** - Mimics null handling, type coercion, and comparison semantics
* **Server Scope Compatibility** - Seeds the `server` scope with engine-specific metadata
* **CFML BIF Compatibility** - Provides legacy function signatures and behaviors
* **Client Scope Management** - Emulates Adobe/Lucee client variable storage
* **JSON Parsing Flexibility** - Supports lenient JSON parsing like Lucee
* **Query Result Compatibility** - Matches Adobe/Lucee query null handling
* **AST Transpiler Settings** - Controls how CFML code is transpiled to BoxLang

### 📦 Installation

If there are any issues, please report them to the [BoxLang JIRA](https://ortussolutions.atlassian.net/browse/BL/issues) or the [Module Issues](https://github.com/ortus-boxlang/bx-compat-cfml/issues) repository.

```bash
# For Operating Systems using the Quick Installer
install-bx-module bx-compat-cfml

# Using CommandBox for web servers
box install bx-compat-cfml
```

---

## ⚙️ Configuration Settings

The module provides extensive configuration options to control runtime behavior. All settings can be configured via your `boxlang.json` configuration file or the module's default settings.

### Complete Settings Reference

```js
settings = {
	// ========================================
	// Engine Selection
	// ========================================

	// Choose your target engine: "adobe" or "lucee"
	// This determines which compatibility interceptor loads and how the server scope is populated
	engine = "lucee",

	// Auto-set based on engine selection (read-only)
	isLucee = false,
	isAdobe = false,

	// ========================================
	// Client Scope Management
	// ========================================

	// Enable Adobe/Lucee client variable management
	clientManagement = false,

	// Client storage mechanism
	// Options: "cache" (uses bxClients cache), or specify your own cache name
	// Legacy options "cookie" and "registry" will fallback to cache storage
	clientStorage = "cache",

	// Default client variable timeout (timespan)
	clientTimeout = createTimeSpan( 0, 1, 0, 0 ), // 1 hour

	// ========================================
	// Null & Type Coercion Behavior
	// ========================================

	// Mimic CFML behavior where null is treated as undefined
	// Set to false for full Java-style null support
	nullIsUndefined = true,

	// Mimic CF/Lucee 5 behavior where boolean true/false = 1/0 in math operations
	// Also affects isNumeric() BIF behavior
	// Set to false to match Lucee 6 behavior
	booleansAreNumbers = true,

	// Auto-cast Java Class instances to strings (calls toString())
	castClassesToStrings = true,

	// Auto-cast Java Throwable instances to strings (calls toString())
	castThrowablesToStrings = true,

	// Perform loose date comparison only to instant level (ignores timezone)
	// Mimics CFML date comparison behavior
	lenientDateComparison = true,

	// Treat null and empty string as equal in comparisons
	// Matches Adobe/Lucee behavior
	nullEqualsEmptyString = true,

	// ========================================
	// JSON Handling
	// ========================================

	// Auto-escape JSON control characters during serialization
	// WARNING: Enabling this escapes the entire JSON output and impacts performance
	jsonEscapeControlCharacters = true,

	// Allow lenient JSON parsing (like Lucee)
	// Accepts: single quotes, unquoted keys, trailing commas, leading numeric zeroes
	// Note: Adobe always uses strict JSON parsing (this setting ignored when engine="adobe")
	lenientJSONParsing = true,

	// ========================================
	// Query Behavior
	// ========================================

	// Convert query null values to empty strings (when not in full null support mode)
	// Simulates Adobe/Lucee query result behavior
	queryNullToEmpty = true,

	// ========================================
	// Struct Casting Behavior
	// ========================================

	// Allow ANY Java class to be generically cast to struct (uses public fields/getters)
	// CF allows even closures to be passed into struct BIFs
	// BoxLang normally only uses generic class-to-struct logic for isObject() types
	// Set to true for maximum Adobe/Lucee compatibility
	extraLooseStructCasting = true,

	// ========================================
	// CFML to BoxLang Transpiler Settings
	// ========================================

	transpiler = {
		// Convert all keys to uppercase (foo.bar becomes foo.BAR)
		// Matches CFML case-insensitive key behavior
		upperCaseKeys = true,

		// Add output=true attribute to all functions and components
		// Matches CFML default output behavior
		forceOutputTrue = true,

		// Merge JavaDoc-style comments into function/class/property annotations
		// Matches CFML hint/documentation behavior
		mergeDocsIntoAnnotations = true
	},

	// ========================================
	// Server Lifecycle
	// ========================================

	// Enable Application.cfc/cfm onServerStart() event interception
	serverStartEnabled = true,

	// Path to Application.cfc/cfm for server start event
	// Can be dot-delimited path using mappings or absolute file path
	serverStartPath = ""
};
```

The valid engines are `adobe` or `lucee` (default: `lucee`). All module settings can be overridden via the `boxlang.json` configuration file.

### Example boxlang.json Configuration

```json
{
	"modules": {
		"compat-cfml": {
			"disabled": false,
			"settings": {
				"engine": "adobe",
				"clientManagement": true,
				"clientStorage": "cache",
				"nullIsUndefined": true,
				"booleansAreNumbers": true,
				"castClassesToStrings": true,
				"castThrowablesToStrings": true,
				"lenientDateComparison": true,
				"nullEqualsEmptyString": true,
				"jsonEscapeControlCharacters": true,
				"queryNullToEmpty": true,
				"extraLooseStructCasting": true,
				"lenientJSONParsing": false,
				"transpiler": {
					"upperCaseKeys": true,
					"forceOutputTrue": true,
					"mergeDocsIntoAnnotations": true
				},
				"serverStartEnabled": true,
				"serverStartPath": "/path/to/Application.cfc"
			}
		}
	}
}
```

---

## 🎭 Engine-Specific Behavior

### Server Scope Simulation

Depending on which engine you select (`adobe` or `lucee`), a corresponding interceptor will be loaded that seeds the `server` scope with engine-specific metadata, ensuring your CFML code sees the expected server information.

**Adobe Mode (`engine = "adobe"`):**

* Loads `AdobeServerScope` interceptor
* Populates `server.coldfusion` struct with Adobe-specific keys
* Sets `server.coldfusion.productname = "ColdFusion Server"`
* Automatically disables `lenientJSONParsing` (Adobe uses strict JSON)

**Lucee Mode (`engine = "lucee"`):**

* Loads `LuceeServerScope` interceptor
* Populates `server.lucee` struct with Lucee-specific keys
* Sets `server.lucee.version` and other Lucee metadata
* Enables `lenientJSONParsing` by default

### Additional Interceptors

The module registers several compatibility interceptors regardless of engine selection:

* **`QueryCompat`** - Ensures query result compatibility (null handling, column types)
* **`ClientScopeListener`** - Manages client variable lifecycle (when `clientManagement = true`)
* **`ApplicationCompatListener`** - Application scope compatibility
* **`SessionListener`** - Session scope compatibility
* **`DateTimeMaskCompat`** - Date/time formatting mask compatibility
* **`ORMApplicationListener`** - ORM compatibility (if ORM is enabled)
* **`RuntimeConfigListener`** - Runtime configuration compatibility

---

## 📚 Contributed Built-In Functions (BIFs)

The compat module registers the following CFML-compatible BIFs globally in the BoxLang runtime:

### Cache Management Functions

| Function | Description | CFDocs Reference |
|----------|-------------|------------------|
| `cacheClear()` | Clears all cached items from a cache region | [CFDocs](https://cfdocs.org/cacheclear) |
| `cacheCount()` | Returns the number of cached items in a cache region | [CFDocs](https://cfdocs.org/cachecount) |
| `cacheGet()` | Retrieves a cached item by key | [CFDocs](https://cfdocs.org/cacheget) |
| `cacheGetAll()` | Returns all cached items as a struct | [CFDocs](https://cfdocs.org/cachegetall) |
| `cacheGetAllIds()` | Returns an array of all cache keys | [CFDocs](https://cfdocs.org/cachegetallids) |
| `cacheGetAsAttempt()` | Retrieves a cached item wrapped in an Attempt monad | [CFDocs](https://cfdocs.org/cachegetasattempt) |
| `cacheGetDefaultCacheName()` | Returns the default cache name | [CFDocs](https://cfdocs.org/cachegetdefaultcachename) |
| `cacheGetEngineProperties()` | Returns the cache engine properties | [CFDocs](https://cfdocs.org/cachegetengineproperties) |
| `cacheGetMetadata()` | Returns metadata for a cached item | [CFDocs](https://cfdocs.org/cachegetmetadata) |
| `cacheGetOrFail()` | Retrieves a cached item or throws an exception if not found | [CFDocs](https://cfdocs.org/cachegetorfail) |
| `cacheGetProperties()` | Returns cache properties | [CFDocs](https://cfdocs.org/cachegetproperties) |
| `cacheGetSession()` | Returns the cache session configuration | [CFDocs](https://cfdocs.org/cachegetsession) |
| `cacheIdExists()` | Checks if a cache key exists | [CFDocs](https://cfdocs.org/cacheidexists) |
| `cachePut()` | Stores an item in the cache | [CFDocs](https://cfdocs.org/cacheput) |
| `cacheRegionExists()` | Checks if a cache region exists | [CFDocs](https://cfdocs.org/cacheregionexists) |
| `cacheRegionNew()` | Creates a new cache region | [CFDocs](https://cfdocs.org/cacheregionnew) |
| `cacheRegionRemove()` | Removes a cache region | [CFDocs](https://cfdocs.org/cacheregionremove) |
| `cacheRemove()` | Removes a cached item by key | [CFDocs](https://cfdocs.org/cacheremove) |
| `cacheRemoveAll()` | Removes all cached items (alias for cacheClear) | [CFDocs](https://cfdocs.org/cacheremoveall) |
| `cacheSetProperties()` | Sets cache properties | [CFDocs](https://cfdocs.org/cachesetproperties) |

### Client Variable Functions

| Function | Description | CFDocs Reference |
|----------|-------------|------------------|
| `deleteClientVariable()` | Deletes a client variable by name | [CFDocs](https://cfdocs.org/deleteclientvariable) |
| `getClientVariablesList()` | Returns a list of all client variable names | [CFDocs](https://cfdocs.org/getclientvariableslist) |

### Metadata & Introspection Functions

| Function | Description | CFDocs Reference |
|----------|-------------|------------------|
| `getComponentMetadata()` | Returns metadata for a component | [CFDocs](https://cfdocs.org/getcomponentmetadata) |
| `getContextRoot()` | Returns the web application context root path | [CFDocs](https://cfdocs.org/getcontextroot) |
| `getFunctionData()` | Returns metadata about a built-in function | [CFDocs](https://cfdocs.org/getfunctiondata) |
| `getMetaData()` | Returns metadata for a component or object | [CFDocs](https://cfdocs.org/getmetadata) |
| `getTagData()` | Returns metadata about a CFML tag | [CFDocs](https://cfdocs.org/gettagdata) |
| `getVariable()` | Retrieves a variable by name from a scope | [CFDocs](https://cfdocs.org/getvariable) |
| `setVariable()` | Sets a variable in a scope by name | [CFDocs](https://cfdocs.org/setvariable) |

### Date/Time Functions

| Function | Description | CFDocs Reference |
|----------|-------------|------------------|
| `createDateTime()` | Creates a datetime object (Adobe/Lucee signature) | [CFDocs](https://cfdocs.org/createdatetime) |
| `dateCompare()` | Compares two dates with CFML-compatible semantics | [CFDocs](https://cfdocs.org/datecompare) |
| `dateTimeFormat()` | Formats a datetime with CFML mask patterns | [CFDocs](https://cfdocs.org/datetimeformat) |
| `getHTTPTimeString()` | Returns current time as HTTP header timestamp | [CFDocs](https://cfdocs.org/gethttptimestring) |
| `lsDateTimeFormat()` | Formats datetime with locale-specific formatting | [CFDocs](https://cfdocs.org/lsdatetimeformat) |
| `lsIsDate()` | Validates if string is a valid locale-specific date | [CFDocs](https://cfdocs.org/lsisdate) |
| `lsParseDateTime()` | Parses a locale-specific date string | [CFDocs](https://cfdocs.org/lsparsedatetime) |
| `parseDateTime()` | Parses a date string with CFML-compatible logic | [CFDocs](https://cfdocs.org/parsedatetime) |
| `toLegacyDate()` | Converts modern date object to legacy CFML date format | [CFDocs](https://cfdocs.org/tolegacydate) |

### Data Conversion Functions

| Function | Description | CFDocs Reference |
|----------|-------------|------------------|
| `jsonDeserialize()` | Deserializes JSON with CFML-compatible behavior | [CFDocs](https://cfdocs.org/jsondeserialize) |

### Encryption & Hashing Functions

| Function | Description | CFDocs Reference |
|----------|-------------|------------------|
| `hash()` | Generates a hash with CFML-compatible algorithms | [CFDocs](https://cfdocs.org/hash) |
| `hmac()` | Generates HMAC with CFML-compatible algorithms | [CFDocs](https://cfdocs.org/hmac) |

### Formatting Functions

| Function | Description | CFDocs Reference |
|----------|-------------|------------------|
| `dollarFormat()` | Formats a number as currency with CFML behavior | [CFDocs](https://cfdocs.org/dollarformat) |
| `htmlCodeFormat()` | HTML-encodes text with CFML-compatible escaping | [CFDocs](https://cfdocs.org/htmlcodeformat) |

### File I/O Functions

| Function | Description | CFDocs Reference |
|----------|-------------|------------------|
| `fileMove()` | Moves a file with CFML-compatible behavior | [CFDocs](https://cfdocs.org/filemove) |

### Math Functions

| Function | Description | CFDocs Reference |
|----------|-------------|------------------|
| `fix()` | Returns integer part of a number (CFML version) | [CFDocs](https://cfdocs.org/fix) |

### Struct Functions

| Function | Description | CFDocs Reference |
|----------|-------------|------------------|
| `structGet()` | Creates nested struct path if it doesn't exist | [CFDocs](https://cfdocs.org/structget) |
| `structKeyTranslate()` | Translates struct keys (Adobe-specific) | [CFDocs](https://cfdocs.org/structkeytranslate) |

### System Functions

| Function | Description | CFDocs Reference |
|----------|-------------|------------------|
| `objectLoad()` | Loads a persisted object from disk | [CFDocs](https://cfdocs.org/objectload) |
| `objectSave()` | Persists an object to disk | [CFDocs](https://cfdocs.org/objectsave) |
| `systemOutput()` | Outputs text to console/stdout | [CFDocs](https://cfdocs.org/systemoutput) |
| `throw()` | Throws an exception with CFML-compatible signature | [CFDocs](https://cfdocs.org/throw) |

---

## 🧩 Contributed Components

The module provides CFML-compatible component implementations:

| Component | Description |
|-----------|-------------|
| `bx:HTTP` | Legacy HTTP component matching Adobe/Lucee `cfhttp` tag behavior |
| `bx:ObjectCache` | Client-side object caching component |

---

## 🪝 Custom Interception Points

The module registers custom interception points for extension:

| Interception Point | Description | Fired When |
|-------------------|-------------|------------|
| `onClientCreated` | Fired when a new client session is created | Client variable management creates a new client |
| `onClientDestroyed` | Fired when a client session is destroyed | Client session times out or is explicitly cleared |
| `onLegacyDateFormatRequest` | Fired when legacy date format is requested | Date formatting functions use CFML mask patterns |

---

## 🗂️ CFIDE Mappings

The module automatically registers the `/CFIDE` mapping pointing to `{moduleRoot}/CFIDE`, providing compatibility interfaces for:

* **ORM** - `CFIDE/orm/IEventHandler.cfc`, `CFIDE/orm/INamingStrategy.cfc`
* **Scheduler** - `CFIDE/scheduler/ITaskEventHandler.cfc`

These interfaces allow CFML applications that extend Adobe/Lucee framework interfaces to run without modification.

---

## 🔄 Client Scope Management

When `clientManagement = true`, the module provides full CFML-compatible client variable storage:

### Client Cache Configuration

The module automatically creates a `bxClients` cache with the following default settings:

```js
{
	evictCount: 1,
	evictionPolicy: "LRU",
	freeMemoryPercentageThreshold: 0,
	maxObjects: 100000,
	defaultLastAccessTimeout: 3600,
	defaultTimeout: 3600,
	objectStore: "ConcurrentStore",
	reapFrequency: 120,
	resetTimeoutOnAccess: true,
	useLastAccessTimeouts: false
}
```

### Client Storage Options

* **`cache`** (default) - Uses the `bxClients` cache for storage
* **`cookie`** - Falls back to cache storage (cookie storage deprecated)
* **`registry`** - Falls back to cache storage (registry storage deprecated)
* **Custom cache name** - Specify your own cache name (must exist)

### Client Context

When client management is enabled, the module provides a `ClientBoxContext` and `ClientScope` that mimics Adobe/Lucee client variable behavior, including automatic persistence and retrieval.

---

## 🚀 Migration Strategy

### Zero-Code Migration Path

1. **Install the module**: `install-bx-module bx-compat-cfml`
2. **Configure engine**: Set `engine = "adobe"` or `engine = "lucee"` in `boxlang.json`
3. **Enable features**: Configure client management, null handling, and other compatibility flags
4. **Test thoroughly**: Run your application test suite to verify compatibility
5. **Optimize gradually**: Once stable, progressively disable compatibility flags to adopt BoxLang's modern features

Please note that this is not guaranteed.  Every codebase is different.

### Recommended Initial Settings (Maximum Compatibility)

```json
{
	"modules": {
		"compat-cfml": {
			"settings": {
				"engine": "lucee",
				"clientManagement": true,
				"nullIsUndefined": true,
				"booleansAreNumbers": true,
				"castClassesToStrings": true,
				"castThrowablesToStrings": true,
				"lenientDateComparison": true,
				"nullEqualsEmptyString": true,
				"jsonEscapeControlCharacters": true,
				"queryNullToEmpty": true,
				"extraLooseStructCasting": true,
				"lenientJSONParsing": true
			}
		}
	}
}
```

### Progressive Modernization

Once your application runs successfully, you can progressively adopt BoxLang's modern features by disabling compatibility flags:

1. **Null Support**: Set `nullIsUndefined = false` for proper null handling
2. **Type Safety**: Set `booleansAreNumbers = false` for type-safe boolean operations
3. **JSON Standards**: Set `lenientJSONParsing = false` for strict JSON parsing
4. **Query Nulls**: Set `queryNullToEmpty = false` for proper null support in queries

---

## 📖 Resources

### Documentation & Support

* **BoxLang Docs**: [https://boxlang.ortusbooks.com](https://boxlang.ortusbooks.com)
* **CFDocs Reference**: [https://cfdocs.org](https://cfdocs.org)
* **GitHub Repository**: [https://github.com/ortus-boxlang/bx-compat-cfml](https://github.com/ortus-boxlang/bx-compat-cfml)
* **Report Issues**: [BoxLang JIRA](https://ortussolutions.atlassian.net/browse/BL) | [Module Issues](https://github.com/ortus-boxlang/bx-compat-cfml/issues)
* **Community**: [BoxLang Slack](https://boxlang.ortusbooks.com/support/slack) | [BoxLang Forums](https://community.ortussolutions.com)

---

## 📝 Version History & Changelog

Visit the [GitHub repository releases](https://github.com/ortus-boxlang/bx-compat-cfml/releases) for detailed version history and changelog.
