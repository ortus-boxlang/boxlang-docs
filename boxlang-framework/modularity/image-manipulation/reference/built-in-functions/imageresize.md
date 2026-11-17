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
| width         | numeric | Yes      |          | The target width. Blank or `0` keeps the aspect ratio from `height`. |
| height        | numeric | Yes      |          | The target height. Blank or `0` keeps the aspect ratio from `width`. |
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

Any other value falls back to `bicubic`.

**Keeping the aspect ratio:** pass a blank string or `0` for one dimension, and it is computed from the other one so the image is not distorted. At least one of `width` or `height` must be given.

For proportional scaling that fits within a box, see `ImageScaleToFit`.

## Example

```boxlang
// Resize image to 200x100 using default interpolation and blur
result = ImageResize( myImage, 200, 100 );

// Resize with custom interpolation and blur factor
result = ImageResize( myImage, 400, 300, "nearest", 2 );

// As a member function
myImage.resize( 800, 600, "bilinear", 1 );

// 800 pixels wide, height keeps the aspect ratio
myImage.resize( 800, "" )

// 300 pixels high, width keeps the aspect ratio
ImageResize( myImage, 0, 300 )
```

## Related BIFs

* ImageCrop
* ImageFlip
* ImageGrayScale

## Notes

* The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
* Supported interpolation methods: nearest, bilinear, bicubic
* The operation modifies the image in place when used as a member function.
* Returns the modified image object for chaining or further processing.
* For proportional scaling within a box, use `ImageScaleToFit` instead.
* Passing neither a width nor a height throws an error.
* An image read from SVG is scaled as pixels. To get it sharp at a new size, read it at that size with `ImageRead( path, width, height )`.
* The blur factor controls smoothing during resize (higher = more blur).
