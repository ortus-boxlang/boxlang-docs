# ImageDrawBeveledRect

Draws a beveled rectangle on an image. This BIF allows you to specify the position, size, whether the bevel is raised, and whether the rectangle is filled in BoxLang.

## Syntax

```
ImageDrawBeveledRect(name, x, y, width, height, raised [, filled])
```

## Arguments

| Name   | Type    | Required | Default | Description                                                             |
| ------ | ------- | -------- | ------- | ----------------------------------------------------------------------- |
| name   | any     | Yes      |         | The image or the name of a variable referencing an image to operate on. |
| x      | numeric | Yes      |         | The x coordinate of the upper left corner of the rectangle.             |
| y      | numeric | Yes      |         | The y coordinate of the upper left corner of the rectangle.             |
| width  | numeric | Yes      |         | The width of the rectangle.                                             |
| height | numeric | Yes      |         | The height of the rectangle.                                            |
| raised | boolean | Yes      |         | Whether the bevel is raised (true) or lowered (false).                  |
| filled | boolean | Yes      | false   | Whether the rectangle should be filled.                                 |

## Returns

* **BoxImage**: The modified BoxImage instance with the beveled rectangle drawn.

## Description

`ImageDrawBeveledRect` draws a beveled rectangle on the specified image, using the provided position, size, and bevel style. The rectangle can be filled or just outlined, depending on the `filled` argument. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Draw a filled, raised beveled rectangle
img = ImageDrawBeveledRect(myImage, 10, 20, 100, 50, true, true);

// Draw an outlined, lowered beveled rectangle
img = ImageDrawBeveledRect(myImage, 10, 20, 100, 50, false);
```

## See Also

* ImageDrawRect
* ImageDrawArc

## Notes

* All arguments except `filled` are required.
* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The bevel style is controlled by the `raised` argument.
* The rectangle is drawn at (x, y) with the specified width and height.
