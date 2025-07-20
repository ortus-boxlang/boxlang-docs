# ImageDrawArc

Draws an arc on an image. This BIF allows you to specify the position, size, angles, and whether the arc is filled in BoxLang.

## Syntax

```
ImageDrawArc(name, x, y, width, height, startAngle, archAngle [, filled])
```

## Arguments

| Name       | Type    | Required | Default | Description                                                                      |
| ---------- | ------- | -------- | ------- | -------------------------------------------------------------------------------- |
| name       | any     | Yes      |         | The image or the name of a variable referencing an image to operate on.          |
| x          | numeric | Yes      |         | The x coordinate of the upper left corner of the bounding rectangle for the arc. |
| y          | numeric | Yes      |         | The y coordinate of the upper left corner of the bounding rectangle for the arc. |
| width      | numeric | Yes      |         | The width of the bounding rectangle for the arc.                                 |
| height     | numeric | Yes      |         | The height of the bounding rectangle for the arc.                                |
| startAngle | numeric | Yes      |         | The starting angle of the arc in degrees.                                        |
| archAngle  | numeric | Yes      |         | The angular extent of the arc in degrees.                                        |
| filled     | boolean | No       | false   | Whether the arc should be filled.                                                |

## Returns

* **BoxImage**: The modified BoxImage instance with the arc drawn.

## Description

`ImageDrawArc` draws an arc on the specified image, using the provided bounding rectangle, start angle, and angular extent. The arc can be filled or just outlined, depending on the `filled` argument. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Draw a filled arc
img = ImageDrawArc(myImage, 10, 20, 100, 50, 0, 180, true);

// Draw an outlined arc
img = ImageDrawArc(myImage, 10, 20, 100, 50, 45, 90);
```

## See Also

* ImageDrawRect
* ImageDrawEllipse

## Notes

* All arguments except `filled` are required.
* The image can be passed as a BoxImage object or as a variable name referencing an image.
* Angles are specified in degrees.
* The arc is drawn within the bounding rectangle defined by (x, y, width, height).
