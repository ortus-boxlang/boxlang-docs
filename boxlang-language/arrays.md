---
description: An array is a data structure consisting of a collection of elements.
icon: array
---

# Arrays

Almost every programming language allows you to represent different types of collections. In BoxLang, we have three types of collections: arrays, [structures](structures.md), and [queries](queries.md).

An array is a number-indexed list. Imagine you had a blank piece of paper and drew a set of three small boxes in a line:

```
 ---  ---  ---
|   ||   ||   |
 ---  ---  ---
```

You could number each one by its position from left to right:

```
 ---  ---  ---
|   ||   ||   |
 ---  ---  ---
  1    2    3
```

Then put strings in each box:

```
 -------------  ---------  ----------
| "Breakfast" || "Lunch" || "Dinner" |
 -------------  ---------  ----------
       1            2           3
```

We have a three-element Array. BoxLang arrays can grow and shrink dynamically at runtime, just like Array Lists or Vectors in Java, so if we added an element, it’d usually go on the end or be appended at the end.

```
 -------------  ---------  ----------  -----------
| "Breakfast" || "Lunch" || "Dinner" || "Dessert" |
 -------------  ---------  ----------  -----------
       1            2           3           4
```

If you asked the array for the element in position two, you’d get back `Lunch`. Ask for the last element, and you’ll get back: `Dessert`.

## The Story of One

Now, have you detected something funny with the ordering of the elements? Come on, look closer....... They start with `1` and not `0`, now isn't that funny. BoxLang is one of the few languages where array indexes start at `1` and not `0`. So if you have a PHP, Ruby, or Java background, remember that `1` is where you start. Is this good or bad? Well, we will refrain from pointing fingers for now.

{% hint style="info" %}
All arrays in BoxLang are passed by **passed by reference**. Please remember this when working with arrays and passing them to functions. There is also the `passby=reference|value` attribute to function arguments where you can decide whether to pass by reference or value.
{% endhint %}

## Arrays in Code

Let's do some code samples:

{% embed url="https://try.boxlang.io/?code=eJx9lMGO0zAQhu95ilEqsa1ou1zgsKI9sKIS0gISXcQBcZg608TCsSPb2WWFeHfGdtKk6UJbqU4y%2Fv3NPzM52lZ6Bxv4DvkBNX%2FzJeQNNvgUVz%2Flowz%2F2DSKwsJY1GVclRYbyuFHll1fwzt0UgBai09gGrLopdEua6zUXuk55HekS1%2FdQA4v4BgPXSvS8wUsRkE7aZ1Pj88ij%2BH%2BJPYOnw1V2EUGql2rRQBBBY01DFzXUpfwKH2VWMeEq9VqvOHzKQvgJ3mn%2BBEbWIFnE9zR2BoIRQWkqCbtO11QWB8KXII2gEKQc%2BANmNY7WRA4wfa4rG1YXqCjXV%2BAjr%2FGZp7WsNqmxboNgZP0v%2FYCKfuJ3tqbvefYcrBCKk%2BW2UvyPbCDGr2ogiUIwuhChnwzZXQ5xTrG7XOYx%2BvFwJaKuIXX58VhCdBYk0t4g%2BQl2RcqWkFMJkx9kJoAlRoIWZFtBMc7FMEDqpYybzyq1FADoY0yTOjaegkDJl%2FCyzHsEl6dsd4HNRAVWhScY0c8PqN3UBedf7EfB%2FM62OxoWl3ENMfG6eIZ25xH6903bph5jvk%2FpwBi3Klnr%2FCqa%2FbhpAS3N9aDsQWXuLcuc3yPimklw10G4v48RB5cs%2B8NWvpkbkObHc5h9lEknToWvKzjbYVSj4afLWSvKrKZJdeqwZMM%2BHPqqEmvp356u4E3LBsD%2Fz8RMSTmNKaOLFSMaFIGieSSnWf5fZjkFfCGONgY3wPAv%2FGIT14XH3hkHmTRcv90Nnevis7rsLUv%2FpJbuaBfC9hs4XfEHrRm8dHsBmYxdBYk%2FsDiLwjQ05s%3D" %}

