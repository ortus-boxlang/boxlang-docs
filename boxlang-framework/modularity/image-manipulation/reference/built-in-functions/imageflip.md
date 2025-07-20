# ImageFlip

Flips or transposes an image. This BIF allows you to specify the type of flip or transpose operation to apply in BoxLang.

## Syntax

```
ImageFlip(name, transpose)
```

## Arguments

| Name      | Type   | Required | Description                                                                                                     |
| --------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------- |
| name      | any    | Yes      | The image or the name of a variable referencing an image to operate on.                                         |
| transpose | string | Yes      | The type of flip or transpose operation (e.g., "horizontal", "vertical", "rotate90", "rotate180", "rotate270"). |

## Returns

* **BoxImage**: The modified BoxImage instance after the flip or transpose operation.

## Description

`ImageFlip` flips or transposes the specified image according to the given operation. Supported values for `transpose` typically include:

* `horizontal`: Flip the image horizontally (mirror left/right)
* `vertical`: Flip the image vertically (mirror top/bottom)
* `rotate90`: Rotate the image 90 degrees
* `rotate180`: Rotate the image 180 degrees
* `rotate270`: Rotate the image 270 degrees

The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Flip an image horizontally
img = ImageFlip(myImage, "horizontal");

// Rotate an image 90 degrees
img = ImageFlip(myImage, "rotate90");
```

## See Also

* ImageRotate
* ImageCrop

## Notes

* All arguments are required.
* The image can be passed as a BoxImage object or as a variable name referencing an image.
* Supported transpose values may vary depending on implementation.
