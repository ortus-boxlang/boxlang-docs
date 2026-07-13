---
description: Serialize a BoxLang struct as TOML text or a file
icon: file-export
---

# Function: `tomlSerialize`

Converts a BoxLang struct into TOML text. If `filepath` is provided, the TOML is written to that file instead and the function returns `null`.

## Method Signature

```text
tomlSerialize( content [, filepath] [, charset] [, options] )
```

## Arguments

| Argument | Type | Required | Description | Default |
| --- | --- | --- | --- | --- |
| `content` | `any` | `true` | The struct to convert to TOML. TOML documents must have a struct at the root. |  |
| `filepath` | `string` | `false` | The path to write the TOML file. If omitted, the TOML text is returned. |  |
| `charset` | `string` | `false` | The charset used when writing a file. | The system default charset |
| `options` | `struct` | `false` | Per-call settings that override the module configuration. Serialization options are `specVersion`, `sortKeys`, `indent`, and `dateTimeStyle`. | `{}` |

## Returns

The serialized TOML string when no filepath is supplied. Returns `null` when the content is written to a file.

## Examples

### Serialize a struct to text

```js
config = {
    name: "bx-toml",
    enabled: true,
    database: {
        host: "localhost",
        port: 5432
    }
}

toml = tomlSerialize( config )
writeOutput( toml )
```

### Apply serialization options

```js
toml = tomlSerialize( config, options={
    sortKeys: true,
    indent: 4
} )
```

### Write directly to a file

```js
tomlSerialize( config, "config/generated.toml" )
tomlSerialize( config, "config/generated-utf8.toml", "UTF-8" )
```

## Related

* [tomlDeserialize](./tomlDeserialize.md)
* [tomlSerializeFile](./tomlSerializeFile.md)
* [TOML Module](../../../README.md)
