# ImageDrawRect

Draws a rectangle on an image. This BIF allows you to specify the position, size, and whether the rectangle is filled in BoxLang.

## Syntax

```
ImageDrawRect(name, x, y, width, height [, filled])
```

## Arguments

| Name   | Type    | Required | Default | Description                                                             |
| ------ | ------- | -------- | ------- | ----------------------------------------------------------------------- |
| name   | any     | Yes      |         | The image or the name of a variable referencing an image to operate on. |
| x      | numeric | Yes      |         | The x coordinate of the upper left corner of the rectangle.             |
| y      | numeric | Yes      |         | The y coordinate of the upper left corner of the rectangle.             |
| width  | numeric | Yes      |         | The width of the rectangle.                                             |
| height | numeric | Yes      |         | The height of the rectangle.                                            |
| filled | boolean | No       | false   | Whether the rectangle should be filled.                                 |

## Returns

* **BoxImage**: The modified BoxImage instance with the rectangle drawn.

## Description

`ImageDrawRect` draws a rectangle on the specified image, using the provided position and size. The rectangle can be filled or just outlined, depending on the `filled` argument. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Draw a filled rectangle
img = ImageDrawRect(myImage, 10, 20, 100, 50, true);

// Draw an outlined rectangle
img = ImageDrawRect(myImage, 10, 20, 100, 50);
```

## See Also

* ImageDrawOval
* ImageDrawArc

## Notes

* All arguments except `filled` are required.
* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The rectangle is drawn at (x, y) with the specified width and height.
* Uses the current drawing color (set with `ImageSetDrawingColor`).
* Line thickness and style are controlled by `ImageSetDrawingStroke`.
* Enable anti-aliasing with `ImageSetAntiAliasing` for smoother edges.
* Returns the image object for method chaining.
