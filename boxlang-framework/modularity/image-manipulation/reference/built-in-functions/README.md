---
description: API reference and usage examples for the bx-image module.
icon: code
---

# Built-in Functions

Complete reference pages for the BoxLang Image module BIFs.

## 🆕 Metadata APIs (1.17.0)

These APIs require the JVM backend. See the [metadata guide](../../metadata.md) for format support and file-versus-image persistence rules.

- [ImageReadMetadata](imagereadmetadata.md) — Read a metadata handle without decoding pixels
- [ImageStripMetadata](imagestripmetadata.md) — Strip file metadata without re-encoding
- [ImageSetExifTag](imagesetexiftag.md) — Set one EXIF tag
- [ImageSetExifMetaData](imagesetexifmetadata.md) — Set EXIF tags from a struct
- [ImageSetIPTCTag](imagesetiptctag.md) — Set one IPTC tag
- [ImageSetIPTCMetaData](imagesetiptcmetadata.md) — Set IPTC tags from a struct
- [ImageSetXMP](imagesetxmp.md) — Replace the XMP packet
- [ImageGetXMP](imagegetxmp.md) — Read the XMP packet
- [ImageRemoveMetadata](imageremovemetadata.md) — Remove metadata types

## Other Recent Additions

- [ImageGetPixels](imagegetpixels.md)
- [ImageGenerateCaptcha](imagegeneratecaptcha.md)
- [ImageSplitGrid](imagesplitgrid.md)

## Tip

Use the quick reference table in the parent reference page for a full alphabetical overview:

- [Reference Home](../README.md)
