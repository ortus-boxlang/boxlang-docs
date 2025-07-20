# ImageDrawCubicCurve

Draws a cubic Bézier curve on an image. This BIF allows you to specify the start point, two control points, and the end point for the curve in BoxLang.

## Syntax

```
ImageDrawCubicCurve(name, x1, y1, ctrlx1, ctrly1, ctrlx2, ctrly2, x2, y2)
```

## Arguments

| Name   | Type    | Required | Description                                                             |
| ------ | ------- | -------- | ----------------------------------------------------------------------- |
| name   | any     | Yes      | The image or the name of a variable referencing an image to operate on. |
| x1     | numeric | Yes      | The x coordinate of the start point of the curve.                       |
| y1     | numeric | Yes      | The y coordinate of the start point of the curve.                       |
| ctrlx1 | numeric | Yes      | The x coordinate of the first control point.                            |
| ctrly1 | numeric | Yes      | The y coordinate of the first control point.                            |
| ctrlx2 | numeric | Yes      | The x coordinate of the second control point.                           |
| ctrly2 | numeric | Yes      | The y coordinate of the second control point.                           |
| x2     | numeric | Yes      | The x coordinate of the end point of the curve.                         |
| y2     | numeric | Yes      | The y coordinate of the end point of the curve.                         |

## Returns

* **BoxImage**: The modified BoxImage instance with the cubic curve drawn.

## Description

`ImageDrawCubicCurve` draws a cubic Bézier curve on the specified image, using the provided start point, two control points, and end point. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Draw a cubic Bézier curve
img = ImageDrawCubicCurve(myImage, 10, 20, 30, 40, 50, 60, 70, 80);
```

## See Also

* ImageDrawQuadCurve
* ImageDrawLine

## Notes

* All arguments are required.
* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The curve is defined by the start point (x1, y1), control points (ctrlx1, ctrly1) and (ctrlx2, ctrly2), and end point (x2, y2).
