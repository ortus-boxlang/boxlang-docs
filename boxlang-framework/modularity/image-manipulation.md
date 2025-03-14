---
icon: camera
---

# Image Manipulation

BoxLang has an extensive and awesome image manipulation library that allows you to create and manipulate images with easy syntax. We cannot see every detail about image manipulation, but it is necessary to understand that this functionality is easy in BoxLang and exists.

Apart from core image functions, all functions can be applied to an image object as member functions. Yes, BoxLang allows you to deal with image objects natively.

```
# For Operating Systems using our Quick Installer.
install-bx-module bx-image

# Using CommandBox to install for web servers.
box install bx-image
```

```java
imgObj = imageRead("https://example.com/company-logo.png");
imgObj.resize(50,50);
bx:image action="writeToBrowser" source=imgObj;

imgObj = imageRead("https://example.com/company-logo.png");
imgObj.blur(5);
bx:image action="writeToBrowser" source=imgObj;

imgObj = imageRead("https://example.com/company-logo.png");
imgObj.rotate(90);
bx:image action="writeToBrowser" source=imgObj;

imgObj = imageRead("https://example.com/company-logo.png");
info = imgObj.info();
writeDump(info);
```

## Contributed Functions

* `getReadableImageFormats()` : Returns a list of image formats that BoxLang can read on the operating system.
* `getWriteableImageFormats()` : Returns a list of image formats that BoxLang can write on the operating system.
* `ImageAddBorder( name, numeric thickness, [string color], [string borderType] )` : Adds a rectangular border around the outside edge of an image.
* `ImageBlur( name, numeric blurRadius = 3 )` Smooths image.
* `ImageCaptcha()`  : Creates a captcha image
* `ImageClearRect( name, numeric x, numeric y, numeric width, numeric height )` : Clears the specified rectangle by filling it with the background color of the current drawing surface.
* `ImageCopy( name, numeric x, numeric y, numeric width, numeric height, [numeric dx], [numeric dy] )` : Copies a rectangular area of an image.
* `ImageCrop( name, numeric x, numeric y, numeric width, numeric height )` : Crops a image to a specified rectangular area.
* `ImageDrawArc( name, numeric x, numeric y, numeric width, numeric height, numeric startAngle, numeric archAngle, [boolean filled] )` : Draws a circular or elliptical arc.
* `ImageDrawBeveledRect( name, numeric x, numeric y, numeric width, numeric height, boolean raised, boolean filled )` : Draws a rectangle with beveled edges.
* `ImageDrawCubicCurve( name, numeric x1, numeric y1, numeric ctrlx1, numeric ctrly1, numeric ctrlx2, numeric ctrly2, numeric x2, numeric y2 )` : Draws a cubic curve.
* `ImageDrawLine( name, numeric x1, numeric y1, numeric x2, numeric y2 )` : Draws a single line defined by two sets of x and y coordinates on a image.
* `ImageDrawLines( name, array xCoords, array yCoords, [boolean isPolygon = false], [boolean filled = false] )` : Draws a sequence of connected lines defined by arrays of x and y coordinates.
* `ImageDrawOval( name, numeric x, numeric y, numeric width, numeric height, [boolean filled = false] )` : Draws an oval.
* `ImageDrawPoint( name, numeric x, numeric y )` : Draws a point at the specified (x,y) coordinate.
* `ImageDrawQuadraticCurve( name, numeric ctrlx1, numeric ctrly1, numeric x1, numeric y1, numeric x2, numeric y2 )` : Draws a curved line. The curve is controlled by a single point.
* `ImageDrawRect( name, numeric x, numeric y, numeric width, numeric height, [boolean filled = false] )` : Draws a rectangle.
* `ImageDrawRoundRect( name, numeric x, numeric y, numeric width, numeric height, numeric arcWidth, numeric arcHeight, [boolean filled = false] )` : Draws a rectangle with rounded corners.
* `ImageDrawText( name, string str, numeric x, numeric y, [struct attributeCollection] )` : Draws a text string on an image with the baseline of the first character positioned at (x,y) in the image.
* `ImageFlip( name, string transpose )` Flips an image across an axis. Transpose can be one of `vertical | horizontal | diagonal | antidiagonal | 90 | 180 | 270`.
* `ImageGetBlob( name )` : Retrieves the bytes of the underlying image. The bytes are in the same image format as the source image.
* `ImageGetBufferedImage( name )` : Returns the java.awt.BufferedImage object underlying the current image.
* `ImageGetEXIFMetadata( name )` : Retrieves the Exchangeable Image File Format (EXIF) headers in an image as a BoxLang structure.
* `ImageGetEXIFTag( name, string tagName )` : Retrieves the specified EXIF tag in an image.
* `ImageGetHeight( name )` : Retrieves the height of the image in pixels.
* `ImageGetIPTCMetadata( name )` : Retrieves the International Press Telecommunications Council (IPTC )headers in a image as a struct. The IPTC metadata contains text that describes the image that is stored with it. IPTC metadata includes, but is not limited to, caption, keywords, credit, copyright, object name, created date, byline, headline, and source
* `ImageGetIPTCTag( name, string tagName )` : Retrieves the value of the IPTC tag for a image.
* `ImageGetWidth( name )` : Retrieves the width of the specified image.
* `ImageGrayscale( name )` : Converts a image to grayscale.
* `ImageInfo( name )` : Returns a structure that contains information about the image, such as height, width, color model, size, and filename.
* `ImageNegative( name )` : Inverts the pixel values of a image.
* `ImageNew( any source, [numeric width], [numeric height], [string imageType], [string color] )` : Creates a image.
* `ImageOverlay( image1, image2, [string rule], [numeric transparency] )` : Reads two source images and overlays the second source image on the first source image.
* `ImagePaste( image1, image2, [numeric x], [numeric y] )` : Takes two images and an (x,y) coordinate and draws the second image over the first image with the upper-left corner at coordinate (x,y).
* `ImageRead( string path )` : Reads the source pathname or URL and creates a image.
* `ImageReadBase64( string string )` Creates a image from a Base64 string.
* `ImageResize( name, numeric width, numeric height, string interpolation, numeric blurFactor )` : Resizes a image.
* `ImageRotate( name, numeric angle )` : Rotates a image at a specified point by a specified angle.
* `ImageRotateDrawingAxis( name, numeric angle, numeric x, numeric y )` : Rotates all subsequent drawing on a image at a specified point by a specified angle.
* `ImageScaleToFit( name, numeric width, numeric height, string interpolation )` : Creates a resized image with the aspect ratio maintained.
* `ImageSetAntialiasing( name, boolean antialias )` : Switches antialiasing on or off in rendered graphics.
* `ImageSetBackgroundColor( name, string color )` : Sets the background color for the image. The background color is used for clearing a region. Setting the background color only affects the subsequent ImageClearRect calls
* `ImageSetDrawingAlpha` Sets the current drawing alpha for images. All subsequent graphics operations use the specified alpha.
* `ImageSetDrawingColor( name, string color )` : Sets the current drawing color for images. All subsequent graphics operations use the specified color.
* `ImageSetDrawingStroke( name, struct attributeCollection )` : Sets the drawing stroke for points and lines in subsequent images.
* `ImageSetDrawingTransparency( name, numeric percent )` : Specifies the degree of transparency of drawing functions.
* `ImageSharpen( name, numeric gain )` : Sharpens an image by using the unsharp mask filter.
* `ImageShear( name, numeric amount, string direction )` : Shears an image either horizontally or vertically.
* `ImageShearDrawingAxis( name, numeric x, numeric y )` : Shears the drawing canvas.
* `ImageTranslate( name, numeric x, numeric y )` : Copies an image to a new location on the plane.
* `ImageTranslateDrawingAxis( name, numeric x, numeric y )` : Translates the origin of the image context to the point (x,y) in the current coordinate system.
* `ImageWrite( name, string path )` : Writes an image to the specified filename or destination.
* `ImageWriteBase64( name, string format )` : Writes Base64 images to the specified filename and destination.
* `IsImage( name )` : Determines whether a variable returns an image.
* `IsImageFile( string value )` : Verifies whether an image file is valid.
