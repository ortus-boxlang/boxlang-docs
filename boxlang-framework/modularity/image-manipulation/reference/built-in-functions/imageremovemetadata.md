---
description: Removes metadata types from an image, a metadata handle or a file.
icon: circle-info
---

# ImageRemoveMetadata

Removes metadata types from an image, a metadata handle or a file.

{% hint style="info" %}
Requires bx-image 1.17.0 or later on the JVM backend. These metadata APIs are not available on MatchBox.
{% endhint %}

## Method Signature

```js
any ImageRemoveMetadata( name [, types] )
image.removeMetadata( types )
metadata.removeMetadata( types )
```

## Arguments

| Argument | Type | Required | Description | Default |
| -------- | ---- | -------- | ----------- | ------- |
| name     | any  | true     | An image, a metadata handle, the name of a variable holding one, or a file path | |
| types    | any  | false    | A list or array of types: `exif`, `iptc`, `xmp`, `icc`, `comment`, `photoshop`, or `all` | all |

## Returns

The image or metadata handle, for chaining.

## Description

- On a **file path**, the file is rewritten in place without re-encoding; `ImageStripMetadata` is the same with a destination option.
- On a **metadata handle**, the working copy is changed; call `write()` to save.
- On an **image object**, only tags set earlier with the setter functions are undone, because an image's `write()` never carries source metadata in the first place.

## Examples

```js
ImageRemoveMetadata( "photo.jpg", "xmp" )
ImageRemoveMetadata( "photo.jpg", [ "exif", "photoshop" ] )
ImageReadMetadata( "photo.jpg" ).removeMetadata( "iptc" ).write( "no-iptc.jpg" )
```

## Related Functions

- [ImageStripMetadata](imagestripmetadata.md) - Remove metadata from a file into a copy or in place
- [ImageReadMetadata](imagereadmetadata.md) - Edit metadata without decoding the image

See the [metadata guide](../../metadata.md) for format support, lossless file editing, and image-object persistence rules.
