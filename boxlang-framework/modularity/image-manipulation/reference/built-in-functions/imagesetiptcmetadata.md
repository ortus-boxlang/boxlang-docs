---
description: Sets several IPTC tags from a struct on an image, a metadata handle or a file.
icon: circle-info
---

# ImageSetIPTCMetaData

Sets several IPTC tags from a struct on an image, a metadata handle or a file.

{% hint style="info" %}
Requires bx-image 1.17.0 or later on the JVM backend. These metadata APIs are not available on MatchBox.
{% endhint %}

## Method Signature

```js
any ImageSetIPTCMetaData( name, tags )
image.setIPTCMetaData( tags )
metadata.setIPTCMetaData( tags )
```

## Arguments

| Argument | Type   | Required | Description | Default |
| -------- | ------ | -------- | ----------- | ------- |
| name     | any    | true     | An image, a metadata handle, the name of a variable holding one, or a file path | |
| tags     | struct | true     | Tag names to values. A null value removes the tag | |

## Returns

The image or metadata handle, for chaining.

## Description

Equivalent to calling `ImageSetIPTCTag` for every key. See `ImageSetIPTCTag` for how images, handles and file paths are treated and which tag names are accepted.

## Examples

```js
ImageSetIPTCMetaData( "photo.jpg", {
	"By-line": "Jane Doe",
	"Copyright Notice": "(c) 2026 akitogo"
} )
```

## Related Functions

- [ImageSetIPTCTag](imagesetiptctag.md) - Set one tag
- [ImageReadMetadata](imagereadmetadata.md) - Edit metadata without decoding the image

See the [metadata guide](../../metadata.md) for format support, lossless file editing, and image-object persistence rules.
