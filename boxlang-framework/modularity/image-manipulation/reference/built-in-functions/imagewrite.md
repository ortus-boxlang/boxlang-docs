# ImageWrite

## Syntax

```
ImageWrite( name [, path] )
```

Or as a member:

```
someImage.write( [path] )
```

## Arguments

| Name | Type   | Required | Description                                                                                                                    |
| ---- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| name | any    | Yes      | The image to write. Can be a `BoxImage` object or image name.                                                                  |
| path | String | No       | The file path to write the image to. If omitted, writes back to the image's original source path (only for images loaded from files). |

## Returns

`BoxImage` — The image object after writing to disk.

## Description

Writes the specified image to disk. The function has two modes:

- **With path parameter**: Writes the image to the specified file location
- **Without path parameter**: Writes the image back to its original source location (requires the image was loaded from a file)

Parent directories are automatically created if they don't exist. The file stream is properly closed after writing, so the file can be safely deleted or moved immediately after writing.

## Example

```boxlang
// Write image to a specific file
ImageWrite( myImage, "output/photo.png" );

// Write image back to its original location (modify in place)
img = ImageRead("photo.jpg");
img.blur(5);
img.write();  // Writes back to photo.jpg

// Write to a new location with directory creation
ImageWrite( myImage, "deep/nested/path/photo.png" );  // Creates directories automatically

// As a member function (chainable)
myImage.resize(800, 600)
       .blur(2)
       .write("output/edited.png");
```

## Related BIFs

- ImageRead
- ImageNew
- ImageGetBlob
- ImageWriteBase64

## Notes

- The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
- If no path is provided, the image must have been loaded from a file (via `ImageRead` or `ImageNew` with a file path).
- Images created from scratch (blank canvases) or from Base64 cannot use the parameterless `write()` - they require an explicit path.
- Parent directories in the path are created automatically if they don't exist.
- The operation returns the image object for chaining or further processing.
- File handles are properly managed - files can be deleted immediately after writing (no Windows file lock issues).
