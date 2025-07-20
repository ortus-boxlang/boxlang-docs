# ImageDrawRoundRect

Draws a rounded rectangle on an image. This BIF allows you to specify the position, size, corner arc dimensions, and whether the rectangle is filled in BoxLang.

## Syntax

```
ImageDrawRoundRect(name, x, y, width, height, arcWidth, arcHeight [, filled])
```

## Arguments

| Name      | Type    | Required | Default | Description                                                             |
| --------- | ------- | -------- | ------- | ----------------------------------------------------------------------- |
| name      | any     | Yes      |         | The image or the name of a variable referencing an image to operate on. |
| x         | numeric | Yes      |         | The x coordinate of the upper left corner of the rectangle.             |
| y         | numeric | Yes      |         | The y coordinate of the upper left corner of the rectangle.             |
| width     | numeric | Yes      |         | The width of the rectangle.                                             |
| height    | numeric | Yes      |         | The height of the rectangle.                                            |
| arcWidth  | numeric | Yes      |         | The horizontal diameter of the arc at the four corners.                 |
| arcHeight | numeric | Yes      |         | The vertical diameter of the arc at the four corners.                   |
| filled    | boolean | No       | false   | Whether the rectangle should be filled.                                 |

## Returns

* **BoxImage**: The modified BoxImage instance with the rounded rectangle drawn.

## Description

`ImageDrawRoundRect` draws a rectangle with rounded corners on the specified image, using the provided position, size, and arc dimensions. The rectangle can be filled or just outlined, depending on the `filled` argument. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Draw a filled rounded rectangle
img = ImageDrawRoundRect(myImage, 10, 20, 100, 50, 20, 20, true);

// Draw an outlined rounded rectangle
img = ImageDrawRoundRect(myImage, 10, 20, 100, 50, 20, 20);
```

## See Also

* ImageDrawRect
* ImageDrawOval

## Notes

* All arguments except `filled` are required.
* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The rectangle is drawn at (x, y) with the specified width, height, and corner arc dimensions.
