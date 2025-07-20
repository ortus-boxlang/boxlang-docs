# ImageShear

## Syntax

```
ImageShear( name, amount [, direction] )
```

Or as a member:

```
someImage.shear( amount [, direction] )
```

## Arguments

| Name      | Type    | Required | Default    | Description                                                   |
| --------- | ------- | -------- | ---------- | ------------------------------------------------------------- |
| name      | any     | Yes      |            | The image to shear. Can be a `BoxImage` object or image name. |
| amount    | numeric | Yes      |            | The amount of shear to apply.                                 |
| direction | string  | No       | horizontal | The direction of shear: "horizontal" or "vertical".           |

## Returns

`BoxImage` — The sheared image object.

## Description

Applies a shear transformation to the specified image. Shearing distorts the image along the horizontal or vertical axis by the given amount, creating a slanted effect.

## Example

```boxlang
// Shear image horizontally by 0.5
result = ImageShear( myImage, 0.5 );

// Shear image vertically by 0.3
result = ImageShear( myImage, 0.3, "vertical" );

// As a member function
myImage.shear( 0.2, "horizontal" );
```

## Related BIFs

* ImageRotate
* ImageResize
* ImageFlip

## Notes

* The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
* The operation modifies the image in place when used as a member function.
* Returns the modified image object for chaining or further processing.
* The `direction` argument must be either "horizontal" or "vertical".
