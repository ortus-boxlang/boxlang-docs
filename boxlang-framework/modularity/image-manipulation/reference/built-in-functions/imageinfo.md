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

`ImageInfo` returns a struct with general properties of the specified image. Typical fields include width, height, format, color model, and other metadata. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Get image info
info = ImageInfo(myImage);
// info might contain { width: 800, height: 600, format: "jpg", colorModel: "RGB" }
```

## See Also

* ImageGetWidth
* ImageGetHeight
* ImageGetExifMetaData

## Notes

* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The returned struct contains general image properties and may vary by image type.
