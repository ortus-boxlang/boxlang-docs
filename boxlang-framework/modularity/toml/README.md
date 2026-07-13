---
description: Parse and serialize TOML configuration data in BoxLang
icon: file-code
---

# TOML

The BoxLang TOML module provides TOML 1.0.0 parsing and serialization through four built-in functions. It is powered by [tomlj](https://github.com/tomlj/tomlj) for parsing and uses a native BoxLang module serializer for writing TOML.

TOML (Tom's Obvious Minimal Language) is a human-friendly configuration format. It uses `key = value` assignments, square-bracket sections for tables, and double square brackets for arrays of tables. TOML supports strings, integers, floats, booleans, arrays, nested tables, and date/time values.

## Installation

```bash
install-bx-module bx-toml
```

For CommandBox-based applications:

```bash
box install bx-toml
```

## Usage

### Deserialize TOML

Use `tomlDeserialize()` for TOML text and `tomlDeserializeFile()` for a TOML file:

```js
toml = '
    title = "bx-toml"

    [owner]
    name = "Ortus Solutions"
'

data = tomlDeserialize( toml )

writeOutput( data.title )
writeOutput( data.owner.name )

config = tomlDeserializeFile( "config/app.toml" )
```

Tables become BoxLang structs, arrays become BoxLang arrays, and TOML date/time values become BoxLang `DateTime` values.

### Serialize BoxLang data

Use `tomlSerialize()` to return TOML text, or provide a filepath to write the result directly. `tomlSerializeFile()` always writes to a filepath:

```js
config = {
    name: "bx-toml",
    enabled: true,
    database: {
        host: "localhost",
        port: 5432
    }
}

toml = tomlSerialize( config, options={ sortKeys: true } )
tomlSerialize( config, "config/generated.toml" )
tomlSerializeFile( config, "config/generated-explicit.toml", "UTF-8" )
```

The file-writing forms return `null` after a successful write. TOML documents must have a struct at the root.

## Module Settings

Module-wide defaults can be configured in `boxlang.json`:

```json
{
    "modules": {
        "bxtoml": {
            "settings": {
                "specVersion": "1.0",
                "ordered": true,
                "sortKeys": false,
                "indent": 2,
                "dateTimeStyle": "auto"
            }
        }
    }
}
```

| Setting | Default | Description |
| --- | --- | --- |
| `specVersion` | `"1.0"` | TOML parser mode. `"1.1"` is accepted as best-effort development-spec mode, but currently behaves like TOML 1.0 with `tomlj` 1.1.1. |
| `ordered` | `true` | Preserve TOML key declaration order in linked, case-sensitive structs. |
| `sortKeys` | `false` | Alphabetize keys during serialization instead of preserving struct iteration order. |
| `indent` | `2` | Number of spaces used for nested serialized output. |
| `dateTimeStyle` | `"auto"` | Date/time output style: `auto`, `offset-datetime`, `local-datetime`, `local-date`, or `local-time`. |

Per-call `options` override module settings. Deserialization uses `specVersion` and `ordered`; serialization uses `specVersion`, `sortKeys`, `indent`, and `dateTimeStyle`.

## Behavior and Limitations

- TOML keys remain case-sensitive regardless of the `ordered` setting.
- LF and CRLF input are accepted. Parsed document line endings are normalized to LF, and serialized TOML uses LF line endings.
- Comments and original formatting are not preserved during a parse/serialize cycle.
- TOML's four date/time kinds become one BoxLang `DateTime` type, so some date/time round trips are lossy. Use `dateTimeStyle` when deterministic output is required.
- TOML 1.1 syntax is not implemented yet; `specVersion: "1.1"` currently behaves like `"1.0"`.
- `tomlj` 1.1.1 accepts a known invalid one-digit UTC offset minute form such as `+09:9`.

## Reference

* [Built-in Functions](reference/built-in-functions/README.md)

## Repository and Issues

Visit the [bx-toml GitHub repository](https://github.com/ortus-boxlang/bx-toml) for source code, releases, and issue reporting.
