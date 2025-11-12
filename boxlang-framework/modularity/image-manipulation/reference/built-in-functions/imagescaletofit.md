# ImageScaleToFit

## Syntax

```
ImageScaleToFit( name, size [, interpolation] )
ImageScaleToFit( name, width, height [, interpolation] )
```

Or as a member:

```
someImage.scaleToFit( size [, interpolation] )
someImage.scaleToFit( width, height [, interpolation] )
```

## Arguments

| Name          | Type   | Required | Default  | Description                                                                                          |
| ------------- | ------ | -------- | -------- | ---------------------------------------------------------------------------------------------------- |
| name          | any    | Yes      |          | The image to scale. Can be a `BoxImage` object or image name.                                        |
| size          | any    | Yes*     |          | Single dimension to fit. Scales to fit this width while maintaining aspect ratio.                    |
| width         | any    | Yes*     |          | Maximum width. Image fits within these dimensions maintaining aspect ratio.                          |
| height        | any    | Yes*     |          | Maximum height. Image fits within these dimensions maintaining aspect ratio.                         |
| interpolation | String | No       | bilinear | The interpolation method: "bilinear" (default), "nearest", "bicubic".                                |

\* Either provide a single `size` parameter OR both `width` and `height` parameters.

## Returns

`BoxImage` — The scaled image object.

## Description

Scales an image to fit within specified dimensions while maintaining the aspect ratio. This function is intelligent about sizing:

- **Single parameter**: Fits the image to the specified width, maintaining aspect ratio
- **Two parameters (width, height)**: Fits the image within a rectangular boundary, maintaining aspect ratio (the image will be as large as possible without exceeding either dimension)

The image is never stretched or distorted - aspect ratio is always preserved.

## Example

```boxlang
// Scale image to fit width 400 (height adjusts automatically)
result = ImageScaleToFit( myImage, 400 );

// Scale image to fit within 800x600 bounds
result = ImageScaleToFit( myImage, 800, 600 );

// Scale with custom interpolation
result = ImageScaleToFit( myImage, 400, "bicubic" );

// As a member function (recommended)
myImage.scaleToFit( 600 );
myImage.scaleToFit( 800, 600, "bilinear" );
```

## Interpolation Methods

- `bilinear` - Good balance of speed and quality (default)
- `nearest` - Fastest, lowest quality (pixelated)
- `bicubic` - Highest quality, slowest

## Related BIFs

- ImageResize
- ImageCrop
- ImageRotate

## Notes

- The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
- The aspect ratio is always preserved - the image is never stretched or distorted.
- For a 500x300 image calling `scaleToFit(400, 600)`: result is 400x240 (width constrained)
- For a 300x500 image calling `scaleToFit(400, 600)`: result is 360x600 (height constrained)
- The operation modifies the image in place when used as a member function.
- Returns the modified image object for chaining or further processing.
