---
description: Reads the metadata of an image file or URL without decoding the image and returns a metadata handle for reading, editing and writing EXIF, IPTC, XMP and ICC data.
icon: circle-info
---

# ImageReadMetadata

Reads the metadata of an image file or URL without decoding the image and returns a metadata handle for reading, editing and writing EXIF, IPTC, XMP and ICC data.

{% hint style="info" %}
Requires bx-image 1.17.0 or later on the JVM backend. These metadata APIs are not available on MatchBox.
{% endhint %}

## Method Signature

```js
metadata ImageReadMetadata( source )
```

## Arguments

| Argument | Type | Required | Description | Default |
| -------- | ---- | -------- | ----------- | ------- |
| source   | any  | true     | A file path or URL, an existing metadata handle, or an image read from a file (reopens its source) | |

## Returns

A metadata handle with these methods:

| Method | Description |
| ------ | ----------- |
| `getExif()` / `getIPTC()` | Structs keyed by display name, the same as `ImageGetExifMetaData()` / `ImageGetIPTCMetadata()`; reflect pending changes |
| `getExifTag(name)` / `getIPTCTag(name)` | One tag, or null if absent; any common spelling of the name |
| `getXMP()` | The XMP packet as a string, or `""` |
| `getICCProfile()` | The ICC profile bytes, or null |
| `getTypes()` | Array of the types present: `exif`, `iptc`, `xmp`, `icc`, `comment`, `photoshop` |
| `getFormat()` | `jpg`, `tiff`, `png`, `gif` or `webp` |
| `canWrite(type)` | Whether the format can hold a type |
| `setExifTag(name, value)` / `setIPTCTag(name, value)` | Set one tag; null removes it; arrays for repeatable IPTC tags |
| `setExifMetaData(struct)` / `setIPTCMetaData(struct)` | Set several tags |
| `setXMP(xml)` / `setICCProfile(bytes)` | Replace the packet / profile; empty or null removes it |
| `removeExifTag(name)` / `removeIPTCTag(name)` | Remove one tag |
| `remove(types...)` / `removeAll()` | Remove whole types |
| `hasChanges()` | Whether a setter has been called |
| `write()` | Rewrite the source file in place (temporary file and atomic move) |
| `write(destination)` | Write a copy with the new metadata |
| `toBinary()` / `toBase64()` | The image with the new metadata as bytes / Base64 |

All setters return the handle, so calls chain.

## Description

`ImageReadMetadata` opens the file, parses only the metadata blocks and keeps the image data untouched. Writing copies the image data byte for byte and replaces the metadata, so metadata-only edits avoid image re-encoding and lose no image quality. Metadata the handle was not told about (maker notes, thumbnails, other IPTC fields) stays as it was.

Tag names accept the display names the getters return (`Date/Time Original`, `Copyright Notice`, `By-line`), the specification names (`DateTimeOriginal`, `CopyrightNotice`) and common aliases (`ISO`, `Copyright`, `Caption`, `Creator`). Values may be strings, numbers, dates or arrays. A decimal `GPSLatitude` / `GPSLongitude` also sets the N/S or E/W reference tag.

JPEG and TIFF hold EXIF, IPTC, XMP and ICC; WebP holds EXIF, XMP and ICC; PNG holds XMP and ICC; GIF holds XMP. Setting a type the format cannot hold throws a clear error.

## Examples

### Add copyright and keywords to a photo

```js
ImageReadMetadata( "photo.jpg" )
	.setExifTag( "Copyright", "(c) 2026 akitogo" )
	.setIPTCTag( "Copyright Notice", "(c) 2026 akitogo" )
	.setIPTCTag( "Keywords", [ "garden", "spring" ] )
	.write()
```

### Geotag and date a scan

```js
meta = ImageReadMetadata( "scan.tif" )
meta.setExifTag( "Date/Time Original", createDateTime( 1998, 7, 14, 10, 30, 0 ) )
	.setExifTag( "GPSLatitude", 52.503472 )
	.setExifTag( "GPSLongitude", 13.41 )
	.write( "scan-tagged.tif" )
```

### Inspect before editing

```js
meta = ImageReadMetadata( "upload.jpg" )
if ( arrayContains( meta.getTypes(), "exif" )) {
	writeOutput( "Camera: " & meta.getExifTag( "Model" ) )
}
```

## Related Functions

- [ImageStripMetadata](imagestripmetadata.md) - Remove metadata from a file
- ImageSetExifTag / ImageSetIPTCTag / ImageSetXMP - The same setters on images and paths
- ImageGetExifMetaData / ImageGetIPTCMetadata - Read metadata as structs

## Notes

- The image is not decoded, so `maxPixels` does not apply; `maxBytes` still caps the file size that is read.
- `write()` needs a local file; for a URL source use `write(destination)` or `toBinary()`.
- A failure during an in-place write leaves the original file untouched.
- The handle retains source bytes in memory; allow for this when processing large files or batches.
- Passing an image reopens its source file, not its pending edits. An image with no source path cannot be used here.

See the [metadata guide](../../metadata.md) for format support, lossless file editing, and image-object persistence rules.
