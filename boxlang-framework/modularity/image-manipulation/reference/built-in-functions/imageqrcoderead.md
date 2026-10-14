# ImageQRCodeRead

Reads the QR code in an image and returns the text it encodes.

## Syntax

```boxlang
ImageQRCodeRead( name [, tryHarder] )
image.readQRCode( [tryHarder] )
```

## Arguments

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| name | any | Yes | N/A | The image or the name of a variable referencing an image to operate on. |
| tryHarder | boolean | No | true | Spend more effort finding the code and also read light-on-dark codes. `false` is fastest. |

## Returns

`string` - The decoded text, or an empty string if no QR code was found.

## Examples

```boxlang
img = ImageRead( "/path/to/qr.png" )
text = ImageQRCodeRead( img )

// Member function
text = img.readQRCode()

// Nothing found returns an empty string
if ( !len( text ) ) {
    writeOutput( "No QR code found" )
}
```

## Related

* [ImageQRCodeGenerate](imageqrcodegenerate.md)
* [ImageRead](imageread.md)
