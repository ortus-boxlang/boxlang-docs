# ImageRead

## Syntax

```
ImageRead( path [, width] [, height] )
```

## Arguments

| Name   | Type    | Required | Description                                                                                                       |
| ------ | ------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
| path   | String  | Yes      | The file path or URL to the image to read.                                                                        |
| width  | numeric | No       | Width to read the image at. An SVG is drawn straight at this size; other formats are resized after decoding.     |
| height | numeric | No       | Height to read the image at. With only one of `width` or `height`, the other keeps the image's aspect ratio.     |

## Returns

`BoxImage` — The image object loaded from the specified path.

## Description

Loads an image from a file path or URL and returns it as a `BoxImage` object. This BIF is used to import images into BoxLang for further processing or manipulation.

Raster formats (PNG, JPEG, GIF, BMP, TIFF, WebP) are decoded as they are. An **SVG** file is rendered to a transparent ARGB image, so every other image function works on it. SVG is detected by the `.svg` extension or by its content.

Pass `width` and/or `height` to get the image at a given size in one step. For an SVG this matters: the drawing is rendered at that size, so it stays sharp, while resizing it later scales the pixels. When both are given, an SVG is fitted into that box following its own `preserveAspectRatio`, and other formats are resized to exactly that size.

## Example

```boxlang
// Load an image from a file
img = ImageRead( "images/photo.png" );

// Load an image from a URL
img = ImageRead( "https://example.com/image.jpg" );

// Render an SVG at 400 pixels wide; the height keeps the aspect ratio
logo = ImageRead( "images/logo.svg", 400 )

// Read a photo straight at a thumbnail height
thumb = ImageRead( path = "images/photo.jpg", height = 150 )
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
* An SVG with neither a `viewBox` nor an absolute `width` and `height` reads as 512 x 512 pixels.
* SVG files never load external resources (linked images or fonts); only embedded `data:` resources are rendered.
* The rendered size of an SVG, like the declared size of any image, is checked against the module's `maxPixels` setting.
* `width` and `height` must be greater than zero.
* Also available on the [MatchBox native backend](../../matchbox.md).
