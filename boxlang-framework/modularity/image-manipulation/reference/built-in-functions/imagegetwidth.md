# ImageGetWidth

Returns the width (in pixels) of an image. This BIF allows you to retrieve the horizontal dimension of an image in BoxLang.

## Syntax

```
ImageGetWidth(name)
```

## Arguments

| Name | Type | Required | Description                                                             |
| ---- | ---- | -------- | ----------------------------------------------------------------------- |
| name | any  | Yes      | The image or the name of a variable referencing an image to operate on. |

## Returns

* **Integer**: The width of the image in pixels.

## Description

`ImageGetWidth` returns the width (number of pixels horizontally) of the specified image. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Get the width of an image
width = ImageGetWidth(myImage);
```

## See Also

* ImageGetHeight
* ImageResize

## Notes

* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The returned value is the width in pixels.
