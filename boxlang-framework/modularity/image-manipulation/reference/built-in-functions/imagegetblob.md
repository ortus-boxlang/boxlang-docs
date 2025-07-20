# ImageGetBlob

Returns the raw binary data (blob) of an image. This BIF allows you to extract the image as a byte array in BoxLang.

## Syntax

```
ImageGetBlob(name)
```

## Arguments

| Name | Type | Required | Description                                                             |
| ---- | ---- | -------- | ----------------------------------------------------------------------- |
| name | any  | Yes      | The image or the name of a variable referencing an image to operate on. |

## Returns

* **byte\[]**: The raw binary data (blob) of the image.

## Description

`ImageGetBlob` extracts the raw binary data from the specified image. This is useful for saving the image to disk, sending it over a network, or further processing. The image can be passed directly or referenced by variable name.

## Example

```boxlang
// Get the binary data of an image
blob = ImageGetBlob(myImage);
```

## See Also

* ImageRead
* ImageWrite

## Notes

* The image can be passed as a BoxImage object or as a variable name referencing an image.
* The returned value is a byte array representing the image data.
