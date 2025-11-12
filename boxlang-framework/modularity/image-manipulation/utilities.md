# Utilities & Reference

Image properties, format support, validation functions, and color reference.

## Table of Contents

- [Image Properties](#image-properties)
- [Format Support](#format-support)
- [Validation Functions](#validation-functions)
- [Color Reference](#color-reference)
- [Image Information](#image-information)
- [Binary Operations](#binary-operations)

## Image Properties

### Get Image Dimensions

```js
img = ImageNew("photo.jpg");

// Get width and height
width = img.getWidth();    // Member function
height = img.getHeight();  // Member function

// BIF syntax
width = ImageGetWidth(img);
height = ImageGetHeight(img);

writeln("Image is #width# x #height# pixels");
```

### Check Image Type

```js
// Check if variable is an image
if (IsImage(img)) {
    writeln("Variable contains an image");
}

// Check if file is a valid image
if (IsImageFile("photo.jpg")) {
    img = ImageNew("photo.jpg");
}
```

### Get Comprehensive Info

```js
img = ImageNew("photo.jpg");
info = img.info();  // or ImageInfo(img)

// Returns struct with:
// - width: Image width in pixels
// - height: Image height in pixels
// - colorModel: Color model (RGB, ARGB, etc.)
// - source: Source path or URL
// - and more...

writeDump(info);
```

## Format Support

### Get Readable Formats

```js
// Get list of formats that can be read
readableFormats = GetReadableImageFormats();

// Returns array: ["BMP", "GIF", "JPEG", "PNG", "TIFF", "WBMP"]

writeDump(readableFormats);
```

### Get Writeable Formats

```js
// Get list of formats that can be written
writeableFormats = GetWriteableImageFormats();

// Returns array: ["BMP", "GIF", "JPEG", "PNG", "TIFF", "WBMP"]

writeDump(writeableFormats);
```

### Check Format Support

```js
function canProcessFormat(extension) {
    var readable = GetReadableImageFormats();
    return arrayFindNoCase(readable, extension) > 0;
}

if (canProcessFormat("PNG")) {
    writeln("PNG format is supported");
}
```

### Supported Formats Reference

| Format | Read | Write | Notes |
|--------|------|-------|-------|
| **BMP** | ✅ | ✅ | Bitmap, no compression |
| **GIF** | ✅ | ✅ | Supports transparency, animation |
| **JPEG** | ✅ | ✅ | Lossy compression, no transparency |
| **PNG** | ✅ | ✅ | Lossless, supports transparency |
| **TIFF** | ✅ | ✅ | High quality, large files |
| **WBMP** | ✅ | ✅ | Wireless bitmap, monochrome |

**Notes:**

- **PNG** - Best for web, supports transparency
- **JPEG** - Best for photos, smaller file size
- **GIF** - Best for animations, limited colors
- **TIFF** - Best for archival, printing
- **BMP** - Uncompressed, large files

## Validation Functions

### IsImage()

Check if a variable contains an image object:

```js
img = ImageNew("photo.jpg");

if (IsImage(img)) {
    writeln("Variable is an image");
    writeln("Size: #img.getWidth()# x #img.getHeight()#");
}

// Not an image
notImage = "hello";
if (!IsImage(notImage)) {
    writeln("Not an image");
}
```

### IsImageFile()

Check if a file is a valid image without loading it:

```js
// Check single file
if (IsImageFile("photo.jpg")) {
    img = ImageNew("photo.jpg");
} else {
    writeln("Not a valid image file");
}

// Filter directory for images
files = directoryList("uploads", false, "path");
imageFiles = [];

for (file in files) {
    if (IsImageFile(file)) {
        arrayAppend(imageFiles, file);
    }
}

writeln("Found #arrayLen(imageFiles)# images");
```

### Validation Examples

```js
// Validate before processing
function processImage(filePath) {
    if (!fileExists(filePath)) {
        throw("File does not exist: #filePath#");
    }

    if (!IsImageFile(filePath)) {
        throw("File is not a valid image: #filePath#");
    }

    img = ImageNew(filePath);

    // Check dimensions
    if (img.getWidth() < 100 || img.getHeight() < 100) {
        throw("Image too small (minimum 100x100)");
    }

    return img;
}
```

## Color Reference

### Named Colors

The module supports these named colors:

```js
img = ImageNew(400, 300, "rgb", "white");

// Set drawing color using names
img.setDrawingColor("red");
img.setDrawingColor("blue");
img.setDrawingColor("green");
```

**Available Named Colors:**

| Color | Hex Value | Color | Hex Value |
|-------|-----------|-------|-----------|
| `black` | #000000 | `white` | #FFFFFF |
| `red` | #FF0000 | `green` | #00FF00 |
| `blue` | #0000FF | `cyan` | #00FFFF |
| `magenta` | #FF00FF | `yellow` | #FFFF00 |
| `orange` | #FFA500 | `pink` | #FFC0CB |
| `gray` | #808080 | `darkgray` | #A9A9A9 |
| `lightgray` | #D3D3D3 | | |

### Hex Colors

```js
// Use hex color codes
img.setDrawingColor("#FF0000");  // Red
img.setDrawingColor("#00FF00");  // Green
img.setDrawingColor("#0000FF");  // Blue

// With alpha (8-digit hex)
img.setDrawingColor("#FF0000FF");  // Opaque red
img.setDrawingColor("#FF000080");  // Semi-transparent red
```

### Color Format Examples

```js
img = ImageNew(400, 300, "rgb", "white");

// All these are equivalent (red)
img.setDrawingColor("red");
img.setDrawingColor("#FF0000");
img.setDrawingColor("#ff0000");  // Case insensitive

// Create custom colors
img.setDrawingColor("#FF6B6B");  // Light red
img.setDrawingColor("#4ECDC4");  // Turquoise
img.setDrawingColor("#95E1D3");  // Mint
```

## Image Information

### ImageInfo() Structure

```js
img = ImageNew("photo.jpg");
info = ImageInfo(img);

// Returns struct with these keys:
info = {
    width: 1920,
    height: 1080,
    colorModel: {
        colorSpace: "RGB",
        numColorComponents: 3,
        hasAlpha: false,
        transparency: "OPAQUE",
        pixelSize: 24
    },
    source: "C:\path\to\photo.jpg"
};
```

### Color Model Types

```js
// RGB - Standard color image
img = ImageNew(800, 600, "rgb", "white");

// ARGB - Color with alpha channel
img = ImageNew(800, 600, "argb", "transparent");

// Grayscale - Black and white
img = ImageNew(800, 600, "grayscale", "white");
```

## Binary Operations

### Get Image as Byte Array

```js
img = ImageNew("photo.jpg");

// Get bytes
bytes = img.getBytes();  // or ImageGetBlob(img)

// Useful for:
// - Streaming images
// - Storing in database
// - Sending via HTTP

writeln("Image size: #arrayLen(bytes)# bytes");
```

### Get Java BufferedImage

```js
img = ImageNew("photo.jpg");

// Get underlying Java BufferedImage
bufferedImage = img.getBufferedImage();
// or ImageGetBufferedImage(img)

// Useful for integration with Java libraries
```

### Base64 Encoding

```js
img = ImageNew("photo.jpg");

// Convert to Base64
base64String = ImageWriteBase64(img);

// Use in HTML
html = "<img src='data:image/png;base64,#base64String#' />";

// Or decode back
img2 = ImageReadBase64(base64String);
```

## Utility Functions Reference

| Function | Purpose | Example |
|----------|---------|---------|
| `GetReadableImageFormats()` | List readable formats | `["BMP", "GIF", ...]` |
| `GetWriteableImageFormats()` | List writable formats | `["BMP", "GIF", ...]` |
| `ImageGetWidth(img)` | Get width in pixels | `1920` |
| `ImageGetHeight(img)` | Get height in pixels | `1080` |
| `ImageInfo(img)` | Get full image info | `{width: 1920, ...}` |
| `ImageGetBlob(img)` | Get byte array | `[binary data]` |
| `ImageGetBufferedImage(img)` | Get Java BufferedImage | Java object |
| `IsImage(var)` | Check if variable is image | `true/false` |
| `IsImageFile(path)` | Check if file is image | `true/false` |

## Complete Utility Examples

### Image File Browser

```js
function getImageGallery(directory) {
    var files = directoryList(directory, false, "path");
    var images = [];

    for (var file in files) {
        if (IsImageFile(file)) {
            var img = ImageNew(file);
            var info = ImageInfo(img);

            arrayAppend(images, {
                path: file,
                filename: getFileFromPath(file),
                width: info.width,
                height: info.height,
                size: info.source.size,
                thumbnail: createThumbnail(file)
            });
        }
    }

    return images;
}
```

### Format Converter

```js
function convertImageFormat(sourcePath, targetFormat) {
    // Validate format
    var writeable = GetWriteableImageFormats();
    if (arrayFindNoCase(writeable, targetFormat) == 0) {
        throw("Unsupported format: #targetFormat#");
    }

    // Load and convert
    var img = ImageNew(sourcePath);
    var targetPath = replaceNoCase(sourcePath,
        listLast(sourcePath, "."),
        lCase(targetFormat),
        "one");

    img.write(targetPath);
    return targetPath;
}

// Convert PNG to JPEG
convertImageFormat("logo.png", "JPEG");
```

### Image Validator

```js
function validateUploadedImage(filePath, maxWidth, maxHeight, maxSizeKB) {
    var errors = [];

    // Check file exists
    if (!fileExists(filePath)) {
        arrayAppend(errors, "File does not exist");
        return errors;
    }

    // Check is image
    if (!IsImageFile(filePath)) {
        arrayAppend(errors, "File is not a valid image");
        return errors;
    }

    // Check format
    var extension = listLast(filePath, ".");
    var readable = GetReadableImageFormats();
    if (arrayFindNoCase(readable, extension) == 0) {
        arrayAppend(errors, "Unsupported format: #extension#");
    }

    // Check dimensions
    var img = ImageNew(filePath);
    if (img.getWidth() > maxWidth) {
        arrayAppend(errors, "Image width exceeds #maxWidth#px");
    }
    if (img.getHeight() > maxHeight) {
        arrayAppend(errors, "Image height exceeds #maxHeight#px");
    }

    // Check file size
    var sizeKB = img.getBytes().len() / 1024;
    if (sizeKB > maxSizeKB) {
        arrayAppend(errors, "File size exceeds #maxSizeKB#KB");
    }

    return errors;
}
```

### Batch Format Detection

```js
// Detect and group images by format
files = directoryList("uploads", true, "path");
byFormat = {};

for (file in files) {
    if (IsImageFile(file)) {
        ext = uCase(listLast(file, "."));

        if (!structKeyExists(byFormat, ext)) {
            byFormat[ext] = [];
        }

        arrayAppend(byFormat[ext], file);
    }
}

// Report
for (format in byFormat) {
    writeln("#format#: #arrayLen(byFormat[format])# files");
}
```

## Next Steps

- **[Getting Started](getting-started.md)** - Basic image operations
- **[Advanced Examples](advanced-examples.md)** - Real-world use cases
- **[BIF Reference](bif-reference.md)** - Complete function reference
