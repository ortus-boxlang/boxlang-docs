# ImageSetDrawingGradient

## Syntax

```
ImageSetDrawingGradient( name, x1, y1, x2, y2, colors [, fractions] )
```

Or as a member:

```
someImage.setDrawingGradient( x1, y1, x2, y2, colors [, fractions] )
```

## Arguments

| Name      | Type    | Required | Description                                                                                                         |
| --------- | ------- | -------- | ------------------------------------------------------------------------------------------------------------------- |
| name      | any     | Yes      | The image to set the gradient on. Can be a `BoxImage` object or image name.                                         |
| x1        | numeric | Yes      | X coordinate of the gradient start point.                                                                           |
| y1        | numeric | Yes      | Y coordinate of the gradient start point.                                                                           |
| x2        | numeric | Yes      | X coordinate of the gradient end point.                                                                             |
| y2        | numeric | Yes      | Y coordinate of the gradient end point.                                                                             |
| colors    | array   | Yes      | Two or more color names or hex codes (`##RGB`, `##RRGGBB`, `##RRGGBBAA`).                                           |
| fractions | array   | No       | Stop positions from 0 to 1, strictly increasing, one per color. Defaults to evenly spaced.                          |

## Returns

`BoxImage` — The image, for chaining.

## Description

Sets a linear gradient as the paint for subsequent drawing. Every operation that paints uses it: filled shapes (`drawRect`, `drawOval`, `drawRoundRect`, `drawArc`, `drawLines`), stroked outlines and rings (using the current stroke width), lines and `drawText`. The gradient is defined in image coordinates, so the same start and end points apply to everything you draw until you change it.

Call `setDrawingColor` to go back to a solid color.

## Errors

A `BoxRuntimeException` is thrown for fewer than two colors, an unparseable color, identical start and end points, a `fractions` array whose length differs from `colors`, or fractions outside 0 to 1 or not strictly increasing.

## Example

```boxlang
img = ImageNew( "", 1200, 630, "rgb", "##0b161b" );

// left-to-right accent bar
img.setDrawingGradient( 0, 0, 1200, 0, [ "##ff6a00", "##ee0979" ] );
img.drawRect( 0, 600, 1200, 30, true );

// ring with a gradient stroke
img.setDrawingStroke( { width: 8 } );
img.drawOval( 900, 100, 200, 200, false );

// gradient text
img.drawText( "Hello", 80, 300, { size: 96, style: "bold" } );

// three stops
img.setDrawingGradient( 0, 0, 0, 630, [ "##ffffff", "##3366ff", "##000000" ], [ 0, 0.3, 1 ] );

// back to solid
img.setDrawingColor( "white" );
```

## Related BIFs

* ImageSetDrawingColor
* ImageSetDrawingStroke
* ImageDrawText

## Notes

* `drawBeveledRect` derives its highlight and shadow from the solid drawing color.
* The gradient is kept when an operation rebuilds the image canvas (for example `resize`), but its coordinates are not rescaled.
