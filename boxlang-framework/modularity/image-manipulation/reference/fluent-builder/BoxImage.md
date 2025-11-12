# BoxImage Fluent API

The `BoxImage` class provides a fluent, chainable API for image manipulation in BoxLang. All methods return the `BoxImage` instance, allowing you to chain multiple operations together in a single expression.

## Creating Images

### ImageNew()

Create a new image from various sources:

```boxlang
// From file path
img = ImageNew("images/photo.jpg");

// From URL
img = ImageNew("https://example.com/image.png");

// From base64 string
img = ImageReadBase64(base64String);

// Blank canvas
img = ImageNew(800, 600);
img = ImageNew(800, 600, "rgb");
img = ImageNew(800, 600, "rgb", "white");
```

## Transformations

### resize(width, height, [interpolation], [blurFactor])

Resize the image to specific dimensions.

```boxlang
img.resize(800, 600);
img.resize(400, 300, "bicubic");
img.resize(1200, 800, "highestQuality", 1);
```

**Interpolation methods:** `nearest`, `bilinear`, `bicubic`, `highestPerformance`, `highestQuality`

### scaleToFit(size, [interpolation])

Scale image proportionally to fit within a bounding box.

```boxlang
// Single size - fits within size x size box
img.scaleToFit(400);
img.scaleToFit(800, "bicubic");

// Width and height - fits within maxWidth x maxHeight box
img.scaleToFit(800, 600);
img.scaleToFit(1024, 768, "highestQuality");
```

### rotate(angle)

Rotate the image by degrees (clockwise).

```boxlang
img.rotate(90);
img.rotate(45);
img.rotate(-30);
```

### crop(x, y, width, height)

Crop a rectangular region from the image.

```boxlang
img.crop(50, 50, 200, 150);
```

### transpose(operation)

Flip or rotate the image in various ways.

```boxlang
img.transpose("horizontal");  // Flip horizontally (mirror)
img.transpose("vertical");    // Flip vertically
img.transpose("diagonal");    // Flip along main diagonal (top-left to bottom-right)
img.transpose("antidiagonal"); // Flip along anti-diagonal (top-right to bottom-left)
img.transpose("90");          // Rotate 90° clockwise
img.transpose("180");         // Rotate 180°
img.transpose("270");         // Rotate 270° clockwise (90° counter-clockwise)
```

**Aliases:** `flip()` is an alias for `transpose()`

### translate(x, y)

Move the image content by offset.

```boxlang
img.translate(100, 50);
```

### shear(amount, dimension)

Shear the image horizontally or vertically.

```boxlang
img.shear(0.5, "horizontal");
img.shear(0.3, "vertical");
```

## Color Adjustments

### grayScale()

Convert the image to grayscale.

```boxlang
img.grayScale();
```

### negative()

Invert the colors (create a negative).

```boxlang
img.negative();
```

## Filters & Effects

### blur([radius])

Apply a blur effect.

```boxlang
img.blur();       // Default blur
img.blur(5);      // Custom blur radius
```

### sharpen(gain)

Sharpen the image.

```boxlang
img.sharpen(0.5);
img.sharpen(1.0);
```

### addBorder(thickness, color)

Add a solid border around the image.

```boxlang
img.addBorder(5, "black");
img.addBorder(10, "#FF0000");
img.addBorder(3, "navy");
```

**Colors:** Accepts color names ("red", "blue", "black") or hex codes ("#FF0000")

## Compositing

### overlay(imageToOverlay, overlayRule, transparency)

Overlay another image on top of this one.

```boxlang
overlay = ImageNew("watermark.png");
img.overlay(overlay, "normal", 0.5);
```

**Overlay rules:** `normal`, `add`, `subtract`, `difference`, `multiply`, `screen`, `overlay`, `hardlight`, `softlight`

### drawImage(image, x, y)

Draw another image onto this image at specific coordinates.

```boxlang
logo = ImageNew("logo.png");
img.drawImage(logo, 10, 10);
```

## Drawing Operations

### Drawing Setup

Before drawing, configure colors, stroke, and transparency:

