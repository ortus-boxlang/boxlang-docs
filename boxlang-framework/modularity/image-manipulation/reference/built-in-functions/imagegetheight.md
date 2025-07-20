# ImageGetHeight

Returns the height (in pixels) of an image. This BIF allows you to retrieve the vertical dimension of an image in BoxLang.

## Syntax

```
ImageGetHeight(name)
```

## Arguments

| Name | Type | Required | Description                                                             |
| ---- | ---- | -------- | ----------------------------------------------------------------------- |
| name | any  | Yes      | The image or the name of a variable referencing an image to operate on. |

## Returns

* **Integer**: The height of the image in pixels.

## Description

`ImageGetHeight` returns the height (number of pixels vertically) of the specified image. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Get the height of an image
height = ImageGetHeight(myImage);
```

## See Also

* ImageGetWidth
* ImageResize

## Notes

* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The returned value is the height in pixels.
