# Advanced Examples

Real-world examples demonstrating practical image manipulation techniques.

## Table of Contents

- [Watermarking Images](#watermarking-images)
- [Thumbnail Generation](#thumbnail-generation)
- [Image Compositing](#image-compositing)
- [Dynamic Graphics](#dynamic-graphics)
- [Photo Processing Pipelines](#photo-processing-pipelines)
- [Batch Processing](#batch-processing)
- [Image Optimization](#image-optimization)

## Watermarking Images

### Text Watermark

```js
function addTextWatermark(sourcePath, text, outputPath) {
    img = ImageNew(sourcePath);

    // Configure watermark appearance
    img.setDrawingColor("white")
       .setDrawingStroke({
           width: 2,
           color: "black"
       })
       .setDrawingTransparency(70)  // 70% transparent
       .setAntialiasing(true);

    // Position in bottom-right corner
    textWidth = 200;  // Approximate text width
    x = img.getWidth() - textWidth - 20;
    y = img.getHeight() - 30;

    // Draw watermark
    img.drawText(text, x, y, {
        font: "Arial",
        size: 24,
        style: "bold"
    });

    img.write(outputPath);

    return outputPath;
}

// Usage
addTextWatermark(
    "photo.jpg",
    "© 2024 MyCompany",
    "watermarked.jpg"
);
```

### Image Watermark

```js
function addLogoWatermark(sourcePath, logoPath, position, opacity) {
    img = ImageNew(sourcePath);
    logo = ImageNew(logoPath);

    // Resize logo to 15% of image width
    targetWidth = img.getWidth() * 0.15;
    logo.scaleToFit(targetWidth, targetWidth);

    // Calculate position
    margin = 20;
    x = 0;
    y = 0;

    switch (position) {
        case "topLeft":
            x = margin;
            y = margin;
            break;
        case "topRight":
            x = img.getWidth() - logo.getWidth() - margin;
            y = margin;
            break;
        case "bottomLeft":
            x = margin;
            y = img.getHeight() - logo.getHeight() - margin;
            break;
        case "bottomRight":
            x = img.getWidth() - logo.getWidth() - margin;
            y = img.getHeight() - logo.getHeight() - margin;
            break;
        case "center":
            x = (img.getWidth() - logo.getWidth()) / 2;
            y = (img.getHeight() - logo.getHeight()) / 2;
            break;
    }

    // Apply watermark with opacity
    img.paste(logo, x, y, opacity);

    return img;
}

// Usage
watermarked = addLogoWatermark(
    "photo.jpg",
    "logo.png",
    "bottomRight",
    50  // 50% opacity
);

watermarked.write("watermarked.jpg");
```

### Tiled Watermark

```js
function addTiledWatermark(sourcePath, text, outputPath) {
    img = ImageNew(sourcePath);

    img.setDrawingColor("white")
       .setDrawingTransparency(85)  // Very transparent
       .setAntialiasing(true);

    // Rotate drawing axis for diagonal watermarks
    img.rotateDrawingAxis(45);

    // Tile watermark across image
    spacing = 200;
    for (x = 0; x < img.getWidth() + 500; x += spacing) {
        for (y = -500; y < img.getHeight() + 500; y += spacing) {
            img.drawText(text, x, y, {
                font: "Arial",
                size: 20,
                style: "bold"
            });
        }
    }

    img.write(outputPath);
    return outputPath;
}

// Usage
addTiledWatermark("photo.jpg", "CONFIDENTIAL", "watermarked.jpg");
```

## Thumbnail Generation

### Fixed-Size Thumbnails

```js
function createThumbnail(sourcePath, size, outputPath) {
    img = ImageNew(sourcePath);

    // Resize to fit within size x size
    img.scaleToFit(size, size, "highQuality");

    // Optional: add border
    img.addBorder(2, "gray", "constant");

    img.write(outputPath);
    return outputPath;
}

// Generate 150x150 thumbnail
createThumbnail("photo.jpg", 150, "thumb_150.jpg");
```

### Square Thumbnails with Crop

```js
function createSquareThumbnail(sourcePath, size, outputPath) {
    img = ImageNew(sourcePath);

    // Calculate crop to center square
    dimension = min(img.getWidth(), img.getHeight());
    x = (img.getWidth() - dimension) / 2;
    y = (img.getHeight() - dimension) / 2;

    img.crop(x, y, dimension, dimension)
       .resize(size, size, "highQuality");

    img.write(outputPath);
    return outputPath;
}

// Create 200x200 square thumbnail
createSquareThumbnail("photo.jpg", 200, "thumb_square.jpg");
```

### Multiple Thumbnail Sizes

```js
function generateThumbnailSet(sourcePath, sizes) {
    img = ImageNew(sourcePath);
    results = {};

    for (size in sizes) {
        // Create copy for each size
        thumb = img.copy();
        thumb.scaleToFit(size, size, "highQuality");

        // Generate filename
        dir = getDirectoryFromPath(sourcePath);
        filename = getFileFromPath(sourcePath);
        name = listFirst(filename, ".");
        ext = listLast(filename, ".");

        outputPath = "#dir##name#_#size#.#ext#";
        thumb.write(outputPath);

        results["thumb_#size#"] = outputPath;
    }

    return results;
}

// Generate multiple sizes
thumbnails = generateThumbnailSet("photo.jpg", [100, 200, 400, 800]);
writeDump(thumbnails);
```

## Image Compositing

### Photo Collage

```js
function createCollage(images, cols, spacing, outputPath) {
    // Calculate dimensions
    thumbSize = 200;
    rows = ceiling(arrayLen(images) / cols);

    canvasWidth = (cols * thumbSize) + ((cols + 1) * spacing);
    canvasHeight = (rows * thumbSize) + ((rows + 1) * spacing);

    // Create canvas
    canvas = ImageNew(canvasWidth, canvasHeight, "rgb", "white");

    // Place images
    currentRow = 0;
    currentCol = 0;

    for (imagePath in images) {
        img = ImageNew(imagePath);
        img.scaleToFit(thumbSize, thumbSize);

        x = spacing + (currentCol * (thumbSize + spacing));
        y = spacing + (currentRow * (thumbSize + spacing));

        canvas.paste(img, x, y);

        currentCol++;
        if (currentCol >= cols) {
            currentCol = 0;
            currentRow++;
        }
    }

    canvas.write(outputPath);
    return outputPath;
}

// Create 3x3 collage
images = [
    "photo1.jpg", "photo2.jpg", "photo3.jpg",
    "photo4.jpg", "photo5.jpg", "photo6.jpg",
    "photo7.jpg", "photo8.jpg", "photo9.jpg"
];

createCollage(images, 3, 10, "collage.jpg");
```

### Before/After Comparison

```js
function createBeforeAfter(beforePath, afterPath, outputPath) {
    before = ImageNew(beforePath);
    after = ImageNew(afterPath);

    // Ensure same height
    height = min(before.getHeight(), after.getHeight());
    before.scaleToFit(9999, height);
    after.scaleToFit(9999, height);

    // Create combined canvas
    totalWidth = before.getWidth() + after.getWidth() + 4;
    canvas = ImageNew(totalWidth, height, "rgb", "white");

    // Paste images side-by-side
    canvas.paste(before, 0, 0);
    canvas.paste(after, before.getWidth() + 4, 0);

    // Add divider line
    canvas.setDrawingColor("black")
          .setDrawingStroke({ width: 4 });

    x = before.getWidth() + 2;
    canvas.drawLine(x, 0, x, height);

    // Add labels
    canvas.setDrawingColor("white")
          .setDrawingTransparency(30);

    canvas.drawText("BEFORE", 20, height - 30, {
        font: "Arial",
        size: 24,
        style: "bold"
    });

    canvas.drawText("AFTER", before.getWidth() + 24, height - 30, {
        font: "Arial",
        size: 24,
        style: "bold"
    });

    canvas.write(outputPath);
    return outputPath;
}

// Usage
createBeforeAfter("original.jpg", "edited.jpg", "comparison.jpg");
```

### Picture Frame Effect

```js
function addFrame(sourcePath, frameWidth, frameColor, outputPath) {
    img = ImageNew(sourcePath);

    // Create larger canvas for frame
    canvasWidth = img.getWidth() + (frameWidth * 2);
    canvasHeight = img.getHeight() + (frameWidth * 2);

    canvas = ImageNew(canvasWidth, canvasHeight, "rgb", frameColor);

    // Paste image centered
    canvas.paste(img, frameWidth, frameWidth);

    // Add inner shadow effect
    canvas.setDrawingColor("black")
          .setDrawingTransparency(50)
          .setDrawingStroke({ width: 2 });

    x = frameWidth;
    y = frameWidth;
    w = img.getWidth();
    h = img.getHeight();

    canvas.drawRect(x, y, w, h);

    canvas.write(outputPath);
    return outputPath;
}

// Add 20px black frame
addFrame("photo.jpg", 20, "black", "framed.jpg");
```

## Dynamic Graphics

### Certificate Generator

```js
function generateCertificate(name, course, date, outputPath) {
    // Create canvas
    img = ImageNew(1200, 800, "rgb", "white");

    // Add decorative border
    img.addBorder(20, "gold", "constant");

    // Draw ornamental corners
    img.setDrawingColor("#FFD700")  // Gold
       .setDrawingStroke({ width: 5 });

    // Top-left corner
    img.drawLine(40, 40, 200, 40)
       .drawLine(40, 40, 40, 200);

    // Top-right corner
    img.drawLine(1000, 40, 1160, 40)
       .drawLine(1160, 40, 1160, 200);

    // Bottom-left corner
    img.drawLine(40, 760, 200, 760)
       .drawLine(40, 600, 40, 760);

    // Bottom-right corner
    img.drawLine(1000, 760, 1160, 760)
       .drawLine(1160, 600, 1160, 760);

    // Add text
    img.setDrawingColor("black")
       .setAntialiasing(true);

    // Title
    img.drawText("Certificate of Completion", 300, 150, {
        font: "Serif",
        size: 48,
        style: "bold"
    });

    // Presented to
    img.drawText("This certificate is presented to", 350, 250, {
        font: "Serif",
        size: 24
    });

    // Name (larger)
    img.setDrawingColor("#0066CC");
    img.drawText(name, 400, 350, {
        font: "Serif",
        size: 56,
        style: "bold"
    });

    // Course
    img.setDrawingColor("black");
    img.drawText("For successfully completing", 370, 450, {
        font: "Serif",
        size: 24
    });

    img.drawText(course, 400, 520, {
        font: "Serif",
        size: 32,
        style: "italic"
    });

    // Date
    img.drawText("Date: #date#", 500, 650, {
        font: "Serif",
        size: 20
    });

    img.write(outputPath);
    return outputPath;
}

// Generate certificate
generateCertificate(
    "John Doe",
    "Advanced BoxLang Development",
    "December 20, 2024",
    "certificate.png"
);
```

### Social Media Graphics

```js
function createSocialPost(title, subtitle, backgroundPath, outputPath) {
    // Load background
    img = ImageNew(backgroundPath);

    // Resize to social media dimensions (1200x630 for sharing)
    img.resize(1200, 630);

    // Add semi-transparent overlay
    overlay = ImageNew(1200, 630, "argb", "transparent");
    overlay.setDrawingColor("black")
           .setDrawingTransparency(40);
    overlay.drawRect(0, 0, 1200, 630, true);

    img.paste(overlay, 0, 0);

    // Add text
    img.setDrawingColor("white")
       .setAntialiasing(true);

    // Title
    img.drawText(title, 100, 250, {
        font: "Arial",
        size: 72,
        style: "bold"
    });

    // Subtitle
    img.drawText(subtitle, 100, 350, {
        font: "Arial",
        size: 36
    });

    img.write(outputPath);
    return outputPath;
}

// Create post
createSocialPost(
    "New Feature Release",
    "BoxLang Image Module 1.0",
    "background.jpg",
    "social-post.jpg"
);
```

### Chart Overlay

```js
function addChartAnnotations(chartPath, annotations, outputPath) {
    img = ImageNew(chartPath);

    img.setAntialiasing(true)
       .setDrawingStroke({ width: 2 });

    for (annotation in annotations) {
        // Draw arrow
        img.setDrawingColor(annotation.color);
        img.drawLine(
            annotation.fromX,
            annotation.fromY,
            annotation.toX,
            annotation.toY
        );

        // Draw arrowhead
        angle = atan2(
            annotation.toY - annotation.fromY,
            annotation.toX - annotation.fromX
        );

        arrowSize = 10;
        x1 = annotation.toX - arrowSize * cos(angle - 0.5);
        y1 = annotation.toY - arrowSize * sin(angle - 0.5);
        x2 = annotation.toX - arrowSize * cos(angle + 0.5);
        y2 = annotation.toY - arrowSize * sin(angle + 0.5);

        img.drawLine(annotation.toX, annotation.toY, x1, y1)
           .drawLine(annotation.toX, annotation.toY, x2, y2);

        // Add label
        img.drawText(annotation.label, annotation.labelX, annotation.labelY, {
            font: "Arial",
            size: 14,
            style: "bold"
        });
    }

    img.write(outputPath);
    return outputPath;
}

// Usage
annotations = [
    {
        color: "red",
        fromX: 100,
        fromY: 50,
        toX: 200,
        toY: 150,
        label: "Peak",
        labelX: 50,
        labelY: 40
    }
];

addChartAnnotations("chart.png", annotations, "annotated-chart.png");
```

## Photo Processing Pipelines

### Instagram-Style Filter

```js
function applyVintageFilter(sourcePath, outputPath) {
    img = ImageNew(sourcePath);

    // Create sepia-toned version
    img.grayScale();

    // Add warmth by overlaying amber color
    overlay = ImageNew(img.getWidth(), img.getHeight(), "argb", "transparent");
    overlay.setDrawingColor("#FFA500")  // Orange/amber
           .setDrawingTransparency(60);
    overlay.drawRect(0, 0, img.getWidth(), img.getHeight(), true);

    img.paste(overlay, 0, 0, 30);

    // Add vignette effect
    vignette = ImageNew(img.getWidth(), img.getHeight(), "argb", "transparent");
    vignette.setDrawingColor("black");

    // Darken edges
    borderSize = img.getWidth() * 0.2;
    for (i = 0; i < borderSize; i++) {
        transparency = 80 - (i / borderSize * 80);
        vignette.setDrawingTransparency(transparency);
        vignette.drawRect(i, i,
            img.getWidth() - (i * 2),
            img.getHeight() - (i * 2),
            false
        );
    }

    img.paste(vignette, 0, 0);

    // Slight blur for dreamy effect
    img.blur(1);

    img.write(outputPath);
    return outputPath;
}

// Apply vintage filter
applyVintageFilter("modern-photo.jpg", "vintage-photo.jpg");
```

### HDR Effect

```js
function applyHDREffect(sourcePath, outputPath) {
    img = ImageNew(sourcePath);
    original = img.copy();

    // Sharpen for detail enhancement
    img.sharpen(1.5);

    // Blend with original at 50%
    img.paste(original, 0, 0, 50);

    // Enhance again
    img.sharpen(0.8);

    img.write(outputPath);
    return outputPath;
}
```

### Photo Restoration Pipeline

```js
function restorePhoto(sourcePath, outputPath) {
    img = ImageNew(sourcePath);

    // 1. Resize if too large (for performance)
    maxDimension = 2000;
    if (img.getWidth() > maxDimension || img.getHeight() > maxDimension) {
        img.scaleToFit(maxDimension, maxDimension);
    }

    // 2. Sharpen slightly to restore detail
    img.sharpen(0.5);

    // 3. Light blur to reduce noise/scratches
    img.blur(0.5);

    // 4. Sharpen again
    img.sharpen(0.3);

    img.write(outputPath);
    return outputPath;
}
```

## Batch Processing

### Batch Resize

```js
function batchResize(sourceDir, targetDir, maxWidth, maxHeight) {
    files = directoryList(sourceDir, false, "path");
    results = { processed: 0, skipped: 0, errors: [] };

    for (file in files) {
        if (!IsImageFile(file)) {
            results.skipped++;
            continue;
        }

        try {
            img = ImageNew(file);
            img.scaleToFit(maxWidth, maxHeight, "highQuality");

            filename = getFileFromPath(file);
            outputPath = "#targetDir#/#filename#";

            img.write(outputPath);
            results.processed++;

        } catch (any e) {
            arrayAppend(results.errors, {
                file: file,
                error: e.message
            });
        }
    }

    return results;
}

// Resize all images to max 800x600
stats = batchResize("uploads/", "resized/", 800, 600);
writeDump(stats);
```

### Batch Watermark

```js
function batchWatermark(sourceDir, targetDir, logoPath, position) {
    logo = ImageNew(logoPath);
    files = directoryList(sourceDir, false, "path");
    processed = 0;

    for (file in files) {
        if (!IsImageFile(file)) continue;

        img = ImageNew(file);

        // Resize logo to 10% of image width
        targetWidth = img.getWidth() * 0.1;
        logoResized = logo.copy();
        logoResized.scaleToFit(targetWidth, targetWidth);

        // Calculate position
        margin = 20;
        x = img.getWidth() - logoResized.getWidth() - margin;
        y = img.getHeight() - logoResized.getHeight() - margin;

        // Apply watermark
        img.paste(logoResized, x, y, 50);

        // Save
        filename = getFileFromPath(file);
        img.write("#targetDir#/#filename#");

        processed++;
    }

    return processed;
}

// Watermark all images
count = batchWatermark("photos/", "watermarked/", "logo.png", "bottomRight");
writeln("Processed #count# images");
```

## Image Optimization

### Smart Compression

```js
function optimizeForWeb(sourcePath, outputPath, quality) {
    img = ImageNew(sourcePath);

    // Limit dimensions
    maxDimension = 1920;
    if (img.getWidth() > maxDimension || img.getHeight() > maxDimension) {
        img.scaleToFit(maxDimension, maxDimension, "highQuality");
    }

    // Convert to RGB if needed (remove alpha channel)
    if (img.getInfo().colorModel.hasAlpha) {
        rgb = ImageNew(img.getWidth(), img.getHeight(), "rgb", "white");
        rgb.paste(img, 0, 0);
        img = rgb;
    }

    // Write as JPEG with specified quality
    img.write(outputPath, quality);

    // Return file sizes for comparison
    return {
        original: getFileInfo(sourcePath).size,
        optimized: getFileInfo(outputPath).size,
        savings: getFileInfo(sourcePath).size - getFileInfo(outputPath).size
    };
}

// Optimize with 85% quality
stats = optimizeForWeb("photo.png", "photo-optimized.jpg", 0.85);
writeln("Saved #stats.savings# bytes");
```

### Progressive Optimization

```js
function createResponsiveSet(sourcePath, outputDir) {
    img = ImageNew(sourcePath);
    sizes = [
        { name: "thumbnail", width: 150 },
        { name: "small", width: 480 },
        { name: "medium", width: 800 },
        { name: "large", width: 1200 },
        { name: "xlarge", width: 1920 }
    ];

    results = {};
    filename = listFirst(getFileFromPath(sourcePath), ".");

    for (size in sizes) {
        resized = img.copy();
        resized.scaleToFit(size.width, 9999, "highQuality");

        outputPath = "#outputDir#/#filename#-#size.name#.jpg";
        resized.write(outputPath, 0.85);

        results[size.name] = {
            path: outputPath,
            width: resized.getWidth(),
            height: resized.getHeight(),
            size: getFileInfo(outputPath).size
        };
    }

    return results;
}

// Create responsive image set
set = createResponsiveSet("photo.jpg", "responsive/");
writeDump(set);
```

## Next Steps

- **[Utilities](utilities.md)** - Format support and validation
- **[BIF Reference](bif-reference.md)** - Complete function reference
- **[Migration Guide](migration-guide.md)** - CF/Lucee compatibility
