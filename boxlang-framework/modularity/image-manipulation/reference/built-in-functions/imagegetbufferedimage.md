# ImageGetBufferedImage

Returns the underlying Java `BufferedImage` object for an image. This BIF allows advanced users to access the raw Java image object in BoxLang for direct manipulation or integration with Java APIs.

## Syntax

```
ImageGetBufferedImage(name)
```

## Arguments

| Name | Type | Required | Description                                                             |
| ---- | ---- | -------- | ----------------------------------------------------------------------- |
| name | any  | Yes      | The image or the name of a variable referencing an image to operate on. |

## Returns

* **BufferedImage**: The underlying Java `BufferedImage` object for the image.

## Description

`ImageGetBufferedImage` returns the Java `BufferedImage` object associated with the specified image. This is useful for advanced operations, interoperability with Java libraries, or custom image processing. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Get the BufferedImage object from a BoxImage
buffered = ImageGetBufferedImage(myImage);
```

## See Also

* ImageGetBlob
* ImageRead

## Notes

* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The returned value is a Java `BufferedImage` object, which may require Java interop for further use.
