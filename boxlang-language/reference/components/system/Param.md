
# Component: `Param`

Tests for a parameter's existence, tests its data type, and, if a default value is not assigned, optionally provides one.

## Component Signature

```
<bx:Param name=[string]
type=[string]
default=[any]
max=[numeric]
min=[numeric]
pattern=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The name of the parameter |  |
| `type` | `string` | `false` | The data type of the parameter |  |
| `default` | `any` | `false` | The default value of the parameter |  |
| `max` | `numeric` | `false` | The maximum value of the parameter |  |
| `min` | `numeric` | `false` | The minimum value of the parameter |  |
| `pattern` | `string` | `false` | The pattern of the parameter |  |

## Examples

### bx:param in BL

A very basic BL bx:param example


```java
<bx:param name="userID" default="0"/>
```


### bx:param in script

A very basic script bx:param example

<a href="https://try.boxlang.io/?code=eJxLqrAqSCxKzFXIS8xNtVUqLU4t8nRRUkhJTUsszSmxNbDmSiKoAgArtxbV" target="_blank">Run Example</a>

```java
bx:param name="userID" default=0;
bx:param name="userID" default=0;

```


### Tag syntax using a regex

Throws an error if the value is not one of a list of possible values


```java
<bx:param name="sortdir" default="ASC" type="regex" pattern="ASC|DESC"/>
```