```java
fruits = [ "banana", "papaya", "kiwi", "apple", "orange", "grape" ]

// Basic array operations
println( "Length: " & fruits.len() )
println( "First fruit: " & fruits.first() )
println( "Last fruit: " & fruits.last() )

// Functional programming with arrays
println( "--- Functional Operations ---" )

// Map - transform each element with a lambda, no access to outside scopes
uppercaseFruits = fruits.map( fruit -> fruit.ucase() )
println( "Uppercase: " & uppercaseFruits.toString() )

// Filter - get elements matching a condition
longFruits = fruits.filter( (fruit) -> fruit.len() > 5 )
println( "Long names: " & longFruits.toString() )

// Reduce - combine all elements into a single value
totalLength = fruits.reduce( (sum, fruit) -> sum + fruit.len(), 0 )
println( "Total characters: " & totalLength )

// Find - get first matching element
foundFruit = fruits.find( (fruit) -> fruit.startsWith("a") )
println( "First fruit starting with 'a': " & foundFruit )

// Sort order elements
sortedFruits = fruits.sort( (a, b) -> a.compareNoCase(b) )
println( "Sorted: " & sortedFruits.toString() )

// Chain operations together
result = fruits
    .filter( fruit -> fruit.len() <= 6 )
    .map( fruit -> fruit.ucase() )
    .sort()
println( "Chained operations: " & result.toString() )

// forEach - perform action on each element
println( "--- Individual Fruits ---" )
fruits.each( (fruit, index) => {
    println( "#index#: #fruit#" )
} )
```

