# Getting Started with BoxLang Image

This guide will help you get up and running with image manipulation in BoxLang.

## Table of Contents

- [Creating Images](#creating-images)
- [Reading Images](#reading-images)
- [Basic Operations](#basic-operations)
- [Method Chaining](#method-chaining)
- [Saving Images](#saving-images)
- [Working with BoxImage](#working-with-boximage)

## Creating Images

There are several ways to create or load images in BoxLang:

### From a File Path

```js
// Using ImageRead()
img = ImageRead("path/to/image.jpg");

// Using ImageNew() - recommended
img = ImageNew("path/to/image.jpg");
```

### From a URL

```js
// Load image from remote URL
img = ImageNew("https://example.com/photo.jpg");
```

### Create a Blank Canvas

```js
// Create blank image: width, height, type, color
img = ImageNew(800, 600, "rgb", "white");

// Available types: "rgb", "argb" (with alpha), "grayscale"
```

### From Base64 String

```js
// Load from Base64 encoded string
base64String = "iVBORw0KGgoAAAANS...";
img = ImageReadBase64(base64String);
```

### From Java BufferedImage

```js
// If you have a Java BufferedImage object
bufferedImage = someJavaImageObject;
img = ImageNew(bufferedImage);
```

## Reading Images

### ImageRead() vs ImageNew()

Both functions read images, but `ImageNew()` is more versatile:

```js
// ImageRead() - traditional CFML
img = ImageRead("photo.jpg");

// ImageNew() - BoxLang (recommended)
// Supports same sources plus blank canvas creation
img = ImageNew("photo.jpg");
```

### Supported Source Types

```js
// File path
img = ImageNew("images/photo.jpg");
img = ImageNew("/absolute/path/to/photo.jpg");

// URL
img = ImageNew("https://cdn.example.com/image.jpg");

// URI
img = ImageNew(createObject("java", "java.net.URI").create("file:///path/to/image.jpg"));

// Blank canvas
img = ImageNew(width=1024, height=768);
```

## Basic Operations

### Get Image Information

```js
img = ImageNew("photo.jpg");

// Get dimensions
width = ImageGetWidth(img);
height = ImageGetHeight(img);

// Or using member functions
width = img.getWidth();
height = img.getHeight();

// Get comprehensive info
info = ImageInfo(img);
// Returns struct with: width, height, colorModel, source, etc.
```

### Check Image Properties

```js
// Validate if variable is an image
if (IsImage(img)) {
    // Work with image
}

// Check if file is an image
if (IsImageFile("photo.jpg")) {
    img = ImageNew("photo.jpg");
}
```

### Get Supported Formats

```js
// Get list of readable formats
readableFormats = GetReadableImageFormats();
// Returns: ["BMP", "GIF", "JPEG", "PNG", "TIFF", "WBMP"]

// Get list of writable formats
writeableFormats = GetWriteableImageFormats();
// Returns: ["BMP", "GIF", "JPEG", "PNG", "TIFF", "WBMP"]
```

## Method Chaining

One of the most powerful features is method chaining with BoxImage:

### Traditional BIF Approach

```js
// Multiple function calls with variable reassignment
img = ImageRead("photo.jpg");
ImageResize(img, 800, 600);
ImageGrayScale(img);
ImageSharpen(img, 2);
ImageWrite(img, "output.jpg");
```

### Fluent BoxImage Approach (Recommended)

```js
// Clean, chainable syntax
ImageNew("photo.jpg")
    .resize(800, 600)
    .grayScale()
    .sharpen(2)
    .write("output.jpg");
```

### Why Method Chaining?

**Benefits:**

1. **Cleaner Code** - More readable and concise
2. **Less Variables** - No need to store intermediate results
3. **Natural Flow** - Operations flow from left to right, top to bottom
4. **IDE Support** - Better autocomplete and IntelliSense
5. **Immutable Operations** - Each method returns the modified image

### Mixing Approaches

You can mix BIF and member function syntax:

```js
// Create with ImageNew, then use member functions
var img = ImageNew("photo.jpg");
img.resize(800, 600).grayScale();

// Or use BIFs on the result
ImageSharpen(img, 2);
ImageWrite(img, "output.jpg");
```

## Saving Images

### Write to File

```js
// Save image to file (auto-creates directories)
img = ImageNew("photo.jpg");
ImageWrite(img, "output/processed.jpg");

// Or using member function
img.write("output/processed.jpg");
```

### Convert to Base64

```js
// Get Base64 encoded string
img = ImageNew("photo.jpg");
base64String = ImageWriteBase64(img);

// Use in HTML
html = "<img src='data:image/png;base64,#base64String#' />";
```

### Get as Byte Array

```js
// Get image data as bytes
img = ImageNew("photo.jpg");
bytes = ImageGetBlob(img);

// Useful for streaming or storing in database
```

### Get Java BufferedImage

```js
// Get underlying Java BufferedImage object
img = ImageNew("photo.jpg");
bufferedImage = ImageGetBufferedImage(img);

// Useful for integration with Java libraries
```

## Working with BoxImage

The `BoxImage` class is a fluent wrapper that makes image manipulation intuitive and powerful.

### Creating BoxImage Instances

```js
// All of these return a BoxImage instance:

// From file
img = ImageNew("photo.jpg");

// From URL
img = ImageNew("https://example.com/image.jpg");

// Blank canvas
img = ImageNew(800, 600, "argb", "white");

// From Base64
img = ImageReadBase64(base64String);

// Using ImageRead (also returns BoxImage)
img = ImageRead("photo.jpg");
```

### BoxImage is Mutable and Chainable

```js
// Each operation modifies the image and returns 'this'
var img = ImageNew(400, 300, "rgb", "blue");

// These all modify the same instance
img.resize(800, 600)    // Returns img
   .blur(5)             // Returns img
   .grayScale()         // Returns img
   .write("out.jpg");   // Returns img

// img variable now holds the final processed image
```

### Copying Images

```js
// Create a copy before modifying
original = ImageNew("photo.jpg");
modified = ImageCopy(original);

// Now modify the copy
modified.grayScale().blur(3);

// original is unchanged
// or use the member function
modified = original.copy();
```

### Complete Example

```js
// Load, process, and save in multiple formats
var original = ImageNew("raw-photo.jpg");

// Create thumbnail
original.copy()
    .scaleToFit(200, 200)
    .sharpen(1)
    .write("thumbnail.jpg");

// Create grayscale version
original.copy()
    .grayScale()
    .sharpen(1.5)
    .write("grayscale.jpg");

// Create blurred background
original.copy()
    .blur(10)
    .write("background.jpg");

// Original is still unmodified
```

## Quick Reference

### Essential BIFs

| Function | Purpose | Example |
|----------|---------|---------|
| `ImageNew()` | Create/load image | `ImageNew("photo.jpg")` |
| `ImageRead()` | Load from file | `ImageRead("photo.jpg")` |
| `ImageWrite()` | Save to file | `ImageWrite(img, "out.jpg")` |
| `ImageInfo()` | Get image details | `ImageInfo(img)` |
| `ImageGetWidth()` | Get width | `ImageGetWidth(img)` |
| `ImageGetHeight()` | Get height | `ImageGetHeight(img)` |
| `IsImage()` | Check if image | `IsImage(img)` |
| `IsImageFile()` | Check if file is image | `IsImageFile("photo.jpg")` |

### Essential Member Functions

```js
// All BIFs available as member functions
img = ImageNew("photo.jpg");

img.getWidth()              // Get width
img.getHeight()             // Get height
img.write("out.jpg")        // Save
img.copy()                  // Create copy
img.resize(800, 600)        // Resize
img.crop(0, 0, 400, 300)    // Crop
img.grayScale()             // Convert to grayscale
img.blur(5)                 // Apply blur
```

## Next Steps

Now that you understand the basics, explore more advanced topics:

- **[Transformations](transformations.md)** - Resize, rotate, crop, flip
- **[Filters & Effects](filters-effects.md)** - Blur, sharpen, overlay
- **[Drawing](drawing.md)** - Draw shapes, lines, and text
- **[Metadata](metadata.md)** - Read EXIF and IPTC data
- **[Advanced Examples](advanced-examples.md)** - Real-world use cases
