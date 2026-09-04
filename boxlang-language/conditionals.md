---
description: Control program flow with if/else, switch, ternary, elvis, and safe navigation operators
icon: diagram-project
---

# 🔀 Conditionals

BoxLang provides powerful conditional expressions and control flow statements to direct program execution based on runtime conditions. From traditional `if/else` blocks to modern operators like elvis (`?:`) and safe navigation (`?.`), BoxLang offers multiple ways to handle conditional logic elegantly.

{% hint style="info" %}
**Modern Operators**: BoxLang supports modern conditional operators including ternary (`? :`), elvis (`?:`), and safe navigation (`?.`) for concise, expressive code. These operators help avoid verbose null checks and make code more readable.
{% endhint %}

## 💻 Conditionals in Code

Let's explore conditional operations with practical examples:

```js
// Traditional if/else
age = 25;
if ( age >= 18 ) {
    println( "You are an adult" );
} else {
    println( "You are a minor" );
}

// Ternary operator - compact conditional
status = ( age >= 18 ) ? "adult" : "minor";
println( "Status: #status#" );

// Elvis operator - default value assignment
username = userInput ?: "Anonymous";
println( "Welcome, #username#!" );

// Safe navigation - avoid null pointer errors
user = { name: "Alice", profile: { email: "alice@example.com" } };
email = user?.profile?.email ?: "no-email@example.com";
println( "Email: #email#" );

// Safe navigation with missing keys - returns undefined instead of error
missingEmail = user?.settings?.notifications?.email;
// missingEmail is undefined, not an error!

// Switch statement for multiple conditions
day = "Monday";
switch ( day ) {
    case "Monday":
    case "Tuesday":
    case "Wednesday":
    case "Thursday":
    case "Friday": {
        println( "Weekday" );
        break;
    }
    case "Saturday":
    case "Sunday": {
        println( "Weekend!" );
        break;
    }
    default: {
        println( "Invalid day" );
    }
}
```

## 🔍 Comparison Operators

Conditional statements evaluate to **true** or **false** only. BoxLang provides both symbolic and word-based operators for comparisons.

### Operator Reference

| Symbolic | Word Form | Description | Example |
|----------|-----------|-------------|---------|
| `==` | `EQ`, `EQUAL`, `IS` | Equal to (with type coercion) | `a == 1` |
| `===` | - | Identity / Strict equality (no cross-type coercion, type-aware normalization) | `a === 1` |
| `!=` | `NEQ`, `NOT EQUAL` | Not equal to (with type coercion) | `a != 2` |
| `!==` | - | Negated identity / strict equality | `a !== 2` |
| `>` | `GT`, `GREATER THAN` | Greater than | `a > 2` |
| `>=` | `GTE`, `GREATER THAN OR EQUAL TO` | Greater than or equal | `a >= 1` |
| `<` | `LT`, `LESS THAN` | Less than | `a < 2` |
| `<=` | `LTE`, `LESS THAN OR EQUAL TO` | Less than or equal | `a <= 1` |
| `CONTAINS` | - | String/array contains value | `str CONTAINS "test"` |
| `DOES NOT CONTAIN` | - | Does not contain value | `str DOES NOT CONTAIN "test"` |

### Basic Comparisons

```js
a = 1;

// Numeric comparisons
if ( a == 1 ) { println( "Equal to 1" ); }
if ( a != 2 ) { println( "Not equal to 2" ); }
if ( a > 0 ) { println( "Greater than 0" ); }
if ( a >= 1 ) { println( "Greater than or equal to 1" ); }
if ( a < 2 ) { println( "Less than 2" ); }
if ( a <= 1 ) { println( "Less than or equal to 1" ); }

// Word-based operators (same behavior)
if ( a EQ 1 ) { println( "Equal using EQ" ); }
if ( a GT 0 ) { println( "Greater than using GT" ); }
if ( a LT 2 ) { println( "Less than using LT" ); }
```

### Type Checking Functions

Many BoxLang functions return `true` or `false`, making them ideal for conditional statements:

