---
description: "Comprehensive reference for all image manipulation functions in BoxLang."
icon: book
---

# Reference

Complete alphabetical reference for all image manipulation Built-In Functions (BIFs).

## Fluent Builder

The BoxLang Image Manipulation module provides a modern, fluent API through the `BoxImage` class. This chainable interface makes image manipulation code more readable and maintainable.

{% hint style="success" %}
**The Fluent API is the recommended approach** for all new image manipulation code in BoxLang.
{% endhint %}

### 🔄 Quick Reference: BIF vs Fluent API

Here's how common BIF patterns translate to the modern Fluent API:

| BIF Approach | Fluent API Equivalent |
|--------------|----------------------|
| `ImageNew("photo.jpg")` | `Image("photo.jpg")` or `ImageNew("photo.jpg")` |
| `ImageResize(img, 800, 600)` | `img.resize(800, 600)` |
| `ImageScaleToFit(img, 400)` | `img.scaleToFit(400)` |
| `ImageCrop(img, 10, 10, 200, 200)` | `img.crop(10, 10, 200, 200)` |
| `ImageRotate(img, 90)` | `img.rotate(90)` |
| `ImageFlip(img, "horizontal")` | `img.flipHorizontal()` |
| `ImageAddBorder(img, 5, "black")` | `img.addBorder(5, "black")` |
| `ImageSetDrawingColor(img, "red")` | `img.setDrawingColor("red")` |
| `ImageDrawText(img, "Hello", 10, 50)` | `img.drawText("Hello", 10, 50)` |
| `ImageBlur(img, 3)` | `img.blur(3)` |
| `ImageSharpen(img, 0.5)` | `img.sharpen(0.5)` |
| `ImageGrayscale(img)` | `img.grayscale()` |
| `ImageNegative(img)` | `img.negative()` |
| `ImageWrite(img, "output.jpg")` | `img.write("output.jpg")` |
| `ImageGetWidth(img)` | `img.getWidth()` |
| `ImageGetHeight(img)` | `img.getHeight()` |

### Chaining Example

**BIF Approach - Verbose and Procedural:**

```js
img = ImageNew("photo.jpg");
ImageResize(img, 800, 600);
ImageRotate(img, 90);
ImageAddBorder(img, 10, "black");
ImageSetDrawingColor(img, "white");
ImageDrawText(img, "© 2025", 10, 50, { font: "Arial", size: 14 });
ImageWrite(img, "output.jpg");
```

**Fluent API - Concise and Chainable:**

```js
Image("photo.jpg")
    .resize(800, 600)
    .rotate(90)
    .addBorder(10, "black")
    .setDrawingColor("white")
    .drawText("© 2025", 10, 50, { font: "Arial", size: 14 })
    .write("output.jpg");
```

---

### 📋 Method Categories

### 🎨 Creation & Loading

- `Image()` / `ImageNew()` - Create/load images from file, URL, base64, or create blank canvas
- `ImageReadBase64()` - Load image from base64 string

### ✂️ Transformations

- `resize()` - Resize to specific dimensions
- `scaleToFit()` - Scale proportionally to fit within bounds
- `crop()` - Extract a rectangular region
- `rotate()` - Rotate by angle
- `flipHorizontal()` - Flip horizontally
- `flipVertical()` - Flip vertically
- `transpose()` - Transpose (swap X/Y axes)
- `shear()` - Apply shear transformation

### 🎨 Effects & Filters

- `blur()` - Apply blur effect
- `sharpen()` - Sharpen the image
- `grayscale()` - Convert to grayscale
- `negative()` - Create negative
- `overlay()` - Overlay another image
- `paste()` - Paste image at position

### 🖌️ Drawing

- `setDrawingColor()` - Set drawing color
- `setDrawingStroke()` - Set stroke style
- `setDrawingTransparency()` - Set transparency
- `setAntialiasing()` - Enable/disable antialiasing
- `drawText()` - Draw text
- `drawLine()` - Draw line
- `drawRect()` - Draw rectangle
- `drawRoundRect()` - Draw rounded rectangle
- `drawOval()` - Draw oval/circle
- `drawArc()` - Draw arc
- `drawPoint()` - Draw point
- `clearRect()` - Clear rectangle area

### 🎀 Decorations

- `addBorder()` - Add border around image
- `setBackground()` - Set background color

### 💾 Output

- `write()` - Write to file
- `writeToBrowser()` - Output to HTTP response
- `writeBase64()` - Export as base64 string
- `getBufferedImage()` - Get Java BufferedImage

### ℹ️ Information

- `getWidth()` - Get image width
- `getHeight()` - Get image height
- `info()` - Get comprehensive image info

---

### 🚀 Complete Example

Here's a real-world example showing the power of method chaining:

```js
// Create a thumbnail with watermark
Image("products/large-photo.jpg")
    .scaleToFit(400)
    .addBorder(2, "##cccccc")
    .setDrawingColor("white")
    .setDrawingTransparency(70)
    .drawRect(0, getHeight() - 30, getWidth(), 30, true)
    .setDrawingColor("##333333")
    .setDrawingTransparency(0)
    .drawText("© MyCompany 2025", 10, getHeight() - 10, {
        font: "Arial",
        size: 12,
        style: "bold"
    })
    .write("products/thumbnails/photo-thumb.jpg");
```

## BIF Quick Reference Table

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
