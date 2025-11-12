# BoxLang Image Module Documentation

<blockquote>
	Copyright Since 2023 by Ortus Solutions, Corp
	<br>
	<a href="https://www.boxlang.io">www.boxlang.io</a> |
	<a href="https://www.ortussolutions.com">www.ortussolutions.com</a>
</blockquote>

## Overview

The BoxLang Image Module provides comprehensive image manipulation functionality for BoxLang applications. It offers a rich set of Built-In Functions (BIFs), a fluent `BoxImage` builder, and a tag-based Component for maximum flexibility in how you work with images.

**Key Features:**

- 🖼️ **53 Image BIFs** - Complete Adobe ColdFusion and Lucee compatibility
- 🎨 **Drawing Operations** - Lines, shapes, curves, text with advanced styling
- ✨ **Filters & Effects** - Blur, sharpen, grayscale, negative, overlay
- 📐 **Transformations** - Resize, rotate, crop, flip, shear, scale
- 📊 **Metadata Support** - Read/write EXIF and IPTC metadata
- 🔗 **Fluent API** - Method chaining with the `BoxImage` builder
- 🏷️ **Component** - Tag-based syntax for templates
- 🎯 **Member Functions** - All BIFs available as member functions

## Three Ways to Work with Images

The module provides three approaches to image manipulation, giving you flexibility based on your coding style:

### 1. Built-In Functions (BIFs)

Traditional CFML function syntax:

```js
img = ImageRead("photo.jpg");
ImageResize(img, 800, 600);
ImageGrayScale(img);
ImageWrite(img, "output.jpg");
```

### 2. Fluent BoxImage Builder (Recommended)

The `BoxImage` class provides a fluent, chainable interface for image operations:

```js
ImageNew("photo.jpg")
    .resize(800, 600)
    .grayScale()
    .blur(5)
    .write("output.jpg");
```

**Why use the fluent builder?**
- ✅ Clean, readable code with method chaining
- ✅ IntelliSense/autocomplete support in IDEs
- ✅ Reduced variable management
- ✅ More concise code
- ✅ All BIF functionality available as methods

### 3. Component (Tag Syntax)

For BoxLang templates (`.bxm` files):

```html
<bx:image action="read" source="photo.jpg" name="img" />
<bx:image action="resize" source="#img#" width="800" height="600" />
<bx:image action="write" source="#img#" destination="output.jpg" />
```

## Installation

### Via CommandBox

```bash
box install bx-image
```

### Requirements

- BoxLang 1.0.0 or higher
- Java 21+

## Quick Start

### Basic Image Processing

```js
// Read, manipulate, and save an image
var logo = ImageNew("logo.png")
    .crop(50, 50, 200, 200)
    .blur(3)
    .grayScale()
    .write("logo-processed.png");
```

### Creating a Thumbnail

```js
// Create a proportionally scaled thumbnail
ImageNew("photo.jpg")
    .scaleToFit(200, 200)
    .sharpen(1.5)
    .write("thumbnail.jpg");
```

### Adding a Watermark

```js
// Add text watermark to an image
ImageNew("photo.jpg")
    .setDrawingColor("white")
    .setDrawingTransparency(50)
    .drawText("© 2025 My Company", 10, 30, {
        font: "Arial",
        size: 24,
        style: "bold"
    })
    .write("watermarked.jpg");
```

### Compositing Images

```js
// Overlay one image on another
var base = ImageNew("background.jpg");
var overlay = ImageNew("logo.png");

base.overlay(overlay, "normal", 0.8)
    .write("composite.jpg");
```

## Documentation Pages

- **[Getting Started](getting-started.md)** - Creating images, basic operations, method chaining
- **[Transformations](transformations.md)** - Resize, rotate, crop, flip, shear operations
- **[Filters & Effects](filters-effects.md)** - Blur, sharpen, grayscale, negative, overlay
- **[Drawing Operations](drawing.md)** - Shapes, lines, curves, text with styling
- **[Metadata](metadata.md)** - EXIF, IPTC metadata reading and tag access
- **[Utilities](utilities.md)** - Format support, validation, color reference
- **[Advanced Examples](advanced-examples.md)** - Watermarking, thumbnails, batch processing
- **[BIF Reference](bif-reference.md)** - Complete alphabetical BIF listing
- **[Migration Guide](migration-guide.md)** - Migrating from Adobe ColdFusion/Lucee

## BIF & Component Reference

### All Available BIFs (53 Functions)