```boxlang
// Set drawing color for shapes and lines
img.setDrawingColor("red");
img.setDrawingColor("#0000FF");

// Set background color
img.setBackgroundColor("white");

// Set drawing transparency (0.0 = transparent, 1.0 = opaque)
img.setDrawingTransparency(0.7);

// Enable/disable anti-aliasing for smoother edges
img.setAntiAliasing(true);

// Configure stroke (line style)
img.setDrawingStroke({
    width: 3,
    endCaps: "round",
    lineJoins: "miter",
    miterLimit: 10,
    dashArray: [5, 3],
    dashPhase: 0
});
```

**Stroke Attributes:**
- `width` (numeric): Line thickness in pixels (default: 1)
- `endCaps` (string): Line end style - "butt", "round", "square" (default: "square")
- `lineJoins` (string): Corner style - "miter", "round", "bevel" (default: "miter")
- `miterLimit` (numeric): Limit for miter joins (default: 10)
- `dashArray` (array): Dash pattern [dash, gap, dash, gap...] (default: solid line)
- `dashPhase` (numeric): Offset for dash pattern (default: 0)

### Shape Drawing

#### drawRect(x, y, width, height, [filled])

Draw a rectangle.

```boxlang
img.drawRect(50, 50, 200, 100);          // Outline
img.drawRect(50, 50, 200, 100, true);    // Filled
img.fillRect(50, 50, 200, 100);          // Filled (convenience method)
```

#### drawRoundRect(x, y, width, height, arcWidth, arcHeight, [filled])

Draw a rounded rectangle.

```boxlang
img.drawRoundRect(50, 50, 200, 100, 20, 20);
img.drawRoundRect(50, 50, 200, 100, 20, 20, true);
```

#### drawOval(x, y, width, height, [filled])

Draw an oval/ellipse.

```boxlang
img.drawOval(100, 100, 150, 100);
img.drawOval(100, 100, 150, 100, true);
```

#### drawBeveledRect(x, y, width, height, raised, [filled])

Draw a 3D beveled rectangle.

```boxlang
img.drawBeveledRect(50, 50, 200, 100, true);         // Raised
img.drawBeveledRect(50, 50, 200, 100, false, true);  // Lowered, filled
```

#### drawArc(x, y, width, height, startAngle, arcAngle, [filled])

Draw an arc or pie slice.

```boxlang
img.drawArc(100, 100, 200, 200, 0, 90);        // Quarter circle outline
img.drawArc(100, 100, 200, 200, 45, 180, true); // Pie slice filled
```

### Line Drawing

#### drawLine(x1, y1, x2, y2)

Draw a straight line.

```boxlang
img.drawLine(0, 0, 100, 100);
```

#### drawLines(xCoords, yCoords, isPolygon, [filled])

Draw connected lines or polygons.

```boxlang
// Polyline
img.drawLines([10, 50, 90], [10, 50, 10], false);

// Polygon (auto-closes)
img.drawLines([50, 150, 100], [50, 150, 100], true);

// Filled polygon
img.drawLines([50, 150, 100], [50, 150, 100], true, true);
```

### Curve Drawing

#### drawCubicCurve(x1, y1, ctrlx1, ctrly1, ctrlx2, ctrly2, x2, y2)

Draw a cubic Bézier curve.

```boxlang
img.drawCubicCurve(20, 20, 100, 200, 200, 100, 300, 300);
```

#### drawQuadraticCurve(ctrlx, ctrly, x1, y1, x2, y2)

Draw a quadratic Bézier curve.

```boxlang
img.drawQuadraticCurve(150, 200, 50, 50, 250, 50);
```

### Text Drawing

#### drawText(text, x, y, [fontConfig])

Draw text on the image.

```boxlang
// Simple text
img.setDrawingColor("black")
   .drawText("Hello World", 100, 100);

// Styled text
img.drawText("Styled Text", 100, 200, {
    font: "Arial",
    size: 24,
    style: "bold",
    underline: true,
    strikethrough: false
});
```

**Font config attributes:**
- `font` (string): Font family name (default: system default)
- `size` (numeric): Font size in points (default: 12)
- `style` (string): "plain", "bold", "italic", "bolditalic" (default: "plain")
- `underline` (boolean): Underline text (default: false)
- `strikethrough` (boolean): Strikethrough text (default: false)

### Utility Drawing

#### clearRect(x, y, width, height)

Clear a rectangular region (makes it transparent).

```boxlang
img.clearRect(50, 50, 100, 100);
```

