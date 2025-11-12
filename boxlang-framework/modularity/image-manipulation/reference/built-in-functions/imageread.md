# ImageRead

## Syntax

```
ImageRead( path )
```

## Arguments

| Name | Type   | Required | Description                                |
| ---- | ------ | -------- | ------------------------------------------ |
| path | String | Yes      | The file path or URL to the image to read. |

## Returns

`BoxImage` — The image object loaded from the specified path.

## Description

Loads an image from a file path or URL and returns it as a `BoxImage` object. This BIF is used to import images into BoxLang for further processing or manipulation.

## Example

```boxlang
// Load an image from a file
img = ImageRead( "images/photo.png" );

// Load an image from a URL
img = ImageRead( "https://example.com/image.jpg" );
```

## Related BIFs

* ImageNew
* ImageCopy
* ImageGetWidth
* ImageGetHeight

## Notes

* The `path` argument must be a non-empty string representing a valid file path or URL.
* If the image cannot be loaded, an error is thrown.
* Returns a `BoxImage` object for use in other image BIFs.
* **File handles are properly closed** - no file locking issues on Windows after reading.
* Files can be deleted immediately after `ImageRead()` completes.
* Images are fully loaded into memory - no lazy loading issues.
* Safe to use immediately without needing to call `info()` first.
