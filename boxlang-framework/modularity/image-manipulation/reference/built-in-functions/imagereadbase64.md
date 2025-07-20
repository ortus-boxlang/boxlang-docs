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

## Example

```boxlang
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