```js
// Type checking
value = [1, 2, 3];
if ( isArray( value ) ) {
    println( "It's an array!" );
}

if ( isStruct( { name: "Alice" } ) ) {
    println( "It's a struct!" );
}

if ( isNumeric( "123" ) ) {
    println( "Can be converted to a number" );
}

// String checks
text = "Hello World";
if ( text.length() > 0 ) {
    println( "Text is not empty" );
}

// Struct key existence
produce = {
    grapes: 2,
    lemons: 1,
    eggplants: 6
};

if ( produce.keyExists( "grapes" ) ) {
    println( "We have grapes!" );
    produce.grapes--;
}

// Alternative syntax
if ( structKeyExists( produce, "lemons" ) ) {
    println( "We have lemons!" );
}
```

### Truthy and Falsy Values

BoxLang evaluates certain values as boolean:

```js
// Numbers: 0 is false, everything else is true
if ( 1 ) { println( "1 is true" ); }      // Executes
if ( -2 ) { println( "-2 is true" ); }    // Executes
if ( 0 ) { println( "0 is true" ); }      // Does NOT execute

// Empty strings are false
if ( "" ) { println( "Empty string" ); }  // Does NOT execute
if ( "text" ) { println( "Has text" ); }  // Executes

// Null/undefined are false
if ( nullValue() ) { println( "Null" ); } // Does NOT execute
```

## 🔀 If, Else If, & Else

Why do we have conditional statements? Most often it's to control conditional instructions, especially `if` / `else if` / `else` expressions. Let's write an example by adding a method to our `PersonalChef.bx` class:

```java
class accessors=true{

    property name="status";

    function init(){
        status = "The water is not boiling yet.";

        return this;
    }

    function water_boiling( numeric minutes ){
        if( arguments.minutes < 7 ){
            status = "The water is not boiling yet.";
        } else if ( arguments.minutes == 7 ){
            status = "It's just barely boiling.";
        } else if ( arguments.minutes == 8 ){
            status = "It's boiling!";
        } else {
            status = "Hot! Hot! Hot!";
        }

        return this;
    }

}
```

Try this example using 5, 7, 8 and 9 for the values of minutes.

```java
chef = new PersonalChef();

for( i in [ 5, 7, 8, 9 ] ){
    chef.water_boiling( i );
    systemOutput( chef.getStatus() );
}
```

* When the minutes is 5, here is how the execution goes: Is it true that 5 is less than 7? Yes, it is, so print out the line `The water is not boiling yet.`.
* When the minutes is 7, it goes like this: Is it true that 7 is less than 7? No. Next, is it true that 7 is equal to 7? Yes, it is, so print out the line `It's just barely boiling`.
* When the minutes is 8, it goes like this: Is it true that 8 is less than 7? No. Next, is it true that 8 is equal to 7? No. Next, is it true that 8 is equal to 8? Yes, it is, so print out the line `It's boiling!.`

Lastly, when total is 9, it goes:" Is it "true" that 9 is less than 7?

No. Next, is it true that 9 is equal to 7? No. Next, is it true that 9 is equal to 8? No. Since none of those are true, execute the else and print the line `Hot! Hot! Hot!`.

An `if` block has:

* One `if` statement whose instructions are executed only if the statement is **true**
* Zero or more `else if` statements whose instructions are executed only if the statement is **true**
* Zero or one `else` statement whose instructions are executed if no `if` nor `else if` statements were **true**

Only one section of the `if / else if / else` structure can have its instructions run. If the if is **true**, for instance, BoxLang will never look at the `else if`. Once one block executes, that’s it.

## ❓ Ternary Operator

The ternary operator provides a compact one-line conditional expression: `condition ? trueValue : falseValue`

### Syntax

```js
result = ( condition ) ? valueIfTrue : valueIfFalse;
```

The `condition` is evaluated. If **true**, the first expression is returned; if **false**, the second expression is returned.

### Basic Examples

```js
// Simple condition
age = 20;
status = ( age >= 18 ) ? "adult" : "minor";
println( status ); // "adult"

// Inline in expressions
message = "You are " & ( age >= 18 ? "eligible" : "not eligible" ) & " to vote";

// Return from function
function getDiscount( boolean isMember ) {
    return isMember ? 0.20 : 0.05;
}

// Assign based on null check
username = inputValue ? inputValue : "Guest";
```

