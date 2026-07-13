---
description: Read and parse a TOML file into a BoxLang struct
icon: file-import
---

# Function: `tomlDeserializeFile`

Reads a TOML file and parses it into a BoxLang struct.

## Method Signature

```text
tomlDeserializeFile( path [, charset] [, options] )
```

## Arguments

| Argument | Type | Required | Description | Default |
| --- | --- | --- | --- | --- |
| `path` | `string` | `true` | The path to the TOML file to parse. |  |
| `charset` | `string` | `false` | The charset used to read the file. | The system default charset |
| `options` | `struct` | `false` | Per-call settings that override the module configuration. Deserialization options are `specVersion` and `ordered`. | `{}` |

## Returns

A BoxLang struct containing the parsed TOML data.

## Examples

### Read a TOML file

```js
config = tomlDeserializeFile( "config/app.toml" )
writeOutput( config.database.host )
```

### Specify a file charset

```js
config = tomlDeserializeFile( "config/legacy.toml", "ISO-8859-1" )
```

### Override parser options

```js
config = tomlDeserializeFile( "config/app.toml", "UTF-8", {
    ordered: false
} )
```

## Related

* [tomlDeserialize](./tomlDeserialize.md)
* [tomlSerializeFile](./tomlSerializeFile.md)
* [TOML Module](../../../README.md)
