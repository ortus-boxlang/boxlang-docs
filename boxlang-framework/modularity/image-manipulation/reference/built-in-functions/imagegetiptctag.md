# ImageGetIPTCTag

Returns the value of a specific IPTC metadata tag from an image. This BIF allows you to extract a single IPTC field in BoxLang, such as copyright, author, headline, or any other IPTC tag.

## Syntax

```
ImageGetIPTCTag(name, tagName)
```

## Arguments

| Name    | Type   | Required | Description                                                                           |
| ------- | ------ | -------- | ------------------------------------------------------------------------------------- |
| name    | any    | Yes      | The image or the name of a variable referencing an image, or a file path to an image. |
| tagName | string | Yes      | The name of the IPTC tag to retrieve (e.g., "Copyright", "Author", "Headline").       |

## Returns

* **Object**: The value of the specified IPTC tag, or `null` if not present.

## Description

`ImageGetIPTCTag` extracts the value of a specific IPTC metadata tag from the specified image. You can pass a BoxImage object, a variable name referencing an image, or a file path string. The tag name should match the IPTC field you want to retrieve.

## Example

```boxlang
// Get the copyright tag from a BoxImage
copyright = ImageGetIPTCTag(myImage, "Copyright");

// Get the headline tag from an image file path
headline = ImageGetIPTCTag("/path/to/image.jpg", "Headline");
```

## See Also

* ImageGetIPTCMetadata
* ImageGetExifMetaData

## Notes

* The image can be passed as a BoxImage object, a variable name referencing an image, or a file path string.
* If the image cannot be read or the tag is not present, `null` is returned.
* Tag names are case-sensitive and must match the IPTC field name.
