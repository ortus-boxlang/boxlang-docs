---
description: >-
  This module provides the CLI runtime with all the web server BIFS, components
  and utilities need for mocking, testing and feature auditing.
icon: globe-pointer
---

# Web Support

This module provides web support for the BoxLang core OS runtime without needing a web server.&#x20;

This means that it will add all the necessary web support to the BoxLang runtime so you can test, simulate, and mock web requests and responses from the CLI. This is a great way to test your web applications without the need for a web server.

```
# For Operating Systems using our Quick Installer.
install-bx-module bx-web-support

# Using CommandBox to install for web servers.
box install bx-web-support
```

{% hint style="danger" %}
THIS MODULE IS NOT NEEDED FOR COMMANDBOX OR THE MINISERVER. IT'S PURELY FOR TESTING, MOCKING AND AUDITING.
{% endhint %}

### Settings

Here are the default settings for this module you can configure:

```json
settings = {
    // The default port for the mock web server
    port = 8080,
    // The default host for the mock web server
    host = "localhost",
    // The default web root for the mock web server
    webRoot = server.java.executionPath,
    // If you want your mock web server to be always secure (SSL)
    secure = false,
    // The key used in the `server` scope we use to track the mock server
    requestKey = "bxMockServer"
};
```

### Functions

Here are some functions collaborated for mocking/testing

#### `getMockServer()`

Creates a new mock server and stores it in the request context.  If it exists already, it will return the existing one.

```java
/**
 * Creates a new mock server and store it in the request context
 * If it exists already, it will return the existing one
 *
 * @webroot string The webroot to use for the mock server, defaults to the module setting
 * @host string The host to use for the mock server, defaults to the module setting
 * @port numeric The port to use for the mock server, defaults to the module setting
 * @secure boolean Whether the mock server should be secure, defaults to the module setting
 * @force boolean Whether to force the creation of a new mock server
 *
 * @return MockHTTPExchange
 */
function invoke(
    string webroot,
    string host,
    numeric port,
    boolean secure,
    boolean force = false
){
```

#### `startMockRequest()`

Handle the start of a mock request using passed arguments.

```java
/**
 * Handle the start of a mock request
 */
function invoke(
	// Request Settings
	string path = "/",
	string method = "GET",
	string pathInfo = "",
	string queryString = "",
	string contentType = "text/html",
	string body = "",
	struct urlScope = {},
	struct formScope = {},
	struct cookieScope = {},
	struct headers = {},
	// Response Mock Settings
	numeric responseStatus = 200,
	string responseContentType = "text/html",
	string responseBody = "",
	struct responseHeaders = {},
	// Web Server Settings
	string webroot,
	string host,
	numeric port,
	boolean secure,
	boolean force = false
){
```

### GitHub Repository and Reporting Issues <a href="#github-repository-and-reporting-issues" id="github-repository-and-reporting-issues"></a>

Visit the [GitHub repository](https://github.com/ortus-boxlang/bx-web-support) for release notes. You can also file a bug report or improvement suggestion via [Jira](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=13359\&components=27030\&issuetype=1).
