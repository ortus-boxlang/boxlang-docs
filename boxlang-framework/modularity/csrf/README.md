---
description: Native Cross Request Site Forgery protection for BoxLang
icon: shield-quartered
---

# CSRF

The CSRF module provides the functionality to generate and verify [Cross-Site Request Forgery](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) tokens for Boxlang Web Runtimes.

### Built-In Functions

This module contributes the following native functions to the boxlang runtime:

* `CSRFGenerateToken( [string key='default'], [boolean forceNew=false] )` - this function generates the CSRF token. The optional `key` argument can be provided to create and scope a specific token.
* `CSRFVerifyToken( required string token, [ string key ] )` - this function verifies the token created by the above method. The `key` argument must be passed if the token was generated with the that argument.
* `CSRFRotate()` - this function will rotate all tokens in the cache by removing them. This will force the next request to generate a new token.
* `CSRFHiddenField( [string key='default'], [boolean forceNew=false] )` - Generates a hidden field with a csrf in it as the value. The name of the field is `csrf`

### Configuration

The module may be configured using the following settings in your `boxlang.json` file. The settings noted below are the defaults:

```javascript
"modules": {
	"csrf": {
		"settings": {
			// The cache storage to use for the csrf tokens, by default we use the current session storage cache. You can provide a custom cache to use, as well.
			"cacheStorage" : "session",
			// The duration in minutes to perform a cache reap of expired tokens
			"reapFrequency" : 1,
			// By default, all csrf tokens have a life-span of 30 minutes. After 30 minutes, they expire and we auto-generate new ones.
			"rotationInterval" : 30,
			// The interval in seconds within which, if a token's expiration is impending, we force generate new token for the user.
			"timeoutSkew" : 120,
			// Whether the the presence of the token should be verified automatically for the verifyMethods
			"autoVerify" : false,
			// The name of the header to check for automatic token verification, if applicable
			"headerName" : "x-csrf-token",
			// The methods to verify the token presence, if enabled
			"verifyMethods" : [ "POST", "PUT", "PATCH", "DELETE" ]
		}
	}
}
```

### Token Storage

Tokens may be stored in any named [caches configured](https://boxlang.ortusbooks.com/getting-started/configuration#caches) within the Boxlang runtime. By default, the user `bxSessions` cache is used for storage.

### Token Expiration

By default, the module is configured to rotate all user csrf tokens every 30 minutes. This setting may be changed to another duration of minutes using the `rotationInterval` module setting. If you do NOT want the tokens to EVER expire, then use the value of 0 zero. Note that using in-memory caches will result in token expiration on runtime shutdown. You may adjust the `timeoutSkew` setting in order to ensure tokens expiring in the near future are force rotated if the existing token expiration is within the interval.

### Auto-Verification

The module may be enabled to perform auto-verification of CSRF inbound headers. If enabled, a check will be performed at the beginning of the request for the presence of the configured CSRF `headerName` setting and, if verification fails, an error will be thrown. Note that any tokens created for use in auto-verification must omit the `key` argument, as only the default token may be verified.

### Cache Reaping

A scheduler is enabled with the module, which will perform a check and remove all expired tokens from the cache at a frequency of minutes ( default `1` ). If you wish to adjust this, you can change the `reapFrequency` setting to your desired interval.

### GitHub Repository and Reporting Issues <a href="#github-repository-and-reporting-issues" id="github-repository-and-reporting-issues"></a>

Visit the [GitHub repository](https://github.com/ortus-boxlang/bx-csrf) for release notes. You can also file a bug report or improvement suggestion via [Jira](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=13359\&components=27182\&issuetype=1).
