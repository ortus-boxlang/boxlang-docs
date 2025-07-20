# ImageWriteBase64

## Syntax

```
ImageWriteBase64( name, format )
```

## Arguments

| Name   | Type   | Required | Description                                                    |
| ------ | ------ | -------- | -------------------------------------------------------------- |
| name   | any    | Yes      | The image to encode. Can be a `BoxImage` object or image name. |
| format | String | Yes      | The image format for encoding (e.g., "png", "jpg").            |

## Returns

`String` — The base64-encoded string representing the image in the specified format.

## Description

Encodes the specified image as a base64 string in the given format. Useful for embedding images in HTML, transmitting via APIs, or storing images as text.

## Example

```boxlang
// Encode image as base64 PNG
base64String = ImageWriteBase64( myImage, "png" );

// Encode image as base64 JPEG
base64String = ImageWriteBase64( myImage, "jpg" );
```

## Related BIFs

* ImageReadBase64
* ImageWrite
* ImageGetBlob

## Notes

* The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
* The `format` argument should be a valid image format supported by BoxLang (e.g., "png", "jpg").
* Returns a base64-encoded string suitable for embedding or transmission.
* If encoding fails, an error is thrown.
