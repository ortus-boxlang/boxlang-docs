
# Component: `Sleep`

Sleep for a specified number of milliseconds

## Component Signature

```
<bx:Sleep time=[any] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `time` | `any` | `true` | The number of milliseconds to sleep |  |

## Examples

### Pause execution for a specified time

Suspends the current thread for the given number of milliseconds.

```java
<bx:sleep time="1000">

```

### Sleep for 5 seconds

```java
<bx:sleep time="5000">

```

### Sleep with a variable

```java
delay = 2000;
<bx:sleep time="#delay#">

```
