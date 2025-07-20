# ImageDrawOval

Draws an oval (ellipse) on an image. This BIF allows you to specify the position, size, and whether the oval is filled in BoxLang.

## Syntax

```
ImageDrawOval(name, x, y, width, height [, filled])
```

## Arguments

| Name   | Type    | Required | Default | Description                                                                       |
| ------ | ------- | -------- | ------- | --------------------------------------------------------------------------------- |
| name   | any     | Yes      |         | The image or the name of a variable referencing an image to operate on.           |
| x      | numeric | Yes      |         | The x coordinate of the upper left corner of the bounding rectangle for the oval. |
| y      | numeric | Yes      |         | The y coordinate of the upper left corner of the bounding rectangle for the oval. |
| width  | numeric | Yes      |         | The width of the bounding rectangle for the oval.                                 |
| height | numeric | Yes      |         | The height of the bounding rectangle for the oval.                                |
| filled | boolean | No       | false   | Whether the oval should be filled.                                                |

## Returns

* **BoxImage**: The modified BoxImage instance with the oval drawn.

## Description

`ImageDrawOval` draws an oval (ellipse) on the specified image, using the provided bounding rectangle. The oval can be filled or just outlined, depending on the `filled` argument. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Draw a filled oval
img = ImageDrawOval(myImage, 10, 20, 100, 50, true);

// Draw an outlined oval
img = ImageDrawOval(myImage, 10, 20, 100, 50);
```

## See Also

* ImageDrawRect
* ImageDrawArc

## Notes

* All arguments except `filled` are required.
* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The oval is drawn within the bounding rectangle defined by (x, y, width, height).
