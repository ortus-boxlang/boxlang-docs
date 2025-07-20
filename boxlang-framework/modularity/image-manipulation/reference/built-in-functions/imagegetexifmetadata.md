# ImageGetExifMetaData

Returns the EXIF metadata from an image. This BIF allows you to extract camera and image metadata in BoxLang, such as date taken, camera model, orientation, and more.

## Syntax

```
ImageGetExifMetaData(name)
```

## Arguments

| Name | Type | Required | Description                                                                           |
| ---- | ---- | -------- | ------------------------------------------------------------------------------------- |
| name | any  | Yes      | The image or the name of a variable referencing an image, or a file path to an image. |

## Returns

* **IStruct**: A struct containing the EXIF metadata from the image.

## Description

`ImageGetExifMetaData` extracts EXIF metadata from the specified image. You can pass a BoxImage object, a variable name referencing an image, or a file path string. The returned struct contains key-value pairs for available EXIF metadata fields, such as camera make/model, date/time, orientation, GPS info, and more.

## Example

```boxlang
// Get EXIF metadata from a BoxImage
meta = ImageGetExifMetaData(myImage);

// Get EXIF metadata from an image file path
meta = ImageGetExifMetaData("/path/to/image.jpg");
```

## See Also

* ImageGetBlob
* ImageRead

## Notes

* The image can be passed as a BoxImage object, a variable name referencing an image, or a file path string.
* If the image cannot be read or metadata cannot be processed, an error is thrown.
* The returned struct contains only available EXIF fields for the image.
