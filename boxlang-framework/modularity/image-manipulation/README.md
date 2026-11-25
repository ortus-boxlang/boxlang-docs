---
description: Comprehensive documentation for the BoxLang Image Module, including installation, usage examples, and API reference.
icon: image
---

# BoxLang Image Module

## Overview

The BoxLang Image Module provides comprehensive image manipulation functionality for BoxLang applications. It offers a rich set of Built-In Functions (BIFs), a fluent `BoxImage` builder, and a tag-based Component for maximum flexibility in how you work with images.

**Key Features:**

- 🖼️ **70 Image BIFs** - Image processing with familiar Adobe ColdFusion and Lucee APIs
- 🎨 **Drawing Operations** - Lines, shapes, curves, text with advanced styling
- ✨ **Filters & Effects** - Blur, sharpen, grayscale, negative, overlay
- 📐 **Transformations** - Resize, rotate, crop, flip, shear, scale
- 📊 **Metadata Support** - Read, write, and strip EXIF, IPTC, XMP, and ICC data; lossless file-level edits
- 🔗 **Fluent API** - Method chaining with the `BoxImage` builder
- 🔳 **QR Codes** - Generate and read QR codes with custom colors and an optional logo
- 🖋️ **SVG Support** - Read SVG files, rendered sharply at the size you ask for
- 🔬 **Pixel Access** - Read every pixel as brightness values or RGBA arrays with `ImageGetPixels()`
- ⚡ **Runs on MatchBox** - A native backend in the same module runs the core functions without a JVM
- 🏷️ **Component** - Tag-based syntax for templates
- 🎯 **Member Functions** - Image operations available as convenient member functions

## 🆕 New in 1.17.0

- Edit metadata without decoding or re-encoding pixels with `ImageReadMetadata()` and `ImageStripMetadata()`.
- Set EXIF/IPTC tags and XMP on files, metadata handles, or image objects; use a handle for ICC profiles.
- Read embedded EXIF/IPTC from `ImageReadBase64()` results.
- Use path-based metadata getters safely before in-place edits on Windows, including paths with spaces and `file:` URIs.

