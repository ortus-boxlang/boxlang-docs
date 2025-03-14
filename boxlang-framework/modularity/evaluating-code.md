---
description: This module incorporates a unsafe evaluation of code BIF.
icon: circle-play
---

# Evaluating Code

This module implements the `evaluate()` function for usage in your applications. Please note that this UNSAFE function can be a security risk if not used properly. Please use it with caution.  It's powerful but can be nasty if misused.

```
# For Operating Systems using our Quick Installer.
install-bx-module bx-unsafe-evaluate

# Using CommandBox to install for web servers.
box install bx-unsafe-evaluate
```

{% hint style="danger" %}
DISCOURAGED

We have provided this function for those who need to evaluate dynamic code in their applications OR fore legacy apps still using it. This function is not for general usage and should be used with caution.
{% endhint %}

* `evaluate( expression )`: Evalutes the expression dynamically from left to right and returns the reuslt of the rightmost expression.

```java
name = "boxlang"
lastName = "majano"
op = "eq"

println( evaluate( "#first# #op# #second#" ) )
```
