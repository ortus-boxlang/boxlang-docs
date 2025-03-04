---
icon: timeline-arrow
description: Configure the logging framework in BoxLang
---

# Logging

This section configures the logging framework in BoxLang.  Please note that BoxLang leverages `RollingFileAppenders` for most of its loggers.  This provides consistency for the language and a consistent destination.  You can customize it as you see fit, but this provides uniformity to the core and modules.

The `logging`section is divided into global log settings and a `loggers`section where you can configure named loggers in the runtime.

{% hint style="success" %}
Please also note that in BoxLang, you can log data as **text** or as **JSON**.
{% endhint %}

{% code title="boxlang.json" %}
```json
// Logging Settings for the runtime
"logging": {
	// The location of the log files the runtime will produce
	"logsDirectory": "${boxlang-home}/logs",
	// The maximum number of days to keep log files before rotation
	// Default is 90 days or 3 months
	// Set to 0 to never rotate
	"maxLogDays": 90,
	// The maximum file size for a single log file before rotation
	// You can use the following suffixes: KB, MB, GB
	// Default is 100MB
	"maxFileSize": "100MB",
	// The total cap size of all log files before rotation
	// You can use the following suffixes: KB, MB, GB
	// Default is 5GB
	"totalCapSize": "5GB",
	// The root logger level
	// Valid values are in order of severity: ERROR, WARN, INFO, DEBUG, TRACE, OFF
	// If the runtime is in Debug mode, this will be set to DEBUG
	"rootLevel": "WARN",
	// Default Encoder for file appenders.
	// The available options are "text" and "json"
	"defaultEncoder": "text",
	// A collection of pre-defined loggers and their configurations
	"loggers": {
		// The runtime main and default log
		"runtime": {
			// Valid values are in order of severity: ERROR, WARN, INFO, DEBUG, TRACE, OFF
			// Leave out if it should inherit from the root logger
			//"level": "WARN",
			// Valid values are: "file", "console",
			// Coming soon: "smtp", "socket", "db", "syslog" or "java class name"
			// Please note that we only use Rolling File Appenders
			"appender": "file",
			// Use the defaults from the runtime
			"appenderArguments": {},
			// The available options are "text" and "json"
			"encoder": "text",
			// Additive logging: true means that this logger will inherit the appenders from the root logger
			// If false, it will only use the appenders defined in this logger
			"additive": true
		},
		// The modules log
		"modules": {
			// Valid values are in order of severity: ERROR, WARN, INFO, DEBUG, TRACE, OFF
			// Leave out if it should inherit from the root logger
			//"level": "WARN",
			// Valid values are: "file", "console",
			// Coming soon: "smtp", "socket", "db", "syslog" or "java class name"
			// Please note that we only use Rolling File Appenders
			"appender": "file",
			// Use the defaults from the runtime
			"appenderArguments": {},
			// The available options are "text" and "json"
			"encoder": "text",
			// Additive logging: true means that this logger will inherit the appenders from the root logger
			// If false, it will only use the appenders defined in this logger
			"additive": true
		},
		// All applications will use this logger
		"application": {
			// Valid values are in order of severity: ERROR, WARN, INFO, DEBUG, TRACE, OFF
			// Leave out if it should inherit from the root logger
			"level": "TRACE",
			// Valid values are: "file", "console",
			// Coming soon: "smtp", "socket", "db", "syslog" or "java class name"
			// Please note that we only use Rolling File Appenders
			"appender": "file",
			// Use the defaults from the runtime
			"appenderArguments": {},
			// The available options are "text" and "json"
			"encoder": "text",
			// Additive logging: true means that this logger will inherit the appenders from the root logger
			// If false, it will only use the appenders defined in this logger
			"additive": true
		},
		// All scheduled tasks logging
		"scheduler": {
			// Valid values are in order of severity: ERROR, WARN, INFO, DEBUG, TRACE, OFF
			// Leave out if it should inherit from the root logger
			"level": "INFO",
			// Valid values are: "file", "console",
			// Coming soon: "smtp", "socket", "db", "syslog" or "java class name"
			// Please note that we only use Rolling File Appenders
			"appender": "file",
			// Use the defaults from the runtime
			"appenderArguments": {},
			// The available options are "text" and "json"
			"encoder": "text",
			// Additive logging: true means that this logger will inherit the appenders from the root logger
			// If false, it will only use the appenders defined in this logger
			"additive": true
		}
	}
},
```
{% endcode %}

