---
description: This module incorporates a unsafe evaluation of code BIF.
icon: circle-play
---

# Evaluating Code

This module implements the `evaluate()` and `precisionEvaluate()` functions for usage in your applications. Please note that these UNSAFE functions can be a security risk if not used properly. Please use them with caution.  They're powerful but can be nasty if misused.

```
# For Operating Systems using our Quick Installer.
install-bx-module bx-unsafe-evaluate

# Using CommandBox to install for web servers.
box install bx-unsafe-evaluate
```

{% hint style="danger" %}
DISCOURAGED

We have provided these functions for those who need to evaluate dynamic code in their applications OR for legacy apps still using it. These functions are not for general usage and should be used with caution.
{% endhint %}

* `evaluate( expression )`: Evaluates the expression dynamically from left to right and returns the result of the rightmost expression.

```java
name = "boxlang"
lastName = "majano"
op = "eq"

println( evaluate( "#first# #op# #second#" ) )
```

* `precisionEvaluate( expression )`: Evaluates the expression dynamically from left to right using BigDecimal precision arithmetic and returns the result of the rightmost expression.

```java
num1 = 5;
num2 = 3 / 8;
println( "The resultant expression is: " & precisionEvaluate( num1 / num2 ) );
```

### GitHub Repository and Reporting Issues <a href="#github-repository-and-reporting-issues" id="github-repository-and-reporting-issues"></a>

Visit the [GitHub repository](https://github.com/ortus-boxlang/bx-unsafe-evaluate) for release notes. You can also file a bug report or improvement suggestion via [Jira](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=13359\&components=27028\&issuetype=1).
