# ImageSetAntiAliasing

## Syntax

```
ImageSetAntiAliasing( name [, antialias] )
```

Or as a member:

```
someImage.setAntiAliasing( [antialias] )
```

## Arguments

| Name      | Type    | Required | Default | Description                                                                   |
| --------- | ------- | -------- | ------- | ----------------------------------------------------------------------------- |
| name      | any     | Yes      |         | The image to set anti-aliasing for. Can be a `BoxImage` object or image name. |
| antialias | boolean | No       | true    | Whether to enable (true) or disable (false) anti-aliasing.                    |

## Returns

`BoxImage` — The image object with updated anti-aliasing setting.

## Description

Enables or disables anti-aliasing for the specified image. Anti-aliasing smooths the edges of graphics and text, improving visual quality when drawing or transforming images.

## Example

```boxlang
// Enable anti-aliasing
result = ImageSetAntiAliasing( myImage, true );

// Disable anti-aliasing
result = ImageSetAntiAliasing( myImage, false );

// As a member function
myImage.setAntiAliasing( true );
```

## Related BIFs

* ImageDrawText
* ImageDrawLine
* ImageResize

## Notes

* The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
* The operation modifies the image in place when used as a member function.
* Returns the modified image object for chaining or further processing.
* Anti-aliasing is recommended for smoother graphics and text rendering.