See the [metadata guide](metadata.md) for persistence rules and format support. These additions require the JVM backend; [MatchBox's supported API](matchbox.md) is unchanged.

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
- ✅ Transformation, drawing, and image metadata setters available as methods

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

- BoxLang 1.6.0 or higher
- Java 21+

To run on [MatchBox](matchbox.md) without a JVM, install the same module: it includes the native backend for Linux x86-64.

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
- **[Metadata](metadata.md)** - EXIF/IPTC/XMP/ICC reading, writing, and lossless stripping
- **[Utilities](utilities.md)** - Format support, pixel access, validation, color reference
- **[MatchBox Native Backend](matchbox.md)** - Running bx-image code without a JVM
- **[Advanced Examples](advanced-examples.md)** - Watermarking, thumbnails, batch processing
- **[BIF Reference](reference/README.md)** - Complete alphabetical BIF listing
- **[Migration Guide](migration-guide.md)** - Migrating from Adobe ColdFusion/Lucee

## BIF & Component Reference

### All Available BIFs (70 Functions)

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
| `ImageGenerateCaptcha()` | - | Creation | Generates a CAPTCHA image from text |
| `ImageGetBlob()` | `image.getBlob()` | Utility | Returns image as byte array |
| `ImageGetBufferedImage()` | `image.getBufferedImage()` | Utility | Returns Java BufferedImage object |
| `ImageGetExifMetaData()` | `image.getExifMetaData()` | Metadata | Returns EXIF metadata struct |
| `ImageGetExifTag()` | `image.getExifTag()` | Metadata | Returns specific EXIF tag value |
| `ImageGetHeight()` | `image.getHeight()` | Utility | Returns image height in pixels |
| `ImageGetIPTCMetadata()` | `image.getIPTCMetadata()` | Metadata | Returns IPTC metadata struct |
| `ImageGetIPTCTag()` | `image.getIPTCTag()` | Metadata | Returns specific IPTC tag value |
| `ImageGetPixels()` | `image.getPixels()` | Utility | Returns every pixel as luma values or RGBA arrays |
| `ImageGetWidth()` | `image.getWidth()` | Utility | Returns image width in pixels |
| `ImageGrayScale()` / `ImageGreyScale()` | `image.grayScale()` | Filter | Converts image to grayscale |
| `ImageInfo()` | `image.info()` | Utility | Returns comprehensive image information |
| `ImageMeasureText()` | `image.measureText()` | Drawing | Measures the rendered size of a line of text |
| `ImageNegative()` | `image.negative()` | Filter | Inverts image colors (negative) |
| `ImageNew()` | - | Creation | Creates new image or reads from source |
| `ImageOverlay()` | `image.overlay()` | Filter | Overlays one image on another |
| `ImagePaste()` / `ImageDrawImage()` | `image.paste()` | Drawing | Pastes/draws one image onto another |
| `ImageQRCodeGenerate()` | `"text".toQRCode()` | Creation | Generates a QR code image from text |
| `ImageQRCodeRead()` | `image.readQRCode()` | Output | Reads the text from a QR code in an image |
| `ImageRead()` | - | Creation | Reads image from file path or URL, optionally at a given size |
| `ImageReadBase64()` | - | Creation | Creates image from Base64 string |
| `ImageRegisterFont()` | - | Drawing | Registers a `.ttf` or `.otf` font file for drawing text |
| `ImageResize()` | `image.resize()` | Transform | Resizes image; a blank or 0 side keeps the aspect ratio |
| `ImageRotate()` | `image.rotate()` | Transform | Rotates image by specified angle |
| `ImageRotateDrawingAxis()` | `image.rotateDrawingAxis()` | Drawing | Rotates coordinate system for drawing |
| `ImageScaleToFit()` | `image.scaleToFit()` | Transform | Scales image proportionally to fit dimensions |
| `ImageSetAntiAliasing()` | `image.setAntiAliasing()` | Drawing | Enables/disables anti-aliasing |
| `ImageSetBackgroundColor()` | `image.setBackgroundColor()` | Drawing | Sets background color |
| `ImageSetDrawingColor()` | `image.setDrawingColor()` | Drawing | Sets color for drawing operations |
| `ImageSetDrawingGradient()` | `image.setDrawingGradient()` | Drawing | Sets a linear gradient as the drawing paint |
| `ImageSetDrawingStroke()` | `image.setDrawingStroke()` | Drawing | Configures line stroke properties |
| `ImageSetDrawingTransparency()` | `image.setDrawingTransparency()` | Drawing | Sets transparency for drawing |
| `ImageSharpen()` | `image.sharpen()` | Filter | Sharpens image edges |
| `ImageShear()` | `image.shear()` | Transform | Shears/skews image |
| `ImageShearDrawingAxis()` | `image.shearDrawingAxis()` | Drawing | Shears coordinate system for drawing |
| `ImageSplitGrid()` | `image.splitGrid()` | Transform | Splits an image into a grid of tiles |
| `ImageTranslate()` | `image.translate()` | Transform | Translates/moves image |
| `ImageTranslateDrawingAxis()` | `image.translateDrawingAxis()` | Drawing | Translates origin for drawing |
| `ImageWrite()` | `image.write()` | Output | Writes image to file |
| `ImageWriteBase64()` | `image.writeBase64()` | Output | Returns image as Base64 string |
| [`ImageReadMetadata()`](reference/built-in-functions/imagereadmetadata.md) | - | Metadata | Read a metadata handle without decoding pixels |
| [`ImageStripMetadata()`](reference/built-in-functions/imagestripmetadata.md) | - | Metadata | Strip file metadata without re-encoding |
| [`ImageSetExifTag()`](reference/built-in-functions/imagesetexiftag.md) | `image.setExifTag()` | Metadata | Set one EXIF tag |
| [`ImageSetExifMetaData()`](reference/built-in-functions/imagesetexifmetadata.md) | `image.setExifMetaData()` | Metadata | Set EXIF tags from a struct |
| [`ImageSetIPTCTag()`](reference/built-in-functions/imagesetiptctag.md) | `image.setIPTCTag()` | Metadata | Set one IPTC tag |
| [`ImageSetIPTCMetaData()`](reference/built-in-functions/imagesetiptcmetadata.md) | `image.setIPTCMetaData()` | Metadata | Set IPTC tags from a struct |
| [`ImageSetXMP()`](reference/built-in-functions/imagesetxmp.md) | `image.setXMP()` | Metadata | Replace the XMP packet |
| [`ImageGetXMP()`](reference/built-in-functions/imagegetxmp.md) | `image.getXMP()` | Metadata | Read the XMP packet |
| [`ImageRemoveMetadata()`](reference/built-in-functions/imageremovemetadata.md) | `image.removeMetadata()` | Metadata | Remove metadata types |
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

**Reading:** BMP, GIF, JPEG, PNG, SVG, TIFF, WBMP, WebP

**Writing:** PNG, JPEG, BMP, GIF, TIFF, WBMP, WebP

SVG files are rendered to an image when read. Read them at the size you need, `ImageRead( "logo.svg", 400 )`, so they stay sharp.

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

## 📦 Metadata Library and License

The JVM module bundles [pixymeta 1.4.0](https://github.com/akitogo/pixymeta/tree/v1.4.0) unmodified for metadata writing. It is licensed under **EPL-1.0**; the distribution includes its license in `licenses/pixymeta-EPL-1.0.txt`. No separate library installation is needed.

## Additional Resources

- **[BoxLang Documentation](https://boxlang.ortusbooks.com)** - Core BoxLang features
- **[CFDocs](https://cfdocs.org/)** - CFML function reference
- **[GitHub Repository](https://github.com/ortus-boxlang/bx-image)** - Source code and issues
- **[Ortus Solutions](https://www.ortussolutions.com)** - Commercial support
