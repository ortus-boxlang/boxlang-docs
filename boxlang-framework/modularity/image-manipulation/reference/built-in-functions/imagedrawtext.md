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

`ImageDrawText` draws a string of text on the specified image at the given (x, y) coordinates. You can optionally provide an attribute collection struct to control font, size, style, and text rendering options. The image can be passed directly or referenced by variable name.

The `attributeCollection` struct supports the following keys:

* `font` (string): Font family name (e.g., "Arial", "Helvetica")
* `size` (numeric): Font size in points (default: 12)
* `style` (string): Font style - "plain", "bold", "italic", or "bolditalic" (default: "plain")
* `underline` (boolean): Whether to underline the text (default: false)
* `strikethrough` (boolean): Whether to strike through the text (default: false)

## Example

```boxlang
// Draw text at (10, 20)
img = ImageDrawText(myImage, "Hello World", 10, 20);

// Draw text with full styling
attrs = {
    font: "Arial",
    size: 24,
    style: "bold",
    underline: true,
    strikethrough: false
};
img = ImageDrawText(myImage, "Styled Text", 10, 20, attrs);

// Chain with color setup
img.setDrawingColor("blue")
   .drawText("Blue Text", 100, 100, { size: 18, style: "italic" });
```

## See Also

* ImageDrawRect
* ImageDrawPoint

## Notes

* All arguments except `attributeCollection` are required.
* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The attribute collection struct controls font properties (font, size, style, underline, strikethrough).
* Text color is set using `ImageSetDrawingColor` before calling this function.
* Enable anti-aliasing with `ImageSetAntiAliasing` for smoother text rendering.
* Returns the image object for method chaining.
