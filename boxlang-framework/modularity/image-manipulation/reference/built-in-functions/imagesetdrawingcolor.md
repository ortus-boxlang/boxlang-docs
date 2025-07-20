# ImageSetDrawingColor

## Syntax

```
ImageSetDrawingColor( name, color )
```

Or as a member:

```
someImage.setDrawingColor( color )
```

## Arguments

| Name  | Type   | Required | Description                                                                       |
| ----- | ------ | -------- | --------------------------------------------------------------------------------- |
| name  | any    | Yes      | The image to set the drawing color for. Can be a `BoxImage` object or image name. |
| color | String | Yes      | The drawing color to set (e.g., "red", "#0000FF").                                |

## Returns

`BoxImage` — The image object with updated drawing color.

## Description

Sets the drawing color for the specified image. This color will be used for subsequent drawing operations such as lines, shapes, and text.

## Example

```boxlang
// Set drawing color to blue
result = ImageSetDrawingColor( myImage, "blue" );

// Set drawing color using hex value
result = ImageSetDrawingColor( myImage, "#FF00FF" );

// As a member function
myImage.setDrawingColor( "green" );
```

## Related BIFs

* ImageSetBackgroundColor
* ImageDrawLine
* ImageDrawText

## Notes

* The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
* The operation modifies the image in place when used as a member function.
* Returns the modified image object for chaining or further processing.
* The `color` argument accepts named colors or hex color codes.
