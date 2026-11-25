---
description: Sets an EXIF tag on an image, a metadata handle or a file.
icon: circle-info
---

# ImageSetExifTag

Sets an EXIF tag on an image, a metadata handle or a file.

{% hint style="info" %}
Requires bx-image 1.17.0 or later on the JVM backend. These metadata APIs are not available on MatchBox.
{% endhint %}

## Method Signature

```js
any ImageSetExifTag( name, tagName, value )
image.setExifTag( tagName, value )
metadata.setExifTag( tagName, value )
```

## Arguments

| Argument | Type   | Required | Description | Default |
| -------- | ------ | -------- | ----------- | ------- |
| name     | any    | true     | An image, a metadata handle from `ImageReadMetadata()`, the name of a variable holding one, or a file path | |
| tagName  | string | true     | The EXIF tag, e.g. `Artist`, `Copyright`, `Date/Time Original` or `DateTimeOriginal`, `ISO`, `FNumber`, `GPSLatitude` | |
| value    | any    | false    | String, number, date or array. Null removes the tag | |

## Returns

The image or metadata handle, for chaining.

## Description

- On an **image**, the tag is applied to the encoded bytes when the image is written (`write()`, `ImageWriteBase64()`, `toByteArray()`). The pixels are not touched. A plain `write()` without setters produces the same file as before, and source metadata is not carried through pixel edits.
- On a **metadata handle**, the working copy is changed; call `write()` on the handle to save.
- On a **file path**, the file is rewritten in place without re-encoding.

Tag names accept the display names the getters return and the specification names. Setting a tag to `null` removes it.

## Examples

```js
// On an image being edited
imageRead( "photo.jpg" ).resize( 800, 600 ).setExifTag( "Artist", "Jane Doe" ).write( "thumb.jpg" )

// On a file, in place and lossless
ImageSetExifTag( "photo.jpg", "Copyright", "(c) 2026 akitogo" )

// Dates and GPS
ImageSetExifTag( "photo.jpg", "Date/Time Original", now() )
ImageSetExifTag( "photo.jpg", "GPSLatitude", 52.503472 )   // sets GPS Latitude Ref "N" too
ImageSetExifTag( "photo.jpg", "GPSLongitude", -13.41 )     // sets GPS Longitude Ref "W"
```

## Related Functions

- [ImageSetExifMetaData](imagesetexifmetadata.md) - Set several EXIF tags from a struct
- [ImageGetExifTag](imagegetexiftag.md) - Read an EXIF tag
- [ImageReadMetadata](imagereadmetadata.md) - Edit metadata without decoding the image

See the [metadata guide](../../metadata.md) for format support, lossless file editing, and image-object persistence rules.
