# ImageTranslateDrawingAxis

Translates (moves) the origin of the drawing coordinate system for subsequent drawing operations.

## Method Signature

```boxlang
BoxImage ImageTranslateDrawingAxis(image, x, y)
image.translateDrawingAxis(x, y)
```

## Arguments

| Argument | Type    | Required | Description                                  | Default |
| -------- | ------- | -------- | -------------------------------------------- | ------- |
| image    | any     | true     | The image object or variable name            |         |
| x        | numeric | true     | Horizontal translation in pixels             | 0       |
| y        | numeric | true     | Vertical translation in pixels               | 0       |

## Returns

Returns the modified `BoxImage` object, allowing for method chaining.

## Description

The `ImageTranslateDrawingAxis` function shifts the origin point (0,0) of the drawing coordinate system by the specified x and y offsets. This affects all subsequent drawing operations but does not move existing image content.

After translation, drawing at coordinates (0,0) will actually draw at (x,y) in the original coordinate system. This is useful for:

- Simplifying complex drawing operations by moving the origin to a convenient location
- Creating patterns by translating and drawing repeatedly
- Drawing relative to a specific point without coordinate calculations

This is different from `ImageTranslate`, which moves existing image content rather than the coordinate system.

## Examples

### Basic Coordinate System Translation

```boxlang
img = ImageNew(400, 400, "rgb", "white");

img.setDrawingColor("red")
   .translateDrawingAxis(100, 100)
   .drawRect(0, 0, 50, 50);  // Actually draws at (100,100)

ImageWrite(img, "translated-axes.jpg");
```

### Draw Relative to Center

```boxlang
img = ImageNew(600, 400, "rgb", "white");

// Move origin to center
centerX = img.getWidth() / 2;
centerY = img.getHeight() / 2;
img.translateDrawingAxis(centerX, centerY);

// Now draw relative to center
img.setDrawingColor("blue")
   .drawOval(-50, -50, 100, 100);  // Draws centered circle

ImageWrite(img, "centered.jpg");
```

### Create Grid Pattern

```boxlang
img = ImageNew(500, 500, "rgb", "white");
img.setDrawingColor("gray");

// Draw grid using translation
for (row = 0; row < 5; row++) {
    for (col = 0; col < 5; col++) {
        img.translateDrawingAxis(100, 100);
        img.drawRect(10, 10, 80, 80);
        img.translateDrawingAxis(-100, -100);  // Reset x
    }
    img.translateDrawingAxis(0, 100);  // Move to next row
}

ImageWrite(img, "grid.jpg");
```

### Complex Shape Composition

```boxlang
img = ImageNew(800, 600, "rgb", "white");

// Draw shapes relative to translated origin
img.setDrawingColor("purple")
   .translateDrawingAxis(200, 200);

// All coordinates now relative to (200,200)
img.drawOval(0, 0, 100, 100)
   .drawLine(50, 0, 50, 100)
   .drawLine(0, 50, 100, 50);

ImageWrite(img, "composition.jpg");
```

### Watermark Positioning

```boxlang
img = ImageNew("photo.jpg");
logo = ImageNew("watermark.png");

// Position relative to bottom-right corner
img.translateDrawingAxis(
    img.getWidth() - logo.getWidth() - 20,
    img.getHeight() - logo.getHeight() - 20
);

img.drawImage(logo, 0, 0);
ImageWrite(img, "watermarked.jpg");
```

## Related Functions

- ImageRotateDrawingAxis - Rotate the drawing coordinate system
- ImageShearDrawingAxis - Shear the drawing coordinate system
- ImageTranslate - Move existing image content
- ImageDrawRect - Draw rectangles
- ImageDrawOval - Draw ovals

## Notes

- Only affects subsequent drawing operations, not existing content
- Translations are cumulative - each call adds to previous translations
- Does not change the image dimensions or content
- Useful for simplifying coordinate calculations in complex drawings
- Returns the image object for method chaining
- The transformation persists until the image is modified or reset
- Can be combined with `ImageRotateDrawingAxis` and `ImageShearDrawingAxis` for complex transformations