### Nested Ternary (Use with Caution)

```js
// Nested ternary for multiple conditions
score = 85;
grade = ( score >= 90 ) ? "A" :
        ( score >= 80 ) ? "B" :
        ( score >= 70 ) ? "C" :
        ( score >= 60 ) ? "D" : "F";

println( "Grade: #grade#" ); // "Grade: B"
```

{% hint style="warning" %}
**Best Practice**: Avoid deeply nested ternary operators as they become hard to read and debug. For complex conditions with multiple branches, use `if / else if / else` or `switch` statements instead.
{% endhint %}

### Practical Uses

```js
// Setting default values
maxItems = config.maxItems ? config.maxItems : 10;

// Pluralization
itemCount = 3;
message = "You have #itemCount# item" & ( itemCount != 1 ? "s" : "" );

// Conditional CSS classes
class = isActive ? "btn-primary" : "btn-secondary";

// Mathematical operations
result = ( x > 0 ) ? x * 2 : x / 2;
```

## 🎸 Elvis Operator

The elvis operator (`?:`) provides elegant null-coalescing and default value assignment. It returns the left operand if it exists and is not null, otherwise returns the right operand.

### Syntax

```js
result = value ?: defaultValue;
```

If `value` is **null** or **undefined**, `defaultValue` is used. Otherwise, `value` is used.

### Basic Examples

```js
// Default username
myName = userName ?: "Anonymous";
// If userName is null/undefined, myName = "Anonymous"

// Function parameters with defaults
function greet( name ) {
    displayName = name ?: "Guest";
    println( "Hello, #displayName#!" );
}

greet( "Alice" ); // "Hello, Alice!"
greet( null );     // "Hello, Guest!"
```

### Before Elvis: The Old Way

Before the elvis operator, you had to use verbose checks:

```js
// Old way - verbose
if ( isDefined( "userName" ) && !isNull( userName ) ) {
    myName = userName;
} else {
    myName = "Anonymous";
}

// Elvis way - concise
myName = userName ?: "Anonymous";
```

### Practical Applications

```js
// Configuration with defaults
config = {
    timeout: 30,
    retries: null
};

timeout = config.timeout ?: 60;  // Uses 30 (exists)
retries = config.retries ?: 3;   // Uses 3 (null)
maxSize = config.maxSize ?: 100; // Uses 100 (doesn't exist)

// Function return values
function getUserEmail( userId ) {
    user = findUser( userId );
    return user.email ?: "no-email@example.com";
}

// Chaining with safe navigation
email = user?.profile?.email ?: "default@example.com";

// Query results
qry = queryExecute( "SELECT name FROM users WHERE id = ?" , [userId] );
userName = qry.name[1] ?: "Unknown User";
```

### Elvis vs Ternary

```js
// Elvis - checks for null/undefined
result = value ?: "default";

// Ternary - checks any boolean condition
result = ( value > 10 ) ? "big" : "small";

// Equivalent elvis using ternary (more verbose)
result = ( value != null && isDefined( "value" ) ) ? value : "default";
```

{% hint style="success" %}
**Best Practice**: Use elvis (`?:`) for null-checking and default values. Use ternary (`? :`) for conditional logic based on comparisons or boolean conditions.
{% endhint %}

## ❓ Safe Navigation Operator

The safe navigation operator (`?.`) allows you to safely navigate nested structures without throwing `key not exists` exceptions. If any part of the chain is null or undefined, the entire expression returns `undefined` instead of throwing an error.

### Syntax

```js
result = object?.property?.nestedProperty;
```

If `object` or `property` is **null** or **undefined**, the expression returns `undefined` instead of throwing an error.

### Before Safe Navigation: The Old Way

```js
// Old way - nested checks (verbose and error-prone)
result = "";
if ( structKeyExists( var, "key" ) ) {
    if ( structKeyExists( var.key, "otherkey" ) ) {
        result = var.key.otherkey;
    }
}

// Safe navigation way - clean and concise
result = var?.key?.otherKey ?: "";
```

