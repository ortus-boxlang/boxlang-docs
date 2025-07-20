# IsImage

## Syntax

```
IsImage( value )
```

## Arguments

| Name  | Type | Required | Description                                    |
| ----- | ---- | -------- | ---------------------------------------------- |
| value | any  | Yes      | The value to check if it is a BoxImage object. |

## Returns

`Boolean` — Returns `true` if the value is a BoxImage object, otherwise `false`.

## Description

Determines whether the provided value is a BoxImage object. Useful for type checking before performing image operations.

## Example

```boxlang
// Check if a variable is an image
if ( IsImage( myVar ) ) {
    // Safe to use image BIFs
    myVar.flip();
}
```

## Related BIFs

* ImageNew
* ImageCopy
* ImageGetWidth

## Notes

* Returns `true` only for BoxImage objects.
* Use this BIF to validate variables before calling image-related functions.
