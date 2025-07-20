# ImageNegative

Inverts the colors of an image to produce a photographic negative. This BIF allows you to create a negative version of an image in BoxLang.

## Syntax

```
ImageNegative(name)
```

## Arguments

| Name | Type | Required | Description                                                             |
| ---- | ---- | -------- | ----------------------------------------------------------------------- |
| name | any  | Yes      | The image or the name of a variable referencing an image to operate on. |

## Returns

* **BoxImage**: The modified BoxImage instance with inverted colors.

## Description

`ImageNegative` inverts the colors of the specified image, producing a photographic negative effect. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Create a negative of an image
negImg = ImageNegative(myImage);
```

## See Also

* ImageGrayScale
* ImageInvert

## Notes

* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The negative effect is applied to all color channels.
