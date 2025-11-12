# BIF Reference

Complete alphabetical reference for all image manipulation Built-In Functions (BIFs).

## Quick Reference Table

| Function | Category | Member Function | Description |
|----------|----------|-----------------|-------------|
| `GetReadableImageFormats()` | Utilities | N/A | Get array of readable image formats |
| `GetWriteableImageFormats()` | Utilities | N/A | Get array of writeable image formats |
| `ImageAddBorder()` | Transformations | `img.addBorder()` | Add border to image |
| `ImageBlur()` | Filters | `img.blur()` | Apply Gaussian blur |
| `ImageClearRect()` | Drawing | `img.clearRect()` | Clear rectangular area |
| `ImageCopy()` | Creation | `img.copy()` | Create copy of image |
| `ImageCrop()` | Transformations | `img.crop()` | Crop image to region |
| `ImageDrawArc()` | Drawing | `img.drawArc()` | Draw arc or pie slice |
| `ImageDrawBeveledRect()` | Drawing | `img.drawBeveledRect()` | Draw beveled rectangle |
| `ImageDrawCubicCurve()` | Drawing | `img.drawCubicCurve()` | Draw cubic Bézier curve |
| `ImageDrawLine()` | Drawing | `img.drawLine()` | Draw straight line |
| `ImageDrawLines()` | Drawing | `img.drawLines()` | Draw multiple connected lines |
| `ImageDrawOval()` | Drawing | `img.drawOval()` | Draw oval or circle |
| `ImageDrawPoint()` | Drawing | `img.drawPoint()` | Draw single point |
| `ImageDrawQuadraticCurve()` | Drawing | `img.drawQuadraticCurve()` | Draw quadratic Bézier curve |
| `ImageDrawRect()` | Drawing | `img.drawRect()` | Draw rectangle |
| `ImageDrawRoundRect()` | Drawing | `img.drawRoundRect()` | Draw rounded rectangle |
| `ImageDrawText()` | Drawing | `img.drawText()` | Draw text string |
| `ImageFlip()` | Transformations | `img.flip()` | Flip image vertically/horizontally |
| `ImageGetBlob()` | Properties | `img.getBytes()` | Get image as byte array |
| `ImageGetBufferedImage()` | Properties | `img.getBufferedImage()` | Get Java BufferedImage |
| `ImageGetExifMetadata()` | Metadata | `img.getExifMetadata()` | Get all EXIF metadata |
| `ImageGetExifTag()` | Metadata | `img.getExifTag()` | Get specific EXIF tag |
| `ImageGetHeight()` | Properties | `img.getHeight()` | Get image height |
| `ImageGetIPTCMetadata()` | Metadata | `img.getIPTCMetadata()` | Get all IPTC metadata |
| `ImageGetIPTCTag()` | Metadata | `img.getIPTCTag()` | Get specific IPTC tag |
| `ImageGetWidth()` | Properties | `img.getWidth()` | Get image width |
| `ImageGrayScale()` | Filters | `img.grayScale()` | Convert to grayscale |
| `ImageInfo()` | Properties | `img.info()` | Get comprehensive image info |
| `ImageNegative()` | Filters | `img.negative()` | Invert colors |
| `ImageNew()` | Creation | N/A | Create new image |
| `ImageOverlay()` | Compositing | `img.overlay()` | Blend two images |
| `ImagePaste()` | Compositing | `img.paste()` | Paste image at position |
| `ImageRead()` | Creation | N/A | Read image from file |
| `ImageReadBase64()` | Creation | N/A | Read image from Base64 |
| `ImageResize()` | Transformations | `img.resize()` | Resize to dimensions |
| `ImageRotate()` | Transformations | `img.rotate()` | Rotate by angle |
| `ImageRotateDrawingAxis()` | Drawing | `img.rotateDrawingAxis()` | Rotate coordinate system |
| `ImageScaleToFit()` | Transformations | `img.scaleToFit()` | Scale to fit dimensions |
| `ImageSetAntiAliasing()` | Configuration | `img.setAntialiasing()` | Enable/disable antialiasing |
| `ImageSetBackgroundColor()` | Configuration | `img.setBackgroundColor()` | Set background color |
| `ImageSetDrawingColor()` | Configuration | `img.setDrawingColor()` | Set drawing color |
| `ImageSetDrawingStroke()` | Configuration | `img.setDrawingStroke()` | Set stroke properties |
| `ImageSetDrawingTransparency()` | Configuration | `img.setDrawingTransparency()` | Set transparency level |
| `ImageSharpen()` | Filters | `img.sharpen()` | Sharpen image |
| `ImageShear()` | Transformations | `img.shear()` | Shear/skew image |
| `ImageShearDrawingAxis()` | Drawing | `img.shearDrawingAxis()` | Shear coordinate system |
| `ImageTranslate()` | Transformations | `img.translate()` | Move image position |
| `ImageTranslateDrawingAxis()` | Drawing | `img.translateDrawingAxis()` | Move coordinate system |
| `ImageWrite()` | Output | `img.write()` | Write image to file |
| `ImageWriteBase64()` | Output | `img.writeBase64()` | Convert to Base64 string |
| `IsImage()` | Validation | N/A | Check if variable is image |
| `IsImageFile()` | Validation | N/A | Check if file is valid image |

