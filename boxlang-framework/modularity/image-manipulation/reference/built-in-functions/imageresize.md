# ImageResize

## Syntax

```
ImageResize( name, width, height [, interpolation] [, blurFactor] )
```

Or as a member:

```
someImage.resize( width, height [, interpolation] [, blurFactor] )
```

## Arguments

| Name          | Type    | Required | Default  | Description                                                    |
| ------------- | ------- | -------- | -------- | -------------------------------------------------------------- |
| name          | any     | Yes      |          | The image to resize. Can be a `BoxImage` object or image name. |
| width         | numeric | Yes      |          | The target width for the resized image.                        |
| height        | numeric | Yes      |          | The target height for the resized image.                       |
| interpolation | String  | No       | bilinear | The interpolation method (e.g., "bilinear", "nearest").        |
| blurFactor    | numeric | No       | 1        | The blur factor to apply during resizing.                      |

## Returns

`BoxImage` — The resized image object.

## Description

Resizes an image to the specified width and height using the chosen interpolation method and blur factor. Useful for scaling images up or down while controlling quality and smoothing.

## Example

```boxlang
// Resize image to 200x100 using default interpolation and blur
result = ImageResize( myImage, 200, 100 );

// Resize with custom interpolation and blur factor
result = ImageResize( myImage, 400, 300, "nearest", 2 );

// As a member function
myImage.resize( 800, 600, "bilinear", 1 );
```

## Related BIFs

* ImageCrop
* ImageFlip
* ImageGrayScale

## Notes

* The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
* Supported interpolation methods may include "bilinear", "nearest", and others.
* The operation modifies the image in place when used as a member function.
* Returns the modified image object for chaining or further processing.
