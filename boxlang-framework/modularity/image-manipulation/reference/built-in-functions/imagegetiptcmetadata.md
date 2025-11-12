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

`ImageGetIPTCMetadata` extracts IPTC (International Press Telecommunications Council) metadata from the specified image. You can pass a BoxImage object, a variable name referencing an image, or a file path string.

IPTC metadata is commonly used by photographers, photo agencies, and news organizations to embed descriptive information in images. The returned struct contains key-value pairs for available IPTC fields.

**Common IPTC fields include:**

* `Copyright` - Copyright notice
* `Caption` or `Caption-Abstract` - Image description
* `Headline` - Brief title or headline
* `Keywords` - Array or list of keywords
* `By-line` or `Author` - Photographer/creator name
* `Credit` - Provider/agency credit
* `Source` - Original owner
* `Date Created` - Creation date
* `City`, `Province-State`, `Country-Primary Location Name` - Location information
* `Category` - Subject category
* `Supplemental Category` - Additional categories

## Example

```boxlang
// Get IPTC metadata from a BoxImage
meta = ImageGetIPTCMetadata(myImage);

if (structKeyExists(meta, "Copyright")) {
    writeOutput("© #meta.Copyright#<br>");
}

if (structKeyExists(meta, "Keywords")) {
    writeOutput("Tags: #arrayToList(meta.Keywords)#<br>");
}

// Get IPTC metadata directly from a file
meta = ImageGetIPTCMetadata("/path/to/photo.jpg");
writeOutput("Caption: #meta["Caption-Abstract"]#");
```

## See Also

* ImageGetExifMetaData
* ImageGetBlob

## Notes

* The image can be passed as a BoxImage object, a variable name referencing an image, or a file path string.
* If the image cannot be read or metadata cannot be processed, an error is thrown.
* The returned struct contains only available IPTC fields for the image.
* Not all images contain IPTC metadata - check for key existence before accessing.
* IPTC data is primarily found in JPEG files from professional photography workflows.
* Field names may vary slightly - use `structKeyList()` to see available keys.
* For individual tag values, use `ImageGetIPTCTag` instead.
