# ImageQRCodeGenerate

Generates a QR code image from text. The result is a regular `BoxImage`, so it works with `ImageWrite`, `ImageResize`, `ImageWriteBase64` and the other image functions.

## Syntax

```boxlang
ImageQRCodeGenerate( text [, size] [, format] [, errorCorrection] [, quietZone] [, foreground] [, background] [, logo] [, logoScale] )
"text".toQRCode( [size] [, format] [, errorCorrection] [, quietZone] [, foreground] [, background] [, logo] [, logoScale] )
```

## Arguments

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| text | string | Yes | N/A | The text to encode. Must be non-empty. |
| size | numeric | No | 125 | Edge length of the square image in pixels. Clamped to 16 to 4096. |
| format | string | No | png | Output format. Any format returned by `GetWriteableImageFormats()`. |
| errorCorrection | string | No | M | `L` (7%), `M` (15%), `Q` (25%) or `H` (30%). Always `H` when a logo is used. |
| quietZone | numeric | No | 4 | Light margin around the code in modules. Clamped to 0 to 32. The QR specification calls for 4. |
| foreground | string | No | black | Color of the dark modules. A color name or hex code (`#RGB`, `#RRGGBB` or `#AARRGGBB`). |
| background | string | No | white | Color of the light modules. A color name or hex code. Use an alpha hex such as `#00ffffff` for transparent. |
| logo | any | No | N/A | An image, file path or URL drawn in the center of the code. |
| logoScale | numeric | No | 0.2 | Fraction of the code's edge length the logo covers. Clamped to 0.3. |

## Returns

`BoxImage` - The QR code. Its format is set to `format`, so `getBlob` and `writeBase64` produce that format.

## Description

The module grid is scaled to the largest whole-pixel module size that fits `size`, then stretched to exactly `size` with nearest-neighbour sampling so the code stays sharp and scannable.

A logo hides part of the code, so error correction is forced to `H` when one is supplied. The generated code is scanned after the logo is drawn. If the logo makes it unreadable, for example a large logo on a very short text, an error is thrown instead of returning a code that will not scan. Use a smaller `logoScale`, a larger `size`, or more text.

## Examples

```boxlang
// Basic usage
qr = ImageQRCodeGenerate( "https://example.com/verify" )
ImageWrite( qr, "/path/to/qr.png" )

// Size, format and error correction
qr = ImageQRCodeGenerate( "ME:12345678", 250, "gif", "H" )

// Colors and a logo
qr = ImageQRCodeGenerate( text="https://example.com", size=400, foreground="#1a237e", background="white", logo="/logo.png" )

// Member function on a string
qr = "https://example.com".toQRCode( 250 )
```

## Related

* [ImageQRCodeRead](imageqrcoderead.md)
* [ImageWrite](imagewrite.md)
* [GetWriteableImageFormats](getwriteableimageformats.md)
