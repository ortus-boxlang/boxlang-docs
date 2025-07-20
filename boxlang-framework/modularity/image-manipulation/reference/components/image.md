# Image

## Syntax

```boxlang
<bx:Image action="read" source="images/photo.png" name="myImage" />
```

## Attributes

| Name          | Type    | Required | Default | Description                                                                                                 |
| ------------- | ------- | -------- | ------- | ----------------------------------------------------------------------------------------------------------- |
| action        | string  | Yes      |         | The action to perform. One of: border, captcha, convert, info, read, resize, rotate, write, writeToBrowser. |
| angle         | string  | No       |         | The angle for rotation (used with `rotate` action).                                                         |
| color         | string  | No       |         | The color for border or other actions.                                                                      |
| destination   | string  | No       |         | The file path to write the image to (used with `write` action).                                             |
| difficulty    | string  | No       |         | Difficulty level for captcha generation.                                                                    |
| fontSize      | string  | No       |         | Font size for text/captcha.                                                                                 |
| format        | string  | No       |         | Image format for writing/converting.                                                                        |
| height        | numeric | No       |         | Height for resizing or creating images.                                                                     |
| isBase64      | string  | No       |         | If true, treats the source as a base64 string.                                                              |
| name          | string  | No       |         | The variable name to assign the image to in the context.                                                    |
| overwrite     | boolean | No       | false   | Whether to overwrite the destination file if it exists.                                                     |
| quality       | string  | No       |         | Image quality for writing/converting.                                                                       |
| source        | any     | No       |         | The source of the image (file path, URL, or base64 string).                                                 |
| structName    | string  | No       |         | The name of the struct to assign image info to (used with `info` action).                                   |
| text          | string  | No       |         | Text for captcha or drawing.                                                                                |
| thickness     | string  | No       |         | Border thickness.                                                                                           |
| width         | numeric | No       |         | Width for resizing or creating images.                                                                      |
| fonts         | string  | No       |         | Font(s) for text/captcha.                                                                                   |
| interpolation | string  | No       |         | Interpolation method for resizing.                                                                          |

## Description

The `Image` component provides a flexible interface for image processing tasks in BoxLang. It supports reading, writing, resizing, rotating, adding borders, generating captchas, and extracting image info. The component is invoked using HTML-like syntax and accepts a variety of attributes to control its behavior.

## Example

```boxlang
<!-- Read an image and assign to context -->
<bx:Image action="read" source="images/photo.png" name="myImage" />

<!-- Resize an image -->
<bx:Image action="resize" source="images/photo.png" width="400" height="300" name="resizedImage" />

<!-- Add a border to an image -->
<bx:Image action="border" source="images/photo.png" color="red" thickness="5" name="borderedImage" />

<!-- Write an image to disk -->
<bx:Image action="write" source="images/photo.png" destination="output/photo.png" overwrite="true" />

<!-- Get image info and assign to a struct -->
<bx:Image action="info" source="images/photo.png" structName="imgInfo" />
```

## Actions

* `read`: Loads an image from a file, URL, or base64 string.
* `resize`: Resizes the image to the specified width and height.
* `rotate`: Rotates the image by the specified angle.
* `border`: Adds a border to the image with specified color and thickness.
* `write`: Writes the image to the specified destination path.
* `convert`: Converts the image format and writes if possible.
* `info`: Extracts EXIF metadata and assigns to a struct.
* `captcha`: Generates a captcha image (attributes: text, difficulty, fontSize, fonts).
* `writeToBrowser`: Writes the image directly to the browser output.

## Notes

* The `source` attribute can be a file path, URL, or base64 string (set `isBase64` to true for base64).
* The `name` attribute assigns the resulting image to a variable in the context for further use.
* The component does not allow a body; all configuration is via attributes.
* Errors are thrown for unknown actions or invalid attribute combinations.
* For advanced use, see the BoxLang image module documentation for more details on supported actions and attributes.
