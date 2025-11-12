# Filters & Effects

Apply visual effects like blur, sharpen, grayscale, and color adjustments to your images.

## Table of Contents

- [Color Adjustments](#color-adjustments)
- [Blur Effects](#blur-effects)
- [Sharpen Effects](#sharpen-effects)
- [Image Compositing](#image-compositing)
- [Combining Effects](#combining-effects)

## Color Adjustments

### Grayscale Conversion

Convert color images to grayscale (black and white):

```js
// Convert to grayscale
ImageNew("colorful.jpg")
    .grayScale()
    .write("grayscale.jpg");
```

**BIF Syntax:**

```js
img = ImageRead("colorful.jpg");
ImageGrayScale(img);  // or ImageGreyScale(img) for British English
ImageWrite(img, "grayscale.jpg");
```

**Use Cases:**

- Black and white photography effects
- Reducing file size
- Preparing images for printing
- Artistic effects

### Negative/Invert

Invert all colors to create a negative effect:

```js
// Create negative (invert colors)
ImageNew("photo.jpg")
    .negative()
    .write("negative.jpg");
```

**BIF Syntax:**

```js
img = ImageRead("photo.jpg");
ImageNegative(img);
ImageWrite(img, "negative.jpg");
```

**How it works:**

- Each RGB value is subtracted from 255
- Red becomes cyan, green becomes magenta, etc.
- Alpha transparency is preserved

## Blur Effects

### Gaussian Blur

Apply Gaussian blur filter to soften or smooth images:

```js
// Light blur
ImageNew("photo.jpg")
    .blur(3)
    .write("blurred-light.jpg");

// Heavy blur
ImageNew("photo.jpg")
    .blur(10)
    .write("blurred-heavy.jpg");
```

**BIF Syntax:**

```js
img = ImageRead("photo.jpg");
ImageBlur(img, radius=5);
ImageWrite(img, "blurred.jpg");
```

**Radius Parameter:**

- `1-3` - Subtle blur, slight softening
- `4-7` - Moderate blur, noticeable effect
- `8-15` - Heavy blur, significant softening
- `15+` - Extreme blur, very soft/dreamy

**Use Cases:**

- Creating background effects
- Softening skin in portraits
- Reducing noise
- Creating depth of field effects
- Privacy (blurring faces/text)

### Blur Examples

```js
// Subtle blur for skin smoothing
ImageNew("portrait.jpg")
    .blur(2)
    .write("smoothed.jpg");

// Create blurred background
ImageNew("photo.jpg")
    .blur(15)
    .write("background.jpg");

// Privacy blur
ImageNew("screenshot.jpg")
    .crop(100, 100, 300, 50)  // Select area
    .blur(20)                  // Heavy blur
    .write("redacted.jpg");
```

## Sharpen Effects

### Image Sharpening

Enhance edge definition and detail:

```js
// Light sharpening
ImageNew("photo.jpg")
    .sharpen(1)
    .write("sharpened-light.jpg");

// Heavy sharpening
ImageNew("photo.jpg")
    .sharpen(5)
    .write("sharpened-heavy.jpg");
```

**BIF Syntax:**

```js
img = ImageRead("photo.jpg");
ImageSharpen(img, gain=2);
ImageWrite(img, "sharpened.jpg");
```

**Gain Parameter:**

- `0.5-1.5` - Subtle sharpening, natural look
- `1.5-3` - Moderate sharpening, enhanced detail
- `3-5` - Heavy sharpening, very pronounced edges
- `5+` - Extreme sharpening (may introduce artifacts)

**Use Cases:**

- Enhancing photos after resizing
- Improving focus appearance
- Compensating for camera blur
- Preparing images for print

**⚠️ Warning:** Over-sharpening can create halos and artifacts. Use moderation.

### Sharpen Examples

```js
// Sharpen after resize
ImageNew("large-photo.jpg")
    .scaleToFit(800, 600)
    .sharpen(1.5)
    .write("resized-sharp.jpg");

// Enhance product photo
ImageNew("product.jpg")
    .sharpen(2)
    .write("product-enhanced.jpg");

// Aggressive sharpening for technical drawings
ImageNew("blueprint.jpg")
    .sharpen(4)
    .write("blueprint-sharp.jpg");
```

## Image Compositing

### Overlay Images

Blend one image on top of another with transparency:

```js
// Load base and overlay images
base = ImageNew("background.jpg");
logo = ImageNew("watermark.png");

// Overlay with 80% opacity
base.overlay(logo, "normal", 0.8)
    .write("watermarked.jpg");
```

**BIF Syntax:**

```js
base = ImageRead("background.jpg");
overlay = ImageRead("watermark.png");
ImageOverlay(base, overlay, "normal", 0.8);
ImageWrite(base, "watermarked.jpg");
```

**Parameters:**

- **overlayImage** - The image to overlay
- **compositeRule** - Blend mode (see below)
- **transparency** - 0.0 (transparent) to 1.0 (opaque)

**Composite Rules:**

- `normal` - Standard overlay (default)
- `multiply` - Darkens by multiplying colors
- `screen` - Lightens by inverting, multiplying, and inverting
- `overlay` - Combines multiply and screen
- `darken` - Uses darker of two colors
- `lighten` - Uses lighter of two colors

### Overlay Examples

```js
// Watermark with transparency
ImageNew("photo.jpg")
    .overlay(ImageNew("logo.png"), "normal", 0.5)
    .write("watermarked.jpg");

// Texture overlay
ImageNew("base.jpg")
    .overlay(ImageNew("texture.png"), "multiply", 0.3)
    .write("textured.jpg");

// Light leak effect
ImageNew("photo.jpg")
    .overlay(ImageNew("light-leak.png"), "screen", 0.6)
    .write("vintage.jpg");
```

### Paste/Draw Images

Paste one image onto another at specific coordinates:

```js
// Paste logo in top-right corner
base = ImageNew("photo.jpg");
logo = ImageNew("logo.png");

base.paste(logo, base.getWidth() - 120, 10)
    .write("branded.jpg");
```

**BIF Syntax:**

```js
base = ImageRead("photo.jpg");
logo = ImageRead("logo.png");
ImagePaste(base, logo, x=680, y=10);
ImageWrite(base, "branded.jpg");
```

## Combining Effects

### Sequential Effects

Chain multiple effects for complex results:

```js
// Grayscale + sharpen + border
ImageNew("photo.jpg")
    .grayScale()
    .sharpen(2)
    .addBorder(10, "black")
    .write("final.jpg");
```

### Photo Enhancement Pipeline

```js
// Professional photo processing
ImageNew("raw-photo.jpg")
    .scaleToFit(1920, 1080)     // Resize
    .sharpen(1.5)                // Enhance detail
    .blur(0.5)                   // Subtle smoothing
    .write("enhanced.jpg");
```

### Vintage Effect

```js
// Create vintage/retro look
ImageNew("modern-photo.jpg")
    .grayScale()                 // Remove color
    .blur(1)                     // Slight blur
    .sharpen(2)                  // Increase contrast
    .write("vintage.jpg");
```

### Soft Focus Effect

```js
// Create dreamy soft focus
original = ImageNew("portrait.jpg");
blurred = original.copy().blur(15);

// Blend sharp and blurred versions
original.overlay(blurred, "screen", 0.4)
    .write("soft-focus.jpg");
```

### Dramatic Black & White

```js
// High contrast black and white
ImageNew("photo.jpg")
    .grayScale()
    .sharpen(3)
    .write("dramatic-bw.jpg");
```

## Complete Effect Examples

### Privacy Blur Regions

```js
// Blur faces or sensitive information
img = ImageNew("document.jpg");

// Blur multiple regions
regions = [
    {x: 100, y: 50, width: 150, height: 200},   // Face 1
    {x: 300, y: 80, width: 150, height: 200},   // Face 2
    {x: 50, y: 400, width: 500, height: 50}     // Text line
];

for (region in regions) {
    // Extract region, blur, and paste back
    blurred = img.copy()
        .crop(region.x, region.y, region.width, region.height)
        .blur(20);

    img.paste(blurred, region.x, region.y);
}

img.write("redacted.jpg");
```

### Multi-Layer Composite

```js
// Create complex composition
background = ImageNew(1200, 800, "rgb", "white");

// Add blurred background
bgImage = ImageNew("texture.jpg")
    .resize(1200, 800)
    .blur(10);

background.overlay(bgImage, "normal", 1.0);

// Add semi-transparent overlay
overlay = ImageNew("pattern.png")
    .resize(1200, 800);

background.overlay(overlay, "multiply", 0.3);

// Add sharp logo
logo = ImageNew("logo.png");
background.paste(logo, 50, 50);

background.write("composition.jpg");
```

### Tilt-Shift Effect

```js
// Simulate miniature/toy effect
img = ImageNew("cityscape.jpg");
height = img.getHeight();

// Keep center sharp, blur top and bottom
top = img.copy().crop(0, 0, img.getWidth(), height/3).blur(15);
bottom = img.copy().crop(0, height*2/3, img.getWidth(), height/3).blur(15);

img.paste(top, 0, 0);
img.paste(bottom, 0, height*2/3);

// Increase saturation with sharpen
img.sharpen(2).write("tilt-shift.jpg");
```

### Before and After Comparison

```js
// Create side-by-side comparison
original = ImageNew("photo.jpg");
width = original.getWidth();
height = original.getHeight();

// Processed version
processed = original.copy()
    .grayScale()
    .sharpen(2);

// Create comparison image
comparison = ImageNew(width * 2, height, "rgb", "white");

// Paste original and processed side-by-side
comparison.paste(original, 0, 0);
comparison.paste(processed, width, 0);

comparison.write("comparison.jpg");
```

## Effect Intensity Guidelines

### Blur Intensity

| Radius | Effect | Use Case |
|--------|--------|----------|
| 1-2 | Very subtle | Noise reduction |
| 3-5 | Noticeable | Soft focus, skin smoothing |
| 6-10 | Moderate | Background blur |
| 11-20 | Heavy | Privacy, artistic effects |
| 20+ | Extreme | Completely obscured |

### Sharpen Intensity

| Gain | Effect | Use Case |
|------|--------|----------|
| 0.5-1.0 | Subtle | General enhancement |
| 1.0-2.0 | Moderate | After resizing |
| 2.0-3.0 | Strong | Product photos |
| 3.0-5.0 | Heavy | Technical images |
| 5.0+ | Extreme | May cause artifacts |

## Performance Tips

1. **Apply blur last** - Blurring is computationally expensive
2. **Resize before effects** - Smaller images process faster
3. **Combine operations** - Use method chaining to reduce intermediate files
4. **Cache processed versions** - Don't reprocess on every request

## Next Steps

- **[Drawing](drawing.md)** - Add shapes, lines, and text
- **[Advanced Examples](advanced-examples.md)** - Complex effect combinations
- **[Transformations](transformations.md)** - Resize, rotate, and crop
