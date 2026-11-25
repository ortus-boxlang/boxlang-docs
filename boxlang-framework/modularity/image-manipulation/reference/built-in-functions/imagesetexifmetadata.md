---
description: Sets several EXIF tags from a struct on an image, a metadata handle or a file.
icon: circle-info
---

# ImageSetExifMetaData

Sets several EXIF tags from a struct on an image, a metadata handle or a file.

{% hint style="info" %}
Requires bx-image 1.17.0 or later on the JVM backend. These metadata APIs are not available on MatchBox.
{% endhint %}

## Method Signature

```js
any ImageSetExifMetaData( name, tags )
image.setExifMetaData( tags )
metadata.setExifMetaData( tags )
```

## Arguments

| Argument | Type   | Required | Description | Default |
| -------- | ------ | -------- | ----------- | ------- |
| name     | any    | true     | An image, a metadata handle, the name of a variable holding one, or a file path | |
| tags     | struct | true     | Tag names to values. A null value removes the tag | |

## Returns

The image or metadata handle, for chaining.

## Description

Equivalent to calling `ImageSetExifTag` for every key. See `ImageSetExifTag` for how images, handles and file paths are treated and which tag names are accepted.

## Examples

```js
ImageSetExifMetaData( "photo.jpg", {
	"Artist": "Jane Doe",
	"Copyright": "(c) 2026 akitogo"
} )
```

## Related Functions

- [ImageSetExifTag](imagesetexiftag.md) - Set one tag
- [ImageReadMetadata](imagereadmetadata.md) - Edit metadata without decoding the image

See the [metadata guide](../../metadata.md) for format support, lossless file editing, and image-object persistence rules.
