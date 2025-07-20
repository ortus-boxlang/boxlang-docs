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

| Name | Type   | Required | Description                                                                                |
| ---- | ------ | -------- | ------------------------------------------------------------------------------------------ |
| name | any    | Yes      | The image to write. Can be a `BoxImage` object or image name.                              |
| path | String | No       | The file path to write the image to. If omitted, uses the image's current path or default. |

## Returns

`BoxImage` — The image object after writing to disk.

## Description

Writes the specified image to disk at the given file path. If no path is provided, the image is saved to its current or default location. Useful for exporting images after processing or manipulation.

## Example

```boxlang
// Write image to a specific file
ImageWrite( myImage, "output/photo.png" );

// As a member function
myImage.write( "output/edited.png" );
```

## Related BIFs

* ImageRead
* ImageNew
* ImageGetBlob

## Notes

* The `name` argument can be a `BoxImage` object or the name of an image variable in the current context.
* The operation writes the image to disk and returns the image object for chaining or further processing.
* The `path` argument should be a valid file path. If omitted, the image is saved to its default location.
