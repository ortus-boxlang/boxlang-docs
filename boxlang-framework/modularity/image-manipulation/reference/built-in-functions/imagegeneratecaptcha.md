# ImageGenerateCaptcha

Generates a CAPTCHA image with distorted text designed to be human-readable and harder for automated parsing.

## Syntax

```boxlang
ImageGenerateCaptcha( [height], [width], text [, difficulty] [, fonts] [, fontSize] [, destination] [, overwrite] )
```

## Arguments

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| height | numeric | No | 75 | Height of the generated image in pixels. |
| width | numeric | No | 200 | Width of the generated image in pixels. |
| text | string | Yes | N/A | Text to render in the CAPTCHA image. |
| difficulty | string | No | low | Distortion level: `low`, `medium`, or `high`. |
| fonts | string | No | N/A | Comma-separated font family names, e.g. `"Arial,Verdana,Georgia"`. |
| fontSize | numeric | No | 24 | Font size in points. |
| destination | string | No | N/A | Optional file path to write the generated image. |
| overwrite | boolean | No | false | If `true`, allows writing over an existing destination file. |

## Returns

`BoxImage` - The generated CAPTCHA image.

## Description

`ImageGenerateCaptcha` creates a new image with rendered text and randomized distortion. The function follows ColdFusion-compatible positional ordering: `height, width, text`.

If `destination` is provided, the image is written to disk. If `overwrite` is `false` and the destination already exists, the function throws an error.

## Example

```boxlang
// Basic CAPTCHA generation
captcha = ImageGenerateCaptcha( 75, 200, "A3X9K2" )
ImageWrite( captcha, "./captcha-basic.png" )

// With difficulty and custom font options
captcha2 = ImageGenerateCaptcha(
    80,
    260,
    "BOXLANG",
    "high",
    "Arial,Verdana,Georgia",
    28,
    "./captcha-high.png",
    true
)
```

## Related BIFs

- ImageRead
- ImageWrite
- IsImage

## Notes

- The `text` argument is required and cannot be empty.
- Difficulty defaults to `low` when omitted.
- When `destination` is empty, the function only returns the in-memory image.
