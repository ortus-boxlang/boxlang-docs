---
description: Compress, extract, and manage ZIP and archive files with BoxLang
icon: file-zip
---

# Compression and Archives

BoxLang provides built-in functions and components for creating, reading, extracting, and managing compressed files. Use `compress()` and `extract()` for straightforward archive workflows, or use `<bx:zip>` when you need to list entries, read content, filter files, or add in-memory content with `<bx:zipParam>`.

## Compress an archive

Pass the source and destination as named arguments when creating an archive:

```js
compress(
    source = "/tmp/project",
    destination = "/tmp/project.tar.gz",
    format = "tar.gz"
)
```

`source` may be a file or directory. When the source is a directory, `compress()` includes its contents recursively by default. Set `includeBaseFolder = false` when the archive should contain the directory contents without the top-level directory name.

```js
compress(
    source = "/tmp/project",
    destination = "/tmp/project.zip",
    format = "zip",
    includeBaseFolder = false,
    compressionLevel = 9
)
```

## Extract an archive

Use `destination` for the output directory:

```js
extract(
    source = "/tmp/project.tbz2",
    destination = "/tmp/project-out",
    format = "tbz2"
)
```

The `destination` argument replaces the older `target` spelling. The transpiler maps `target` to `destination` for compatibility with older source code.

Use `overwrite`, `filter`, and `entryPaths` to control extraction:

```js
extract(
    source = "/tmp/project.tar.gz",
    destination = "/tmp/project-out",
    format = "tar.gz",
    overwrite = true,
    filter = ( path ) => path.endsWith( ".json" )
)
```

{% hint style="info" %}
When an archive is created inside the directory being compressed, BoxLang avoids adding the archive itself to the archive. This supports destinations such as `/tmp/project/project.zip` without recursively including the output file.
{% endhint %}

## Supported archive formats

| Format | `compress()` | `extract()` |
| --- | :---: | :---: |
| `zip` | Yes | Yes |
| `gzip` | Yes | Yes |
| `bzip` | Yes | Yes |
| `bzip2` | Yes | Yes |
| `tar` | Yes | Yes |
| `tar.bz` | Yes | No |
| `tbz` | Yes | Yes |
| `tbz2` | Yes | Yes |
| `tgz` | Yes | Yes |
| `tar.gz` | Yes | Yes |

## ZIP components

The `<bx:zip>` component supports actions for zipping, unzipping, listing, reading, and deleting ZIP entries.

### Zip a file or directory

```xml
<bx:zip
    action="zip"
    file="/tmp/archive.zip"
    source="/tmp/project"
    recurse="true"
    overwrite="true">
</bx:zip>
```

The script form is also available:

```js
bx:zip
    action = "zip"
    file = "/tmp/archive.zip"
    source = "/tmp/project"
    recurse = true
    overwrite = true
```

### Extract a ZIP file

```xml
<bx:zip
    action="unzip"
    file="/tmp/archive.zip"
    destination="/tmp/project-out"
    overwrite="true">
</bx:zip>
```

### List or read entries

```js
bx:zip action = "list" file = "/tmp/archive.zip" result = "entries"

bx:zip
    action = "read"
    file = "/tmp/archive.zip"
    entryPath = "config/settings.json"
    variable = "settings"
```

### Add in-memory content

Use `<bx:zipParam>` to add content directly to an archive or to apply a source filter:

```xml
<bx:zip action="zip" file="/tmp/archive.zip">
    <bx:zipParam
        content="Hello BoxLang"
        entryPath="hello.txt">
    </bx:zipParam>
</bx:zip>
```

```xml
<bx:zip action="zip" file="/tmp/logs.zip" source="/tmp/logs">
    <bx:zipParam filter="*.log">
    </bx:zipParam>
</bx:zip>
```

## Related reference

- [`compress()`](../../boxlang-language/reference/built-in-functions/zip/Compress.md)
- [`extract()`](../../boxlang-language/reference/built-in-functions/zip/Extract.md)
- [`isZipFile()`](../../boxlang-language/reference/built-in-functions/zip/IsZipFile.md)
- [`<bx:zip>`](../../boxlang-language/reference/components/zip/Zip.md)
- [`<bx:zipParam>`](../../boxlang-language/reference/components/zip/ZipParam.md)