### Basic Examples

```js
// Safely access nested properties
user = {
    name: "Alice",
    profile: {
        email: "alice@example.com"
    }
};

// Safe access - no error if profile or email is missing
email = user?.profile?.email;
println( email ); // "alice@example.com"

// Missing property - returns undefined
phone = user?.profile?.phone;
println( phone ); // undefined

// Combining with elvis for defaults
phone = user?.profile?.phone ?: "No phone number";
println( phone ); // "No phone number"
```

### Practical Applications

```js
// API response handling
apiResponse = {
    data: {
        user: {
            details: {
                address: {
                    city: "San Francisco"
                }
            }
        }
    }
};

// Safe deep navigation
city = apiResponse?.data?.user?.details?.address?.city;
println( city ); // "San Francisco"

// Handle missing data gracefully
zipCode = apiResponse?.data?.user?.details?.address?.zipCode ?: "Unknown";

// Database query results
qry = queryExecute( "SELECT * FROM users WHERE id = ?", [userId] );
firstName = qry?.firstName[1] ?: "Unknown";

// Configuration access
dbHost = config?.database?.connection?.host ?: "localhost";
dbPort = config?.database?.connection?.port ?: 3306;
```

### Chaining with Other Operators

```js
// Safe navigation + elvis operator
email = user?.contacts?.email ?: "no-email@example.com";

// Safe navigation + method calls
upperName = user?.profile?.name?.ucase() ?: "UNKNOWN";

// Array access with safe navigation
firstItem = data?.items?[1];

// Multiple chains
street = order?.customer?.billing?.address?.street ?:
         order?.customer?.shipping?.address?.street ?:
         "No address provided";
```

### Error Prevention

```js
// Without safe navigation - throws error if user is null
try {
    city = user.profile.address.city; // ERROR if user, profile, or address is null
} catch ( any e ) {
    city = "Unknown";
}

// With safe navigation - no error, returns undefined
city = user?.profile?.address?.city ?: "Unknown";
```

{% hint style="success" %}
**Best Practice**: Use safe navigation (`?.`) when accessing properties that might not exist. Combine with elvis (`?:`) to provide default values for missing data. This pattern is especially useful for API responses, configuration files, and optional struct properties.
{% endhint %}

## 🔀 Switch, Case, & Default

The `switch` statement evaluates a single expression and executes different code blocks based on matching case values. It's ideal when you have multiple discrete values to check against a single variable.

### Syntax

```js
switch ( expression ) {
    case value1: {
        // Execute if expression == value1
        break;
    }
    case value2:
    case value3: {
        // Execute if expression == value2 OR value3
        break;
    }
    default: {
        // Execute if no case matches
    }
}
```

### Structure

- **One `switch` statement** - Evaluates a single expression once
- **Multiple `case` statements** - Define values to match against
- **Optional `break`** - Exits the switch block (prevents fall-through)
- **One optional `default`** - Executes if no case matches

{% hint style="info" %}
**Switch vs If/Else**: `switch` evaluates a **single expression** against multiple values. `if / else if / else` can evaluate **different conditions** with different variables and comparisons in each branch.
{% endhint %}

### Basic Example

```js
day = "Monday";

switch ( day ) {
    case "Monday": {
        println( "Start of the work week" );
        break;
    }
    case "Friday": {
        println( "TGIF!" );
        break;
    }
    case "Saturday":
    case "Sunday": {
        println( "Weekend!" );
        break;
    }
    default: {
        println( "Midweek day" );
    }
}
```

### Multiple Cases (Fall-Through)

```js
// Group multiple values that execute the same code
city = "Cleveland";

switch ( city ) {
    case "New York":
    case "Boston":
    case "Philadelphia": {
        region = "East Coast";
        break;
    }
    case "Los Angeles":
    case "San Francisco":
    case "Seattle": {
        region = "West Coast";
        break;
    }
    case "Chicago":
    case "Cleveland":
    case "Cincinnati": {
        region = "Midwest";
        break;
    }
    default: {
        region = "Unknown";
    }
}

println( "Region: #region#" ); // "Region: Midwest"
```

### Break Statement

