# GetWriteableImageFormats

Returns an array of writeable image formats supported by the underlying Java ImageIO library. This BIF is useful for determining which image formats can be written (exported) in BoxLang on the current platform.

## Syntax

```
GetWriteableImageFormats()
```

## Arguments

This BIF does not accept any arguments.

## Returns

* **Array**: An array of strings, each representing a writeable image format name (e.g., "png", "jpg", "gif").

## Description

`GetWriteableImageFormats` queries the Java ImageIO subsystem for all image formats that can be written (encoded) in the current environment. The returned array contains the format names as strings. This is useful for dynamically checking which image types are supported for writing, especially in environments where available formats may vary.

## Example

```boxlang
formats = GetWriteableImageFormats();
// formats might be ["png", "jpg", "gif", ...]
```

## See Also

* GetReadableImageFormats
* ImageWrite

## Notes

* The list of formats depends on the Java runtime and any installed imageio plugins.
* Common formats include "png", "jpg", "gif", but may include others depending on the environment.