## Global Properties

#### Logs Directory

This is the folder where BoxLang will store it's log files.  By default we use the following:

```json
// The location of the log files the runtime will produce
"logsDirectory": "${boxlang-home}/logs",
```

#### Max Log Days

The maximum number of days to keep log files before rotations.  The default is 90 days or 3 months.  If you put a `0` then rotation will never happen and you will log forever!

```json
"maxLogDays": 90,
```

#### Max File Size

The maximum filesize for a **single** log file before rotation occurs.  The default is 100 Megabytes.  You can use a number or the following suffixes: KB, MB, GB.

```json
"maxFileSize": "100MB",
```

#### Total Cap Size

The total cap size of ALL log files before rotation and compression begins.  The default is 5 Gigabytes.  You can use a number or the following suffixes: KB, MB, GB.

```json
"totalCapSize": "5GB",
```

#### Root Level

This is the level at which the root logger will be allowed to be logged.  By default, it is `WARN`, However, if it detects you are in debug mode, it will bump it to `DEBUG`.

```json
"rootLevel": "WARN",
```

#### Default Encoder

By default, BoxLang is configured to log using a pattern textual encoder.  However, if you want to leverage the new JSON Lines format, you can switch the encoder for ALL loggers to be `JSON`.  Valid values are `text` or `json`

```json
"defaultEncoder" : "text"
```

## Loggers

BoxLang allows you to pre-define named loggers that will be configured when used via BoxLang calls to:

* `writeLog()` BIF
* `log` component

However, you can also retrieve named loggers via the `LoggingService.` By default, we will register the following named loggers:

* `application` - Application-specific logs
* `modules` - For all modular information, activation, etc
* `runtime` - The default log file for all runtime-related logging
* `scheduler` - All tasks and schedulers can log here

### Logger Properties

Every logger has the following configuration properties:

```json
"runtime": {
    // Valid values are in order of severity: ERROR, WARN, INFO, DEBUG, TRACE, OFF
    // Leave out if it should inherit from the root logger
    //"level": "WARN",
    // Valid values are: "file", "console",
    // Coming soon: "smtp", "socket", "db", "syslog" or "java class name"
    // Please note that we only use Rolling File Appenders
    "appender": "file",
    // Use the defaults from the runtime
    "appenderArguments": {},
    // The available options are "text" and "json"
    "encoder": "text",
    // Additive logging: true means that this logger will inherit the appenders from the root logger
    // If false, it will only use the appenders defined in this logger
    "additive": true
},
```

Each logger will have the following configuration items:

<table><thead><tr><th width="205">Property</th><th width="129">Default</th><th width="121">Type</th><th>Description</th></tr></thead><tbody><tr><td><strong>additive</strong></td><td><code>true</code></td><td><code>boolean</code></td><td><strong>true</strong> means that this logger will inherit the appenders from the root logger and log through all of them.  <code>false</code> means it doesn't buble up log messages.</td></tr><tr><td><strong>appender</strong></td><td><code>file</code></td><td><code>string</code></td><td>The type of appender to use for this logger. By default we use the rolling file appender.  <br><br>Valid values are:<br>- file<br>- console<br><br>Coming soon values:<br>- smtp<br>- socket<br>- db<br>- syslog<br>- class name</td></tr><tr><td><strong>appenderArguments</strong></td><td>---</td><td><code>object</code></td><td>Name-value pairs that configure the appender.  Each appender can have different arguments.</td></tr><tr><td><strong>encoder</strong></td><td><code>logging > defaultEncoder</code></td><td><code>text</code> or <code>json</code></td><td>The encoder to use for logging. By default it levereages what was defined in the <code>logging.defaultEncoder</code> configuration.</td></tr><tr><td><strong>level</strong></td><td><code>TRACE</code></td><td><code>logLevel</code></td><td>The log level is to be assigned to the appender.  By default, each appender is wide open to the maximum level of <code>TRACE</code></td></tr></tbody></table>

