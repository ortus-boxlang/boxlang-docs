---
description: A module that allows you to execute Python code in BoxLang
icon: python
---

# Jython

This module allows you to execute python in BoxLang via Jython. This is a very powerful feature that allows you to execute python code in your BoxLang scripts. It also allows you to create python modules and classes that can be used in your BoxLang scripts by using the `jythonEvalFile( path )` function.

```
# For Operating Systems using our Quick Installer.
install-bx-module bx-jython

# Using CommandBox to install for web servers.
box install bx-jython
```

### Usage

You can execute python code in your BoxLang scripts by using the `jythonEval( code )` function. Here is an example:

```js
jythonEval( "print('Hello World')" );
```

You can also evaluate python code from a file by using the `jythonEvalFile( path )` function. Here is an example:

```js
jythonEvalFile( "path/to/file.py" );
```

You can also create python modules and classes that can be used in your BoxLang scripts. Here is an example:

```python
# mymodule.py
def hello():
	return "Hello World"
```

```js
jythonEvalFile( "path/to/mymodule.py" );
var result = jythonEval( "hello()" );
print( result );
```

You can also use the `<bx:jython>{python code}</bx:jython>` tag to execute python code in your BoxLang scripts. Here is an example:

```js
<bx:jython variable="result">
print("Hello, World!")

# Addition
num1 = 5
num2 = 10
sum = num1 + num2
print("Sum:", sum)

# Subtraction
num3 = 8
num4 = 3
difference = num3 - num4
print("Difference:", difference)

# Multiplication
num5 = 4
num6 = 6
product = num5 * num6
print("Product:", product)

# Division
num7 = 15
num8 = 3
quotient = num7 / num8
print("Quotient:", quotient)

# Modulo
num9 = 17
num10 = 5
remainder = num9 % num10
print("Remainder:", remainder)

# Exponentiation
base = 2
exponent = 3
result = base ** exponent
print("Result:", result)
</bx:jython>
```

### Bindings

We will automatically bind all the variables in your `variables` scope into the engine bindings via JSR223. You can then use them as native variables in your python code.

```js
variables.name = "Luis Majano";
jythonEval( "print(name)" );
```

### Result

Each execution produces a result which is a structure with the following keys:

* `engine` : A reference to the engine
* `globalScope` : A reference to the global scope of JSR223
* `engineScope` : A reference to the engine scope of JSR223

### GitHub Repository and Reporting Issues <a href="#github-repository-and-reporting-issues" id="github-repository-and-reporting-issues"></a>

Visit the [GitHub repository](https://github.com/ortus-boxlang/bx-jython) for release notes. You can also file a bug report or improvement suggestion via [Jira](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=13359\&components=27023\&issuetype=1).
