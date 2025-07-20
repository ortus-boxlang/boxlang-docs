# ImageDrawText

Draws text on an image. This BIF allows you to specify the text, position, and optional attributes for rendering text in BoxLang.

## Syntax

```
ImageDrawText(name, str, x, y [, attributeCollection])
```

## Arguments

| Name                | Type    | Required | Default | Description                                                                 |
| ------------------- | ------- | -------- | ------- | --------------------------------------------------------------------------- |
| name                | any     | Yes      |         | The image or the name of a variable referencing an image to operate on.     |
| str                 | string  | Yes      |         | The text string to draw.                                                    |
| x                   | numeric | Yes      |         | The x coordinate for the text position.                                     |
| y                   | numeric | Yes      |         | The y coordinate for the text position.                                     |
| attributeCollection | struct  | No       |         | Optional struct of attributes for text rendering (e.g., font, size, color). |

## Returns

* **BoxImage**: The modified BoxImage instance with the text drawn.

## Description

`ImageDrawText` draws a string of text on the specified image at the given (x, y) coordinates. You can optionally provide an attribute collection struct to control font, size, color, and other text rendering options. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Draw text at (10, 20)
img = ImageDrawText(myImage, "Hello World", 10, 20);

// Draw text with attributes
attrs = { font: "Arial", size: 24, color: "red" };
img = ImageDrawText(myImage, "Hello World", 10, 20, attrs);
```

## See Also

* ImageDrawRect
* ImageDrawPoint

## Notes

* All arguments except `attributeCollection` are required.
* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The attribute collection struct can include font, size, color, and other text properties.
