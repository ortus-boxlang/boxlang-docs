# ImageSplitGrid

Splits an image into a grid of tiles and returns the tiles as a two-dimensional array.

## Syntax

```boxlang
ImageSplitGrid( name, columns, rows )
```

Or as a member:

```boxlang
someImage.splitGrid( columns, rows )
```

## Arguments

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| name | any | Yes | N/A | The source image or variable name that references an image. |
| columns | numeric | Yes | N/A | Number of columns to split the image into. |
| rows | numeric | Yes | N/A | Number of rows to split the image into. |

## Returns

`Array` - A two-dimensional array of `BoxImage` tiles.

- Outer array: rows
- Inner arrays: tiles in each row

## Description

`ImageSplitGrid` divides an image into equally sized tile regions based on the requested `columns` and `rows` values. Each tile is returned as a new `BoxImage` object.

This is useful for sprite sheets, puzzle effects, tiled thumbnails, and per-tile processing workflows.

## Example

```boxlang
img = ImageNew( "./sprite-sheet.png" )

tiles = ImageSplitGrid( img, 4, 3 )

// Access first tile (row 1, column 1)
firstTile = tiles[ 1 ][ 1 ]
ImageWrite( firstTile, "./tile-1-1.png" )

// Member syntax
moreTiles = img.splitGrid( 8, 8 )
```

## Related BIFs

- ImageCopy
- ImageCrop
- ImageScaleToFit

## Notes

- Both `columns` and `rows` are required.
- The function returns a nested array, not a flat array.
- Each tile is a `BoxImage`, so you can immediately call image methods on each tile.
