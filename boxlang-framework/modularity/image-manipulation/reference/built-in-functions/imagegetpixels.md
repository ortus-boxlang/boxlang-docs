# ImageGetPixels

Returns every pixel of an image as an array of rows, as brightness values or as `[r, g, b, a]` arrays.

## Syntax

```
ImageGetPixels( name [, mode] )
```

Or as a member:

```
someImage.getPixels( [mode] )
```

## Arguments

| Name | Type   | Required | Default | Description                                                                 |
| ---- | ------ | -------- | ------- | --------------------------------------------------------------------------- |
| name | any    | Yes      |         | The image to read. Can be a `BoxImage` object or image name.                |
| mode | String | No       | luma    | `luma` for one brightness number per pixel, or `rgba` for `[r, g, b, a]`.   |

## Returns

`Array` — One array per row, from top to bottom. Each row holds one entry per pixel, from left to right:

* `luma` mode: a number from 0 (black) to 255 (white).
* `rgba` mode: an array `[r, g, b, a]` of numbers from 0 to 255. An alpha of 0 is fully transparent.

## Description

`ImageGetPixels` gives you the raw pixel data of an image, so you can analyse it or turn it into something else, such as ASCII art, a color histogram or a brightness map.

The brightness in `luma` mode is computed as `(77 × r + 150 × g + 29 × b + 128) >> 8`, ignoring alpha. These are the integer weights Java uses when it converts an image to grayscale, so `ImageGetPixels` and `ImageGrayScale` agree.

Rows and pixels are 1-based like any BoxLang array: the pixel at `x`, `y` (counted from 0) is `pixels[ y + 1 ][ x + 1 ]`.

## Examples

### Brightness of each pixel

```js
img = ImageRead( "logo.png" )
rows = ImageGetPixels( img )

writeOutput( "Rows: #rows.len()#, columns: #rows[ 1 ].len()#" )
writeOutput( "Top-left brightness: #rows[ 1 ][ 1 ]#" )
```

### Colors of each pixel

```js
pixel = ImageRead( "logo.png" ).getPixels( "rgba" )[ 1 ][ 1 ]

writeOutput( "Red #pixel[ 1 ]#, green #pixel[ 2 ]#, blue #pixel[ 3 ]#, alpha #pixel[ 4 ]#" )
```

### ASCII art

```js
ramp = " .:-=+*##%@"
art = ImageRead( "logo.png" )
    .resize( 60, "" )
    .getPixels()
    .map( ( row ) => row.map( ( value ) => ramp.mid( int( ( 255 - value ) / 256 * ramp.len() ) + 1, 1 ) ).toList( "" ) )
    .toList( char( 10 ) )

println( art )
```

## Related BIFs

* ImageGrayScale
* ImageInfo
* ImageResize
* ImageGetWidth
* ImageGetHeight

## Notes

* A large image returns a large array: one entry per pixel. Resize first when you only need a coarse view.
* Grayscale images report their stored gray level, so in `rgba` mode `r`, `g` and `b` are equal and alpha is 255.
* An unknown `mode` throws an error.
* Available on the JVM and on the [MatchBox native backend](../../matchbox.md), with the same values on both.
