---
description: >-
  A comprehensive CFML RESTful services compatibility module for BoxLang that
  provides compatibility for the CFML REST implementations
icon: file-brackets-curly
---

# REST Compat +

## BoxLang REST Compatibility Module

A comprehensive CFML RESTful services compatibility module for BoxLang that provides compatibility for the CFML REST specification including routing and serialization

### Overview

This module provides CFML-compatible REST services for BoxLang web applications, supporting:

* **RESTful Service Discovery & Registration**: Automatic discovery and registration of REST-enabled CFCs
* **Intelligent Routing**: Path-based routing with support for path parameters, query strings, and HTTP method matching
* **Content Negotiation**: Automatic serialization/deserialization based on Accept and Content-Type headers
* **OpenAPI Documentation**: Auto-generated OpenAPI 3.0 documentation for all registered services
* **CF-Compatible BIFs**: `restInitApplication`, `restSetResponse`, `restDeleteApplication`
* **Multiple HTTP Methods**: GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS
* **Rich Annotations Support**: All standard CF REST annotations including `httpMethod`, `produces`, `consumes`, `restPath`, `restArgSource`

### Installation

#### Add a servlet pass predicate which will match your default entry prefix in the `web` section of your `server.json`

```
"web":{
	"servletPassPredicate":"regex( '^/(.+?\\.cf[cms])(/.*)?$' ) or regex( '^/(.+?\\.bx[sm])(/.*)?$' ) or path-prefix-nocase( /rest/ )",
	...
}
```

#### Install the module on your initial server start

`.server.json` scripts block:

```
"scripts" : {
	"onServerInitialInstall" : "install bx-plus,bx-compat-rest",
	...
}
```

#### Seed your server directory with a dryRun start and update the `web.xml` file

```
box server start --dryRun
```

Once the server is seeded, open the `web.xml` file in the server home ( e.g. `{server-home}/WEB-INF/web.xml`) and update the `servlet-mapping` section to add the `url-pattern` node for the REST prefix:

```xml
<servlet-mapping>
	<servlet-name>BoxLangServlet</servlet-name>
	<url-pattern>*.cfc</url-pattern>
	<url-pattern>*.cfm</url-pattern>
	<url-pattern>*.cfs</url-pattern>
	<url-pattern>*.cfml</url-pattern>
	<url-pattern>*.bx</url-pattern>
	<url-pattern>*.bxm</url-pattern>
	<url-pattern>*.bxs</url-pattern>
	<url-pattern>rest/*</url-pattern>
</servlet-mapping>
```

#### Start your server and go

### Configuration

The following configuration items are supported and can be configured in the `modules` block of your `boxlang.json` or `.cfconfig.json` file:

```json
"bx-compat-rest":{
	"settings":{
		// The entry prefix to use for all rest applications
		"entryPrefix" : "/rest/",
		// A struct containing the service name and fully expanded route to the directory containing the REST classes
		"applications":{
			// Key-value pairs
			"api":"/home/resty/my/rest/api/classes",
			// Key with struct to specify default application
			"resty" : {
				"path" : "/home/resty/my/rest/defaultAPI",
				"default" : true
			}
		}
	}
}
```

### Quick Start

#### 1. Create a REST-Enabled Component

```java
// HelloService.bx
component rest="true" restPath="hello" {
    
    remote string function sayHello() httpMethod="GET" produces="application/json" {
        return "Hello, World!";
    }
    
    remote string function sayHelloTo(
        required string name restArgSource="Path"
    ) httpMethod="GET" restPath="{name}" produces="application/json" {
        return "Hello, #arguments.name#!";
    }
}
```

#### 2. Register Your REST Application

In your `Application.cfc`:

```java
component {
    this.name = "MyRESTApp";
    
    // Register REST application on startup
    function onApplicationStart() {
        restInitApplication(
            expandPath("./services"),  // Directory containing REST CFCs
            "api"                       // Service mapping name
        );
    }
}
```

#### 3. Access Your REST Endpoints

```
GET  /rest/api/hello
GET  /rest/api/hello/John
```

### Built-in Functions (BIFs)

#### restInitApplication()

Registers a REST application directory.

```java
restInitApplication(
    rootPath,      // Required: Directory containing REST CFCs
    serviceName,   // Optional: Service name/mapping
    options        // Optional: Struct with host, useHost, isDefault
)
```

Example:

```java
restInitApplication(expandPath("./api"), "myapi", {
    "host": "api.example.com",
    "isDefault": true
});
```

#### restSetResponse()

Sets a custom HTTP response with status, content, and headers.

```java
restSetResponse({
    "status": 201,
    "content": {"id": 123, "message": "Created"},
    "headers": {"Location": "/api/resource/123"}
});
```

#### restDeleteApplication()

Removes a registered REST application.

```java
restDeleteApplication("myapi");
```

### OpenAPI Documentation

Access auto-generated OpenAPI 3.0 documentation:

```
GET /bxrest/public/RestController.bx?method=docs
```

The documentation includes:

* All registered services and routes
* HTTP methods and paths
* Request parameters and their types
* Response schemas
* Content types (produces/consumes)

### Advanced Features

#### Path Parameters

```java
remote function getUser(
    required numeric id restArgSource="Path"
) httpMethod="GET" restPath="users/{id}" {
    return getUserById(arguments.id);
}
```

Access as: `/api/users/123`

#### Custom HTTP Status Codes

```java
remote function createUser(
    required string name restArgSource="Form"
) httpMethod="POST" {
    var newUser = saveUser(arguments.name);
    
    restSetResponse({
        "status": 201,
        "content": newUser,
        "headers": {"Location": "/api/users/" & newUser.id}
    });
    
    return newUser;
}
```

#### Content Negotiation

The module automatically handles content negotiation based on:

* `Accept` header for responses
* `Content-Type` header for requests

Supported formats:

* `application/json`, `text/json`
* `application/xml`, `text/xml`
* `application/x-www-form-urlencoded`
* `multipart/form-data`
* `text/plain`

#### Error Handling

```java
remote function getUser(required numeric id restArgSource="Path") {
    if (!userExists(id)) {
		restSetResponse( 
			{
				"status" : 404,
				"content" : "User not found"
			}
		);
		return;
    }
    return getUser By(id);
}
```

The module automatically returns appropriate HTTP status codes:

* 200 OK - Successful response with body
* 204 No Content - Successful response without body
* 400 Bad Request - Missing required parameters
* 404 Not Found - No matching route
* 405 Method Not Allowed - HTTP method not supported for route
* 406 Not Acceptable - Cannot produce requested content type
* 415 Unsupported Media Type - Cannot consume request content type
* 500 Internal Server Error - Exception during processing

### Compatibility

This module implements the CFML RESTful services specification as documented in: https://helpx.adobe.com/CFML/developing-applications/changes-in-CFML/restful-web-services-in-CFML.html

Supported features:

* ✅ REST component and function annotations
* ✅ HTTP method binding
* ✅ Path parameters and routing
* ✅ Content negotiation
* ✅ JSON and XML serialization
* ✅ Custom responses
* ✅ Parameter sources (Path, Query, Form, Header, Cookie, Body)
* ✅ restInitApplication, restSetResponse, restDeleteApplication BIFs
* ⚠️ Subresource locators (partial - basic implementation complete)
* ⚠️ Custom serializers (not yet implemented)

***

**Ortus Solutions, Corp** https://www.ortussolutions.com
