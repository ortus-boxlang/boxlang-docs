# ImageTranslate

Moves (translates) the entire image content by the specified offset.

## Method Signature

```boxlang
BoxImage ImageTranslate(image, x, y)
image.translate(x, y)
```

## Arguments

| Argument | Type    | Required | Description                                  | Default |
| -------- | ------- | -------- | -------------------------------------------- | ------- |
| image    | any     | true     | The image object or variable name            |         |
| x        | numeric | true     | Horizontal offset in pixels                  |         |
| y        | numeric | true     | Vertical offset in pixels                    |         |

## Returns

Returns the modified `BoxImage` object, allowing for method chaining.

## Description

The `ImageTranslate` function shifts the entire image content by the specified x and y offsets. This operation moves all pixels in the image, creating empty space where the image moved from and potentially cropping content that moves beyond the image boundaries.

Positive x values move the content right, negative values move it left. Positive y values move the content down, negative values move it up.

This is different from `ImageTranslateDrawingAxis`, which translates the drawing coordinate system for subsequent drawing operations without moving existing content.

## Examples

### Basic Translation

```boxlang
img = ImageNew("photo.jpg");
ImageTranslate(img, 50, 30);
ImageWrite(img, "translated.jpg");
```

### Move Content with Chaining

```boxlang
result = ImageNew("logo.png")
    .translate(100, 100)
    .write("logo-shifted.png");
```

### Create Border Effect

```boxlang
// Translate content to create space for a border
img = ImageNew("photo.jpg");
img.setBackgroundColor("white")
   .translate(20, 20)
   .setDrawingColor("black")
   .drawRect(0, 0, img.getWidth()-1, img.getHeight()-1);
ImageWrite(img, "bordered.jpg");
```

### Center Content

```boxlang
img = ImageNew(800, 600, "rgb", "white");
logo = ImageNew("logo.png");

// Calculate centering offset
xOffset = (img.getWidth() - logo.getWidth()) / 2;
yOffset = (img.getHeight() - logo.getHeight()) / 2;

// Translate and composite
logo.translate(xOffset, yOffset);
img.drawImage(logo, 0, 0);
ImageWrite(img, "centered-logo.jpg");
```

### Animation Frame Sequence

```boxlang
baseImage = ImageNew("sprite.png");

// Create multiple frames with different translations
for (i = 1; i <= 5; i++) {
    frame = baseImage.copy();
    frame.translate(i * 10, 0);
    ImageWrite(frame, "frame-#i#.png");
}
```

## Related Functions

- ImageTranslateDrawingAxis - Translate the drawing coordinate system
- ImageRotate - Rotate image content
- ImageCrop - Extract a portion of the image
- ImageResize - Change image dimensions

## Notes

- Content that moves beyond the image boundaries will be cropped
- Empty areas created by translation are filled with the background color
- The image dimensions remain unchanged
- This operation modifies the existing image object
- Returns the image object for method chaining
- Coordinate system: (0,0) is top-left corner