```js
// With break - stops after first match
value = 2;
result = "";

switch ( value ) {
    case 1: {
        result = "one";
        break;
    }
    case 2: {
        result = "two";
        break; // Stops here, doesn't continue to case 3
    }
    case 3: {
        result = "three";
        break;
    }
}
println( result ); // "two"

// Without break - falls through to next case (rare, usually unintended)
value = 2;
result = "";

switch ( value ) {
    case 1: {
        result &= "one ";
    }
    case 2: {
        result &= "two ";  // Matches here
        // No break! Falls through to case 3
    }
    case 3: {
        result &= "three "; // Also executes!
    }
}
println( result ); // "two three "
```

{% hint style="warning" %}
**Best Practice**: Always include curly braces `{}` for case blocks and use `break` statements unless you specifically want fall-through behavior. Forgetting `break` is a common bug!
{% endhint %}

### Practical Examples

```js
// HTTP status code handling
statusCode = 404;

switch ( statusCode ) {
    case 200:
    case 201:
    case 204: {
        message = "Success";
        break;
    }
    case 400:
    case 404: {
        message = "Client Error";
        break;
    }
    case 500:
    case 502:
    case 503: {
        message = "Server Error";
        break;
    }
    default: {
        message = "Unknown Status";
    }
}

// File extension handling
fileExt = "pdf";

switch ( fileExt ) {
    case "jpg":
    case "jpeg":
    case "png":
    case "gif": {
        contentType = "image";
        break;
    }
    case "pdf": {
        contentType = "document";
        break;
    }
    case "mp4":
    case "avi":
    case "mov": {
        contentType = "video";
        break;
    }
    default: {
        contentType = "unknown";
    }
}

// User role permissions
role = "editor";

switch ( role ) {
    case "admin": {
        permissions = ["read", "write", "delete", "manage"];
        break;
    }
    case "editor": {
        permissions = ["read", "write"];
        break;
    }
    case "viewer": {
        permissions = ["read"];
        break;
    }
    default: {
        permissions = [];
    }
}
```

### When to Use Switch vs If/Else

```js
// Use SWITCH when checking a single variable against multiple discrete values
switch ( dayOfWeek ) {
    case "Monday": { /* ... */ break; }
    case "Tuesday": { /* ... */ break; }
    // ...
}

// Use IF/ELSE when evaluating different conditions or ranges
if ( score >= 90 ) {
    grade = "A";
} else if ( score >= 80 ) {
    grade = "B";
} else if ( score >= 70 ) {
    grade = "C";
}

// Use IF/ELSE when conditions involve different variables
if ( isLoggedIn && hasPermission ) {
    // ...
} else if ( isGuest ) {
    // ...
}
```

## 🔁 While Loops

The `while` loop executes a code block repeatedly as long as the conditional expression evaluates to **true**. It's useful for processing queues, polling, and iterating when the number of iterations isn't known in advance.

### Syntax

```js
while ( condition ) {
    // Execute while condition is true
}
```

### Basic Example

```js
count = 0;

while ( count < 5 ) {
    println( "Count: #count#" );
    count++;
}

/* Output:
Count: 0
Count: 1
Count: 2
Count: 3
Count: 4
*/
```

### Practical Examples

```js
// Processing a queue
queue = ["task1", "task2", "task3"];

while ( queue.len() > 0 ) {
    task = queue.shift(); // Remove first item
    println( "Processing: #task#" );
}

// Reading until a condition is met
userInput = "";

while ( userInput != "quit" ) {
    userInput = getInput( "Enter command (or 'quit' to exit): " );
    if ( userInput != "quit" ) {
        processCommand( userInput );
    }
}

// Polling with timeout
timeout = 30;
elapsed = 0;
ready = false;

while ( !ready && elapsed < timeout ) {
    ready = checkIfReady();
    if ( !ready ) {
        sleep( 1000 ); // Wait 1 second
        elapsed++;
    }
}

if ( ready ) {
    println( "System ready!" );
} else {
    println( "Timeout waiting for system" );
}
```

### Do-While Loop

BoxLang also supports `do-while` loops, which execute the block **at least once** before checking the condition:

