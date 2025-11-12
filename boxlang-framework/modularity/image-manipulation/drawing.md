# Drawing Operations

Learn how to draw shapes, lines, curves, and text on images in BoxLang.

## Table of Contents

- [Setup & Configuration](#setup--configuration)
- [Drawing Shapes](#drawing-shapes)
- [Drawing Lines](#drawing-lines)
- [Drawing Curves](#drawing-curves)
- [Drawing Text](#drawing-text)
- [Advanced Drawing](#advanced-drawing)
- [Drawing Axis Transformations](#drawing-axis-transformations)

## Setup & Configuration

Before drawing, configure colors, strokes, and rendering options:

### Set Drawing Color

```js
// Named color
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("red");

// Hex color
img.setDrawingColor("#FF0000");
```

**Supported Colors:** `black`, `blue`, `cyan`, `darkgray`, `gray`, `green`, `lightgray`, `magenta`, `orange`, `pink`, `red`, `white`, `yellow`

### Set Background Color

```js
img.setBackgroundColor("white");
img.setBackgroundColor("#F0F0F0");
```

### Configure Stroke (Line Style)

```js
// Configure stroke properties
img.setDrawingStroke({
    width: 3,
    endCaps: "round",        // "butt", "round", "square"
    lineJoins: "round",      // "miter", "round", "bevel"
    miterLimit: 10,
    dashArray: [10, 5],      // Dash pattern
    dashPhase: 0
});
```

**Stroke Properties:**

- **width** - Line thickness in pixels
- **endCaps** - How line ends are drawn
- **lineJoins** - How line corners are drawn
- **miterLimit** - Miter join limit
- **dashArray** - Dash pattern (on, off, on, off...)
- **dashPhase** - Offset for dash pattern

### Set Transparency

```js
// 50% transparency (0-100)
img.setDrawingTransparency(50);

// Fully opaque
img.setDrawingTransparency(100);
```

### Enable Anti-Aliasing

```js
// Smooth edges
img.setAntiAliasing("on");

// Fast rendering (jagged edges)
img.setAntiAliasing("off");
```

## Drawing Shapes

### Draw Rectangle

```js
img = ImageNew(400, 300, "rgb", "white");
img.setDrawingColor("blue");

// Outline rectangle: x, y, width, height, filled
img.drawRect(50, 50, 200, 100, false);

// Filled rectangle
img.drawRect(50, 170, 200, 100, true);

img.write("rectangles.jpg");
```

**BIF Syntax:**

```js
ImageDrawRect(img, x=50, y=50, width=200, height=100, filled=false);
```

### Draw Rounded Rectangle

```js
// Rounded corners: x, y, width, height, arcWidth, arcHeight, filled
img.drawRoundRect(50, 50, 200, 100, 30, 30, false);
```

### Draw Beveled Rectangle (3D Effect)

```js
// 3D beveled rectangle: x, y, width, height, raised, filled
img.drawBeveledRect(50, 50, 200, 100, true, true);

// Lowered bevel
img.drawBeveledRect(50, 170, 200, 100, false, true);
```

### Draw Oval/Circle

```js
// Oval: x, y, width, height, filled
img.drawOval(50, 50, 200, 150, false);

// Circle (width = height)
img.drawOval(100, 100, 100, 100, true);
```

### Clear Rectangle

```js
// Clear region to transparent: x, y, width, height
img.clearRect(50, 50, 100, 100);
```

## Drawing Lines

### Draw Single Line

```js
img.setDrawingColor("black");
img.setDrawingStroke({width: 2});

// Draw line: x1, y1, x2, y2
img.drawLine(50, 50, 350, 250);
```

### Draw Multiple Lines (Polyline)

```js
// Array of x and y coordinates
xCoords = [50, 150, 250, 350];
yCoords = [50, 150, 50, 150];

// Draw polyline: xCoords, yCoords, isPolygon, filled
img.drawLines(xCoords, yCoords, false, false);
```

### Draw Polygon

```js
xCoords = [100, 200, 250, 200, 100, 50];
yCoords = [50, 50, 150, 250, 250, 150];

// Closed polygon outline
img.drawLines(xCoords, yCoords, true, false);

// Filled polygon
img.drawLines(xCoords, yCoords, true, true);
```

### Draw Single Point

```js
// Draw point: x, y
img.drawPoint(200, 150);
```

### Draw Arc

```js
// Arc: x, y, width, height, startAngle, arcAngle, filled
img.drawArc(50, 50, 200, 150, 0, 90, false);

// Pie slice (filled arc)
img.drawArc(50, 50, 200, 150, 0, 90, true);
```

**Angles:**

- 0° = 3 o'clock position
- 90° = 12 o'clock position
- Positive angles go counter-clockwise

## Drawing Curves

### Quadratic Bézier Curve

```js
// Quadratic curve: ctrlX, ctrlY, startX, startY, endX, endY
img.drawQuadraticCurve(200, 50, 50, 150, 350, 150);
```

### Cubic Bézier Curve

```js
// Cubic curve: startX, startY, ctrl1X, ctrl1Y, ctrl2X, ctrl2Y, endX, endY
img.drawCubicCurve(50, 150, 100, 50, 300, 250, 350, 150);
```

## Drawing Text

### Simple Text

```js
img.setDrawingColor("black");

// Draw text: text, x, y
img.drawText("Hello World", 50, 100);
```

### Styled Text

```js
// Draw text with font configuration
img.drawText("Styled Text", 50, 150, {
    font: "Arial",
    size: 24,
    style: "bold",
    underline: false,
    strikeThrough: false
});
```

**Font Configuration:**

- **font** - Font family name (e.g., "Arial", "Times New Roman")
- **size** - Font size in points
- **style** - "plain", "bold", "italic", "bolditalic"
- **underline** - true/false
- **strikeThrough** - true/false

### Text Examples

```js
// Title text
img.setDrawingColor("black");
img.drawText("My Photo Album", 100, 50, {
    font: "Arial",
    size: 36,
    style: "bold"
});

// Subtitle
img.setDrawingColor("gray");
img.drawText("Summer 2025", 100, 90, {
    font: "Arial",
    size: 18,
    style: "italic"
});

// Watermark with transparency
img.setDrawingColor("white");
img.setDrawingTransparency(30);
img.drawText("© 2025 My Company", 20, 280, {
    font: "Arial",
    size: 12
});
```

## Advanced Drawing

### Complex Shape Example

```js
img = ImageNew(500, 400, "rgb", "white");
img.setAntiAliasing("on");

// Draw robot face
img.setDrawingColor("lightgray");
img.drawRoundRect(150, 100, 200, 250, 30, 30, true);

// Eyes
img.setDrawingColor("black");
img.drawOval(180, 150, 50, 50, true);
img.drawOval(270, 150, 50, 50, true);

// Pupils
img.setDrawingColor("blue");
img.drawOval(195, 165, 20, 20, true);
img.drawOval(285, 165, 20, 20, true);

// Mouth
img.setDrawingStroke({width: 3});
img.drawArc(200, 220, 100, 80, 180, 180, false);

img.write("robot.jpg");
```

### Chart/Graph Drawing

```js
img = ImageNew(600, 400, "rgb", "white");
img.setAntiAliasing("on");

// Draw axes
img.setDrawingColor("black");
img.setDrawingStroke({width: 2});
img.drawLine(50, 350, 550, 350);  // X-axis
img.drawLine(50, 50, 50, 350);    // Y-axis

// Draw bars
colors = ["red", "blue", "green", "orange"];
values = [200, 150, 300, 180];

for (i = 1; i <= arrayLen(values); i++) {
    img.setDrawingColor(colors[i]);
    x = 50 + (i * 100);
    height = values[i];
    img.drawRect(x, 350 - height, 80, height, true);
}

img.write("chart.jpg");
```

## Drawing Axis Transformations

These transformations affect the coordinate system for drawing, not the image itself.

### Translate Origin

```js
// Move origin to center of image
img = ImageNew(400, 300, "rgb", "white");
img.translateDrawingAxis(200, 150);

// Now (0,0) is at center
img.setDrawingColor("red");
img.drawRect(-50, -50, 100, 100, true);

img.write("centered.jpg");
```

### Rotate Coordinate System

```js
img = ImageNew(400, 300, "rgb", "white");
img.translateDrawingAxis(200, 150);

// Rotate 45 degrees
img.rotateDrawingAxis(45);

// Rectangle will be rotated
img.setDrawingColor("blue");
img.drawRect(-50, -50, 100, 100, false);

img.write("rotated-drawing.jpg");
```

### Shear Coordinate System

```js
img = ImageNew(400, 300, "rgb", "white");

// Shear axis
img.shearDrawingAxis(0.3, 0.1);

// Rectangle will be sheared
img.setDrawingColor("green");
img.drawRect(50, 50, 100, 100, false);

img.write("sheared-drawing.jpg");
```

## Complete Drawing Examples

### Create Badge

```js
// Create circular badge
img = ImageNew(200, 200, "argb", "transparent");
img.setAntiAliasing("on");

// Outer circle (border)
img.setDrawingColor("gold");
img.setDrawingStroke({width: 5});
img.drawOval(10, 10, 180, 180, false);

// Inner circle
img.setDrawingColor("yellow");
img.drawOval(20, 20, 160, 160, true);

// Star or text
img.setDrawingColor("red");
img.drawText("★", 75, 130, {
    font: "Arial",
    size: 72,
    style: "bold"
});

img.write("badge.png");
```

### Create Button

```js
// Create web button
img = ImageNew(200, 60, "rgb", "white");
img.setAntiAliasing("on");

// Gradient effect (simplified)
img.setDrawingColor("#4CAF50");
img.drawRoundRect(0, 0, 200, 60, 10, 10, true);

// Highlight
img.setDrawingColor("white");
img.setDrawingTransparency(30);
img.drawRoundRect(5, 5, 190, 25, 8, 8, true);

// Text
img.setDrawingColor("white");
img.setDrawingTransparency(100);
img.drawText("Click Me", 60, 40, {
    font: "Arial",
    size: 20,
    style: "bold"
});

img.write("button.png");
```

### Watermark with Text

```js
// Add watermark to photo
img = ImageNew("photo.jpg");
width = img.getWidth();
height = img.getHeight();

// Semi-transparent white text
img.setDrawingColor("white");
img.setDrawingTransparency(40);
img.drawText("© 2025 My Company",
    width - 250,
    height - 30,
    {
        font: "Arial",
        size: 16,
        style: "bold"
    }
);

img.write("watermarked.jpg");
```

## Drawing Tips

1. **Enable anti-aliasing** for smooth curves and text
2. **Set stroke before drawing** for consistent line widths
3. **Use transparency** for subtle effects like watermarks
4. **Translate axis to center** for symmetrical drawing
5. **Rotate axis** for angled text without rotating the image

## Next Steps

- **[Advanced Examples](advanced-examples.md)** - Complex drawing projects
- **[Filters & Effects](filters-effects.md)** - Apply visual effects
- **[Transformations](transformations.md)** - Resize and rotate images
