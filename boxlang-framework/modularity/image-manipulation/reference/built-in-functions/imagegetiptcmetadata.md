# ImageGetIPTCMetadata

Returns the IPTC metadata from an image. This BIF allows you to extract professional image metadata in BoxLang, such as copyright, author, headline, and more.

## Syntax

```
ImageGetIPTCMetadata(name)
```

## Arguments

| Name | Type | Required | Description                                                                           |
| ---- | ---- | -------- | ------------------------------------------------------------------------------------- |
| name | any  | Yes      | The image or the name of a variable referencing an image, or a file path to an image. |

## Returns

* **IStruct**: A struct containing the IPTC metadata from the image.

## Description

`ImageGetIPTCMetadata` extracts IPTC metadata from the specified image. You can pass a BoxImage object, a variable name referencing an image, or a file path string. The returned struct contains key-value pairs for available IPTC metadata fields, such as copyright, author, headline, caption, keywords, and more.

## Example

```boxlang
// Get IPTC metadata from a BoxImage
meta = ImageGetIPTCMetadata(myImage);

// Get IPTC metadata from an image file path
meta = ImageGetIPTCMetadata("/path/to/image.jpg");
```

## See Also

* ImageGetExifMetaData
* ImageGetBlob

## Notes

* The image can be passed as a BoxImage object, a variable name referencing an image, or a file path string.
* If the image cannot be read or metadata cannot be processed, an error is thrown.
* The returned struct contains only available IPTC fields for the image.
