# ImageOverlay

## Syntax

```
ImageOverlay( image1, image2 [, rule] [, transparency] )
```

Or as a member:

```
someImage.overlay( imageToDraw [, rule] [, transparency] )
```

## Arguments

| Name         | Type    | Required | Default   | Description                                                                     |
| ------------ | ------- | -------- | --------- | ------------------------------------------------------------------------------- |
| image1       | any     | Yes      |           | The base image to overlay onto. Can be a `BoxImage` object or image name.       |
| image2       | any     | Yes      |           | The image to overlay. Can be a `BoxImage` object or image name.                 |
| rule         | string  | No       | SRC\_OVER | The compositing rule for overlay (e.g., "SRC\_OVER", "SRC\_ATOP").              |
| transparency | numeric | No       | 0.25      | The transparency level for the overlay (0.0 = fully transparent, 1.0 = opaque). |

## Returns

`BoxImage` — The base image with the overlay applied.

## Description

Overlays one image (`image2`) onto another (`image1`) using the specified compositing rule and transparency. This allows for blending images with various effects, such as watermarking or combining graphics.

## Example

```boxlang
// Overlay image2 onto image1 with default rule and transparency
result = ImageOverlay( image1, image2 );

// Overlay with custom rule and transparency
result = ImageOverlay( image1, image2, "SRC_ATOP", 0.5 );

// As a member function
image1.overlay( image2, "SRC_OVER", 0.75 );
```

## Related BIFs

* ImageCopy
* ImageDrawImage
* ImageNew

## Notes

* Both `image1` and `image2` can be `BoxImage` objects or the names of images in the current context.
* The `rule` argument determines how the overlay is composited. Common values include "SRC\_OVER" and "SRC\_ATOP".
* The operation modifies the base image in place when used as a member function.
* Returns the modified image object for chaining or further processing.
