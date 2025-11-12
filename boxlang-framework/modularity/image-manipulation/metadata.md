# Image Metadata

Learn how to read and extract EXIF and IPTC metadata from images.

## Table of Contents

- [What is Metadata?](#what-is-metadata)
- [Reading EXIF Metadata](#reading-exif-metadata)
- [Reading IPTC Metadata](#reading-iptc-metadata)
- [Common EXIF Tags](#common-exif-tags)
- [Common IPTC Tags](#common-iptc-tags)
- [Practical Examples](#practical-examples)

## What is Metadata?

Image metadata is embedded information about the image and how it was created:

**EXIF (Exchangeable Image File Format):**

- Camera settings (ISO, aperture, shutter speed)
- Date/time photo was taken
- GPS coordinates
- Camera make and model
- Image dimensions and orientation

**IPTC (International Press Telecommunications Council):**

- Copyright information
- Creator/photographer name
- Keywords and categories
- Caption/description
- Headline and title

## Reading EXIF Metadata

### Get All EXIF Data

```js
img = ImageNew("photo.jpg");
exifData = img.getExifMetaData();

// Returns struct with all EXIF tags
writeDump(exifData);
```

**BIF Syntax:**

```js
img = ImageRead("photo.jpg");
exifData = ImageGetExifMetaData(img);
```

### Get Specific EXIF Tag

```js
img = ImageNew("photo.jpg");

// Get camera make
make = img.getExifTag("Make");

// Get date taken
dateTaken = img.getExifTag("DateTime");

// Get ISO speed
iso = img.getExifTag("ISO Speed Ratings");
```

**BIF Syntax:**

```js
make = ImageGetExifTag(img, "Make");
```

### Check for EXIF Data

```js
img = ImageNew("photo.jpg");
exifData = img.getExifMetaData();

if (structCount(exifData) > 0) {
    // Image has EXIF data
    writeln("Photo taken with: " & exifData["Make"]);
} else {
    // No EXIF data
    writeln("No camera information available");
}
```

## Reading IPTC Metadata

### Get All IPTC Data

```js
img = ImageNew("photo.jpg");
iptcData = img.getIPTCMetaData();

// Returns struct with all IPTC tags
writeDump(iptcData);
```

**BIF Syntax:**

```js
img = ImageRead("photo.jpg");
iptcData = ImageGetIPTCMetadata(img);
```

### Get Specific IPTC Tag

```js
img = ImageNew("photo.jpg");

// Get copyright
copyright = img.getIPTCTag("Copyright Notice");

// Get keywords
keywords = img.getIPTCTag("Keywords");

// Get caption
caption = img.getIPTCTag("Caption/Abstract");
```

**BIF Syntax:**

```js
copyright = ImageGetIPTCTag(img, "Copyright Notice");
```

## Common EXIF Tags

### Camera Information

```js
img = ImageNew("photo.jpg");

// Camera details
make = img.getExifTag("Make");              // "Canon"
model = img.getExifTag("Model");            // "EOS 5D Mark IV"
software = img.getExifTag("Software");      // "Adobe Photoshop"
```

### Camera Settings

```js
// Exposure settings
iso = img.getExifTag("ISO Speed Ratings");       // 400
aperture = img.getExifTag("F-Number");           // 2.8
shutterSpeed = img.getExifTag("Exposure Time");  // "1/500"
exposureProgram = img.getExifTag("Exposure Program"); // "Manual"

// Lens information
focalLength = img.getExifTag("Focal Length");    // "50mm"
lens = img.getExifTag("Lens Model");             // "EF50mm f/1.8 STM"
```

### Date and Time

```js
// When photo was taken
dateTime = img.getExifTag("DateTime");                   // "2025:01:15 14:30:22"
dateTimeOriginal = img.getExifTag("Date/Time Original"); // Original capture time
dateTimeDigitized = img.getExifTag("Date/Time Digitized"); // When digitized
```

### GPS Information

```js
// Location data
latitude = img.getExifTag("GPS Latitude");       // [40, 44, 54.36]
longitude = img.getExifTag("GPS Longitude");     // [-73, 59, 10.56]
altitude = img.getExifTag("GPS Altitude");       // "10.5m"
```

### Image Information

```js
// Image properties
width = img.getExifTag("Image Width");           // 6000
height = img.getExifTag("Image Height");         // 4000
orientation = img.getExifTag("Orientation");     // "Rotate 90 CW"
resolution = img.getExifTag("Resolution Unit");  // "Inches"
xResolution = img.getExifTag("X Resolution");    // 300
yResolution = img.getExifTag("Y Resolution");    // 300
```

### Common EXIF Tag Reference

| Tag Name | Description | Example Value |
|----------|-------------|---------------|
| `Make` | Camera manufacturer | "Canon", "Nikon" |
| `Model` | Camera model | "EOS 5D Mark IV" |
| `DateTime` | Last modification time | "2025:01:15 14:30:22" |
| `Date/Time Original` | Original capture time | "2025:01:15 14:30:22" |
| `ISO Speed Ratings` | ISO sensitivity | 400, 800, 1600 |
| `F-Number` | Aperture value | 2.8, 5.6, 16 |
| `Exposure Time` | Shutter speed | "1/500", "1/60" |
| `Focal Length` | Lens focal length | "50mm", "24mm" |
| `Flash` | Flash status | "Flash fired", "No flash" |
| `GPS Latitude` | GPS latitude | [40, 44, 54.36] |
| `GPS Longitude` | GPS longitude | [-73, 59, 10.56] |
| `Orientation` | Image orientation | "Normal", "Rotate 90 CW" |

## Common IPTC Tags

### Copyright Information

```js
img = ImageNew("photo.jpg");

copyright = img.getIPTCTag("Copyright Notice");
creator = img.getIPTCTag("By-line");  // Photographer name
credit = img.getIPTCTag("Credit");
source = img.getIPTCTag("Source");
```

### Descriptive Information

```js
// Content description
headline = img.getIPTCTag("Headline");
caption = img.getIPTCTag("Caption/Abstract");
keywords = img.getIPTCTag("Keywords");
category = img.getIPTCTag("Category");
```

### Editorial Information

```js
// Publication details
city = img.getIPTCTag("City");
state = img.getIPTCTag("Province/State");
country = img.getIPTCTag("Country/Primary Location Name");
instructions = img.getIPTCTag("Special Instructions");
```

### Common IPTC Tag Reference

| Tag Name | Description | Example Value |
|----------|-------------|---------------|
| `Copyright Notice` | Copyright information | "© 2025 John Doe" |
| `By-line` | Creator/photographer | "John Doe" |
| `Headline` | Image headline | "Sunset Over Mountains" |
| `Caption/Abstract` | Image description | "Beautiful sunset..." |
| `Keywords` | Search keywords | ["landscape", "sunset"] |
| `Category` | Image category | "Nature" |
| `Credit` | Credit line | "Photo by John Doe" |
| `Source` | Image source | "Photography Studio" |
| `City` | City of origin | "New York" |
| `Country/Primary Location Name` | Country | "United States" |

## Practical Examples

### Display Photo Information

```js
img = ImageNew("photo.jpg");
exif = img.getExifMetaData();

if (structCount(exif) > 0) {
    writeOutput("
        <h3>Photo Information</h3>
        <p><strong>Camera:</strong> #exif['Make']# #exif['Model']#</p>
        <p><strong>Date:</strong> #exif['Date/Time Original']#</p>
        <p><strong>Settings:</strong> ISO #exif['ISO Speed Ratings']#,
           f/#exif['F-Number']#, #exif['Exposure Time']#s</p>
        <p><strong>Lens:</strong> #exif['Focal Length']#</p>
    ");
}
```

### Check Image Copyright

```js
img = ImageNew("photo.jpg");
iptc = img.getIPTCMetaData();

if (structKeyExists(iptc, "Copyright Notice")) {
    copyright = iptc["Copyright Notice"];
    writeln("Copyright: " & copyright);
} else {
    writeln("No copyright information found");
}
```

### Extract GPS Coordinates

```js
img = ImageNew("photo.jpg");
exif = img.getExifMetaData();

if (structKeyExists(exif, "GPS Latitude") && structKeyExists(exif, "GPS Longitude")) {
    lat = exif["GPS Latitude"];
    lon = exif["GPS Longitude"];

    // Convert to decimal degrees
    latDecimal = convertGPSToDecimal(lat);
    lonDecimal = convertGPSToDecimal(lon);

    writeln("Location: #latDecimal#, #lonDecimal#");
    writeln("View on map: https://maps.google.com?q=#latDecimal#,#lonDecimal#");
} else {
    writeln("No GPS data available");
}
```

### Generate Image Report

```js
img = ImageNew("photo.jpg");
info = img.info();
exif = img.getExifMetaData();
iptc = img.getIPTCMetaData();

report = {
    filename: "photo.jpg",
    dimensions: "#info.width# x #info.height#",
    fileSize: info.source.size,
    camera: structKeyExists(exif, "Make") ? "#exif.Make# #exif.Model#" : "Unknown",
    dateTaken: structKeyExists(exif, "Date/Time Original") ? exif["Date/Time Original"] : "Unknown",
    copyright: structKeyExists(iptc, "Copyright Notice") ? iptc["Copyright Notice"] : "None",
    keywords: structKeyExists(iptc, "Keywords") ? iptc.Keywords : []
};

writeDump(report);
```

### Filter Images by Camera

```js
// Find all images taken with specific camera
files = directoryList("photos", false, "path", "*.jpg");
canonPhotos = [];

for (file in files) {
    img = ImageNew(file);
    exif = img.getExifMetaData();

    if (structKeyExists(exif, "Make") && exif.Make == "Canon") {
        arrayAppend(canonPhotos, file);
    }
}

writeln("Found #arrayLen(canonPhotos)# Canon photos");
```

### Sort Images by Date

```js
// Sort images by capture date
files = directoryList("photos", false, "path", "*.jpg");
photosByDate = [];

for (file in files) {
    img = ImageNew(file);
    exif = img.getExifMetaData();

    if (structKeyExists(exif, "Date/Time Original")) {
        arrayAppend(photosByDate, {
            file: file,
            date: exif["Date/Time Original"]
        });
    }
}

// Sort by date
arraySort(photosByDate, function(a, b) {
    return compare(a.date, b.date);
});
```

### Add Metadata to Thumbnails

```js
// Create thumbnails with metadata overlays
files = directoryList("photos", false, "path", "*.jpg");

for (file in files) {
    original = ImageNew(file);
    exif = original.getExifMetaData();

    // Create thumbnail
    thumb = original.copy()
        .scaleToFit(400, 300);

    // Add metadata text
    if (structKeyExists(exif, "Date/Time Original")) {
        thumb.setDrawingColor("white")
            .setDrawingTransparency(80)
            .drawText(exif["Date/Time Original"], 10, 290, {
                font: "Arial",
                size: 12
            });
    }

    filename = getFileFromPath(file);
    thumb.write("thumbnails/#filename#");
}
```

## Important Notes

1. **Not all images have metadata** - Check for existence before accessing
2. **EXIF data can be removed** - Privacy tools often strip EXIF
3. **Format support** - EXIF typically in JPEG/TIFF, not PNG/GIF
4. **GPS privacy** - Consider removing GPS data before publishing
5. **Tag names vary** - Different cameras may use different tag names

## Next Steps

- **[Utilities](utilities.md)** - Image properties and format support
- **[Advanced Examples](advanced-examples.md)** - Metadata-driven workflows
- **[Getting Started](getting-started.md)** - Basic image operations