Please note that all member functions can also be used as traditional [array functions](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/array). However, [member functions](https://boxlang.ortusbooks.com/getting-started/overview/syntax-style-guide#member-functions) look much better for readability.

{% hint style="success" %}
**Tip:** You can use the `toString()` call on any array to get a string representation of its values: `grid.toString()`
{% endhint %}

## Multi-Dimensional Arrays

While BoxLang arrays are inherently one-dimensional, you can create multi-dimensional structures by nesting arrays within arrays. This approach provides flexibility for representing matrices, tables, grids, and other complex data structures.

### Creating Multi-Dimensional Arrays

#### 2D Arrays (Matrix/Grid)

```javascript
// Create a simple 2D array (3x3 grid)
grid = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

// Mixed data types in a 2D array
studentGrades = [
    [ "Alice", 85, 92, 78 ],
    [ "Bob", 91, 88, 95 ],
    [ "Carol", 76, 84, 89 ]
]
```

#### 3D Arrays (Cube/Volume)

```javascript
// 3D array representing a 2x2x2 cube
cube = [
    [
        [ 1, 2 ],
        [ 3, 4 ]
    ],
    [
        [ 5, 6 ],
        [ 7, 8 ]
    ]
]
```

#### Dynamic Creation

```javascript
// Create a 5x5 matrix dynamically
matrix = []
for( row = 1; row <= 5; row++ ) {
    matrix.append( [] )
    for( col = 1; col <= 5; col++ ) {
        matrix[ row ].append( row * col )
    }
}
```

### Accessing Elements

#### 2D Array Access

```javascript
grid = [
    [ "A1", "A2", "A3" ],
    [ "B1", "B2", "B3" ],
    [ "C1", "C2", "C3" ]
]

// Access element at row 2, column 3
println( grid[2][3] )  // Output: "B3"

// Access entire row
println( grid[1] )     // Output: ["A1", "A2", "A3"]
```

#### 3D Array Access

```javascript
// Access element in 3D array
println( cube[1][2][1] )  // Access layer 1, row 2, column 1
```

### Modifying Multi-Dimensional Arrays

#### Adding Rows and Columns

```javascript
data = [
    [ 1, 2 ],
    [ 3, 4 ]
]

// Add a new row
data.append( [ 5, 6 ] )

// Add a column to each existing row
data.each( (row) => row.append( 0 ) )

println( data )
// Output: [[1, 2, 0], [3, 4, 0], [5, 6, 0]]
```

#### Updating Elements

```javascript
// Update a specific cell
data[1][2] = 99

// Update an entire row
data[2] = [ 10, 20, 30 ]
```

### Working with Multi-Dimensional Arrays

#### Iterating Through 2D Arrays

```javascript
matrix = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

// Iterate through all elements
matrix.each( (row, rowIndex) => {
    row.each( (cell, colIndex) => {
        println( "Row #rowIndex#, Col #colIndex#: #cell#" )
    })
})

// Find specific values
matrix.each( (row) => {
    foundIndex = row.find( (cell) => cell > 5 )
    if( foundIndex > 0 ) {
        println( "Found value > 5 at column #foundIndex#" )
    }
})
```

#### Functional Programming with 2D Arrays

```javascript
// Transform all elements in a 2D array
doubled = matrix.map( (row) =>
    row.map( (cell) => cell * 2 )
)

// Filter rows based on criteria
evenRows = matrix.filter( (row) =>
    row.every( (cell) => cell % 2 == 0 )
)

// Sum all elements in the matrix
total = matrix
    .map( (row) => row.reduce( (sum, cell) => sum + cell, 0 ) )
    .reduce( (sum, rowTotal) => sum + rowTotal, 0 )
```

### Practical Examples

#### Game Board (Tic-Tac-Toe)

{% embed url="https://try.boxlang.io/?code=eJyVjk0LwjAMhu%2F9FS%2FZpYXpcLs6T17FqzB66FzF4r7YxA%2FU%2F27bOefVEEJ48%2BRN8kZ1BVJkDDYyECj8FsjwL5lJxqIIG3XSqJqL7lnu7LOFtGmP0I4%2BSixtOmVLE5OMjDNZm74t1R1%2BOjBzrfZHDt411xCmLvRNIF3h4Z9pO1Ofy5qDAju3dgGe8G08tYkMCMLz5sAHDyyRQPzsz8Zw6Eu8AWHPSBI%3D" %}

```javascript
board = [
    [ " ", " ", " " ],
    [ " ", " ", " " ],
    [ " ", " ", " " ]
]

// Make moves
board[1][1] = "X"
board[2][2] = "O"
board[1][3] = "X"

// Display board
board.each( (row, index) => {
    println( "#row[1]# | #row[2]# | #row[3]#" )
    if( index < 3 ) println( "---------" )
})
```

#### Spreadsheet Data

{% embed url="https://try.boxlang.io/?code=eJyFUE1vgzAMvedXWJxAQyVq1%2B3EpH1p0qTt0iPi4LUeRA0BJaFT%2F%2F2cwNSul%2Bbi2H5%2Bz89usIQ71xJ5KKESwK%2BC5BM7SnJIHpsYXmhA6zsyPmQb1GiPCdT5H%2Fy9bw13VpK7r6ZRhsgq03Dpfi2lPEeiCYzLNSM%2F0O7JT7i7C9xT%2FxUI15McuUAlI0TUQhQFvPHCqDVQN%2Bj%2BSORAGTjTFjT%2FHftyJ5dRYOG02lIKS8gAmGyzVwO0DCELtv%2BZMN9Ke7IppFzJoHwInWpVQ1n%2BNwlZXOgZ9XbU6AnwQBYbAhfvJGJQdGWPKe9wuBC8reeewEMzXT4QzZwLS7sxMKRu7PJZMc5yDjdzIQfJRovTlCaTZr8VS5LK" %}

```javascript
spreadsheet = [
    [ "Name", "Age", "Department", "Salary" ],
    [ "John", 30, "Engineering", 75000 ],
    [ "Jane", 25, "Marketing", 65000 ],
    [ "Bob", 35, "Sales", 70000 ]
]

// Get all employees in Engineering
engineers = spreadsheet
    .slice( 2 )  // Skip header row
    .filter( (row) => row[3] == "Engineering" )

// Calculate average salary
salaries = spreadsheet
    .slice( 2 )
    .map( (row) => row[4] )

avgSalary = salaries.reduce( (sum, salary) => sum + salary, 0 ) / salaries.len()
```

#### Image Pixel Data (RGB)

{% embed url="https://try.boxlang.io/?code=eJxVkMtugzAQRff%2BirsMqlUKKFI3qdRkwaqbLFpViIVFJgSV2Mg4L1X9945NCMnIMvNgDpcbx1hTZ6kn7aCQnTM0e1UTTo3bYZ0vcVTtgXoxdBcoBDgKFOl8LvHCp5Qo%2BDnU12KoS3DJEfuPbCRyS6Qllgx8oEyrI9Qv32FHFoO%2BqW3NSeKD5WinJFYXpUdakr5KjNckZULf0YKs3KqLF6SqH4mvXeNIlELw4L2qqO9haYPK7DujvT9mi645UwvlMEtlEgmef3p%2F2JhgUJGWReLPQCfXw%2B3oERP4K6OPZB2cQc0a%2Bkq1JG7ZiHveq26GmTWnCIu38JecX7tBiu%2FjN0x8eAIvDzMv42lQzLpuaVZGiJHddiy5g9VsXx3MmG6U4Z2%2FSET%2Fk72WFA%3D%3D" %}

```javascript
// Represent a 3x3 image with RGB values
image = [
    [ [255, 0, 0], [0, 255, 0], [0, 0, 255] ],    // Red, Green, Blue
    [ [255, 255, 0], [255, 0, 255], [0, 255, 255] ], // Yellow, Magenta, Cyan
    [ [128, 128, 128], [0, 0, 0], [255, 255, 255] ]  // Gray, Black, White
]

// Access red component of pixel at (2,1)
redValue = image[2][1][1]  // Gets the red component

// Convert to grayscale
grayscale = image.map( (row) =>
    row.map( (pixel) => {
        gray = (pixel[1] + pixel[2] + pixel[3]) / 3
        return [ gray, gray, gray ]
    })
)
```

### Helper Functions

#### Utility Functions for Multi-Dimensional Arrays

```javascript
// Get dimensions of a 2D array
function getDimensions( array2D ) {
    return {
        "rows": array2D.len(),
        "cols": array2D.len() > 0 ? array2D[1].len() : 0
    }
}

// Transpose a 2D array (swap rows and columns)
function transpose( array2D ) {
    if( array2D.len() == 0 ) return []

    result = []
    for( col = 1; col <= array2D[1].len(); col++ ) {
        newRow = []
        for( row = 1; row <= array2D.len(); row++ ) {
            newRow.append( array2D[row][col] )
        }
        result.append( newRow )
    }
    return result
}

// Flatten a 2D array into 1D
function flatten( array2D ) {
    return array2D.reduce( (flat, row) => {
        flat.addAll( row )
        return flat
    }, [] )
}
```

### Best Practices

1. **Consistent Structure**: Ensure all sub-arrays have the same length when representing regular grids
2. **Bounds Checking**: Always verify array indices exist before accessing nested elements
3. **Memory Considerations**: Large multi-dimensional arrays can consume significant memory
4. **Initialization**: Pre-populate arrays with default values to avoid null reference errors
5. **Documentation**: Clearly document the expected structure and dimensions of your nested arrays

Multi-dimensional arrays in BoxLang provide powerful data organization capabilities while maintaining the simplicity of single-dimensional array operations.

## Common Methods

The best way to learn about using arrays is to check out the available [member functions](https://boxlang.ortusbooks.com/getting-started/overview/syntax-style-guide#member-functions) and [array functions](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/array).

```javascript
// Sort an array
meals.sort( "textnocase" );

// Clear the array
meals.clear();

// Go on a diet
meals.delete( "Dessert" );
meals.deleteAt( 4 );

// Iterate
meals.each( function( element, index) {
   systemOutput( element & " " & index );
} );

// Filter an array
meals.filter( function( item ){
 return item.findNoCase( "unch" ) gt 0 ? true : false;
} );

// Convert to a list
meals.toList();

// Map/ Reduce
complexData = [ {a: 4}, {a: 18}, {a: 51} ];
newArray = arrayMap( complexData, function(item){
   return item.a;
});
writeDump(newArray);

complexData = [ {a: 4}, {a: 18}, {a: 51} ];
 sum = arrayReduce( complexData, function(prev, element)
 {
 return prev + element.a;
 }, 0 );
writeDump(sum);
```

## Negative Indices

BoxLang also supports the concept of negative indices. This allows you to retrieve the elements from the end of the array backward. So you can easily count back instead of counting forwards:

```javascript
numbers = [1,2,3,4,5]

writedump( numbers[ -1 ] ) // 5
writedump( numbers[ -2 ] ) // 4
writedump( numbers[ -3 ] ) // 3
writedump( numbers[ -4 ] ) // 2
writedump( numbers[ -5 ] ) // 1
writedump( numbers[ -6 ] ) // EXCEPTION!!! Array index out of range
```

## Array Slices

BoxLang supports the [slicing](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/array/arrayslice) of an array via the `arraySlice()` method or the `slice()` member function, respectively.  Slicing allows you to return a **new** array from the start position up to the count of elements you want.

```java
// Signature
arraySlice( array, offset, length )
// Member method
array.slice( offset, length )
```

{% hint style="success" %}
Tip: You can also use negative offsets.
{% endhint %}

```java
array = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
newArray = array.slice( 2, 3 )
println( newArray ) // [ 2, 3, 4 ]
```

## Looping Over Arrays

You can use different constructs for looping over arrays:

* `for` loops
* `loop` constructs
* `each()` closures

```javascript
for( var thisMeal in meals ){
 systemOutput( "I just had #thisMeal#" );
}

for( var x = 1; x lte meals.len(); x++ ){
 systemOutput( "I just had #meals[ x ]#" );
}

meals.each( function( element, index ){
  systemOutput( "I just had #element#" );
} );

bx:loop( from=1, to=meals.len(), index=x ){
  systemOutput( "I just had #meals[ x ]#" );
}
```

### Multi-Threaded Looping

BoxLang allows you to leverage the `each()` operations in a multi-threaded fashion. The `arrayEach()` or `each()` functions allow for a `parallel` and `maxThreads` arguments so the iteration can happen concurrently on as many `maxThreads` as supported by your JVM.

```java
arrayEach( array, callback, parallel:boolean, maxThreads:numeric );
each( collection, callback, parallel:boolean, maxThreads:numeric );
```

This is incredibly awesome, as your callback will now be called concurrently! However, please note that once you enter concurrency land, you should shiver and tremble. Thread concurrency will be of the utmost importance, and you must ensure that scoping is done correctly and that appropriate locking strategies are in place when accessing shared scopes and/or resources.  Here is where unmodifiable arrays, structs, and queries can help.

```java
myArray.each( item => {
   myservice.process( item );
}, true, 20 );
```



## Spread Operator

{% hint style="danger" %}
Coming soon, still in development
{% endhint %}

Arrays also allow the usage of the spread operator syntax to quickly copy all or part of an existing array or object into another array or object. This operator is used by leveraging three dots `...` in specific expressions.

The Spread syntax allows an iterable such as an array expression or string, to be expanded in places where zero or more arguments (for function calls) or elements (for array literals) are expected. Here are some examples to help you understand this operator:

#### Function Calls

```javascript
numbers = [ 1, 2, 3 ]
function sum( x, y, z ){
    return x + y + z;
}
// Call the function using the spread operator
results = sum( ...numbers ) // 6

// Ignore the others
numbers = [ 1, 2, 3, 4, 5 ]
results = sum( ...numbers ) // 6
```

#### Array Definitions

```javascript
numbers = [ 1, 2, 3 ]
myArray = [ 3, 4, ...numbers ]
myArray2 = [ ...numbers ]
myArray2 = [ ...numbers, 4, 66 ]
```

## Rest Operator

{% hint style="danger" %}
Coming soon, still in development
{% endhint %}

The rest operator is similar to the spread operator but behaves oppositely. Instead of expanding the literals, it contracts them into an array you designate via the `...{name}` syntax. You can use this to define endless arguments for a function, for example. In this case, I can create a dynamic `findBy` function that takes in multiple criteria name-value pairs.

```javascript
function findBy( ...args ){
    writeDump( args )
}
findBy( 1, 2, 3, 4, 5 )

function findBy( entityName, ...args ){
    writeDump( args )
}
findBy( "Luis", 1, 2, 3, 4, 5 )
```

## Trailing Commas

BoxLang supports trailing commas when defining array and struct literals. Just in case you miss a dangling comma, we won't shout at you!

```groovy
myArray = [
    "BoxLang",
    "ColdBox",
    "TestBox",
    "CommandBox",
]
println( myArray )

myStruct = {
    name: "BoxLang",
    type: "JVM Dynamic Language",
    version: "1.0.0",
}
println( myStruct )
```

## Change Listeners

All arrays and structures offer the ability to listen to changes to themselves.  This is all done via our `$bx` metadata object available on all arrays/structures.  You will call the `registerChangeListener()` function to register a closure/lambda that will listen to changes on the array.  You can listen:

* To all changes in the array
* To a specific index in the array

However, you must EXPLICITLY return the value that will be stored in the change.

```java
// Listen to all changes in the array
array.$bx.registerChangeListener( closure/lambda )

// Listen to a specific index in the array
array.$bx.registerChangeListener( index, closure/lambda )
```

{% hint style="warning" %}
Please note that this change listener will fire on every array access, so ensure it's performant.
{% endhint %}

The signature of the closure/lambda is the following

```groovy
( Key key, any newValue, any oldValue, array ) => {}
```

{% hint style="success" %}
Please note that the Key is a BoxLang Key object, which simulates a case-insensitive string.  You can use methods on it like:\


* `getName()`
* `getNameNoCase()`
* `toString()`
{% endhint %}

Here are a few simple examples:

{% embed url="https://try.boxlang.io/?code=eJxdT7EKwkAM3fsVjxukhSK4WiqIq%2BjmIg4njfXoEY%2F0ainiv3utbRGTIY%2FkvZfkJo3xNXKcoa6aQ6oUymmnuwFVpjV91c5ZUrhEt0GwFCpN7Ul2d80l7XvMJDHiiroUTO1J24ZSPGwxIi2iOyT55hUhhBPD3nIMdaAWz56zhsJi1iLJ%2FohHW%2FwSJ%2BuJKOQb4VmfRW8k0XRvuJ%2B4CCbOMI3PJNOwIEuetj7GqpfMG7%2Fj0PoAbqZdjg%3D%3D" %}

```java
fruits = [ "banana", "papaya", "kiwi", "apple" ]
// Listen to all changes of the array: add, remove, replace, etc.
fruits.registerChangeListener( (key, newValue, oldValue, array )=>{
    println( "New value: " & newValue );
    println( "Old value: " & oldValue );
    return newValue;
} )

fruits.append( "pineapple" )
fruits.deleteAt( 1 )

println( fruits )

```

Here is another example when listening to a specific index:

{% embed url="https://try.boxlang.io/?code=eJxdT0EKwkAMvPcVwx6khSJ4VRTEq%2BjNi3hYadTFEJd0ayni392WtorJIcNkZkguWrlQYokjzNlKbJPDeOtt06G7q107rfdMBqfk0hmmSldXBtLNzcqVti0W0hSzHOmdmhxC9cFyRTkeXPTIqtoG2XL1ShDLq5PAksLsqMaz1cxhMBm9yBZ%2Fwj0Xv8IhehAqhUpl9C%2BSN7JkODm%2BQFLEEK5caeKi5wtiCrQO8fgv6aQkDR0Zv78R86O1fABV5V9G" %}

```java
fruits = [ "banana", "papaya", "kiwi", "apple" ]
fruits.registerChangeListener( 1, (key, newValue, oldValue, array )=>{
    println( "New value: " & newValue );
    println( "Old value: " & oldValue );
    return newValue;
} )

fruits.append( "luis" )
fruits.deleteAt( 1 )
fruits.insertAt( 1, "hello" )
```
