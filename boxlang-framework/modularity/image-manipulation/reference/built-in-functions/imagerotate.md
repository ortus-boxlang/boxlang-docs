# ImageRotate

## Syntax

```
ImageRotate( name, angle )
```

Or as a member:

```
someImage.rotate( angle )
```

## Arguments

| Name  | Type    | Required | Description                                                    |
| ----- | ------- | -------- | -------------------------------------------------------------- |
| name  | any     | Yes      | The image to rotate. Can be a `BoxImage` object or image name. |
| angle | numeric | Yes      | The angle (in degrees) to rotate the image.                    |

## Returns

`BoxImage` — The rotated image object.

## Description

Rotates an image by the specified angle (in degrees). Positive values rotate clockwise, negative values rotate counterclockwise. Useful for correcting orientation or creating rotated graphics.

## Example

```boxlang
// Rotate image 90 degrees clockwise
result = ImageRotate( myImage, 90 );

// Rotate image 45 degrees counterclockwise
result = ImageRotate( myImage, -45 );

// As a member function
myImage.rotate( 180 );
```

## Related BIFs

* ImageResize
* ImageFlip
* ImageCrop

## Notes

* The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
* The operation modifies the image in place when used as a member function.
* Returns the modified image object for chaining or further processing.
* Only the `angle` argument is supported; x and y arguments are not implemented.
* Positive angles rotate clockwise, negative angles rotate counterclockwise.
* The image dimensions may change after rotation (except for 90° increments).
* For simple 90°, 180°, 270° rotations, consider using `ImageFlip()` with transpose values.
