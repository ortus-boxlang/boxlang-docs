# ImageRegisterFont

## Syntax

```
ImageRegisterFont( path )
```

## Arguments

| Name | Type   | Required | Description                                                                            |
| ---- | ------ | -------- | -------------------------------------------------------------------------------------- |
| path | string | Yes      | Path to a `.ttf` or `.otf` file. Relative paths resolve from the working directory.   |

## Returns

`string` — The font's family name.

## Description

Loads a TrueType or OpenType font file and registers it so the returned family name works as `font` in the attribute struct of `ImageDrawText` and `ImageMeasureText`. The registration is for the whole JVM and loading is cached, so calling it again for the same file is harmless.

If you only need the font for a few calls you can skip registering and use the `file` key instead:

```boxlang
img.drawText( "Hello", 20, 80, { file: "/app/fonts/Brand-Bold.ttf", size: 64 } );
```

With `file`, the font is used directly; `font` is ignored and `size`, `style`, `underline` and `strikeThrough` still apply (`size` defaults to 12). Both forms go through the same font resolution as measuring, so `measureText` and `drawText` always agree.

## Errors

A `BoxRuntimeException` is thrown when the path is empty, the file does not exist (or is a directory), or the file is not a valid TrueType/OpenType font.

## Example

```boxlang
family = ImageRegisterFont( "/app/fonts/Brand-Bold.ttf" );

img = ImageNew( "", 1200, 630, "rgb", "##0b161b" );
img.setDrawingColor( "white" );
img.drawText( "Hello", 80, 300, { font: family, size: 96 } );
```

## Related BIFs

* ImageDrawText
* ImageMeasureText

## Notes

* Java picks the face from the file itself. For `style: "bold"` or `"italic"` with a single-file font, a synthetic bold or oblique is applied; register or point `file` at the bold or italic file for true variants.
* If a system font with the same family name already exists, `font: family` may resolve to that one. Use `file` to be certain.
