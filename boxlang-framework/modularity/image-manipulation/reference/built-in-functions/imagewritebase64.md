# ImageWriteBase64

## Syntax

```
ImageWriteBase64( name [, format] )
```

Or as a member:

```
someImage.toBase64String( [format] )
```

## Arguments

| Name   | Type   | Required | Description                                                                     |
| ------ | ------ | -------- | ------------------------------------------------------------------------------- |
| name   | any    | Yes      | The image to encode. Can be a `BoxImage` object or image name.                  |
| format | String | No       | The image format for encoding (e.g., "png", "jpg", "webp"). Auto-detected from the source if omitted. |

## Returns

`String` — The base64-encoded string representing the image in the specified or detected format.

## Description

Encodes the specified image as a base64 string. If no `format` is specified, the format is auto-detected from the image's original source (e.g., a JPEG file produces a JPEG base64 string). You can override this by providing an explicit format. Useful for embedding images in HTML, transmitting via APIs, or storing images as text.

## Example

```boxlang
// Encode image as base64 (auto-detect format from source)
base64String = ImageWriteBase64( myImage );

// Encode with explicit format
base64PNG  = ImageWriteBase64( myImage, "png" );
base64JPG  = ImageWriteBase64( myImage, "jpg" );
base64WebP = ImageWriteBase64( myImage, "webp" );

// Member syntax with auto-detect
base64 = myImage.toBase64String();

// Member syntax with explicit format
base64 = myImage.toBase64String( "webp" );
```

## Related BIFs

* ImageReadBase64
* ImageWrite
* ImageGetBlob

## Notes

* The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
* The `format` argument is optional. When omitted, the format is detected from the image's source file extension.
* Supported formats include "png", "jpg", "webp", "gif", "bmp", "tiff".
* Returns a base64-encoded string suitable for embedding or transmission.
* If encoding fails, an error is thrown.
