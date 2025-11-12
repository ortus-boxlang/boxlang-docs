# Image Transformations

Learn how to resize, rotate, crop, flip, and transform images in BoxLang.

## Table of Contents

- [Resizing Images](#resizing-images)
- [Scaling Images](#scaling-images)
- [Rotating Images](#rotating-images)
- [Cropping Images](#cropping-images)
- [Flipping & Transposing](#flipping--transposing)
- [Shearing](#shearing)
- [Translation](#translation)
- [Drawing Axis Transformations](#drawing-axis-transformations)

## Resizing Images

### Resize to Exact Dimensions

```js
// Resize to exact width and height
ImageNew("photo.jpg")
    .resize(800, 600)
    .write("resized.jpg");

// With interpolation method
ImageNew("photo.jpg")
    .resize(800, 600, "bicubic", 0)
    .write("resized-hq.jpg");
```

**Interpolation Options:**

- `nearest` - Fastest, lowest quality
- `bilinear` - Good balance of speed and quality (default)
- `bicubic` - Highest quality, slower

**BIF Syntax:**

```js
img = ImageRead("photo.jpg");
ImageResize(img, 800, 600);
ImageResize(img, 800, 600, "bicubic");  // High quality
ImageWrite(img, "resized.jpg");
```

## Scaling Images

### Scale to Fit (Proportional)

Scales the image to fit within specified dimensions while maintaining aspect ratio:

```js
// Scale to fit within 800x600 (maintains aspect ratio)
ImageNew("photo.jpg")
    .scaleToFit(800, 600)
    .write("scaled.jpg");

// With interpolation
ImageNew("photo.jpg")
    .scaleToFit(800, 600, "bicubic")
    .write("scaled-hq.jpg");
```

**BIF Syntax:**

```js
img = ImageRead("photo.jpg");
ImageScaleToFit(img, 800, 600);
ImageScaleToFit(img, 800, 600, "bicubic", 0);  // High quality
ImageWrite(img, "scaled.jpg");
```

### Resize vs ScaleToFit

```js
// Resize: Forces exact dimensions (may distort)
ImageNew("photo.jpg")
    .resize(800, 600)     // Exactly 800x600
    .write("resized.jpg");

// ScaleToFit: Maintains aspect ratio (may be smaller)
ImageNew("photo.jpg")
    .scaleToFit(800, 600) // Max 800x600, keeps proportions
    .write("scaled.jpg");
```

**Example:**

If your image is 1600x900 (16:9 aspect ratio):

- `resize(800, 600)` → 800x600 (distorted to 4:3)
- `scaleToFit(800, 600)` → 800x450 (maintains 16:9)

## Rotating Images

### Rotate by Angle

```js
// Rotate 90 degrees clockwise
ImageNew("photo.jpg")
    .rotate(90)
    .write("rotated-90.jpg");

// Rotate 45 degrees
ImageNew("photo.jpg")
    .rotate(45)
    .write("rotated-45.jpg");

// Rotate counter-clockwise (negative angle)
ImageNew("photo.jpg")
    .rotate(-90)
    .write("rotated-ccw.jpg");
```

**BIF Syntax:**

```js
img = ImageRead("photo.jpg");
ImageRotate(img, 90);
ImageWrite(img, "rotated.jpg");
```

**Notes:**

- Positive angles rotate clockwise
- Negative angles rotate counter-clockwise
- Canvas size expands to accommodate rotated image
- Empty areas filled with background color

### Rotate with Interpolation

```js
// High-quality rotation
ImageNew("photo.jpg")
    .rotate(45, "bicubic")
    .write("rotated-hq.jpg");
```

## Cropping Images

### Basic Cropping

```js
// Crop: x, y, width, height
ImageNew("photo.jpg")
    .crop(100, 100, 400, 300)
    .write("cropped.jpg");
```

**BIF Syntax:**

```js
img = ImageRead("photo.jpg");
ImageCrop(img, x=100, y=100, width=400, height=300);
ImageWrite(img, "cropped.jpg");
```

### Center Crop to Square

```js
// Crop image to square from center
img = ImageNew("photo.jpg");
width = img.getWidth();
height = img.getHeight();

// Calculate square crop from center
cropSize = min(width, height);
x = (width - cropSize) / 2;
y = (height - cropSize) / 2;

img.crop(x, y, cropSize, cropSize)
   .write("square.jpg");
```

### Creating Thumbnails with Cropping

```js
// Create 200x200 thumbnail with center crop
img = ImageNew("large-photo.jpg");
width = img.getWidth();
height = img.getHeight();

// Determine crop dimensions
cropSize = min(width, height);
x = (width - cropSize) / 2;
y = (height - cropSize) / 2;

img.crop(x, y, cropSize, cropSize)
   .resize(200, 200)
   .write("thumbnail.jpg");
```

## Flipping & Transposing

### Flip Horizontally

```js
// Mirror image left-to-right
ImageNew("photo.jpg")
    .flip("horizontal")
    .write("flipped-h.jpg");
```

### Flip Vertically

```js
// Mirror image top-to-bottom
ImageNew("photo.jpg")
    .flip("vertical")
    .write("flipped-v.jpg");
```

### Transpose Operations

The `flip()` function supports various transpose operations:

```js
// Horizontal flip
ImageFlip(img, "horizontal");

// Vertical flip
ImageFlip(img, "vertical");

// Rotate 90 degrees
ImageFlip(img, "90");

// Rotate 180 degrees
ImageFlip(img, "180");

// Rotate 270 degrees
ImageFlip(img, "270");

// Diagonal transpose
ImageFlip(img, "diagonal");

// Anti-diagonal transpose
ImageFlip(img, "antidiagonal");
```

**Member Function:**

```js
ImageNew("photo.jpg")
    .flip("horizontal")
    .write("mirrored.jpg");
```

## Shearing

Shearing skews the image along an axis:

### Shear Horizontally

```js
// Shear along width (horizontal skew)
ImageNew("photo.jpg")
    .shear(0.5, "width")
    .write("sheared-h.jpg");
```

### Shear Vertically

```js
// Shear along height (vertical skew)
ImageNew("photo.jpg")
    .shear(0.5, "height")
    .write("sheared-v.jpg");
```

**BIF Syntax:**

```js
img = ImageRead("photo.jpg");
ImageShear(img, shear=0.5, direction="width");
ImageWrite(img, "sheared.jpg");
```

**Shear Amount:**

- Positive values shear in one direction
- Negative values shear in opposite direction
- Typical range: -1.0 to 1.0

## Translation

Translation moves the image within its canvas:

```js
// Translate (move) image: x-offset, y-offset
ImageNew("photo.jpg")
    .translate(50, 100)
    .write("translated.jpg");
```

**BIF Syntax:**

```js
img = ImageRead("photo.jpg");
ImageTranslate(img, x=50, y=100);
ImageWrite(img, "translated.jpg");
```

**Use Cases:**

- Adjusting image position
- Creating padding/margins
- Aligning images for compositing

## Drawing Axis Transformations

These transformations affect the coordinate system for subsequent **drawing** operations, not the image itself.

### Translate Drawing Axis

Moves the origin point for drawing operations:

```js
img = ImageNew(400, 300, "rgb", "white");

// Move origin to center
img.translateDrawingAxis(200, 150);

// Now (0,0) is at image center
img.setDrawingColor("red");
img.drawRect(0, 0, 50, 50, true);  // Draws at center

img.write("translated-axis.jpg");
```

**BIF Syntax:**

```js
ImageTranslateDrawingAxis(img, x=200, y=150);
```

### Rotate Drawing Axis

Rotates the coordinate system for drawing:

```js
img = ImageNew(400, 300, "rgb", "white");

// Rotate drawing axis 45 degrees
img.rotateDrawingAxis(45);

// Subsequent drawing operations are rotated
img.setDrawingColor("blue");
img.drawRect(100, 100, 100, 50, true);

img.write("rotated-axis.jpg");
```

**BIF Syntax:**

```js
ImageRotateDrawingAxis(img, angle=45);
```

### Shear Drawing Axis

Shears the coordinate system for drawing:

```js
img = ImageNew(400, 300, "rgb", "white");

// Shear drawing axis
img.shearDrawingAxis(0.3, 0.1);

// Drawing operations will be sheared
img.setDrawingColor("green");
img.drawRect(50, 50, 100, 100, false);

img.write("sheared-axis.jpg");
```

**BIF Syntax:**

```js
ImageShearDrawingAxis(img, shearX=0.3, shearY=0.1);
```

### Why Use Drawing Axis Transformations?

Drawing axis transformations are useful for:

1. **Creating rotated text/graphics** without rotating the entire image
2. **Perspective effects** using shearing
3. **Complex compositions** with transformed coordinate systems
4. **Efficient drawing** - transform once, draw many times

## Complete Transformation Examples

### Create Multiple Sizes

```js
// Generate multiple image sizes from one source
original = ImageNew("photo.jpg");

// Thumbnail
original.copy().scaleToFit(200, 200).write("thumb.jpg");

// Medium
original.copy().scaleToFit(800, 600).write("medium.jpg");

// Large
original.copy().scaleToFit(1920, 1080).write("large.jpg");
```

### Rotate and Crop

```js
// Rotate then crop to remove empty corners
ImageNew("photo.jpg")
    .rotate(15)
    .crop(100, 100, 600, 400)
    .write("rotated-cropped.jpg");
```

### Scale, Crop, and Sharpen

```js
// Professional thumbnail generation
ImageNew("raw-photo.jpg")
    .scaleToFit(400, 400)
    .crop(0, 0, 300, 300)
    .sharpen(1.5)
    .write("thumbnail.jpg");
```

### Flip and Transform

```js
// Create mirror effect
ImageNew("photo.jpg")
    .flip("horizontal")
    .translate(20, 0)
    .write("mirrored.jpg");
```

## Performance Tips

1. **Resize before other operations** - Smaller images process faster
2. **Choose interpolation wisely:**
   - Use `nearest` for pixel art or when speed is critical
   - Use `bilinear` for good balance (default)
   - Use `bicubic` only when quality is paramount
3. **Batch transformations** - Apply multiple operations before saving
4. **Use scaleToFit()** instead of manual ratio calculations

## Next Steps

- **[Filters & Effects](filters-effects.md)** - Apply blur, sharpen, and color effects
- **[Drawing](drawing.md)** - Add shapes, lines, and text
- **[Advanced Examples](advanced-examples.md)** - Real-world transformation pipelines
