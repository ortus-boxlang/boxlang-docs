# IsImageFile

## Syntax

```
IsImageFile( value )
```

## Arguments

| Name  | Type | Required | Description                                           |
| ----- | ---- | -------- | ----------------------------------------------------- |
| value | any  | Yes      | The file path or URL to check if it is an image file. |

## Returns

`Boolean` — Returns `true` if the value is a valid image file or URL, otherwise `false`.

## Description

Determines whether the provided value is a valid image file or image URL. Useful for validating file paths or URLs before attempting to read or process images.

## Example

```boxlang
// Check if a file is an image
if ( IsImageFile( "images/photo.png" ) ) {
    img = ImageRead( "images/photo.png" );
}

// Check if a URL is an image
if ( IsImageFile( "https://example.com/image.jpg" ) ) {
    img = ImageRead( "https://example.com/image.jpg" );
}
```

## Related BIFs

* IsImage
* ImageRead
* ImageNew

## Notes

* Returns `true` for valid image files or URLs that can be read as images.
* Returns `false` if the file or URL is not a valid image or cannot be read.
* Use this BIF to validate paths before calling image-related functions.
