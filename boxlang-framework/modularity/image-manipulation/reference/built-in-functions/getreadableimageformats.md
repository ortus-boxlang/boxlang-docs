# GetReadableImageFormats

Returns an array of readable image formats supported by the underlying Java ImageIO library. This BIF is useful for determining which image formats can be read (imported) in BoxLang on the current platform.

## Syntax

```
GetReadableImageFormats()
```

## Arguments

This BIF does not accept any arguments.

## Returns

* **Array**: An array of strings, each representing a readable image format name (e.g., "png", "jpg", "gif").

## Description

`GetReadableImageFormats` queries the Java ImageIO subsystem for all image formats that can be read (decoded) in the current environment. The returned array contains the format names as strings. This is useful for dynamically checking which image types are supported for reading, especially in environments where available formats may vary.

## Example

```boxlang
formats = GetReadableImageFormats();
// formats might be ["BMP", "GIF", "JPEG", "PNG", "TIFF", "WEBP", "WBMP"]
```

## See Also

* GetWriteableImageFormats
* ImageRead
* IsImageFile

## Notes

* The list of formats depends on the Java runtime and any installed ImageIO plugins.
* BoxLang ships with `com.twelvemonkeys.imageio:imageio-webp` for cross-platform WebP reading (including macOS ARM64 / Apple Silicon).
* Common formats include "png", "jpg", "gif", "webp", "bmp", "tiff", but may include others depending on the environment.
