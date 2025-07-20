# ImageDrawLine

Draws a straight line on an image. This BIF allows you to specify the start and end points for the line in BoxLang.

## Syntax

```
ImageDrawLine(name, x1, y1, x2, y2)
```

## Arguments

| Name | Type    | Required | Description                                                             |
| ---- | ------- | -------- | ----------------------------------------------------------------------- |
| name | any     | Yes      | The image or the name of a variable referencing an image to operate on. |
| x1   | numeric | Yes      | The x coordinate of the start point of the line.                        |
| y1   | numeric | Yes      | The y coordinate of the start point of the line.                        |
| x2   | numeric | Yes      | The x coordinate of the end point of the line.                          |
| y2   | numeric | Yes      | The y coordinate of the end point of the line.                          |

## Returns

* **BoxImage**: The modified BoxImage instance with the line drawn.

## Description

`ImageDrawLine` draws a straight line on the specified image, using the provided start and end points. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Draw a line from (10, 20) to (100, 50)
img = ImageDrawLine(myImage, 10, 20, 100, 50);
```

## See Also

* ImageDrawCubicCurve
* ImageDrawQuadCurve

## Notes

* All arguments are required.
* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The line is drawn from (x1, y1) to (x2, y2).
