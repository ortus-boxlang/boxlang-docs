---
description: Removes all or some metadata from an image file without re-encoding it.
icon: circle-info
---

# ImageStripMetadata

Removes all or some metadata from an image file without re-encoding it.

{% hint style="info" %}
Requires bx-image 1.17.0 or later on the JVM backend. These metadata APIs are not available on MatchBox.
{% endhint %}

## Method Signature

```js
metadata ImageStripMetadata( source [, destination [, types ]] )
```

## Arguments

| Argument    | Type   | Required | Description | Default |
| ----------- | ------ | -------- | ----------- | ------- |
| source      | any    | true     | A file path, or an image that was read from a file | |
| destination | string | false    | Where to write the stripped copy; omit or empty to rewrite the source in place | |
| types       | any    | false    | A list or array of types to remove: `exif`, `iptc`, `xmp`, `icc`, `comment`, `photoshop` | all |

## Returns

The metadata handle used to write the result (see [ImageReadMetadata](imagereadmetadata.md)). Writing a copy does not change the handle's source path.

## Description

Remove embedded metadata before publishing uploads. The encoded image data is copied byte for byte, so no image quality is lost. File size changes according to the metadata removed. Without `types` everything the format can hold is removed, including the Photoshop resource block and JPEG comments.

## Examples

```js
// Everything, in place
ImageStripMetadata( "upload.jpg" )

// Everything, into a copy
ImageStripMetadata( "upload.jpg", "public/upload.jpg" )

// Remove EXIF and the Photoshop block (which may also contain IPTC)
ImageStripMetadata( "upload.jpg", "", "exif,photoshop" )
```

## Related Functions

- [ImageReadMetadata](imagereadmetadata.md) - Read and edit metadata
- [ImageRemoveMetadata](imageremovemetadata.md) - Remove types from an image, a handle or a file

## Notes

- Types the format cannot hold are ignored, so `ImageStripMetadata("logo.png")` never fails because PNG has no IPTC.
- A failure while writing leaves the original file untouched.

See the [metadata guide](../../metadata.md) for format support, lossless file editing, and image-object persistence rules.