## Detailed Reference

### Creation & I/O

#### GetReadableImageFormats()

Get array of image formats that can be read.

**Syntax:**
```js
formats = GetReadableImageFormats();
```

**Returns:** Array of format names (e.g., `["BMP", "GIF", "JPEG", "PNG", "TIFF", "WBMP"]`)

**Example:**
```js
formats = GetReadableImageFormats();
writeDump(formats);
```

**See Also:** [GetWriteableImageFormats()](#getwriteableimageformats), [Utilities](utilities.md#format-support)

---

#### GetWriteableImageFormats()

Get array of image formats that can be written.

**Syntax:**
```js
formats = GetWriteableImageFormats();
```

**Returns:** Array of format names

**Example:**
```js
formats = GetWriteableImageFormats();
if (arrayFindNoCase(formats, "PNG")) {
    writeln("PNG writing is supported");
}
```

**See Also:** [GetReadableImageFormats()](#getreadableimageformats), [Utilities](utilities.md#format-support)

---

#### ImageCopy()

Create an independent copy of an image.

**Syntax:**
```js
copy = ImageCopy(image);
// Member function
copy = image.copy();
```

**Parameters:**
- `image` - Source image

**Returns:** New image instance

**Example:**
```js
img = ImageNew("photo.jpg");
copy = img.copy();
copy.blur(5);  // Original unchanged
```

**See Also:** [ImageNew()](#imagenew), [Getting Started](getting-started.md#creating-images)

---

#### ImageNew()

Create a new image from various sources or as a blank canvas.

**Syntax:**
```js
// Blank canvas
img = ImageNew(width, height, imageType, fillColor);

// From file
img = ImageNew(filepath);

// From URL
img = ImageNew(url);

// From BufferedImage
img = ImageNew(bufferedImage);
```

**Parameters:**
- `width` - Canvas width in pixels
- `height` - Canvas height in pixels
- `imageType` - "rgb", "argb", or "grayscale"
- `fillColor` - Initial fill color (name or hex)
- `filepath` - Path to image file
- `url` - HTTP(S) URL to image
- `bufferedImage` - Java BufferedImage object

**Returns:** New image instance

**Examples:**
```js
// Blank white canvas
img = ImageNew(800, 600, "rgb", "white");

// From file
img = ImageNew("photo.jpg");

// From URL
img = ImageNew("https://example.com/image.png");

// Transparent canvas
img = ImageNew(400, 300, "argb", "transparent");
```

**See Also:** [ImageRead()](#imageread), [Getting Started](getting-started.md#creating-images)

---

#### ImageRead()

Read an image from a file path.

**Syntax:**
```js
img = ImageRead(filepath);
```

**Parameters:**
- `filepath` - Absolute or relative path to image file

**Returns:** Image instance

**Example:**
```js
img = ImageRead("C:\photos\vacation.jpg");
writeln("Loaded: #img.getWidth()# x #img.getHeight()#");
```

**See Also:** [ImageNew()](#imagenew), [ImageReadBase64()](#imagereadbase64)

---

#### ImageReadBase64()

Create an image from a Base64-encoded string.

**Syntax:**
```js
img = ImageReadBase64(base64String);
```

**Parameters:**
- `base64String` - Base64-encoded image data

**Returns:** Image instance

**Example:**
```js
base64 = "iVBORw0KGgoAAAANSUhEUgA...";
img = ImageReadBase64(base64);
```

**See Also:** [ImageWriteBase64()](#imagewritebase64), [Getting Started](getting-started.md#reading-from-base64)

---

#### ImageWrite()

Write an image to a file.

**Syntax:**
```js
ImageWrite(image, filepath, [quality]);
// Member function
image.write(filepath, [quality]);
```

**Parameters:**
- `image` - Image to write
- `filepath` - Output file path (extension determines format)
- `quality` - JPEG quality (0.0 to 1.0), optional

**Example:**
```js
img = ImageNew("photo.jpg");
img.blur(3);
img.write("blurred.jpg", 0.85);  // 85% quality
```

**See Also:** [ImageWriteBase64()](#imagewritebase64), [Getting Started](getting-started.md#saving-images)

---

#### ImageWriteBase64()

Convert image to Base64-encoded string.

**Syntax:**
```js
base64 = ImageWriteBase64(image, [format]);
// Member function
base64 = image.writeBase64([format]);
```

**Parameters:**
- `image` - Image to encode
- `format` - Output format ("png", "jpeg", etc.), defaults to PNG

**Returns:** Base64 string

**Example:**
```js
img = ImageNew("logo.png");
base64 = img.writeBase64("png");
html = "<img src='data:image/png;base64,#base64#' />";
```

**See Also:** [ImageReadBase64()](#imagereadbase64), [Getting Started](getting-started.md#saving-as-base64)

---

### Transformations

#### ImageAddBorder()

Add a border around an image.

**Syntax:**
```js
ImageAddBorder(image, thickness, color, borderType);
// Member function
image.addBorder(thickness, color, borderType);
```

**Parameters:**
- `image` - Target image
- `thickness` - Border thickness in pixels
- `color` - Border color (name or hex)
- `borderType` - "constant" or "reflect"

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew("photo.jpg");
img.addBorder(10, "black", "constant");
```

**See Also:** [Transformations](transformations.md#adding-borders)

---

#### ImageCrop()

Crop image to a rectangular region.

**Syntax:**
```js
ImageCrop(image, x, y, width, height);
// Member function
image.crop(x, y, width, height);
```

**Parameters:**
- `image` - Target image
- `x` - X coordinate of top-left corner
- `y` - Y coordinate of top-left corner
- `width` - Crop width
- `height` - Crop height

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew("photo.jpg");
img.crop(100, 100, 400, 300);  // Crop to 400x300 at (100,100)
```

**See Also:** [Transformations](transformations.md#cropping)

---

#### ImageFlip()

Flip image vertically or horizontally.

**Syntax:**
```js
ImageFlip(image, transpose);
// Member function
image.flip(transpose);
```

**Parameters:**
- `image` - Target image
- `transpose` - "vertical", "horizontal", "diagonal", "antidiagonal", "90", "180", or "270"

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew("photo.jpg");
img.flip("horizontal");  // Mirror horizontally
```

**See Also:** [Transformations](transformations.md#flipping-and-transposing)

---

#### ImageResize()

Resize image to exact dimensions.

**Syntax:**
```js
ImageResize(image, width, height, [interpolation]);
// Member function
image.resize(width, height, [interpolation]);
```

**Parameters:**
- `image` - Target image
- `width` - New width
- `height` - New height
- `interpolation` - "nearest", "bilinear", "bicubic", or "highQuality"

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew("photo.jpg");
img.resize(800, 600, "highQuality");
```

**See Also:** [ImageScaleToFit()](#imagescaletofit), [Transformations](transformations.md#resizing)

---

#### ImageRotate()

Rotate image by specified angle.

**Syntax:**
```js
ImageRotate(image, angle, [x], [y]);
// Member function
image.rotate(angle, [x], [y]);
```

**Parameters:**
- `image` - Target image
- `angle` - Rotation angle in degrees (clockwise)
- `x` - X coordinate of rotation center (optional)
- `y` - Y coordinate of rotation center (optional)

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew("photo.jpg");
img.rotate(45);  // Rotate 45° clockwise
```

**See Also:** [Transformations](transformations.md#rotating)

---

#### ImageScaleToFit()

Scale image to fit within dimensions, maintaining aspect ratio.

**Syntax:**
```js
ImageScaleToFit(image, width, height, [interpolation]);
// Member function
image.scaleToFit(width, height, [interpolation]);
```

**Parameters:**
- `image` - Target image
- `width` - Maximum width
- `height` - Maximum height
- `interpolation` - "nearest", "bilinear", "bicubic", or "highQuality"

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew("photo.jpg");
img.scaleToFit(800, 600);  // Fit within 800x600, keep aspect ratio
```

**See Also:** [ImageResize()](#imageresize), [Transformations](transformations.md#scaling)

---

#### ImageShear()

Shear (skew) image along axes.

**Syntax:**
```js
ImageShear(image, shearX, shearY, [interpolation]);
// Member function
image.shear(shearX, shearY, [interpolation]);
```

**Parameters:**
- `image` - Target image
- `shearX` - Horizontal shear factor
- `shearY` - Vertical shear factor
- `interpolation` - Interpolation method

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew("photo.jpg");
img.shear(0.2, 0);  // Shear horizontally
```

**See Also:** [Transformations](transformations.md#shearing)

---

#### ImageTranslate()

Move image position within canvas.

**Syntax:**
```js
ImageTranslate(image, x, y, [interpolation]);
// Member function
image.translate(x, y, [interpolation]);
```

**Parameters:**
- `image` - Target image
- `x` - Horizontal offset
- `y` - Vertical offset
- `interpolation` - Interpolation method

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew("photo.jpg");
img.translate(50, 30);  // Move right 50px, down 30px
```

**See Also:** [Transformations](transformations.md#translating)

---

### Filters & Effects

#### ImageBlur()

Apply Gaussian blur effect.

**Syntax:**
```js
ImageBlur(image, [blurRadius]);
// Member function
image.blur([blurRadius]);
```

**Parameters:**
- `image` - Target image
- `blurRadius` - Blur intensity (1-10), default 3

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew("photo.jpg");
img.blur(5);  // Apply moderate blur
```

**See Also:** [ImageSharpen()](#imagesharpen), [Filters & Effects](filters-effects.md#blur)

---

#### ImageGrayScale()

Convert image to grayscale.

**Syntax:**
```js
ImageGrayScale(image);
// Member function
image.grayScale();
```

**Parameters:**
- `image` - Target image

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew("photo.jpg");
img.grayScale();  // Convert to black & white
```

**See Also:** [ImageNegative()](#imagenegative), [Filters & Effects](filters-effects.md#grayscale)

---

#### ImageNegative()

Invert image colors (negative effect).

**Syntax:**
```js
ImageNegative(image);
// Member function
image.negative();
```

**Parameters:**
- `image` - Target image

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew("photo.jpg");
img.negative();  // Invert colors
```

**See Also:** [ImageGrayScale()](#imagegrayscale), [Filters & Effects](filters-effects.md#negative)

---

#### ImageSharpen()

Sharpen image to enhance edges.

**Syntax:**
```js
ImageSharpen(image, [gain]);
// Member function
image.sharpen([gain]);
```

**Parameters:**
- `image` - Target image
- `gain` - Sharpening intensity (0.0-10.0), default 1.0

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew("photo.jpg");
img.sharpen(1.5);  // Moderate sharpening
```

**See Also:** [ImageBlur()](#imageblur), [Filters & Effects](filters-effects.md#sharpen)

---

### Compositing

#### ImageOverlay()

Blend two images with specified blend mode.

**Syntax:**
```js
ImageOverlay(baseImage, overlayImage, [blendMode]);
// Member function
baseImage.overlay(overlayImage, [blendMode]);
```

**Parameters:**
- `baseImage` - Bottom image
- `overlayImage` - Top image to blend
- `blendMode` - "normal", "multiply", "screen", "overlay", "darken", "lighten"

**Returns:** Modified base image (chainable)

**Example:**
```js
base = ImageNew("background.jpg");
overlay = ImageNew("foreground.png");
base.overlay(overlay, "multiply");
```

**See Also:** [ImagePaste()](#imagepaste), [Filters & Effects](filters-effects.md#overlay)

---

#### ImagePaste()

Paste one image onto another at specific position.

**Syntax:**
```js
ImagePaste(baseImage, sourceImage, x, y, [transparency]);
// Member function
baseImage.paste(sourceImage, x, y, [transparency]);
```

**Parameters:**
- `baseImage` - Destination image
- `sourceImage` - Image to paste
- `x` - X position
- `y` - Y position
- `transparency` - Opacity percentage (0-100), optional

**Returns:** Modified base image (chainable)

**Example:**
```js
canvas = ImageNew(800, 600, "rgb", "white");
logo = ImageNew("logo.png");
canvas.paste(logo, 100, 100, 80);  // 80% opaque
```

**See Also:** [ImageOverlay()](#imageoverlay), [Filters & Effects](filters-effects.md#paste)

---

### Drawing

#### ImageClearRect()

Clear (erase) a rectangular area.

**Syntax:**
```js
ImageClearRect(image, x, y, width, height);
// Member function
image.clearRect(x, y, width, height);
```

**Parameters:**
- `image` - Target image
- `x` - X coordinate
- `y` - Y coordinate
- `width` - Rectangle width
- `height` - Rectangle height

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("red");
img.drawRect(0, 0, 400, 300, true);
img.clearRect(50, 50, 100, 100);  // Erase center
```

**See Also:** [ImageDrawRect()](#imagedrawrect), [Drawing](drawing.md#clearing)

---

#### ImageDrawArc()

Draw an arc or pie slice.

**Syntax:**
```js
ImageDrawArc(image, x, y, width, height, startAngle, arcAngle, [filled]);
// Member function
image.drawArc(x, y, width, height, startAngle, arcAngle, [filled]);
```

**Parameters:**
- `image` - Target image
- `x` - X coordinate of bounding box
- `y` - Y coordinate of bounding box
- `width` - Width of bounding box
- `height` - Height of bounding box
- `startAngle` - Starting angle in degrees
- `arcAngle` - Arc span in degrees
- `filled` - true for filled pie slice, false for outline

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("blue");
img.drawArc(100, 100, 200, 200, 0, 90, true);  // Quarter circle
```

**See Also:** [ImageDrawOval()](#imagedrawoval), [Drawing](drawing.md#arcs)

---

#### ImageDrawBeveledRect()

Draw a rectangle with beveled corners.

**Syntax:**
```js
ImageDrawBeveledRect(image, x, y, width, height, raised, [filled]);
// Member function
image.drawBeveledRect(x, y, width, height, raised, [filled]);
```

**Parameters:**
- `image` - Target image
- `x` - X coordinate
- `y` - Y coordinate
- `width` - Rectangle width
- `height` - Rectangle height
- `raised` - true for raised bevel, false for lowered
- `filled` - true to fill, false for outline

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("gray");
img.drawBeveledRect(50, 50, 200, 100, true, true);  // Raised button
```

**See Also:** [ImageDrawRect()](#imagedrawrect), [Drawing](drawing.md#beveled-rectangles)

---

#### ImageDrawCubicCurve()

Draw a cubic Bézier curve.

**Syntax:**
```js
ImageDrawCubicCurve(image, x1, y1, ctrlx1, ctrly1, ctrlx2, ctrly2, x2, y2);
// Member function
image.drawCubicCurve(x1, y1, ctrlx1, ctrly1, ctrlx2, ctrly2, x2, y2);
```

**Parameters:**
- `image` - Target image
- `x1`, `y1` - Start point
- `ctrlx1`, `ctrly1` - First control point
- `ctrlx2`, `ctrly2` - Second control point
- `x2`, `y2` - End point

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("blue");
img.drawCubicCurve(50, 200, 100, 50, 300, 50, 350, 200);
```

**See Also:** [ImageDrawQuadraticCurve()](#imagedrawquadraticcurve), [Drawing](drawing.md#curves)

---

#### ImageDrawLine()

Draw a straight line.

**Syntax:**
```js
ImageDrawLine(image, x1, y1, x2, y2);
// Member function
image.drawLine(x1, y1, x2, y2);
```

**Parameters:**
- `image` - Target image
- `x1`, `y1` - Start point
- `x2`, `y2` - End point

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("red");
img.drawLine(0, 0, 400, 300);  // Diagonal line
```

**See Also:** [ImageDrawLines()](#imagedrawlines), [Drawing](drawing.md#lines)

---

#### ImageDrawLines()

Draw multiple connected lines.

**Syntax:**
```js
ImageDrawLines(image, points);
// Member function
image.drawLines(points);
```

**Parameters:**
- `image` - Target image
- `points` - Array of coordinate pairs: `[[x1,y1], [x2,y2], ...]`

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("blue");
points = [[50,200], [100,50], [200,100], [300,50], [350,200]];
img.drawLines(points);  // Connected zigzag
```

**See Also:** [ImageDrawLine()](#imagedrawline), [Drawing](drawing.md#lines)

---

#### ImageDrawOval()

Draw an oval or circle.

**Syntax:**
```js
ImageDrawOval(image, x, y, width, height, [filled]);
// Member function
image.drawOval(x, y, width, height, [filled]);
```

**Parameters:**
- `image` - Target image
- `x` - X coordinate of bounding box
- `y` - Y coordinate of bounding box
- `width` - Oval width
- `height` - Oval height
- `filled` - true to fill, false for outline

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("red");
img.drawOval(100, 50, 200, 200, true);  // Filled circle
```

**See Also:** [ImageDrawArc()](#imagedrawarc), [Drawing](drawing.md#ovals-and-circles)

---

#### ImageDrawPoint()

Draw a single point (pixel).

**Syntax:**
```js
ImageDrawPoint(image, x, y);
// Member function
image.drawPoint(x, y);
```

**Parameters:**
- `image` - Target image
- `x` - X coordinate
- `y` - Y coordinate

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("black");
for (i = 0; i < 100; i++) {
    img.drawPoint(randRange(0, 400), randRange(0, 300));
}
```

**See Also:** [ImageDrawLine()](#imagedrawline), [Drawing](drawing.md#points)

---

#### ImageDrawQuadraticCurve()

Draw a quadratic Bézier curve.

**Syntax:**
```js
ImageDrawQuadraticCurve(image, x1, y1, ctrlx, ctrly, x2, y2);
// Member function
image.drawQuadraticCurve(x1, y1, ctrlx, ctrly, x2, y2);
```

**Parameters:**
- `image` - Target image
- `x1`, `y1` - Start point
- `ctrlx`, `ctrly` - Control point
- `x2`, `y2` - End point

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("green");
img.drawQuadraticCurve(50, 200, 200, 50, 350, 200);
```

**See Also:** [ImageDrawCubicCurve()](#imagedrawcubiccurve), [Drawing](drawing.md#curves)

---

#### ImageDrawRect()

Draw a rectangle.

**Syntax:**
```js
ImageDrawRect(image, x, y, width, height, [filled]);
// Member function
image.drawRect(x, y, width, height, [filled]);
```

**Parameters:**
- `image` - Target image
- `x` - X coordinate
- `y` - Y coordinate
- `width` - Rectangle width
- `height` - Rectangle height
- `filled` - true to fill, false for outline

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("blue");
img.drawRect(50, 50, 200, 100, false);  // Outline only
```

**See Also:** [ImageDrawRoundRect()](#imagedrawroundrect), [Drawing](drawing.md#rectangles)

---

#### ImageDrawRoundRect()

Draw a rectangle with rounded corners.

**Syntax:**
```js
ImageDrawRoundRect(image, x, y, width, height, arcWidth, arcHeight, [filled]);
// Member function
image.drawRoundRect(x, y, width, height, arcWidth, arcHeight, [filled]);
```

**Parameters:**
- `image` - Target image
- `x` - X coordinate
- `y` - Y coordinate
- `width` - Rectangle width
- `height` - Rectangle height
- `arcWidth` - Horizontal corner radius
- `arcHeight` - Vertical corner radius
- `filled` - true to fill, false for outline

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("purple");
img.drawRoundRect(50, 50, 200, 100, 20, 20, true);
```

**See Also:** [ImageDrawRect()](#imagedrawrect), [Drawing](drawing.md#rounded-rectangles)

---

#### ImageDrawText()

Draw text string on image.

**Syntax:**
```js
ImageDrawText(image, text, x, y, [attributes]);
// Member function
image.drawText(text, x, y, [attributes]);
```

**Parameters:**
- `image` - Target image
- `text` - Text string to draw
- `x` - X coordinate
- `y` - Y coordinate (baseline)
- `attributes` - Struct with: `font`, `size`, `style` ("plain", "bold", "italic", "bolditalic")

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("black")
   .setAntialiasing(true);
img.drawText("Hello World", 100, 150, {
    font: "Arial",
    size: 32,
    style: "bold"
});
```

**See Also:** [Drawing](drawing.md#text-rendering)

---

#### ImageRotateDrawingAxis()

Rotate the drawing coordinate system.

**Syntax:**
```js
ImageRotateDrawingAxis(image, angle, [x], [y]);
// Member function
image.rotateDrawingAxis(angle, [x], [y]);
```

**Parameters:**
- `image` - Target image
- `angle` - Rotation angle in degrees
- `x` - X coordinate of rotation point (optional)
- `y` - Y coordinate of rotation point (optional)

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("red");
img.rotateDrawingAxis(45, 200, 150);
img.drawText("Rotated Text", 200, 150);
```

**See Also:** [ImageTranslateDrawingAxis()](#imagetranslatedrawingaxis), [Drawing](drawing.md#axis-rotation)

---

#### ImageShearDrawingAxis()

Shear the drawing coordinate system.

**Syntax:**
```js
ImageShearDrawingAxis(image, shearX, shearY);
// Member function
image.shearDrawingAxis(shearX, shearY);
```

**Parameters:**
- `image` - Target image
- `shearX` - Horizontal shear factor
- `shearY` - Vertical shear factor

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("blue");
img.shearDrawingAxis(0.3, 0);
img.drawText("Skewed Text", 100, 150);
```

**See Also:** [ImageShear()](#imageshear), [Drawing](drawing.md#axis-shearing)

---

#### ImageTranslateDrawingAxis()

Move the drawing coordinate system origin.

**Syntax:**
```js
ImageTranslateDrawingAxis(image, x, y);
// Member function
image.translateDrawingAxis(x, y);
```

**Parameters:**
- `image` - Target image
- `x` - Horizontal offset
- `y` - Vertical offset

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.translateDrawingAxis(200, 150);  // Move origin to center
img.setDrawingColor("red");
img.drawOval(-50, -50, 100, 100, true);  // Draw at new origin
```

**See Also:** [ImageRotateDrawingAxis()](#imagerotatedrawingaxis), [Drawing](drawing.md#axis-translation)

---

### Configuration

#### ImageSetAntiAliasing()

Enable or disable antialiasing for smooth edges.

**Syntax:**
```js
ImageSetAntiAliasing(image, enabled);
// Member function
image.setAntialiasing(enabled);
```

**Parameters:**
- `image` - Target image
- `enabled` - true or "on" to enable, false or "off" to disable

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setAntialiasing(true);  // Smooth edges
img.setDrawingColor("black");
img.drawOval(50, 50, 300, 200, false);
```

**See Also:** [Drawing](drawing.md#antialiasing)

---

#### ImageSetBackgroundColor()

Set the background fill color.

**Syntax:**
```js
ImageSetBackgroundColor(image, color);
// Member function
image.setBackgroundColor(color);
```

**Parameters:**
- `image` - Target image
- `color` - Color name or hex code

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setBackgroundColor("lightblue");
```

**See Also:** [ImageSetDrawingColor()](#imagesetdrawingcolor), [Drawing](drawing.md#colors)

---

#### ImageSetDrawingColor()

Set the color for drawing operations.

**Syntax:**
```js
ImageSetDrawingColor(image, color);
// Member function
image.setDrawingColor(color);
```

**Parameters:**
- `image` - Target image
- `color` - Color name or hex code

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("red");
img.drawRect(50, 50, 200, 100, true);
```

**See Also:** [Utilities](utilities.md#color-reference), [Drawing](drawing.md#colors)

---

#### ImageSetDrawingStroke()

Configure stroke properties for drawing.

**Syntax:**
```js
ImageSetDrawingStroke(image, attributes);
// Member function
image.setDrawingStroke(attributes);
```

**Parameters:**
- `image` - Target image
- `attributes` - Struct with: `width` (number), `color` (string), `cap` ("butt", "round", "square"), `join` ("miter", "round", "bevel"), `dashArray` (array of numbers)

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingStroke({
    width: 5,
    color: "blue",
    cap: "round",
    dashArray: [10, 5]  // 10px dash, 5px gap
});
img.drawLine(50, 150, 350, 150);
```

**See Also:** [Drawing](drawing.md#stroke-configuration)

---

#### ImageSetDrawingTransparency()

Set transparency level for drawing operations.

**Syntax:**
```js
ImageSetDrawingTransparency(image, percentage);
// Member function
image.setDrawingTransparency(percentage);
```

**Parameters:**
- `image` - Target image
- `percentage` - Transparency level (0-100, where 0=opaque, 100=transparent)

**Returns:** Modified image (chainable)

**Example:**
```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("red");
img.setDrawingTransparency(50);  // 50% transparent
img.drawRect(50, 50, 200, 100, true);
```

**See Also:** [Drawing](drawing.md#transparency)

---

### Metadata

#### ImageGetExifMetadata()

Get all EXIF metadata from image.

**Syntax:**
```js
metadata = ImageGetExifMetadata(image);
// Member function
metadata = image.getExifMetadata();
```

**Parameters:**
- `image` - Source image

**Returns:** Struct containing EXIF data

**Example:**
```js
img = ImageNew("photo.jpg");
exif = img.getExifMetadata();
writeln("Camera: #exif["Model"]#");
writeln("ISO: #exif["ISO Speed Ratings"]#");
```

**See Also:** [ImageGetExifTag()](#imagegetexiftag), [Metadata](metadata.md#exif)

---

#### ImageGetExifTag()

Get specific EXIF tag value.

**Syntax:**
```js
value = ImageGetExifTag(image, tagName);
// Member function
value = image.getExifTag(tagName);
```

**Parameters:**
- `image` - Source image
- `tagName` - EXIF tag name

**Returns:** Tag value or empty string if not found

**Example:**
```js
img = ImageNew("photo.jpg");
aperture = img.getExifTag("F-Number");
writeln("Aperture: f/#aperture#");
```

**See Also:** [ImageGetExifMetadata()](#imagegetexifmetadata), [Metadata](metadata.md#exif-tags)

---

#### ImageGetIPTCMetadata()

Get all IPTC metadata from image.

**Syntax:**
```js
metadata = ImageGetIPTCMetadata(image);
// Member function
metadata = image.getIPTCMetadata();
```

**Parameters:**
- `image` - Source image

**Returns:** Struct containing IPTC data

**Example:**
```js
img = ImageNew("photo.jpg");
iptc = img.getIPTCMetadata();
writeln("Caption: #iptc["Caption/Abstract"]#");
writeln("Copyright: #iptc["Copyright Notice"]#");
```

**See Also:** [ImageGetIPTCTag()](#imagegetiptctag), [Metadata](metadata.md#iptc)

---

#### ImageGetIPTCTag()

Get specific IPTC tag value.

**Syntax:**
```js
value = ImageGetIPTCTag(image, tagName);
// Member function
value = image.getIPTCTag(tagName);
```

**Parameters:**
- `image` - Source image
- `tagName` - IPTC tag name

**Returns:** Tag value or empty string if not found

**Example:**
```js
img = ImageNew("photo.jpg");
keywords = img.getIPTCTag("Keywords");
writeln("Keywords: #keywords#");
```

**See Also:** [ImageGetIPTCMetadata()](#imagegetiptcmetadata), [Metadata](metadata.md#iptc-tags)

---

### Properties

#### ImageGetBlob()

Get image as byte array (binary data).

**Syntax:**
```js
bytes = ImageGetBlob(image);
// Member function
bytes = image.getBytes();
```

**Parameters:**
- `image` - Source image

**Returns:** Byte array

**Example:**
```js
img = ImageNew("photo.jpg");
bytes = img.getBytes();
writeln("Size: #arrayLen(bytes)# bytes");
```

**See Also:** [Utilities](utilities.md#binary-operations)

---

#### ImageGetBufferedImage()

Get underlying Java BufferedImage object.

**Syntax:**
```js
bufferedImage = ImageGetBufferedImage(image);
// Member function
bufferedImage = image.getBufferedImage();
```

**Parameters:**
- `image` - Source image

**Returns:** Java BufferedImage

**Example:**
```js
img = ImageNew("photo.jpg");
buffered = img.getBufferedImage();
// Use with Java libraries
```

**See Also:** [Utilities](utilities.md#binary-operations)

---

#### ImageGetHeight()

Get image height in pixels.

**Syntax:**
```js
height = ImageGetHeight(image);
// Member function
height = image.getHeight();
```

**Parameters:**
- `image` - Source image

**Returns:** Height in pixels

**Example:**
```js
img = ImageNew("photo.jpg");
height = img.getHeight();
writeln("Height: #height#px");
```

**See Also:** [ImageGetWidth()](#imagegetwidth), [Utilities](utilities.md#image-properties)

---

#### ImageGetWidth()

Get image width in pixels.

**Syntax:**
```js
width = ImageGetWidth(image);
// Member function
width = image.getWidth();
```

**Parameters:**
- `image` - Source image

**Returns:** Width in pixels

**Example:**
```js
img = ImageNew("photo.jpg");
width = img.getWidth();
writeln("Width: #width#px");
```

**See Also:** [ImageGetHeight()](#imagegetheight), [Utilities](utilities.md#image-properties)

---

#### ImageInfo()

Get comprehensive image information.

**Syntax:**
```js
info = ImageInfo(image);
// Member function
info = image.info();
```

**Parameters:**
- `image` - Source image

**Returns:** Struct with width, height, colorModel, source, etc.

**Example:**
```js
img = ImageNew("photo.jpg");
info = img.info();
writeDump(info);
```

**See Also:** [Utilities](utilities.md#image-information)

---

### Validation

#### IsImage()

Check if a variable is an image object.

**Syntax:**
```js
result = IsImage(variable);
```

**Parameters:**
- `variable` - Variable to check

**Returns:** true if image, false otherwise

**Example:**
```js
img = ImageNew("photo.jpg");
if (IsImage(img)) {
    writeln("Valid image");
}
```

**See Also:** [IsImageFile()](#isimagefile), [Utilities](utilities.md#validation-functions)

---

#### IsImageFile()

Check if a file is a valid image without loading it.

**Syntax:**
```js
result = IsImageFile(filepath);
```

**Parameters:**
- `filepath` - Path to file

**Returns:** true if valid image file, false otherwise

**Example:**
```js
if (IsImageFile("photo.jpg")) {
    img = ImageNew("photo.jpg");
}
```

**See Also:** [IsImage()](#isimage), [Utilities](utilities.md#validation-functions)

---

## See Also

- **[Getting Started](getting-started.md)** - Basic usage and concepts
- **[Transformations](transformations.md)** - Resize, rotate, crop operations
- **[Drawing](drawing.md)** - Shape and text rendering
- **[Filters & Effects](filters-effects.md)** - Visual effects and compositing
- **[Metadata](metadata.md)** - EXIF and IPTC data extraction
- **[Utilities](utilities.md)** - Format support and validation
- **[Advanced Examples](advanced-examples.md)** - Real-world use cases
- **[Migration Guide](migration-guide.md)** - CF/Lucee compatibility
