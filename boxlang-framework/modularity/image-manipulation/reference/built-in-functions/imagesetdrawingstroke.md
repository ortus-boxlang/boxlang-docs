# ImageSetDrawingStroke

Sets the stroke properties for subsequent drawing operations on an image.

## Syntax

```
ImageSetDrawingStroke( name [, attributeCollection] )
```

Or as a member:

```
someImage.setDrawingStroke( [attributeCollection] )
```

## Arguments

| Name                | Type   | Required | Description                                                                        |
| ------------------- | ------ | -------- | ---------------------------------------------------------------------------------- |
| name                | any    | Yes      | The image to set the drawing stroke for. Can be a `BoxImage` object or image name. |
| attributeCollection | struct | No       | A struct of stroke attributes. See below for supported keys.                       |

## Returns

`BoxImage` — The image object with updated drawing stroke settings.

## Description

Sets the drawing stroke attributes for the specified image. Stroke attributes control how lines and shapes are drawn, including thickness, end cap style, line join style, and dash patterns.

## Attribute Collection Keys

The `attributeCollection` struct supports the following optional keys:

| Key          | Type  | Description                                                                                                           | Valid Values                          |
| ------------ | ----- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| width        | float | The stroke width in pixels. Controls the thickness of lines and shape outlines.                                       | Any positive number (e.g., 2.5)       |
| endCaps      | string | The end cap style for unclosed subpaths and dash segments.                                                            | "butt", "round", "square"             |
| lineJoins    | string | The line join style for path segment intersections.                                                                   | "miter", "round", "bevel"             |
| miterLimit   | float | The miter limit for mitered line joins. Controls when a miter join is replaced with a bevel join.                     | Any positive number (e.g., 10.0)      |
| dashArray    | array | An array of floats defining the dash pattern. Alternating values represent lengths of opaque and transparent segments. | Array of floats (e.g., [10, 5, 2, 5]) |
| dashPhase    | float | The offset to start the dash pattern. Controls where in the dash pattern to begin.                                    | Any number (e.g., 0.0)                |

### End Cap Styles

- `butt` - Ends with no added decoration (square end at the endpoint)
- `round` - Ends with a round decoration (semicircle beyond the endpoint)
- `square` - Ends with a square projection (square beyond the endpoint)

### Line Join Styles

- `miter` - Joins segments by extending outer edges until they meet
- `round` - Joins segments by rounding off the corner
- `bevel` - Joins segments by connecting outer corners with a straight segment

## Example

```boxlang
// Set basic stroke width
ImageSetDrawingStroke( myImage, { width: 3.0 } );

// Set width and end cap style
ImageSetDrawingStroke( myImage, { width: 5.0, endCaps: "round" } );

// Create a dashed line
ImageSetDrawingStroke( myImage, {
    width: 2.0,
    dashArray: [10, 5],
    dashPhase: 0
} );

// Full configuration
ImageSetDrawingStroke( myImage, {
    width: 4.0,
    endCaps: "round",
    lineJoins: "miter",
    miterLimit: 10.0,
    dashArray: [15, 5, 5, 5],
    dashPhase: 0
} );

// As a member function (chainable)
myImage.setDrawingStroke({ width: 2 })
       .drawLine(0, 0, 100, 100)
       .setDrawingStroke({ width: 4, dashArray: [5, 5] })
       .drawRect(50, 50, 100, 100, false);
```

## Related BIFs

- ImageSetDrawingColor
- ImageDrawLine
- ImageDrawRect
- ImageDrawOval
- ImageSetAntiAliasing

## Notes

- The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
- All attributes in the `attributeCollection` are optional - only provide the ones you want to change.
- If an attribute is not provided, the corresponding stroke property remains unchanged from its current value.
- The operation modifies the image in place when used as a member function.
- Returns the modified image object for chaining or further processing.
- Default values: `width=1.0`, `endCaps="round"`, `lineJoins="bevel"`
- The stroke settings affect all subsequent drawing operations until changed again.
