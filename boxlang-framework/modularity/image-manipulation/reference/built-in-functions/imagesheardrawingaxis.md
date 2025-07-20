# ImageShearDrawingAxis

## Syntax

```
ImageShearDrawingAxis( name, x, y )
```

Or as a member:

```
someImage.shearDrawingAxis( x, y )
```

## Arguments

| Name | Type    | Required | Default | Description                                                   |
| ---- | ------- | -------- | ------- | ------------------------------------------------------------- |
| name | any     | Yes      |         | The image to shear. Can be a `BoxImage` object or image name. |
| x    | numeric | Yes      | 0       | The shear amount along the x-axis.                            |
| y    | numeric | Yes      | 0       | The shear amount along the y-axis.                            |

## Returns

`BoxImage` — The sheared image object.

## Description

Applies a shear transformation to the specified image along custom axes. The `x` and `y` arguments control the amount of shear along the horizontal and vertical axes, respectively. Useful for advanced graphics effects and custom distortions.

## Example

```boxlang
// Shear image by 0.5 along x-axis and 0.2 along y-axis
result = ImageShearDrawingAxis( myImage, 0.5, 0.2 );

// As a member function
myImage.shearDrawingAxis( 0.3, 0.1 );
```

## Related BIFs

* ImageShear
* ImageRotateDrawingAxis
* ImageResize

## Notes

* The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
* The operation modifies the image in place when used as a member function.
* Returns the modified image object for chaining or further processing.
* The `x` and `y` arguments specify the shear amount along each axis.
