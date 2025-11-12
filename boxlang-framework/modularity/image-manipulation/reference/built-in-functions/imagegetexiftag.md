# ImageGetExifTag

Retrieves the value of a specific EXIF metadata tag from an image.

## Method Signature

```boxlang
string ImageGetExifTag(image, tagName)
image.getExifTag(tagName)
```

## Arguments

| Argument | Type   | Required | Description                                  | Default |
| -------- | ------ | -------- | -------------------------------------------- | ------- |
| image    | any    | true     | The image object or variable name            |         |
| tagName  | string | true     | The name of the EXIF tag to retrieve         |         |

## Returns

Returns the value of the specified EXIF tag as a string, or an empty string if the tag is not found.

## Description

The `ImageGetExifTag` function extracts a specific EXIF (Exchangeable Image File Format) metadata tag value from an image. EXIF metadata is commonly embedded in photos taken by digital cameras and smartphones, containing information about camera settings, date/time, GPS coordinates, and more.

Common EXIF tags include:

- `Make` - Camera manufacturer
- `Model` - Camera model
- `DateTime` - Date and time the image was created
- `DateTimeOriginal` - Date and time the photo was taken
- `Orientation` - Image orientation
- `ExposureTime` - Shutter speed
- `FNumber` - F-stop/aperture
- `ISO` - ISO speed
- `FocalLength` - Lens focal length
- `Flash` - Flash mode used
- `WhiteBalance` - White balance setting
- `GPSLatitude` / `GPSLongitude` - GPS coordinates
- `Artist` - Photographer name
- `Copyright` - Copyright information

## Examples

### Get Camera Information

```boxlang
img = ImageNew("photo.jpg");
make = ImageGetExifTag(img, "Make");
model = ImageGetExifTag(img, "Model");
writeOutput("Camera: #make# #model#");
```

### Get Photo Settings

```boxlang
img = ImageNew("photo.jpg");
iso = img.getExifTag("ISO");
aperture = img.getExifTag("FNumber");
shutterSpeed = img.getExifTag("ExposureTime");
focalLength = img.getExifTag("FocalLength");

writeOutput("ISO: #iso#<br>");
writeOutput("Aperture: f/#aperture#<br>");
writeOutput("Shutter Speed: #shutterSpeed#s<br>");
writeOutput("Focal Length: #focalLength#mm");
```

### Get Date and Location

```boxlang
img = ImageNew("vacation.jpg");
dateTime = img.getExifTag("DateTimeOriginal");
lat = img.getExifTag("GPSLatitude");
lon = img.getExifTag("GPSLongitude");

writeOutput("Taken: #dateTime#<br>");
if (len(lat) && len(lon)) {
    writeOutput("Location: #lat#, #lon#");
}
```

### Check Copyright Information

```boxlang
img = ImageNew("professional.jpg");
artist = ImageGetExifTag(img, "Artist");
copyright = ImageGetExifTag(img, "Copyright");

if (len(copyright)) {
    writeOutput("© #copyright#");
} else if (len(artist)) {
    writeOutput("Photo by: #artist#");
}
```

## Related Functions

- ImageGetExifMetadata - Get all EXIF metadata as a struct
- ImageGetIPTCTag - Get a specific IPTC tag value
- ImageGetIPTCMetadata - Get all IPTC metadata as a struct
- ImageInfo - Get comprehensive image information including metadata

## Notes

- EXIF metadata is only available for images that contain it (primarily JPEG files from digital cameras)
- Not all images will have all EXIF tags
- Tag names are case-sensitive
- Returns an empty string if the tag is not found
- EXIF data is extracted automatically when the image is loaded
- For a complete list of available tags, use `ImageGetExifMetadata()` to see all metadata
