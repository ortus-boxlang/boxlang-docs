# ImageAddBorder

Adds a border to an image. This BIF allows you to specify the thickness, color, and type of border to apply to an image in BoxLang.

## Syntax

```
ImageAddBorder(name, thickness [, color] [, borderType])
```

## Arguments

| Name       | Type    | Required | Default | Description                                                             |
| ---------- | ------- | -------- | ------- | ----------------------------------------------------------------------- |
| name       | any     | Yes      |         | The image or the name of a variable referencing an image to operate on. |
| thickness  | numeric | Yes      |         | Border thickness (in pixels).                                           |
| color      | string  | No       | "black" | Border color: hex value or constant color name.                         |
| borderType | string  | No       |         | Border type: one of `zero`, `constant`, `copy`, `reflect`, or `wrap`.   |

## Returns

* **BoxImage**: The modified BoxImage instance with the border applied.

## Description

`ImageAddBorder` adds a border around the specified image. You can control the thickness and color of the border, as well as the border type. The image can be passed directly or referenced by variable name. The border type determines how the border is generated:

* `zero`: Border pixels are set to zero.
* `constant`: Border pixels are set to the specified color.
* `copy`: Border pixels are copied from the edge of the image.
* `reflect`: Border pixels are a reflection of the image edge.
* `wrap`: Border pixels wrap around from the opposite edge.

## Example

```boxlang
// Add a 10px black border to an image
img = ImageAddBorder(myImage, 10);

// Add a 5px red constant border
img = ImageAddBorder(myImage, 5, "red", "constant");
```

## See Also

* ImageResize
* ImageCrop

## Notes

* The default border color is black if not specified.
* The default border type is implementation-dependent if not specified.
* The image can be passed as a BoxImage object or as a variable name referencing an image.