| BIF | Member Function | Category | Description |
|-----|----------------|----------|-------------|
| `GetReadableImageFormats()` | - | Utility | Returns array of readable image formats |
| `GetWriteableImageFormats()` | - | Utility | Returns array of writable image formats |
| `ImageAddBorder()` | `image.addBorder()` | Transform | Adds solid color border around image |
| `ImageBlur()` | `image.blur()` | Filter | Applies Gaussian blur filter |
| `ImageClearRect()` | `image.clearRect()` | Drawing | Clears rectangular region to transparent |
| `ImageCopy()` | `image.copy()` | Utility | Creates copy of image or region |
| `ImageCrop()` | `image.crop()` | Transform | Crops image to specified rectangle |
| `ImageDrawArc()` | `image.drawArc()` | Drawing | Draws arc or filled arc |
| `ImageDrawBeveledRect()` | `image.drawBeveledRect()` | Drawing | Draws 3D beveled rectangle |
| `ImageDrawCubicCurve()` | `image.drawCubicCurve()` | Drawing | Draws cubic Bézier curve |
| `ImageDrawLine()` | `image.drawLine()` | Drawing | Draws straight line |
| `ImageDrawLines()` | `image.drawLines()` | Drawing | Draws polyline or polygon |
| `ImageDrawOval()` | `image.drawOval()` | Drawing | Draws oval or filled oval |
| `ImageDrawPoint()` | `image.drawPoint()` | Drawing | Draws single point |
| `ImageDrawQuadraticCurve()` | `image.drawQuadraticCurve()` | Drawing | Draws quadratic Bézier curve |
| `ImageDrawRect()` | `image.drawRect()` | Drawing | Draws rectangle or filled rectangle |
| `ImageDrawRoundRect()` | `image.drawRoundRect()` | Drawing | Draws rounded rectangle |
| `ImageDrawText()` | `image.drawText()` | Drawing | Draws text with font styling |
| `ImageFlip()` | `image.flip()` | Transform | Flips image horizontally or vertically |
| `ImageGetBlob()` | `image.getBlob()` | Utility | Returns image as byte array |
| `ImageGetBufferedImage()` | `image.getBufferedImage()` | Utility | Returns Java BufferedImage object |
| `ImageGetExifMetaData()` | `image.getExifMetaData()` | Metadata | Returns EXIF metadata struct |
| `ImageGetExifTag()` | `image.getExifTag()` | Metadata | Returns specific EXIF tag value |
| `ImageGetHeight()` | `image.getHeight()` | Utility | Returns image height in pixels |
| `ImageGetIPTCMetadata()` | `image.getIPTCMetadata()` | Metadata | Returns IPTC metadata struct |
| `ImageGetIPTCTag()` | `image.getIPTCTag()` | Metadata | Returns specific IPTC tag value |
| `ImageGetWidth()` | `image.getWidth()` | Utility | Returns image width in pixels |
| `ImageGrayScale()` / `ImageGreyScale()` | `image.grayScale()` | Filter | Converts image to grayscale |
| `ImageInfo()` | `image.info()` | Utility | Returns comprehensive image information |
| `ImageNegative()` | `image.negative()` | Filter | Inverts image colors (negative) |
| `ImageNew()` | - | Creation | Creates new image or reads from source |
| `ImageOverlay()` | `image.overlay()` | Filter | Overlays one image on another |
| `ImagePaste()` / `ImageDrawImage()` | `image.paste()` | Drawing | Pastes/draws one image onto another |
| `ImageRead()` | - | Creation | Reads image from file path or URL |
| `ImageReadBase64()` | - | Creation | Creates image from Base64 string |
| `ImageResize()` | `image.resize()` | Transform | Resizes image to exact dimensions |
| `ImageRotate()` | `image.rotate()` | Transform | Rotates image by specified angle |
| `ImageRotateDrawingAxis()` | `image.rotateDrawingAxis()` | Drawing | Rotates coordinate system for drawing |
| `ImageScaleToFit()` | `image.scaleToFit()` | Transform | Scales image proportionally to fit dimensions |
| `ImageSetAntiAliasing()` | `image.setAntiAliasing()` | Drawing | Enables/disables anti-aliasing |
| `ImageSetBackgroundColor()` | `image.setBackgroundColor()` | Drawing | Sets background color |
| `ImageSetDrawingColor()` | `image.setDrawingColor()` | Drawing | Sets color for drawing operations |
| `ImageSetDrawingStroke()` | `image.setDrawingStroke()` | Drawing | Configures line stroke properties |
| `ImageSetDrawingTransparency()` | `image.setDrawingTransparency()` | Drawing | Sets transparency for drawing |
| `ImageSharpen()` | `image.sharpen()` | Filter | Sharpens image edges |
| `ImageShear()` | `image.shear()` | Transform | Shears/skews image |
| `ImageShearDrawingAxis()` | `image.shearDrawingAxis()` | Drawing | Shears coordinate system for drawing |
| `ImageTranslate()` | `image.translate()` | Transform | Translates/moves image |
| `ImageTranslateDrawingAxis()` | `image.translateDrawingAxis()` | Drawing | Translates origin for drawing |
| `ImageWrite()` | `image.write()` | Output | Writes image to file |
| `ImageWriteBase64()` | `image.writeBase64()` | Output | Returns image as Base64 string |
| `IsImage()` | - | Validation | Checks if variable is an image |
| `IsImageFile()` | - | Validation | Checks if file is a valid image |

