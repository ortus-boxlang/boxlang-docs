# ImageSetDrawingTransparency

## Syntax

```
ImageSetDrawingTransparency( name, percent )
```

Or as a member:

```
someImage.setDrawingTransparency( percent )
```

## Arguments

| Name    | Type    | Required | Description                                                                          |
| ------- | ------- | -------- | ------------------------------------------------------------------------------------ |
| name    | any     | Yes      | The image to set drawing transparency for. Can be a `BoxImage` object or image name. |
| percent | numeric | Yes      | The transparency percentage (0-100) for drawing operations.                          |

## Returns

`BoxImage` — The image object with updated drawing transparency.

## Description

Sets the drawing transparency for the specified image. This affects the opacity of subsequent drawing operations (lines, shapes, text) on the image. A value of 0 is fully transparent, 100 is fully opaque.

## Example

```boxlang
// Set drawing transparency to 50%
result = ImageSetDrawingTransparency( myImage, 50 );

// As a member function
myImage.setDrawingTransparency( 75 );
```

## Related BIFs

* ImageSetDrawingColor
* ImageSetDrawingStroke
* ImageDrawText

## Notes

* The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
* The operation modifies the image in place when used as a member function.
* Returns the modified image object for chaining or further processing.
* The `percent` argument should be between 0 and 100.
