# ImageCrop

Crops an image to a specified rectangular area. This BIF allows you to select a region of an image to keep, discarding the rest, in BoxLang.

## Syntax

```
ImageCrop(name, x, y, width, height)
```

## Arguments

| Name   | Type    | Required | Description                                                             |
| ------ | ------- | -------- | ----------------------------------------------------------------------- |
| name   | any     | Yes      | The image or the name of a variable referencing an image to operate on. |
| x      | numeric | Yes      | The x coordinate of the upper left corner of the crop area.             |
| y      | numeric | Yes      | The y coordinate of the upper left corner of the crop area.             |
| width  | numeric | Yes      | The width of the crop area.                                             |
| height | numeric | Yes      | The height of the crop area.                                            |

## Returns

* **BoxImage**: The modified BoxImage instance cropped to the specified area.

## Description

`ImageCrop` crops the specified image to a rectangular region, starting at (x, y) and extending to the given width and height. Only the selected area will remain visible after the operation. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Crop a 100x50 region at position (10, 20)
img = ImageCrop(myImage, 10, 20, 100, 50);
```

## See Also

* ImageResize
* ImageCopy

## Notes

* All arguments are required.
* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The crop region must be within the image boundaries.
* Returns the modified image object for method chaining.
* The cropped image becomes the new image - original content outside the crop area is discarded.
* Coordinates start at (0, 0) in the top-left corner.
