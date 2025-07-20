# ImageGrayScale / ImageGreyScale

Converts an image to grayscale. This BIF allows you to remove color and produce a black-and-white version of an image in BoxLang.

## Syntax

```
ImageGrayScale(name)
ImageGreyScale(name)
```

## Arguments

| Name | Type | Required | Description                                                             |
| ---- | ---- | -------- | ----------------------------------------------------------------------- |
| name | any  | Yes      | The image or the name of a variable referencing an image to operate on. |

## Returns

* **BoxImage**: The modified BoxImage instance in grayscale.

## Description

`ImageGrayScale` (also available as `ImageGreyScale`) converts the specified image to grayscale, removing all color information. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Convert an image to grayscale
grayImg = ImageGrayScale(myImage);
// Or using the alias
grayImg = ImageGreyScale(myImage);
```

## See Also

* ImageInvert
* ImageBlur

## Notes

* The image can be passed as a BoxImage object or as a variable name referencing an image.
* Both `grayScale` and `greyScale` member methods are available for BoxImage objects.