```js
// do-while: executes at least once
count = 0;

do {
    println( "Count: #count#" );
    count++;
} while ( count < 5 );

// Practical use: input validation
do {
    userAge = getInput( "Enter your age: " );
} while ( !isNumeric( userAge ) || userAge < 0 );

println( "Valid age entered: #userAge#" );
```

### Infinite Loops and Break

```js
// Infinite loop with break condition
while ( true ) {
    data = fetchNextItem();

    if ( !data ) {
        break; // Exit loop
    }

    processItem( data );
}

// Continue to skip iterations
count = 0;

while ( count < 10 ) {
    count++;

    if ( count % 2 == 0 ) {
        continue; // Skip even numbers
    }

    println( "Odd number: #count#" );
}
```

{% hint style="warning" %}
**Caution**: Ensure your while loop condition will eventually become **false**, or use a `break` statement to exit. Infinite loops without an exit condition will hang your application!
{% endhint %}

## ⚠️ Common Mistakes

### The `==` vs `=` Confusion

The #1 mistake in conditional statements is confusing assignment (`=`) with comparison (`==`).

| Operator | Purpose | Example |
|----------|---------|---------|
| `=` | **Assignment** - "Put value on right into variable on left" | `x = 5` |
| `==` | **Comparison** - "Is left equal to right?" | `x == 5` |

```js
// WRONG - Assignment in condition (always true if x is non-zero)
x = 5;
if ( x = 10 ) {  // ❌ This assigns 10 to x, doesn't compare!
    println( "This will execute!" );
}
println( x ); // Outputs: 10 (x was changed!)

// CORRECT - Comparison in condition
x = 5;
if ( x == 10 ) {  // ✅ This compares x to 10
    println( "This will NOT execute" );
}
println( x ); // Outputs: 5 (x unchanged)
```

### Other Common Pitfalls

```js
// 1. Forgetting parentheses in conditions
if score > 90 { // ❌ Missing parentheses
    println( "A" );
}

if ( score > 90 ) { // ✅ Correct
    println( "A" );
}

// 2. Using = instead of == in comparisons
if ( status = "active" ) { // ❌ Assignment, not comparison
    // ...
}

if ( status == "active" ) { // ✅ Comparison
    // ...
}

// 3. Forgetting break in switch statements
switch ( value ) {
    case 1: {
        result = "one";
        // ❌ Missing break! Falls through to case 2
    }
    case 2: {
        result = "two";
        break; // ✅ Proper break
    }
}

// 4. Comparing strings case-sensitively when you don't mean to
name = "Alice";
if ( name == "alice" ) { // ❌ Won't match due to case
    println( "Found!" );
}

if ( name.lcase() == "alice" ) { // ✅ Case-insensitive comparison
    println( "Found!" );
}
```

## 📚 Best Practices Summary

1. ✅ **Use appropriate operators**: `if/else` for complex logic, `switch` for discrete values, ternary/elvis for simple assignments
2. ✅ **Always use `==` for comparisons**, never `=` in conditions
3. ✅ **Use safe navigation (`?.`)** to avoid null pointer errors
4. ✅ **Combine elvis (`?:`) with safe navigation** for elegant default values
5. ✅ **Include `break` in switch cases** unless you specifically want fall-through
6. ✅ **Add curly braces `{}`** around all code blocks for clarity
7. ✅ **Avoid deeply nested ternary operators** - use `if/else` for complex conditions
8. ✅ **Ensure while loops have exit conditions** to prevent infinite loops
9. ✅ **Use meaningful variable names** in conditions for readability
10. ✅ **Format conditions consistently** with spaces: `if ( condition )` not `if(condition)`

## 🔗 Related Documentation

{% content-ref url="operators.md" %}
[operators.md](operators.md)
{% endcontent-ref %}

{% content-ref url="ranges.md" %}
[ranges.md](ranges.md)
{% endcontent-ref %}

{% content-ref url="program-structure.md" %}
[program-structure.md](program-structure.md)
{% endcontent-ref %}

{% content-ref url="exception-management.md" %}
[exception-management.md](exception-management.md)
{% endcontent-ref %}
