# ImageRotateDrawingAxis

## Syntax

```
ImageRotateDrawingAxis( name, angle [, x] [, y] )
```

Or as a member:

```
someImage.rotateDrawingAxis( angle [, x] [, y] )
```

## Arguments

| Name  | Type    | Required | Default | Description                                                    |
| ----- | ------- | -------- | ------- | -------------------------------------------------------------- |
| name  | any     | Yes      |         | The image to rotate. Can be a `BoxImage` object or image name. |
| angle | numeric | Yes      |         | The angle (in degrees) to rotate the image.                    |
| x     | numeric | No       | 0       | The x-coordinate of the rotation axis.                         |
| y     | numeric | No       | 0       | The y-coordinate of the rotation axis.                         |

## Returns

`BoxImage` — The rotated image object.

## Description

Rotates an image by the specified angle (in degrees) around a custom axis defined by the x and y coordinates. Useful for advanced graphics operations where rotation needs to occur around a specific point rather than the default center.

## Example

```boxlang
// Rotate image 90 degrees around axis (100, 50)
result = ImageRotateDrawingAxis( myImage, 90, 100, 50 );

// As a member function
myImage.rotateDrawingAxis( 45, 200, 100 );
```

## Related BIFs

* ImageRotate
* ImageResize
* ImageFlip

## Notes

* The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
* The operation modifies the image in place when used as a member function.
* Returns the modified image object for chaining or further processing.
* The x and y arguments specify the axis of rotation; defaults to (0, 0) if not provided.
