# ImageDrawLines

Draws multiple connected lines or a polygon on an image. This BIF allows you to specify arrays of x and y coordinates, and optionally draw a filled polygon in BoxLang.

## Syntax

```
ImageDrawLines(name, xCoords, yCoords [, isPolygon] [, filled])
```

## Arguments

| Name      | Type    | Required | Default | Description                                                             |
| --------- | ------- | -------- | ------- | ----------------------------------------------------------------------- |
| name      | any     | Yes      |         | The image or the name of a variable referencing an image to operate on. |
| xCoords   | array   | Yes      |         | Array of x coordinates for the points.                                  |
| yCoords   | array   | Yes      |         | Array of y coordinates for the points.                                  |
| isPolygon | boolean | No       | false   | If true, draws a closed polygon; if false, draws open lines.            |
| filled    | boolean | No       | false   | If true and isPolygon is true, fills the polygon.                       |

## Returns

* **BoxImage**: The modified BoxImage instance with the lines or polygon drawn.

## Description

`ImageDrawLines` draws a series of connected lines on the specified image, using the provided arrays of x and y coordinates. If `isPolygon` is true, the lines are closed to form a polygon, which can be filled if `filled` is also true. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Draw open lines connecting points
img = ImageDrawLines(myImage, [10, 50, 100], [20, 60, 80]);

// Draw a filled triangle
img = ImageDrawLines(myImage, [10, 50, 100], [20, 60, 80], true, true);
```

## See Also

* ImageDrawLine
* ImageDrawPolygon

## Notes

* The xCoords and yCoords arrays must be of equal length.
* The image can be passed as a BoxImage object or as a variable name referencing an image.
* If `isPolygon` is true and `filled` is true, the polygon will be filled.
