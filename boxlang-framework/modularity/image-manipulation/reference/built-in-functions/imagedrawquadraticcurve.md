# ImageDrawQuadraticCurve

Draws a quadratic Bézier curve on an image. This BIF allows you to specify the control point, start point, and end point for the curve in BoxLang.

## Syntax

```
ImageDrawQuadraticCurve(name, ctrlx1, ctrly1, x1, y1, x2, y2)
```

## Arguments

| Name   | Type    | Required | Description                                                             |
| ------ | ------- | -------- | ----------------------------------------------------------------------- |
| name   | any     | Yes      | The image or the name of a variable referencing an image to operate on. |
| ctrlx1 | numeric | Yes      | The x coordinate of the control point.                                  |
| ctrly1 | numeric | Yes      | The y coordinate of the control point.                                  |
| x1     | numeric | Yes      | The x coordinate of the start point of the curve.                       |
| y1     | numeric | Yes      | The y coordinate of the start point of the curve.                       |
| x2     | numeric | Yes      | The x coordinate of the end point of the curve.                         |
| y2     | numeric | Yes      | The y coordinate of the end point of the curve.                         |

## Returns

* **BoxImage**: The modified BoxImage instance with the quadratic curve drawn.

## Description

`ImageDrawQuadraticCurve` draws a quadratic Bézier curve on the specified image, using the provided control point, start point, and end point. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Draw a quadratic Bézier curve
img = ImageDrawQuadraticCurve(myImage, 30, 40, 10, 20, 70, 80);
```

## See Also

* ImageDrawCubicCurve
* ImageDrawLine

## Notes

* All arguments are required.
* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The curve is defined by the control point (ctrlx1, ctrly1), start point (x1, y1), and end point (x2, y2).
