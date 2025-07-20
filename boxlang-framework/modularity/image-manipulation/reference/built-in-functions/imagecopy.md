# ImageCopy

Copies a rectangular region of an image and draws it at a new location. This BIF allows you to specify the source area and the destination offset in BoxLang.

## Syntax

```
ImageCopy(name, x, y, width, height [, dx] [, dy])
```

## Arguments

| Name   | Type    | Required | Default | Description                                                             |
| ------ | ------- | -------- | ------- | ----------------------------------------------------------------------- |
| name   | any     | Yes      |         | The image or the name of a variable referencing an image to operate on. |
| x      | numeric | Yes      |         | The x coordinate of the rectangular area of the image to copy.          |
| y      | numeric | Yes      |         | The y coordinate of the rectangular area of the image to copy.          |
| width  | numeric | Yes      |         | The width of the rectangular area of the image to copy.                 |
| height | numeric | Yes      |         | The height of the rectangular area of the image to copy.                |
| dx     | numeric | No       | 0       | The amount to shift the x coordinate when drawing the copied area.      |
| dy     | numeric | No       | 0       | The amount to shift the y coordinate when drawing the copied area.      |

## Returns

* **BoxImage**: The modified BoxImage instance with the copied region drawn at the new location.

## Description

`ImageCopy` copies a rectangular region from the specified image, starting at (x, y) with the given width and height, and draws it at a new location offset by (dx, dy). The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Copy a 100x50 region at (10, 20) and draw it at (110, 70)
img = ImageCopy(myImage, 10, 20, 100, 50, 100, 50);

// Copy a region and draw it at the same location (no offset)
img = ImageCopy(myImage, 10, 20, 100, 50);
```

## See Also

* ImageClearRect
* ImageDrawRect

## Notes

* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The default offset is (0, 0) if dx and dy are not specified.
