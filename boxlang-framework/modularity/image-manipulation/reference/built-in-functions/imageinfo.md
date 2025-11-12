# ImageInfo

Returns general information about an image. This BIF allows you to retrieve a struct of image properties in BoxLang, such as width, height, format, color model, and more.

## Syntax

```
ImageInfo(name)
```

## Arguments

| Name | Type | Required | Description                                                             |
| ---- | ---- | -------- | ----------------------------------------------------------------------- |
| name | any  | Yes      | The image or the name of a variable referencing an image to operate on. |

## Returns

* **IStruct**: A struct containing general information about the image.

## Description

`ImageInfo` returns a comprehensive struct with properties and metadata of the specified image. The image can be passed directly or referenced by variable name.

**Returned struct contains:**

* `width` (numeric): Image width in pixels
* `height` (numeric): Image height in pixels
* `source` (string): Original source path or URL
* `colormodel` (struct): Color model information including type and color space
* `transparency` (boolean): Whether the image supports transparency
* `EXIF` (struct): EXIF metadata (camera settings, date/time, GPS, etc.) - if available
* `IPTC` (struct): IPTC metadata (copyright, keywords, author, etc.) - if available

## Example

```boxlang
// Get comprehensive image info
info = ImageInfo(myImage);

writeOutput("Dimensions: #info.width# x #info.height#<br>");
writeOutput("Source: #info.source#<br>");
writeOutput("Color Model: #info.colormodel.colormodel_type#<br>");
writeOutput("Has Transparency: #info.transparency#<br>");

// Access EXIF data if available
if (structKeyExists(info, "EXIF") && !structIsEmpty(info.EXIF)) {
    writeOutput("Camera: #info.EXIF.Make# #info.EXIF.Model#<br>");
}

// Access IPTC data if available
if (structKeyExists(info, "IPTC") && !structIsEmpty(info.IPTC)) {
    writeOutput("Copyright: #info.IPTC.Copyright#<br>");
}
```

## See Also

* ImageGetWidth
* ImageGetHeight
* ImageGetExifMetaData

## Notes

* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The returned struct always contains width, height, source, colormodel, and transparency fields.
* EXIF and IPTC metadata are included only if present in the image (typically JPEG files).
* Metadata is extracted automatically when the image is loaded.
* For specific EXIF or IPTC values, use `ImageGetExifTag` or `ImageGetIPTCTag`.