### Image Component

The `<bx:image>` component provides tag-based syntax for image operations:

| Action | Description | Key Attributes |
|--------|-------------|----------------|
| `read` | Read image from file or URL | `source`, `name` |
| `write` | Write image to file | `source`, `destination`, `overwrite` |
| `resize` | Resize image | `source`, `width`, `height` |
| `rotate` | Rotate image | `source`, `angle` |
| `border` | Add border | `source`, `color`, `thickness` |
| `info` | Get image information | `source`, `structName` |

**Example:**

```html
<bx:image action="read" source="photo.jpg" name="myImage" />
<bx:image action="resize" source="#myImage#" width="800" height="600" />
<bx:image action="border" source="#myImage#" color="black" thickness="5" />
<bx:image action="write" source="#myImage#" destination="output.jpg" />
```

## Supported Image Formats

**Reading:** BMP, GIF, JPEG, PNG, TIFF, WBMP

**Writing:** PNG, JPEG, BMP, GIF, TIFF, WBMP

Use `GetReadableImageFormats()` and `GetWriteableImageFormats()` to get the current list.

## Color Support

The module supports both named colors and hex codes:

**Named Colors:** `black`, `blue`, `cyan`, `darkgray`, `gray`, `green`, `lightgray`, `magenta`, `orange`, `pink`, `red`, `white`, `yellow`

**Hex Codes:** `#FF0000` (red), `#00FF00` (green), `#0000FF` (blue), etc.

## Examples by Use Case

### Photo Processing

```js
// Professional photo processing pipeline
ImageNew("raw-photo.jpg")
    .resize(1920, 1080, "bicubic", 0)
    .sharpen(2)
    .setDrawingColor("white")
    .drawText("© 2025 Photo Studio", 20, 1060, {
        font: "Arial",
        size: 16
    })
    .write("final-photo.jpg");
```

### Thumbnail Generation

```js
// Create square thumbnail with cropping
var img = ImageNew("large-image.jpg");
var size = 300;

// Crop to square first
var width = img.getWidth();
var height = img.getHeight();
var cropSize = min(width, height);
var x = (width - cropSize) / 2;
var y = (height - cropSize) / 2;

img.crop(x, y, cropSize, cropSize)
    .resize(size, size)
    .write("thumbnail.jpg");
```

### Batch Processing

```js
// Process all images in directory
var files = directoryList("photos", false, "path", "*.jpg");

for (var file in files) {
    var filename = getFileFromPath(file);

    ImageNew(file)
        .scaleToFit(800, 600)
        .sharpen(1)
        .write("processed/#filename#");
}
```

## Performance Tips

1. **Use method chaining** - Reduces object creation and variable assignments
2. **Choose appropriate interpolation** - `nearest` is fastest, `bicubic` is highest quality
3. **Process dimensions wisely** - Resize before applying filters for better performance
4. **Reuse BoxImage instances** - When processing multiple operations on the same image
5. **Consider memory** - Very large images may require JVM memory tuning

## Additional Resources

- **[BoxLang Documentation](https://boxlang.io/docs)** - Core BoxLang features
- **[CFDocs](https://cfdocs.org/)** - CFML function reference
- **[GitHub Repository](https://github.com/ortus-boxlang/bx-image)** - Source code and issues
- **[Ortus Solutions](https://www.ortussolutions.com)** - Commercial support

## Support & Sponsorship

BoxLang is a professional open-source project funded by the community and Ortus Solutions, Corp.

**Become a Sponsor:** [https://patreon.com/ortussolutions](https://patreon.com/ortussolutions)

**Patreon Benefits:**
- CFCasts account
- FORGEBOX Pro account
- Priority support
- Exclusive content

---

**License:** Apache 2.0 | **Copyright** © 2023 Ortus Solutions, Corp
