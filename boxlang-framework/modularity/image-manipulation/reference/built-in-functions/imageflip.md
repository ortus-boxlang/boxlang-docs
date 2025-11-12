# ImageFlip

Flips or transposes an image along various axes.

## Syntax

```
ImageFlip( name, transpose )
```

Or as a member:

```
someImage.flip( transpose )
```

## Arguments

| Name      | Type   | Required | Description                                                                              |
| --------- | ------ | -------- | ---------------------------------------------------------------------------------------- |
| name      | any    | Yes      | The image or the name of a variable referencing an image to operate on.                  |
| transpose | string | Yes      | The type of flip or transpose operation. Valid values: See below.                        |

## Returns

**BoxImage**: The modified BoxImage instance after the flip or transpose operation.

## Description

`ImageFlip` flips or transposes the specified image according to the given operation. This function supports both simple flips (mirror operations) and more complex transpose operations including rotations.

### Valid Transpose Values

- `horizontal` - Flip the image horizontally (mirror left/right)
- `vertical` - Flip the image vertically (mirror top/bottom)
- `diagonal` - Transpose along the main diagonal (top-left to bottom-right)
- `antidiagonal` - Transpose along the anti-diagonal (top-right to bottom-left)
- `90` - Rotate 90 degrees clockwise
- `180` - Rotate 180 degrees
- `270` - Rotate 270 degrees clockwise (same as 90 degrees counter-clockwise)

## Example

```boxlang
// Flip an image horizontally (mirror)
img = ImageFlip( myImage, "horizontal" );

// Flip vertically
img = ImageFlip( myImage, "vertical" );

// Rotate 90 degrees clockwise
img = ImageFlip( myImage, "90" );

// Transpose along diagonal
img = ImageFlip( myImage, "diagonal" );

// As a member function (chainable)
myImage.flip("horizontal")
       .flip("vertical");  // Results in 180-degree rotation
```

## Use Cases

- **horizontal**: Create mirror images for design purposes
- **vertical**: Flip images upside down
- **90, 180, 270**: Rotate images without quality loss
- **diagonal/antidiagonal**: Advanced image transformations for effects

## Related BIFs

- ImageRotate
- ImageCrop
- ImageResize

## Notes

- All arguments are required.
- The image can be passed as a BoxImage object or as a variable name referencing an image.
- The operation modifies the image in place when used as a member function.
- Returns the modified image object for chaining or further processing.
- Invalid transpose values will throw a validation error.
