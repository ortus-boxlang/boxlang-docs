---
description: >-
  The lens* built-in functions that let your code talk to BxLens: messages,
  timers, tags, custom panels and the data functions.
icon: code
---

# Built-in functions

These functions work whenever the module is loaded. When BxLens is not collecting for the request, or the caller is not allowed, the first group does nothing. The [data functions](#data-functions) work in every request.

## 📋 Functions

### Talk to the bar

| Function | Signature | Purpose |
| --- | --- | --- |
| `lensMessage` | `( message, label="info" )` | Add a message to the Messages panel. Structs and arrays are serialized. |
| `lensDump` | `( value, label="" )` | Push a value to the Messages panel as a collapsible tree. |
| `lensStart` | `( label )` | Start a timer and return its id. |
| `lensStop` | `( labelOrId )` | End a timer. |
| `lensMeasure` | `( label, callable )` | Time a closure and return its result. |
| `lensAddMeasure` | `( label, startMs, endMs )` | Add a span that you measured yourself. |
| `lensException` | `( exception, [tags] )` | Record a caught exception, with optional tags for the issue. |
| `lensTag` | `( name )` | Tag the request. The tag shows in the console and can be filtered. |
| `lensFramework` | `( name, version="" )` | Say which framework handled the request, when BxLens does not detect it. |
| `lensPanel` | `( id, label, renderer )` | Create a custom panel from application code. |
| `lensEnable`, `lensDisable` | `()` | Switch BxLens on or off for the current request. |
| `lensIsEnabled` | `()` | True when BxLens is active for the request. |
| `lensRender` | `()` | Place the bar yourself, when `inject` is `false`. |
| `lensRequestId` | `()` | The id of this request, the same as the `X-BxLens-Id` header. |

### Data functions

These return the numbers that the console shows, as plain structs and arrays. Use them for a health endpoint, a smoke test or your own page.

| Function | Signature | Returns |
| --- | --- | --- |
| `lensReport` | `()` | Totals, a per-minute series, and the slowest, busiest and most failing URLs |
| `lensErrors` | `( limit=20 )` | The error groups, newest first |
| `lensQueries` | `( limit=20, sort="slowest" )` | Statistics per SQL statement. `sort` is `slowest`, `total`, `count` or `failures`. |
| `lensInflight` | `()` | The requests running now, longest first |
| `lensLicense` | `()` | The license state: `plus`, `trial`, `expired` or `none` |
| `lensDiagnostics` | `()` | How BxLens itself is doing |
| `lensServer` | `()` | The identity of this server |

{% hint style="warning" %}
The data functions describe every request on the server and do not check the access rules. Do not hand their output to untrusted users. `lensReport`, `lensErrors`, `lensQueries` and `lensInflight` return data only with BoxLang+ or a trial.
{% endhint %}

## 💡 Examples

Time a block of code and tag the request:

```js
lensTag( "checkout" )

orders = lensMeasure( "load orders", () => {
  return queryExecute( "SELECT * FROM orders" )
} )
```

Send a caught exception with tags for its issue:

```js
try {
  callPaymentApi()
} catch ( any e ) {
  lensException( e, { plan : user.plan, release : "2.8.1" } )
}
```

Build a small health check from the data functions:

```js
report = lensReport()
writeOutput( "p95: #report.session.p95# ms over #report.session.requests# requests" )

stuck = lensInflight().filter( ( r ) => r.elapsedMs > 5000 )
```

Tie your own log lines to a request:

```js
return { ok : true, requestId : lensRequestId() }
```

## 🔗 Full reference

Each function, with all of its options and result keys, is documented in the [BxLens BIF reference](https://bxlens.boxlang.io/guides/bifs/).
