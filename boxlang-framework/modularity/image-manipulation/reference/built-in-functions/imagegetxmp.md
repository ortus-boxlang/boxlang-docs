---
description: Returns the XMP packet of an image, a metadata handle or a file as a string.
icon: circle-info
---

# ImageGetXMP

Returns the XMP packet of an image, a metadata handle or a file as a string.

{% hint style="info" %}
Requires bx-image 1.17.0 or later on the JVM backend. These metadata APIs are not available on MatchBox.
{% endhint %}

## Method Signature

```js
string ImageGetXMP( name )
image.getXMP()
metadata.getXMP()
```

## Arguments

| Argument | Type | Required | Description | Default |
| -------- | ---- | -------- | ----------- | ------- |
| name     | any  | true     | An image, a metadata handle, the name of a variable holding one, or a file path | |

## Returns

The XMP packet as XML, or an empty string if there is none.

## Description

For a metadata handle or a file path this is the packet stored in the file. For an image object it is the packet set with `setXMP()`, because image objects do not retain their source file's XMP.

## Examples

```js
xmp = ImageGetXMP( "photo.jpg" )
if (len( xmp )) {
	doc = xmlParse( xmp )
}
```

## Related Functions

- [ImageSetXMP](imagesetxmp.md) - Set the XMP packet
- [ImageReadMetadata](imagereadmetadata.md) - Edit metadata without decoding the image

See the [metadata guide](../../metadata.md) for format support, lossless file editing, and image-object persistence rules.
