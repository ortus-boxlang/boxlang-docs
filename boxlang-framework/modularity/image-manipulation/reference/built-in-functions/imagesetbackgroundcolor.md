# ImageSetBackgroundColor

## Syntax

```
ImageSetBackgroundColor( name, color )
```

Or as a member:

```
someImage.setBackgroundColor( color )
```

## Arguments

| Name  | Type   | Required | Description                                                                          |
| ----- | ------ | -------- | ------------------------------------------------------------------------------------ |
| name  | any    | Yes      | The image to set the background color for. Can be a `BoxImage` object or image name. |
| color | String | Yes      | The background color to set (e.g., "white", "#FF0000").                              |

## Returns

`BoxImage` — The image object with updated background color.

## Description

Sets the background color of the specified image. Useful for preparing images for compositing, overlays, or ensuring a consistent background before further processing.

## Example

```boxlang
// Set background color to white
result = ImageSetBackgroundColor( myImage, "white" );

// Set background color using hex value
result = ImageSetBackgroundColor( myImage, "#00FF00" );

// As a member function
myImage.setBackgroundColor( "black" );
```

## Related BIFs

* ImageSetAntiAliasing
* ImageDrawRect
* ImageNew

## Notes

* The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
* The operation modifies the image in place when used as a member function.
* Returns the modified image object for chaining or further processing.
* The `color` argument accepts named colors or hex color codes.
