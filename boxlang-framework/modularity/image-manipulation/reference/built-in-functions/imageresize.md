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

Resizes an image to the specified width and height using the chosen interpolation method and blur factor. This function allows precise control over resizing quality and is useful for scaling images up or down while maintaining visual quality.

**Interpolation Methods:**

* `nearest` - Fastest but lowest quality (blocky/pixelated)
* `bilinear` - Good balance of speed and quality (default)
* `bicubic` - Higher quality, slower than bilinear
* `highestPerformance` - Optimized for speed
* `highestQuality` - Best quality, slowest performance

For proportional scaling that maintains aspect ratio, see `ImageScaleToFit`.

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
* Supported interpolation methods: nearest, bilinear, bicubic, highestPerformance, highestQuality
* The operation modifies the image in place when used as a member function.
* Returns the modified image object for chaining or further processing.
* For proportional scaling, use `ImageScaleToFit` instead.
* The blur factor controls smoothing during resize (higher = more blur).
