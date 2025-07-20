# ImageClearRect

Clears a rectangular region of an image using the configured background color. This BIF allows you to specify the position and size of the rectangle to clear in BoxLang.

## Syntax

```
ImageClearRect(name, x, y, width, height)
```

## Arguments

| Name   | Type    | Required | Description                                                             |
| ------ | ------- | -------- | ----------------------------------------------------------------------- |
| name   | any     | Yes      | The image or the name of a variable referencing an image to operate on. |
| x      | numeric | Yes      | X coordinate of the upper left corner of the rectangle.                 |
| y      | numeric | Yes      | Y coordinate of the upper left corner of the rectangle.                 |
| width  | numeric | Yes      | The width of the rectangle.                                             |
| height | numeric | Yes      | The height of the rectangle.                                            |

## Returns

* **BoxImage**: The modified BoxImage instance with the cleared rectangle.

## Description

`ImageClearRect` clears a rectangular region of the specified image, starting at the given (x, y) coordinates and extending to the specified width and height. The cleared area uses the image's configured background color. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Clear a 100x50 rectangle at position (10, 20)
img = ImageClearRect(myImage, 10, 20, 100, 50);
```

## See Also

* ImageFillRect
* ImageDrawRect

## Notes

* All arguments are required.
* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The cleared region uses the image's background color.
