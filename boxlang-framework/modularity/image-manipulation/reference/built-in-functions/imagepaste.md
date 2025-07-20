# ImagePaste

## Syntax

```
ImagePaste( image1, image2 [, x] [, y] )
ImageDrawImage( image1, image2 [, x] [, y] )
```

Or as a member:

```
someImage.paste( imageToDraw [, x] [, y] )
someImage.drawImage( imageToDraw [, x] [, y] )
```

## Arguments

| Name   | Type    | Required | Default | Description                                                             |
| ------ | ------- | -------- | ------- | ----------------------------------------------------------------------- |
| image1 | any     | Yes      |         | The base image to paste onto. Can be a `BoxImage` object or image name. |
| image2 | any     | Yes      |         | The image to paste. Can be a `BoxImage` object or image name.           |
| x      | numeric | No       | 0       | The x-coordinate where the image will be pasted.                        |
| y      | numeric | No       | 0       | The y-coordinate where the image will be pasted.                        |

## Returns

`BoxImage` — The base image with the pasted image applied.

## Description

Pastes one image (`image2`) onto another (`image1`) at the specified coordinates. Useful for combining images, adding watermarks, or overlaying graphics at precise locations.

## Example

```boxlang
// Paste image2 onto image1 at (100, 50)
result = ImagePaste( image1, image2, 100, 50 );

// Using the alias
result = ImageDrawImage( image1, image2, 200, 75 );

// As a member function
image1.paste( image2, 10, 10 );
image1.drawImage( image2, 0, 0 );
```

## Related BIFs

* ImageOverlay
* ImageCopy
* ImageNew

## Notes

* Both `image1` and `image2` can be `BoxImage` objects or the names of images in the current context.
* The default coordinates are (0, 0) if not specified.
* The operation modifies the base image in place when used as a member function.
* Returns the modified image object for chaining or further processing.
* This BIF is also available as `ImageDrawImage` and as member functions `paste` and `drawImage`.
