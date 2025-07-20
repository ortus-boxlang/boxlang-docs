# ImageSharpen

## Syntax

```
ImageSharpen( name [, gain] )
```

Or as a member:

```
someImage.sharpen( [gain] )
```

## Arguments

| Name | Type    | Required | Default | Description                                                     |
| ---- | ------- | -------- | ------- | --------------------------------------------------------------- |
| name | any     | Yes      |         | The image to sharpen. Can be a `BoxImage` object or image name. |
| gain | numeric | No       | 1       | The sharpening gain factor. Higher values increase sharpness.   |

## Returns

`BoxImage` — The sharpened image object.

## Description

Applies a sharpening filter to the specified image. The `gain` argument controls the intensity of the sharpening effect. Useful for enhancing image details and improving clarity.

## Example

```boxlang
// Sharpen image with default gain
result = ImageSharpen( myImage );

// Sharpen image with custom gain
result = ImageSharpen( myImage, 2.5 );

// As a member function
myImage.sharpen( 1.5 );
```

## Related BIFs

* ImageBlur
* ImageGrayScale
* ImageResize

## Notes

* The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
* The operation modifies the image in place when used as a member function.
* Returns the modified image object for chaining or further processing.
* The `gain` argument should be a positive number; higher values produce a stronger sharpening effect.
