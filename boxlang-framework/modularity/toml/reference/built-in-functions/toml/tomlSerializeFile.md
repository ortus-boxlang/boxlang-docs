---
description: Serialize a BoxLang struct directly to a TOML file
icon: file-export
---

# Function: `tomlSerializeFile`

Converts a BoxLang struct into TOML and writes it to a file. This is the explicit, filepath-required counterpart to `tomlSerialize()`.

## Method Signature

```text
tomlSerializeFile( content, filepath [, charset] [, options] )
```

## Arguments

| Argument | Type | Required | Description | Default |
| --- | --- | --- | --- | --- |
| `content` | `any` | `true` | The struct to convert to TOML. TOML documents must have a struct at the root. |  |
| `filepath` | `string` | `true` | The path to write the TOML file to. |  |
| `charset` | `string` | `false` | The charset used when writing the file. | The system default charset |
| `options` | `struct` | `false` | Per-call settings that override the module configuration. Serialization options are `specVersion`, `sortKeys`, `indent`, and `dateTimeStyle`. | `{}` |

## Returns

`null` after the TOML document has been written successfully.

## Examples

### Write a TOML file

```js
config = {
    name: "bx-toml",
    enabled: true,
    database: {
        host: "localhost",
        port: 5432
    }
}

tomlSerializeFile( config, "config/app.toml" )
```

### Specify a charset and options

```js
tomlSerializeFile(
    config,
    "config/app.toml",
    "UTF-8",
    {
        sortKeys: true,
        dateTimeStyle: "local-datetime"
    }
)
```

## Related

* [tomlSerialize](./tomlSerialize.md)
* [tomlDeserializeFile](./tomlDeserializeFile.md)
* [TOML Module](../../../README.md)
