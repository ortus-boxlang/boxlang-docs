# Image

The `<bx:Image>` component provides tag-based image manipulation in BoxLang.

## Syntax

```boxlang
<bx:Image action="read" source="images/photo.png" name="myImage" />
```

## Attributes

| Name          | Type    | Required | Default | Description                                                                                                 |
| ------------- | ------- | -------- | ------- | ----------------------------------------------------------------------------------------------------------- |
| action        | string  | Yes      |         | The action to perform. One of: `border`, `captcha`, `convert`, `info`, `read`, `resize`, `rotate`, `write`, `writeToBrowser`. |
| angle         | numeric | No       |         | The angle for rotation in degrees (used with `rotate` action).                                               |
| color         | string  | No       |         | The color for border. Accepts color names ("red", "blue") or hex codes ("#FF0000").                         |
| destination   | string  | No       |         | The file path to write the image to (used with `write` action).                                             |
| difficulty    | string  | No       |         | Difficulty level for captcha generation: "low", "medium", "high".                                            |
| fontSize      | numeric | No       |         | Font size for text/captcha in points.                                                                       |
| fonts         | string  | No       |         | Comma-separated list of font names for captcha text.                                                        |
| format        | string  | No       |         | Image format for writing/converting: "png", "jpg", "gif", etc.                                              |
| height        | numeric | No       |         | Height in pixels for resizing or creating images.                                                           |
| interpolation | string  | No       | bilinear | Interpolation method for resizing: "bilinear", "nearest", "bicubic".                                        |
| isBase64      | boolean | No       | false   | If true, treats the source as a base64-encoded string.                                                      |
| name          | string  | No       |         | The variable name to assign the image to in the execution context.                                          |
| overwrite     | boolean | No       | false   | Whether to overwrite the destination file if it exists.                                                     |
| quality       | numeric | No       |         | Image quality for JPEG compression (0.0 to 1.0).                                                            |
| source        | any     | No       |         | The source of the image: file path, URL, BoxImage object, or base64 string.                                 |
| structName    | string  | No       |         | The name of the struct to assign image info to (used with `info` action).                                   |
| text          | string  | No       |         | Text string for captcha generation.                                                                         |
| thickness     | numeric | No       | 1       | Border thickness in pixels.                                                                                 |
| width         | numeric | No       |         | Width in pixels for resizing or creating images.                                                            |
| writeType     | string  | No       | url     | How to write to browser: "url" (cached, returns URL) or "base64" (inline Base64 data URI).                  |

## Description

The `Image` component provides a flexible, tag-based interface for image processing in BoxLang. It supports reading, writing, resizing, rotating, adding borders, generating captchas, and extracting image metadata.

## Actions

### read

Loads an image from a file, URL, or base64 string and assigns it to a variable.

```boxlang
<bx:Image action="read" source="images/photo.png" name="myImage" />
<bx:Image action="read" source="https://example.com/image.jpg" name="remoteImage" />
<bx:Image action="read" source="#base64String#" isBase64="true" name="decodedImage" />
```

**Required Attributes:** `source`, `name`

### resize

Resizes an image to the specified dimensions.

```boxlang
<bx:Image action="resize" source="#myImage#" width="400" height="300" />
<bx:Image action="resize" source="#myImage#" width="800" height="600" interpolation="bicubic" />
```

**Required Attributes:** `source`, `width`, `height`
**Optional Attributes:** `interpolation`

### rotate

Rotates an image by the specified angle (in degrees).

```boxlang
<bx:Image action="rotate" source="#myImage#" angle="45" />
<bx:Image action="rotate" source="#myImage#" angle="90" destination="rotated.jpg" />
```

**Required Attributes:** `source`, `angle`
**Optional Attributes:** `destination`

### border

Adds a solid border around the image.

```boxlang
<bx:Image action="border" source="#myImage#" color="black" thickness="5" />
<bx:Image action="border" source="#myImage#" color="#FF0000" thickness="10" />
```

**Required Attributes:** `source`, `color`, `thickness`

### write

Writes the image to a file on disk.

```boxlang
<bx:Image action="write" source="#myImage#" destination="output/photo.jpg" />
<bx:Image action="write" source="#myImage#" destination="output/photo.jpg" overwrite="true" />
```

**Required Attributes:** `source`, `destination`
**Optional Attributes:** `overwrite`

### info

Extracts metadata and information about the image (dimensions, color model, EXIF data, etc.).

```boxlang
<bx:Image action="info" source="#myImage#" structName="imageInfo" />
<cfoutput>Width: #imageInfo.width#, Height: #imageInfo.height#</cfoutput>
```

**Required Attributes:** `source`, `structName`

### convert

Converts the image to a different format.

```boxlang
<bx:Image action="convert" source="#myImage#" destination="output/photo.png" format="png" />
```

**Required Attributes:** `source`, `destination`, `format`

### captcha

Generates a CAPTCHA image with the specified text.

```boxlang
<bx:Image action="captcha" text="ABC123" difficulty="high" fontSize="24" name="captchaImage" />
```

**Required Attributes:** `text`, `name`
**Optional Attributes:** `difficulty`, `fontSize`, `fonts`

### writeToBrowser

Streams the image directly to the browser response. Returns an `<img>` tag with the image URL or inline data.

```boxlang
<bx:Image action="writeToBrowser" source="#myImage#" />
<bx:Image action="writeToBrowser" source="#myImage#" writeType="base64" alt="My Image" />
<bx:Image action="writeToBrowser" source="#myImage#" writeType="url" width="400" height="300" />
```

**Required Attributes:** `source`
**Optional Attributes:** `writeType` ("url" or "base64"), plus any HTML img attributes (alt, class, style, etc.)

## Complete Example

```boxlang
<!-- Read an image -->
<bx:Image action="read" source="images/photo.jpg" name="myImage" />

<!-- Resize it -->
<bx:Image action="resize" source="#myImage#" width="800" height="600" interpolation="bicubic" />

<!-- Add a border -->
<bx:Image action="border" source="#myImage#" color="navy" thickness="5" />

<!-- Write to disk -->
<bx:Image action="write" source="#myImage#" destination="output/photo-processed.jpg" overwrite="true" />

<!-- Get image information -->
<bx:Image action="info" source="#myImage#" structName="imgInfo" />
<cfoutput>
    <p>Dimensions: #imgInfo.width# x #imgInfo.height#</p>
    <p>Color Model: #imgInfo.colormodel.colormodel_type#</p>
</cfoutput>

<!-- Display in browser -->
<bx:Image action="writeToBrowser" source="#myImage#" alt="Processed Photo" class="img-responsive" />
```

## Related Functions

- ImageRead
- ImageWrite
- ImageResize
- ImageRotate
- ImageInfo

## Notes

- The `source` attribute can be a file path, URL, BoxImage object, or base64 string (with `isBase64=true`).
- The `name` attribute assigns the resulting image to a variable in the execution context for further use.
- The component does not allow a body; all configuration is via attributes.
- For complex workflows with multiple operations, consider using the fluent BoxImage API instead of components.
- File handles are properly managed - no file locking issues on Windows after reading/writing.
- Parent directories are automatically created when writing files.
- The `writeToBrowser` action with `writeType="url"` caches the image in memory and returns a URL for retrieval.
