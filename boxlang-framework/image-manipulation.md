# Image Manipulation

BoxLang has an extensive and awesome image manipulation library that allows you to create and manipulate images with easy syntax. We cannot see every detail about image manipulation, but it is necessary to understand that this functionality is easy in BoxLang and exists.

Apart from core image functions, all functions can be applied to an image object as member functions. Yes, BoxLang allows you to deal with image objects natively.

```java
imgObj = imageRead("https://cfdocs.org/apple-touch-icon.png");
imgObj.resize(50,50);
cfimage(action="writeToBrowser", source=imgObj);

imgObj = imageRead("https://cfdocs.org/apple-touch-icon.png");
imgObj.blur(5);
cfimage(action="writeToBrowser", source=imgObj);

imgObj = imageRead("https://cfdocs.org/apple-touch-icon.png");
imgObj.rotate(90);
cfimage(action="writeToBrowser", source=imgObj);

imgObj = imageRead("https://cfdocs.org/apple-touch-icon.png");
info = imgObj.info();
writeDump(info);
```

You can find some great samples here: [https://cfdocs.org/cfimage](https://cfdocs.org/cfimage) and a listing of all manipulation functions here: [https://cfdocs.org/image%2Dfunctions](https://cfdocs.org/image-functions)


* `GetReadableImageFormats`  Returns a list of image formats that BoxLang can read on the operating system.
* `GetWriteableImageFormats`  Returns a list of image formats that BoxLang can write on the operating system.
* `ImageAddBorder`  Adds a rectangular border around the outside edge of a image.
* `ImageBlur`  Smooths image.
* `ImageCaptcha`  Creates a captcha image
* `ImageClearRect`  Clears the specified rectangle by filling it with the background color of the current drawing surface.
* `ImageCopy`  Copies a rectangular area of an image.
* `ImageCrop`  Crops a image to a specified rectangular area.
* `ImageDrawArc`  Draws a circular or elliptical arc.
* `ImageDrawBeveledRect`  Draws a rectangle with beveled edges.
* `ImageDrawCubicCurve`  Draws a cubic curve.
* `ImageDrawImage`  this function is deprecated, use ImagePaste instead. Draws a image on a image with the baseline of the first character positioned at (x,y) in the image.
* `ImageDrawLine`  Draws a single line defined by two sets of x and y coordinates on a image.
* `ImageDrawLines`  Draws a sequence of connected lines defined by arrays of x and y coordinates.
* `ImageDrawOval`  Draws an oval.
* `ImageDrawPoint`  Draws a point at the specified (x,y) coordinate.
* `ImageDrawQuadraticCurve`  Draws a curved line. The curve is controlled by a single point.
* `ImageDrawRect`  Draws a rectangle.
* `ImageDrawRoundRect`  Draws a rectangle with rounded corners.
* `ImageDrawText`  Draws a text string on a image with the baseline of the first character positioned at (x,y) in the image.
* `ImageFilter`  the function ImageFilter allows to execute a filter against a image.
* `ImageFilterColorMap`  These are passed to the function ImageFilters (see ImageFilter documentation) which convert gray values to colors.
* `ImageFilterCurves`  the curves for the wrap grid
* `ImageFilterKernel`  These are passed to the function ImageFilters
* `ImageFilterWarpGrid`  A warp grid. These are passed to the function ImageFilters (see ImageFilter documentation).
* `ImageFlip`  Flips an image across an axis.
* `ImageFonts`  return all available
* `ImageFormats`  return all available readers and writers
* `ImageGetBlob`  Retrieves the bytes of the underlying image. The bytes are in the same image format as the source image.
* `ImageGetBufferedImage`  Returns the java.awt.BufferedImage object underlying the current image.
* `ImageGetEXIFMetadata`  Retrieves the Exchangeable Image File Format (EXIF) headers in an image as a BoxLang structure.
* `ImageGetEXIFTag`  Retrieves the specified EXIF tag in an image.
* `ImageGetHeight`  Retrieves the height of the image in pixels.
* `ImageGetIptcMetadata`  Retrieves the International Press Telecommunications Council (IPTC )headers in a image as a struct. The IPTC metadata contains text that describes the image that is stored with it. IPTC metadata includes, but is not limited to, caption, keywords, credit, copyright, object name, created date, byline, headline, and source
* `ImageGetIPTCTag`  Retrieves the value of the IPTC tag for a image.
* `ImageGetWidth`  Retrieves the width of the specified image.
* `ImageGrayscale`  Converts a image to grayscale.
* `ImageInfo`  Returns a structure that contains information about the image, such as height, width, color model, size, and filename.
* `ImageNegative`  Inverts the pixel values of a image.
* `ImageNew`  Creates a image.
* `ImageOverlay`  Reads two source images and overlays the second source image on the first source image.
* `ImagePaste`  Takes two images and an (x,y) coordinate and draws the second image over the first image with the upper-left corner at coordinate (x,y).
* `ImageRead`  Reads the source pathname or URL and creates a image.
* `ImageReadBase64`  Creates a image from a Base64 string.
* `ImageResize`  Resizes a image.
* `ImageRotate`  Rotates a image at a specified point by a specified angle.
* `ImageRotateDrawingAxis`  Rotates all subsequent drawing on a image at a specified point by a specified angle.
* `ImageScaleToFit`  Creates a resized image with the aspect ratio maintained.
* `ImageSetAntialiasing`  Switches antialiasing on or off in rendered graphics.
* `ImageSetBackgroundColor`  Sets the background color for the image. The background color is used for clearing a region. Setting the background color only affects the subsequent ImageClearRect calls
* `ImageSetDrawingAlpha`  Sets the current drawing alpha for images. All subsequent graphics operations use the specified alpha.
* `ImageSetDrawingColor`  Sets the current drawing color for images. All subsequent graphics operations use the specified color.
* `ImageSetDrawingStroke`  Sets the drawing stroke for points and lines in subsequent images.
* `ImageSetDrawingTransparency`  Specifies the degree of transparency of drawing functions.
* `ImageSharpen`  Sharpens a image by using the unsharp mask filter.
* `ImageShear`  Shears an image either horizontally or vertically.
* `ImageShearDrawingAxis`  Shears the drawing canvas.
* `ImageTranslate`  Copies an image to a new location on the plane.
* `ImageTranslateDrawingAxis`  Translates the origin of the image context to the point (x,y) in the current coordinate system.
* `ImageWrite`  Writes a image to the specified filename or destination.
* `ImageWriteBase64`  Writes Base64 images to the specified filename and destination.
* `ImageWriteToBrowser`  Writes image to browser.
* `ImageXORDrawingMode`  Sets the paint mode of the image to alternate between the image's current color and the new specified color.
* `IsImage`  Determines whether a variable returns a image.
* `IsImageFile`  Verifies whether an image file is valid.
