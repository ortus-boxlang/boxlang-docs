# ImageDrawPoint

Draws a single point on an image. This BIF allows you to specify the position of the point in BoxLang.

## Syntax

```
ImageDrawPoint(name, x, y)
```

## Arguments

| Name | Type    | Required | Description                                                             |
| ---- | ------- | -------- | ----------------------------------------------------------------------- |
| name | any     | Yes      | The image or the name of a variable referencing an image to operate on. |
| x    | numeric | Yes      | The x coordinate of the point.                                          |
| y    | numeric | Yes      | The y coordinate of the point.                                          |

## Returns

* **BoxImage**: The modified BoxImage instance with the point drawn.

## Description

`ImageDrawPoint` draws a single point on the specified image at the given (x, y) coordinates. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Draw a point at (10, 20)
img = ImageDrawPoint(myImage, 10, 20);
```

## See Also

* ImageDrawLine
* ImageDrawRect

## Notes

* All arguments are required.
* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The point is drawn as a 1x1 filled rectangle at (x, y).
