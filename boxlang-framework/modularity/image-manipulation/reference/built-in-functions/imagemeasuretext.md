# ImageMeasureText

## Syntax

```
ImageMeasureText( name, str [, attributeCollection] )
```

Or as a member:

```
someImage.measureText( str [, attributeCollection] )
```

## Arguments

| Name                | Type   | Required | Description                                                                                         |
| ------------------- | ------ | -------- | --------------------------------------------------------------------------------------------------- |
| name                | any    | Yes      | The image or the name of a variable referencing an image. Its rendering settings are used.          |
| str                 | string | Yes      | The single line of text to measure. An empty string has width 0.                                    |
| attributeCollection | struct | No       | The same font struct `ImageDrawText` takes: `font`, `size`, `style`, `underline`, `strikeThrough`.  |

## Returns

A struct, all values in pixels:

| Key     | Description                                                       |
| ------- | ----------------------------------------------------------------- |
| width   | Advance width of the string.                                      |
| height  | `ascent + descent`.                                               |
| ascent  | Distance from the baseline up to the top of the font.             |
| descent | Distance from the baseline down to the bottom of the font.        |
| leading | Extra space the font recommends between lines.                    |

## Description

Measures text without drawing it. It uses the very same font resolution as `ImageDrawText`, so the numbers match what gets rendered. An invalid `style` throws, as it does for `ImageDrawText`. The text is treated as one line; split on newlines yourself.

The `y` you pass to `drawText` is the baseline, so the text occupies `y - ascent` to `y + descent`. The distance between baselines of consecutive lines is `height + leading`.

## Example

```boxlang
img   = ImageNew( "", 1200, 630, "rgb", "black" );
attrs = { font: "SansSerif", size: 64, style: "bold" };

m = img.measureText( "Hello World", attrs );
// m.width, m.height, m.ascent, m.descent, m.leading

// center horizontally
img.setDrawingColor( "white" );
img.drawText( "Hello World", ( img.getWidth() - m.width ) / 2, 300, attrs );
```

### Word wrap and shrink to fit

Wrapping is left to the caller on purpose (breaking rules, ellipsis, hyphenation and max lines are policy), but it is a few lines on top of `measureText`:

```boxlang
function wrapLines( img, text, attrs, maxWidth ) {
    var lines = [];
    var line  = "";
    for ( var word in text.listToArray( " " ) ) {
        var candidate = line.len() ? line & " " & word : word;
        if ( line.len() && img.measureText( candidate, attrs ).width > maxWidth ) {
            lines.append( line );
            line = word;
        } else {
            line = candidate;
        }
    }
    if ( line.len() ) lines.append( line );
    return lines;
}

attrs = { font: "SansSerif", size: 72, style: "bold" };
lines = wrapLines( img, title, attrs, 1000 );
while ( lines.len() > 3 && attrs.size > 24 ) {
    attrs.size -= 4;
    lines = wrapLines( img, title, attrs, 1000 );
}
```

## Related BIFs

* ImageDrawText

## Notes

* Measurement uses the image's graphics settings (such as anti-aliasing), the same as drawing.
* Results are fractional; round up when sizing boxes.
