# ImageBlur

Blurs an image by a specified radius. This BIF allows you to apply a blur effect to an image in BoxLang, controlling the strength of the blur.

## Syntax

```
ImageBlur(name [, blurRadius])
```

## Arguments

| Name       | Type    | Required | Default | Description                                                                 |
| ---------- | ------- | -------- | ------- | --------------------------------------------------------------------------- |
| name       | any     | Yes      |         | The image or the name of a variable referencing an image to operate on.     |
| blurRadius | numeric | No       | 3       | The amount to blur the image. Higher values produce a stronger blur effect. |

## Returns

* **BoxImage**: The modified BoxImage instance with the blur applied.

## Description

`ImageBlur` applies a blur effect to the specified image. The blur radius controls the strength of the blur; higher values result in a more pronounced blur. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Blur an image with the default radius (3)
img = ImageBlur(myImage);

// Blur an image with a radius of 10
img = ImageBlur(myImage, 10);
```

## See Also

* ImageSharpen
* ImageAddBorder

## Notes

* The default blur radius is 3 if not specified.
* The image can be passed as a BoxImage object or as a variable name referencing an image.
