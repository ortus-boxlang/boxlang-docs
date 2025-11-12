# ImageNew

## Syntax

```
ImageNew( source [, width] [, height] [, imageType] [, color] )
```

## Arguments

| Name      | Type    | Required | Default | Description                                                                                  |
| --------- | ------- | -------- | ------- | -------------------------------------------------------------------------------------------- |
| source    | any     | Yes      |         | The source for the image. Can be a file path, URL, BufferedImage, BoxImage, or empty string. |
| width     | numeric | No       |         | Width of the new image (required if creating a blank image).                                 |
| height    | numeric | No       |         | Height of the new image (required if creating a blank image).                                |
| imageType | string  | No       |         | Type of image to create (e.g., "RGB", "ARGB").                                               |
| color     | string  | No       | black   | Background color for a new blank image.                                                      |

## Returns

`BoxImage` — The newly created image object.

## Description

Creates a new image from a variety of sources:

* If `source` is a file path or URL, loads the image from that location.
* If `source` is a `BufferedImage`, wraps it in a `BoxImage`.
* If `source` is a `BoxImage`, returns a copy of it.
* If `source` is an empty string, creates a blank image using the provided `width`, `height`, `imageType`, and `color` arguments.

## Example

```boxlang
// Create from file path
img = ImageNew( "images/photo.png" );

// Create from URL
img = ImageNew( "https://example.com/image.jpg" );

// Create blank image
img = ImageNew( "", 400, 300, "RGB", "white" );

// Copy an existing BoxImage
imgCopy = ImageNew( img );
```

## Related BIFs

* ImageCopy
* ImageInfo
* ImageGetWidth
* ImageGetHeight

## Notes

* If creating a blank image, `width` and `height` are required.
* The `imageType` should match supported types (e.g., "RGB", "ARGB").
* If loading from a file or URL fails, an error is thrown.
* The default color for blank images is black unless specified.
* **File handles are properly managed** - no file locking issues on Windows.
* Files can be deleted immediately after loading with `ImageNew()`.
* Images are fully loaded into memory upon creation - no lazy loading issues.
* Safe to use immediately after creation without needing to call `info()` first.
