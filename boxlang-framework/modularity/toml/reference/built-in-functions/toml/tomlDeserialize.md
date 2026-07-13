---
description: Parse TOML text into a BoxLang struct
icon: bracket-curly
---

# Function: `tomlDeserialize`

Parses a TOML string into a BoxLang struct.

## Method Signature

```text
tomlDeserialize( toml [, options] )
```

## Arguments

| Argument | Type | Required | Description | Default |
| --- | --- | --- | --- | --- |
| `toml` | `string` | `true` | The TOML string to parse. |  |
| `options` | `struct` | `false` | Per-call settings that override the module configuration. Deserialization options are `specVersion` and `ordered`. | `{}` |

## Returns

A BoxLang struct containing the parsed TOML data. Tables are case-sensitive. By default, key declaration order is preserved.

## Examples

### Parse TOML text

```js
toml = '
    title = "bx-toml"

    [owner]
    name = "Ortus Solutions"
'

data = tomlDeserialize( toml )

writeOutput( data.title )
writeOutput( data.owner.name )
```

### Override parser options

```js
data = tomlDeserialize( toml, {
    specVersion: "1.0",
    ordered: false
} )
```

## Related

* [tomlDeserializeFile](./tomlDeserializeFile.md)
* [tomlSerialize](./tomlSerialize.md)
* [TOML Module](../../../README.md)
