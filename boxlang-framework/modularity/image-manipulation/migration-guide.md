# Migration Guide

Guide for migrating from Adobe ColdFusion or Lucee image functions to BoxLang Image Module.

## Table of Contents

- [Compatibility Overview](#compatibility-overview)
- [Syntax Differences](#syntax-differences)
- [Function Mapping](#function-mapping)
- [Component Differences](#component-differences)
- [Known Limitations](#known-limitations)
- [Migration Checklist](#migration-checklist)
- [Common Migration Patterns](#common-migration-patterns)

## Compatibility Overview

The BoxLang Image Module aims for **high compatibility** with Adobe ColdFusion and Lucee image functions. Most code should work with minimal or no changes.

### Compatibility Matrix

| Feature | Adobe CF | Lucee | BoxLang | Notes |
|---------|----------|-------|---------|-------|
| **ImageNew()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageRead()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageWrite()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageResize()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageRotate()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageCrop()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageFlip()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageBlur()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageSharpen()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageGrayScale()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageNegative()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageOverlay()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImagePaste()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageAddBorder()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageScaleToFit()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageDrawLine()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageDrawRect()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageDrawOval()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageDrawText()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageSetDrawingColor()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageGetExifMetadata()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageGetIPTCMetadata()** | ✅ | ✅ | ✅ | Full compatibility |
| **ImageInfo()** | ✅ | ✅ | ✅ | Full compatibility |
| **IsImage()** | ✅ | ✅ | ✅ | Full compatibility |
| **IsImageFile()** | ✅ | ✅ | ✅ | Full compatibility |
| **Member Functions** | ✅ | ✅ | ✅ | CF11+, Lucee 4.5+ |
| **Image Component** | ✅ | ✅ | ✅ | `<cfimage>` → `<bx:image>` |
| **CAPTCHA** | ✅ | ✅ | ⚠️ | Planned for future release |
| **ImageFilter()** | ✅ | ⚠️ | ⚠️ | Planned for future release |
| **ImageXOR()** | ✅ | ⚠️ | ⚠️ | Planned for future release |

**Legend:**
- ✅ Fully supported
- ⚠️ Partial support or planned for future release
- ❌ Not supported

## Syntax Differences

### BIF vs Member Functions

Both Adobe ColdFusion (11+) and Lucee support member function syntax. BoxLang maintains this compatibility:

**Adobe CF / Lucee / BoxLang (all compatible):**

```js
// BIF syntax
img = ImageNew("photo.jpg");
ImageResize(img, 800, 600);
ImageWrite(img, "resized.jpg");

// Member function syntax (CF11+, Lucee 4.5+, BoxLang)
img = ImageNew("photo.jpg");
img.resize(800, 600);
img.write("resized.jpg");
```

**No changes needed** - both syntaxes work identically in BoxLang.

### Component Tag Syntax

The main difference is the tag prefix:

**Adobe ColdFusion / Lucee:**

```cfml
<cfimage action="read" source="photo.jpg" name="myImage">
<cfimage action="resize" source="#myImage#" width="800" height="600">
<cfimage action="write" source="#myImage#" destination="resized.jpg">
```

**BoxLang:**

```boxlang
<bx:image action="read" source="photo.jpg" name="myImage" />
<bx:image action="resize" source="#myImage#" width="800" height="600" />
<bx:image action="write" source="#myImage#" destination="resized.jpg" />
```

**Migration:** Simple find/replace: `<cfimage` → `<bx:image`

## Function Mapping

Most functions have identical names and signatures between platforms:

### Direct 1:1 Mappings

These functions work **identically** in CF, Lucee, and BoxLang:

| Function | CF | Lucee | BoxLang | Notes |
|----------|-----|-------|---------|-------|
| `ImageNew()` | ✅ | ✅ | ✅ | No changes |
| `ImageRead()` | ✅ | ✅ | ✅ | No changes |
| `ImageWrite()` | ✅ | ✅ | ✅ | No changes |
| `ImageResize()` | ✅ | ✅ | ✅ | No changes |
| `ImageRotate()` | ✅ | ✅ | ✅ | No changes |
| `ImageCrop()` | ✅ | ✅ | ✅ | No changes |
| `ImageFlip()` | ✅ | ✅ | ✅ | No changes |
| `ImageBlur()` | ✅ | ✅ | ✅ | No changes |
| `ImageSharpen()` | ✅ | ✅ | ✅ | No changes |
| `ImageGrayScale()` | ✅ | ✅ | ✅ | No changes |
| `ImageNegative()` | ✅ | ✅ | ✅ | No changes |
| `ImagePaste()` | ✅ | ✅ | ✅ | No changes |
| `ImageCopy()` | ✅ | ✅ | ✅ | No changes |
| `ImageGetWidth()` | ✅ | ✅ | ✅ | No changes |
| `ImageGetHeight()` | ✅ | ✅ | ✅ | No changes |
| `ImageInfo()` | ✅ | ✅ | ✅ | No changes |

### Parameter Differences

#### ImageNew()

**Adobe CF:**

```js
img = ImageNew("", 800, 600, "rgb", "white");
```

**BoxLang:**

```js
// Preferred (no empty string)
img = ImageNew(800, 600, "rgb", "white");

// Also works (CF-compatible)
img = ImageNew("", 800, 600, "rgb", "white");
```

**Migration:** Remove empty string first parameter (optional).

#### ImageRotate()

All platforms support the same syntax:

```js
// Basic rotation
img.rotate(45);

// Rotation around point
img.rotate(45, x, y);
```

**No changes needed**.

#### ImageResize()

**Adobe CF / Lucee:**

```js
ImageResize(img, 800, 600, "highestQuality");
```

**BoxLang:**

```js
ImageResize(img, 800, 600, "highQuality");
```

**Migration:** `"highestQuality"` → `"highQuality"` (or use `"bicubic"`).

**Interpolation values:**

| Adobe CF | BoxLang | Notes |
|----------|---------|-------|
| `"nearest"` | `"nearest"` | No change |
| `"bilinear"` | `"bilinear"` | No change |
| `"bicubic"` | `"bicubic"` | No change |
| `"highestQuality"` | `"highQuality"` | Name difference |
| `"highQuality"` | `"highQuality"` | No change |
| `"mediumQuality"` | `"bilinear"` | Use bilinear |
| `"highestPerformance"` | `"nearest"` | Use nearest |

## Component Differences

### Component Name

**Adobe CF / Lucee:**

```cfml
<cfimage action="read" source="photo.jpg" name="img">
```

**BoxLang:**

```boxlang
<bx:image action="read" source="photo.jpg" name="img" />
```

### Supported Actions

| Action | CF | Lucee | BoxLang | Notes |
|--------|-----|-------|---------|-------|
| `border` | ✅ | ✅ | ✅ | No changes |
| `captcha` | ✅ | ✅ | ⚠️ | Planned |
| `convert` | ✅ | ✅ | ✅ | No changes |
| `info` | ✅ | ✅ | ✅ | No changes |
| `read` | ✅ | ✅ | ✅ | No changes |
| `resize` | ✅ | ✅ | ✅ | No changes |
| `rotate` | ✅ | ✅ | ✅ | No changes |
| `write` | ✅ | ✅ | ✅ | No changes |
| `writeToBrowser` | ✅ | ✅ | ✅ | No changes |

### Action-Specific Attributes

Most attributes are **identical** across platforms:

**Read:**

```boxlang
<bx:image action="read" source="photo.jpg" name="myImage" />
```

**Resize:**

```boxlang
<bx:image action="resize"
    source="#myImage#"
    width="800"
    height="600"
    interpolation="highQuality" />
```

**Write:**

```boxlang
<bx:image action="write"
    source="#myImage#"
    destination="output.jpg"
    quality="0.85" />
```

## Known Limitations

### Not Yet Implemented

These features exist in Adobe CF/Lucee but are **planned** for future BoxLang releases:

1. **CAPTCHA generation** - `<bx:image action="captcha">` not yet available
2. **ImageFilter()** - Custom Java filter application
3. **ImageXOR()** - XOR blending operation
4. **ImageSetAlpha()** - Alpha channel manipulation (use `setDrawingTransparency()` as alternative)

### Platform-Specific Differences

#### Font Rendering

Font rendering may vary slightly across platforms/OS:

```js
// Works on all platforms, but rendering may differ
img.drawText("Hello World", 100, 100, {
    font: "Arial",
    size: 24,
    style: "bold"
});
```

**Solution:** Test font output on target platform, use web-safe fonts.

#### Color Models

BoxLang supports standard color models:

| Color Model | CF | Lucee | BoxLang |
|-------------|-----|-------|---------|
| RGB | ✅ | ✅ | ✅ |
| ARGB | ✅ | ✅ | ✅ |
| Grayscale | ✅ | ✅ | ✅ |
| CMYK | ⚠️ | ❌ | ❌ |

**Migration:** Convert CMYK images to RGB before processing.

## Migration Checklist

### Pre-Migration Assessment

- [ ] Identify all image manipulation code (BIFs, components, member functions)
- [ ] Check for CAPTCHA usage (needs alternative in BoxLang)
- [ ] Check for ImageFilter() usage (needs alternative)
- [ ] Review custom interpolation values (highestQuality → highQuality)
- [ ] Identify CMYK images (convert to RGB)

### Migration Steps

1. **Replace component tags:**
   ```bash
   # Find and replace
   <cfimage → <bx:image
   </cfimage> → </bx:image>
   ```

2. **Update interpolation values:**
   ```js
   // Before
   img.resize(800, 600, "highestQuality");

   // After
   img.resize(800, 600, "highQuality");
   ```

3. **Test CAPTCHA alternatives:**
   If using CAPTCHA, implement alternative until BoxLang support is added:
   ```js
   // Alternative: Use external CAPTCHA service
   // or implement custom text-based CAPTCHA
   ```

4. **Verify font rendering:**
   Test text drawing on target platform:
   ```js
   img.drawText("Test", 100, 100, {
       font: "Arial",  // Use web-safe fonts
       size: 24
   });
   ```

5. **Test metadata extraction:**
   EXIF/IPTC should work identically:
   ```js
   exif = img.getExifMetadata();
   iptc = img.getIPTCMetadata();
   ```

### Post-Migration Testing

- [ ] Verify all images load correctly
- [ ] Check resize/crop operations
- [ ] Validate drawing operations (text, shapes)
- [ ] Test metadata extraction (EXIF/IPTC)
- [ ] Verify file format conversions
- [ ] Check error handling

## Common Migration Patterns

### Pattern 1: Simple Resize

**Adobe CF / Lucee:**

```js
img = ImageRead("photo.jpg");
ImageResize(img, 800, 600);
ImageWrite(img, "resized.jpg");
```

**BoxLang (no changes):**

```js
img = ImageRead("photo.jpg");
ImageResize(img, 800, 600);
ImageWrite(img, "resized.jpg");
```

### Pattern 2: Thumbnail with Crop

**Adobe CF / Lucee:**

```js
img = ImageRead("photo.jpg");
ImageScaleToFit(img, 200, 200);
ImageAddBorder(img, 2, "gray");
ImageWrite(img, "thumb.jpg");
```

**BoxLang (no changes):**

```js
img = ImageRead("photo.jpg");
ImageScaleToFit(img, 200, 200);
ImageAddBorder(img, 2, "gray");
ImageWrite(img, "thumb.jpg");
```

### Pattern 3: Member Function Chaining

**Adobe CF 11+ / Lucee 4.5+:**

```js
img = ImageNew("photo.jpg")
    .resize(800, 600)
    .blur(3)
    .sharpen(1);

img.write("processed.jpg");
```

**BoxLang (no changes):**

```js
img = ImageNew("photo.jpg")
    .resize(800, 600)
    .blur(3)
    .sharpen(1);

img.write("processed.jpg");
```

### Pattern 4: Watermarking

**Adobe CF / Lucee:**

```js
photo = ImageNew("photo.jpg");
logo = ImageNew("logo.png");
ImageScaleToFit(logo, 100, 100);
ImagePaste(photo, logo, 20, 20);
ImageWrite(photo, "watermarked.jpg");
```

**BoxLang (no changes):**

```js
photo = ImageNew("photo.jpg");
logo = ImageNew("logo.png");
ImageScaleToFit(logo, 100, 100);
ImagePaste(photo, logo, 20, 20);
ImageWrite(photo, "watermarked.jpg");
```

### Pattern 5: Component Usage

**Adobe CF / Lucee:**

```cfml
<cfimage action="read" source="photo.jpg" name="myImage">
<cfimage action="resize" source="#myImage#" width="800" height="600">
<cfimage action="border" source="#myImage#" thickness="5" color="black">
<cfimage action="write" source="#myImage#" destination="final.jpg">
```

**BoxLang (tag name change only):**

```boxlang
<bx:image action="read" source="photo.jpg" name="myImage" />
<bx:image action="resize" source="#myImage#" width="800" height="600" />
<bx:image action="border" source="#myImage#" thickness="5" color="black" />
<bx:image action="write" source="#myImage#" destination="final.jpg" />
```

### Pattern 6: EXIF Metadata

**Adobe CF / Lucee:**

```js
img = ImageNew("photo.jpg");
exif = ImageGetExifMetadata(img);
camera = exif["Model"];
iso = exif["ISO Speed Ratings"];
```

**BoxLang (no changes):**

```js
img = ImageNew("photo.jpg");
exif = ImageGetExifMetadata(img);
camera = exif["Model"];
iso = exif["ISO Speed Ratings"];
```

## Advanced Migration

### Custom Image Processing Pipeline

**Adobe CF / Lucee:**

```js
function processPhoto(sourcePath, outputPath) {
    img = ImageRead(sourcePath);

    // Resize to max 1920px
    if (ImageGetWidth(img) > 1920) {
        ImageScaleToFit(img, 1920, 1920, "highestQuality");
    }

    // Enhance
    ImageSharpen(img, 0.5);

    // Add watermark
    logo = ImageNew("logo.png");
    ImageScaleToFit(logo, 100, 100);
    ImagePaste(img, logo,
        ImageGetWidth(img) - 120,
        ImageGetHeight(img) - 120,
        50
    );

    ImageWrite(img, outputPath, 0.85);
}
```

**BoxLang (change interpolation only):**

```js
function processPhoto(sourcePath, outputPath) {
    img = ImageRead(sourcePath);

    // Resize to max 1920px
    if (ImageGetWidth(img) > 1920) {
        ImageScaleToFit(img, 1920, 1920, "highQuality");  // Changed
    }

    // Enhance
    ImageSharpen(img, 0.5);

    // Add watermark
    logo = ImageNew("logo.png");
    ImageScaleToFit(logo, 100, 100);
    ImagePaste(img, logo,
        ImageGetWidth(img) - 120,
        ImageGetHeight(img) - 120,
        50
    );

    ImageWrite(img, outputPath, 0.85);
}
```

### Batch Processing

**Adobe CF / Lucee / BoxLang (identical):**

```js
function batchResize(sourceDir, targetDir, maxWidth, maxHeight) {
    files = directoryList(sourceDir, false, "path");

    for (file in files) {
        if (IsImageFile(file)) {
            img = ImageNew(file);
            img.scaleToFit(maxWidth, maxHeight);

            filename = getFileFromPath(file);
            img.write("#targetDir#/#filename#");
        }
    }
}
```

## Performance Considerations

### Memory Usage

All platforms handle images similarly:

```js
// Load large image
img = ImageNew("large-photo.jpg");  // ~10MB

// Process
img.resize(800, 600);  // Memory efficient

// Release (automatic GC)
img = null;
```

### Optimization Tips

Same best practices apply across all platforms:

1. **Resize early:** Reduce dimensions before heavy processing
2. **Reuse images:** Copy instead of reloading
3. **Chain operations:** Use member functions for cleaner code
4. **Format selection:** Use JPEG for photos, PNG for graphics
5. **Quality settings:** Balance file size vs. quality

## Troubleshooting

### Common Issues

#### Issue: "Function not found"

**Cause:** Typo in function name

**Solution:** Check function spelling (case-insensitive but verify)

```js
// Wrong
ImageGrayScale(img);  // Note spelling

// Correct
ImageGrayScale(img);
```

#### Issue: "Invalid image object"

**Cause:** Passing variable name instead of image object

**Solution:** Pass actual image object

```js
// Wrong
ImageResize("myImage", 800, 600);

// Correct
ImageResize(myImage, 800, 600);
// Or
myImage.resize(800, 600);
```

#### Issue: Font rendering differs

**Cause:** Platform/OS font differences

**Solution:** Use web-safe fonts, test on target platform

```js
// More portable
img.drawText("Text", 100, 100, {
    font: "Arial",  // Web-safe
    size: 24
});
```

## Additional Resources

- **[BoxLang Documentation](https://boxlang.io/docs)** - Core BoxLang language reference
- **[Adobe ColdFusion Image Functions](https://helpx.adobe.com/coldfusion/cfml-reference/coldfusion-functions/functions-h-im/image-functions.html)** - Original CF documentation
- **[Lucee Image Functions](https://docs.lucee.org/)** - Lucee image function reference
- **[Getting Started Guide](getting-started.md)** - BoxLang image basics
- **[BIF Reference](bif-reference.md)** - Complete function reference
- **[Advanced Examples](advanced-examples.md)** - Real-world use cases

## Summary

**Migration Complexity: Low**

Most Adobe ColdFusion and Lucee image code will work in BoxLang with **minimal or no changes**:

✅ **No changes needed:**
- BIF function names and signatures
- Member function syntax
- Parameter order and types
- Return values
- EXIF/IPTC metadata extraction
- Drawing operations
- Color handling

⚠️ **Minor changes:**
- Component tags: `<cfimage>` → `<bx:image>`
- Interpolation: `"highestQuality"` → `"highQuality"`

❌ **Not yet available:**
- CAPTCHA generation
- ImageFilter()
- ImageXOR()

**Migration time estimate:** 1-2 hours for typical applications.

## Next Steps

- **[Getting Started](getting-started.md)** - Learn BoxLang image basics
- **[BIF Reference](bif-reference.md)** - Complete function reference
- **[Advanced Examples](advanced-examples.md)** - Real-world patterns
