---
description: Usage and arguments for ImageReadBase64 in the bx-image module.
icon: code
---

# ImageReadBase64

## Syntax

```
ImageReadBase64( string )
```

## Arguments

| Name   | Type   | Required | Description                                            |
| ------ | ------ | -------- | ------------------------------------------------------ |
| string | String | Yes      | The base64-encoded string representing the image data. |

## Returns

`BoxImage` — The image object decoded from the base64 string.

## Description

Decodes a base64-encoded string into an image and returns it as a `BoxImage` object. This BIF is useful for importing images that are stored or transmitted as base64 strings, such as those embedded in data URIs or received from APIs.

Base64-encoded SVG documents are supported too: they are rendered to an image at the SVG's own size.

Since bx-image **1.17.0**, embedded EXIF and IPTC are also extracted from decoded Base64 bytes, as with file-loaded images:

```js
img = ImageReadBase64( myBase64String )
writeDump( img.getExifMetaData() )
writeDump( img.getIPTCMetaData() )
```

This exposes metadata for reading; it does not automatically preserve it when the image is written. See the [metadata guide](../../metadata.md).

## Example

```js
// Load an image from a base64 string
img = ImageReadBase64( myBase64String );
```

## Related BIFs

* ImageRead
* ImageNew
* ImageGetBlob

## Notes

* The `string` argument must be a non-empty base64-encoded string representing valid image data.
* If the image cannot be decoded, an error is thrown.
* Returns a `BoxImage` object for use in other image BIFs.
