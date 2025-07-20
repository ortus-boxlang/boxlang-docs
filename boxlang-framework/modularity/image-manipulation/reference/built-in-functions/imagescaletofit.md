# ImageScaleToFit

## Syntax

```
ImageScaleToFit( name, width [, height] [, interpolation] )
```

Or as a member:

```
someImage.scaleToFit( width [, height] [, interpolation] )
```

## Arguments

| Name          | Type   | Required | Default  | Description                                                            |
| ------------- | ------ | -------- | -------- | ---------------------------------------------------------------------- |
| name          | any    | Yes      |          | The image to scale. Can be a `BoxImage` object or image name.          |
| width         | any    | Yes      |          | The target width for scaling.                                          |
| height        | any    | No       |          | The target height for scaling (optional; if omitted, scales by width). |
| interpolation | String | No       | bilinear | The interpolation method (e.g., "bilinear", "nearest").                |

## Returns

`BoxImage` — The scaled image object.

## Description

Scales an image to fit the specified width or height, maintaining the aspect ratio. If both width and height are provided, width takes precedence. The interpolation method controls the quality of scaling.

## Example

```boxlang
// Scale image to fit width 400
result = ImageScaleToFit( myImage, 400 );

// Scale image to fit height 300
result = ImageScaleToFit( myImage, null, 300 );

// Scale with custom interpolation
result = ImageScaleToFit( myImage, 800, null, "nearest" );

// As a member function
myImage.scaleToFit( 600, null, "bilinear" );
```

## Related BIFs

* ImageResize
* ImageCrop
* ImageRotate

## Notes

* The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
* If both width and height are provided, width is used for scaling.
* Supported interpolation methods may include "bilinear", "nearest", and others.
* The operation modifies the image in place when used as a member function.
* Returns the modified image object for chaining or further processing.
