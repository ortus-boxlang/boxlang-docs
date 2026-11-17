---
description: Run bx-image code on MatchBox, without a JVM, using the native backend that ships in the same module.
icon: microchip
---

# MatchBox Native Backend

The bx-image module also runs on [MatchBox](https://github.com/ortus-boxlang/matchbox), the native BoxLang runtime, with no JVM. The same module zip carries the JVM jar and a native plugin. On the JVM nothing changes, and on MatchBox the native plugin provides the image functions.

{% hint style="info" %}
The native backend covers a portable subset of the module: reading images, resizing, grayscale, image information and pixel access. Scripts that stay within that subset run unchanged on both runtimes.
{% endhint %}

## 🚀 Getting Started

Install bx-image as usual. The module zip includes the prebuilt native plugin for Linux on x86-64 (`x86_64-unknown-linux-gnu`), listed under `matchbox.artifacts` in the module's `box.json`. MatchBox users do not need Rust or a compiler.

Run a script with the module:

```bash
matchbox --module /path/to/bx-image my-script.bxs
```

Or build a self-contained native binary. The plugin is embedded in it, so the binary runs on another machine without the module installed:

```bash
matchbox --target native --module /path/to/bx-image --output my-app my-script.bxs
./my-app
```

{% hint style="warning" %}
MatchBox options go before the script file.
{% endhint %}

## 📋 Supported Functions

These functions take the same names and arguments as on the JVM:

| Function | Member | Notes |
| -------- | ------ | ----- |
| `ImageRead( path, [width], [height] )` | | PNG, JPEG, GIF, WebP and SVG, detected by extension or content. Local files only. With a size, an SVG is drawn straight at that size. |
| `ImageNew( source, [width], [height], [imageType], [color] )` | | A path reads the file, an image is copied, and `""` creates a blank image. |
| `ImageResize( name, width, height, [interpolation] )` | `resize()` | A blank or `0` width or height keeps the aspect ratio. Interpolation: `bilinear` (default), `bicubic`, `nearest` or `lanczos`. |
| `ImageGrayScale( name )` / `ImageGreyScale( name )` | `grayScale()` / `greyScale()` | Same gray levels as the JVM. |
| `ImageInfo( name )` | `info()` | Returns `width`, `height` and `source`. |
| [`ImageGetPixels( name, [mode] )`](reference/built-in-functions/imagegetpixels.md) | `getPixels()` | Same values as the JVM. |
| `GetReadableImageFormats()` | | `PNG`, `JPEG`, `JPG`, `GIF`, `WEBP`, `SVG`. |

## ⚖️ Differences from the JVM

* **Unsupported functions** - Writing, drawing, metadata and the other bx-image functions do not exist on MatchBox, so calling one fails. Stay within the functions listed above for code that runs on both runtimes.
* **Local files only** - `ImageRead()` and `ImageNew()` read local files. A URL fails with a clear error.
* **Images, not variable names** - Pass the image itself. Looking an image up by its variable name works only on the JVM.
* **SVG resize** - On MatchBox, `resize()` on an image read from SVG redraws the drawing at the new size. The JVM scales the pixels. For the same sharp result on both, read the SVG at the size you want: `ImageRead( "logo.svg", 400 )`.
* **SVG rendering** - The JVM draws SVG with JSVG and MatchBox with resvg. Shapes and colors match, but anti-aliased edges can differ by a few gray levels.
* **Image info** - `ImageInfo()` returns `width`, `height` and `source`, without the JVM's `colormodel` details.
* **Size limits** - Images are limited to 16384 pixels per side and 256 megapixels.

## 💡 Example: One Script, Both Runtimes

This script turns an image into ASCII art. It uses only supported functions, so it runs on the JVM and on MatchBox:

```js
ramp = " .:-=+*##%@"
art = ImageRead( "logo.svg", 80 )
    .grayScale()
    .getPixels()
    .map( ( row ) => row.map( ( value ) => ramp.mid( int( ( 255 - value ) / 256 * ramp.len() ) + 1, 1 ) ).toList( "" ) )
    .toList( char( 10 ) )

println( art )
```

To branch on what a runtime can read, check the formats:

```js
if ( GetReadableImageFormats().findNoCase( "svg" ) ) {
    icon = ImageRead( "icon.svg", 64 )
}
```

## 🔗 Related

{% content-ref url="reference/built-in-functions/imagegetpixels.md" %}
[imagegetpixels.md](reference/built-in-functions/imagegetpixels.md)
{% endcontent-ref %}

{% content-ref url="getting-started.md" %}
[getting-started.md](getting-started.md)
{% endcontent-ref %}
