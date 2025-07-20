# ImageSetDrawingStroke

## Syntax

```
ImageSetDrawingStroke( name [, attributeCollection] )
```

Or as a member:

```
someImage.setDrawingStroke( [attributeCollection] )
```

## Arguments

| Name                | Type   | Required | Description                                                                        |
| ------------------- | ------ | -------- | ---------------------------------------------------------------------------------- |
| name                | any    | Yes      | The image to set the drawing stroke for. Can be a `BoxImage` object or image name. |
| attributeCollection | struct | No       | A struct of stroke attributes (e.g., thickness, dash pattern).                     |

## Returns

`BoxImage` — The image object with updated drawing stroke settings.

## Description

Sets the drawing stroke attributes for the specified image. Stroke attributes control how lines and shapes are drawn, such as thickness, dash patterns, and more.

## Example

```boxlang
// Set stroke thickness to 5
result = ImageSetDrawingStroke( myImage, { thickness: 5 } );

// Set stroke with dash pattern
result = ImageSetDrawingStroke( myImage, { thickness: 3, dash: [4, 2] } );

// As a member function
myImage.setDrawingStroke( { thickness: 2 } );
```

## Related BIFs

* ImageSetDrawingColor
* ImageDrawLine
* ImageDrawRect

## Notes

* The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
* The operation modifies the image in place when used as a member function.
* Returns the modified image object for chaining or further processing.
* The `attributeCollection` struct can include keys like `thickness`, `dash`, and other stroke properties.