## Drawing Axis Transformations

Apply transformations to the drawing coordinate system:

### rotateDrawingAxis(angle, x, y)

Rotate the drawing axis around a point.

```boxlang
img.rotateDrawingAxis(45, 100, 100);
```

### translateDrawingAxis(x, y)

Translate (move) the drawing origin.

```boxlang
img.translateDrawingAxis(50, 50);
```

### shearDrawingAxis(x, y)

Shear the drawing coordinate system.

```boxlang
img.shearDrawingAxis(0.5, 0.5);
```

## Copying & Duplication

### copy()

Create a duplicate of the entire image.

```boxlang
copy = img.copy();
```

### copy(x, y, width, height, dx, dy)

Copy a region within the image to another location.

```boxlang
img.copy(50, 50, 100, 100, 200, 200);
```

## Writing Images

### write([path])

Write the image to disk.

```boxlang
// Write to original source path (if loaded from file)
img.write();

// Write to specific path
img.write("output/processed.jpg");
img.write("output/converted.png");
```

**Notes:**
- Parent directories are automatically created
- Format is determined by file extension
- File handles are properly closed (no Windows locking issues)

## Information & Metadata

### getWidth() / getHeight()

Get image dimensions.

```boxlang
width = img.getWidth();
height = img.getHeight();
```

### info()

Get comprehensive image information.

```boxlang
info = img.info();
// Returns struct with: width, height, colormodel, source, transparency, EXIF, IPTC
```

### getExifMetadata() / getIPTCMetadata()

Get metadata as a struct.

```boxlang
exif = img.getExifMetadata();
iptc = img.getIPTCMetadata();
```

### getExifTag(tag) / getIPTCTag(tag)

Get specific metadata tag value.

```boxlang
camera = img.getExifTag("Model");
keywords = img.getIPTCTag("Keywords");
```

### getBlob()

Get the image as a byte array.

```boxlang
bytes = img.getBlob();
```

### getBufferedImage()

Get the underlying Java BufferedImage object.

```boxlang
bi = img.getBufferedImage();
```

## Complete Chaining Example

The fluent API allows complex image processing pipelines:

```boxlang
result = ImageNew("photo.jpg")
    .scaleToFit(1200, 800, "bicubic")
    .crop(100, 100, 800, 600)
    .setAntiAliasing(true)
    .setDrawingColor("white")
    .setDrawingStroke({ width: 3, endCaps: "round" })
    .drawRect(10, 10, 780, 580)
    .setDrawingColor("black")
    .drawText("Copyright 2025", 20, 560, {
        font: "Arial",
        size: 16,
        style: "bold"
    })
    .sharpen(0.5)
    .write("output/processed.jpg");
```

## Working with Multiple Images

```boxlang
// Load and process multiple images
base = ImageNew(800, 600, "rgb", "white");

logo = ImageNew("logo.png")
    .scaleToFit(100)
    .setDrawingTransparency(0.8);

watermark = ImageNew("watermark.png")
    .scaleToFit(200);

// Composite them
result = base
    .drawImage(logo, 10, 10)
    .overlay(watermark, "normal", 0.3)
    .write("output/composite.png");
```

## Important Notes

### File Handling
- Images loaded from files are immediately read into memory - no file locking issues
- Files can be deleted immediately after `ImageNew()` or `ImageRead()`
- `write()` automatically creates parent directories if they don't exist

### Lazy Loading
- Images are fully loaded upon creation - no lazy loading issues
- Safe to use immediately after `ImageNew()` without calling `info()` first

### Color Format
- Colors accept both names ("red", "blue", "navy") and hex codes ("#FF0000", "#0000FF")
- See `BoxImage.COLORS` map for supported color names

### Method Chaining
- All transformation and drawing methods return `BoxImage` for chaining
- Getters (info, getWidth, getBlob, etc.) return their respective types and break the chain

### Metadata
- EXIF and IPTC metadata extracted automatically when loading from files
- Metadata is preserved when copying images
- Use `info()` to access all metadata in a single struct

## Related Documentation

- [Built-In Functions](/docs/reference/built-in-functions/) - Individual BIF documentation
- [Image Component](/docs/reference/components/image.md) - Tag-based approach
- [readme.md](/readme.md) - Module overview and quick start
