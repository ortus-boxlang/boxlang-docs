---
description: This module provides WDDX standards support
icon: money-bill-transfer
---

# WDDX

The WDDX module provides the bridge between the WDDX exchange format and BoxLang. It involves reading and parsing XML, converting data types, handling errors, and ensuring performance and compatibility. The module enables the integration of legacy systems with new applications.

It provides the `wddx` component along with its actions of `bx2wddx`, `wddx2bx`, `bx2js` and `wddx2js`. Note that if the compatibility module is installed in the BoxLang runtime, the usage of `bx` in the action changes to `cfml`.

```
# For Operating Systems using our Quick Installer.
install-bx-module bx-wddx

# Using CommandBox to install for web servers.
box install bx-wddx
```

{% hint style="danger" %}
_Important Note: WDDX is, effectively, no longer supported for new development, and its continued use as a data interchange format is highly discouraged. This module should only be used to maintain compatibility with legacy code, and developers should be encouraged to sunset its usage._
{% endhint %}

| From | To         |
| ---- | ---------- |
| CFML | WDDX       |
| CFML | JavaScript |
| WDDX | CFML       |
| WDDX | JavaScript |



## Contributed Functions

This module will contribute the following components globally:

* wddx ( e.g. `<cfwddx.../>` and `<bx:wddx.../>` depending on the template type and `wddx...;` in script )

```java
bx:wddx 
    action="cfml2wddx" 
    input="#MyQueryObject#" 
    output="WddxTextVariable"
```

## Attributes

### **action:string (required)**

The action to execute

* `cfml2wddx`
* `wddx2cfml`
* `cfml2js`
* `wddx2js`

### `input:string (required)`

`The value to process`

### `output:variableName`

The name of the variable of the output&#x20;

### topLevelVariable:string

Name of top-level JavaScript object created by deserialization. The object is an instance of the WddxRecordset object.

### **useTimezoneInfo:boolean=true**

Whether to output time-zone information when serializing CFML to WDDX.

### validate:boolean=false

Applies if action = "wddx2cfml" or "wddx2js".

* Yes: validates WDDX input with an XML parser using WDDX DTD. If parser processes input without error, packet is deserialized. Otherwise, an error is thrown.
* No: no input validation
