---
description: The power of now!
---

# Dates & Times

## Working with Dates in BoxLang

BoxLang provides comprehensive date and time functionality through its `DateTime` object and extensive collection of temporal Built-in Functions (BIFs). All date and time operations in BoxLang work with the unified `DateTime` type, which internally wraps Java's `ZonedDateTime` to provide robust timezone and formatting support.

### The DateTime Object

The `DateTime` object is the cornerstone of all temporal operations in BoxLang. It represents a specific moment in time with timezone information and provides methods for formatting, manipulation, and comparison. DateTime objects are created using BoxLang's temporal BIFs and provide member methods for advanced operations.

## Creating DateTime Objects

BoxLang provides several Built-in Functions (BIFs) for creating `DateTime` objects:

**Current Date and Time**

```javascript
// Get current date and time in system timezone
now = now()
```

**From String Representations**

```javascript
// Parse from various string formats
dt = parseDateTime("December 25, 2023")
dt = parseDateTime("2023-12-25T15:30:00Z")
dt = parseDateTime("25-Dec-2023 3:30 PM")

// Parse with specific locale and timezone
dt = parseDateTime("25/12/2023", "en_US", "America/New_York")
```

**From Numeric Components**

```javascript
// Create specific date (year, month, day)
dt = createDate(2023, 12, 25)

// Create date with time (year, month, day, hour, minute, second)
dt = createDateTime(2023, 12, 25, 15, 30, 45)

// Create time only (hour, minute, second)
timeObj = createTime(15, 30, 45)
```

**Creating Time Spans**

```javascript
// Create timespan for durations (days, hours, minutes, seconds)
span = createTimeSpan(1, 2, 30, 45)  // 1 day, 2 hours, 30 min, 45 sec
```

## Date Time Format Masks

BoxLang supports extensive formatting options through format masks:

### Basic Date and Time Components

| Mask   | Description                            | Example           |
| ------ | -------------------------------------- | ----------------- |
| `d`    | Day of month, no leading zero          | 5, 25             |
| `dd`   | Day of month, leading zero             | 05, 25            |
| `EEE`  | Day of week, three-letter abbreviation | Mon, Tue          |
| `EEEE` | Day of week, full name                 | Monday, Tuesday   |
| `m`    | Month, no leading zero                 | 1, 12             |
| `mm`   | Month, leading zero                    | 01, 12            |
| `mmm`  | Month, three-letter abbreviation       | Jan, Dec          |
| `mmmm` | Month, full name                       | January, December |
| `M`    | Month in year                          | 1, 12             |
| `D`    | Day in year                            | 1, 365            |
| `yy`   | Year, last two digits                  | 23                |
| `yyyy` | Year, four digits                      | 2023              |
| `YYYY` | Week year, four digits                 | 2023              |
| `Y`    | Week year                              | 2023              |
| `YY`   | Week year, last two digits             | 23                |
| `G`    | Period/era string                      | BC, AD            |

### Time Components

| Mask       | Description                      | Example |
| ---------- | -------------------------------- | ------- |
| `h`        | Hours (12-hour), no leading zero | 3, 11   |
| `hh`       | Hours (12-hour), leading zero    | 03, 11  |
| `H`        | Hours (24-hour), no leading zero | 15, 23  |
| `HH`       | Hours (24-hour), leading zero    | 15, 23  |
| `n`        | Minutes, no leading zero         | 5, 30   |
| `nn`       | Minutes, leading zero            | 05, 30  |
| `s`        | Seconds, no leading zero         | 5, 45   |
| `ss`       | Seconds, leading zero            | 05, 45  |
| `l` or `L` | Milliseconds, no leading zeros   | 123     |
| `t`        | One-character time marker        | A, P    |
| `tt`       | Time marker string               | AM, PM  |

### Week Components

| Mask | Description                 | Example |
| ---- | --------------------------- | ------- |
| `w`  | Week of year, single digit  | 1, 52   |
| `ww` | Week of year, leading zero  | 01, 52  |
| `W`  | Week of month, single digit | 1, 5    |
| `WW` | Week of month, leading zero | 01, 05  |

### Predefined Full Date/Time Formats

These masks format the complete date and time and cannot be combined with other masks:

| Mask     | Equivalent Format                     | Example                                  |
| -------- | ------------------------------------- | ---------------------------------------- |
| `short`  | `"m/d/y h:nn tt"`                     | 12/25/23 3:30 PM                         |
| `medium` | `"mmm d, yyyy h:nn:ss tt"`            | Dec 25, 2023 3:30:45 PM                  |
| `long`   | Medium with full month and timezone   | December 25, 2023 3:30:45 PM EST         |
| `full`   | `"EEEE, mmmm d, yyyy h:mm:ss tt EST"` | Monday, December 25, 2023 3:30:45 PM EST |
| `iso`    | ISO8601 format                        | 2023-12-25T15:30:45-05:00                |

## Formatting Dates

### Using Built-in Functions

```javascript
dt = now()

// Combined date and time formatting
formatted = dateTimeFormat(dt, "yyyy-mm-dd HH:nn:ss")
formatted = dateTimeFormat(dt, "medium")  // Dec 25, 2023 3:30:45 PM
formatted = dateTimeFormat(dt, "iso")     // 2023-12-25T15:30:45-05:00

// Date only formatting
dateString = dateFormat(dt, "mm/dd/yyyy")
dateString = dateFormat(dt, "mmmm d, yyyy")  // December 25, 2023

// Time only formatting  
timeString = timeFormat(dt, "HH:nn:ss")
timeString = timeFormat(dt, "h:nn tt")       // 3:30 PM

// With timezone specification
formatted = dateTimeFormat(dt, "yyyy-mm-dd HH:nn:ss", "UTC")
formatted = dateTimeFormat(dt, "medium", "America/New_York")
```

## Timezone Support

BoxLang supports timezone specification using:

* **3-letter codes**: `"EST"`, `"UTC"`, `"PST"`
* **Full timezone names**: `"America/New_York"`, `"Europe/London"`, `"Asia/Tokyo"`

```javascript
dt = now()

// Format with specific timezone
utcFormatted = dateTimeFormat(dt, "yyyy-mm-dd HH:nn:ss", "UTC")
nyFormatted = dateTimeFormat(dt, "full", "America/New_York")
```

### Working with Timezones

BoxLang provides timezone support at two levels: request-level and formatting-level.

### Request-Level Timezone Management

These BIFs set the timezone for the **current request only**. If not set, BoxLang uses the runtime configuration timezone.

```javascript
// Set timezone for current request
setTimezone("America/New_York")
setTimezone("EST")

// Get current request timezone
currentTZ = getTimezone()

// Clear request timezone (reverts to runtime default)
clearTimezone()

// Get timezone information
info = getTimezoneInfo()
```

### Formatting with Timezones

When formatting dates, you can specify a timezone without affecting the request timezone:

```javascript
dt = now()

// Format with specific timezone (doesn't change request timezone)
utcFormatted = dateTimeFormat(dt, "yyyy-mm-dd HH:nn:ss", "UTC")
nyFormatted = dateTimeFormat(dt, "full", "America/New_York")

// Convert between timezones for calculations
utcTime = dateConvert("local2utc", dt)
localTime = dateConvert("utc2local", utcTime)

// Get timezone offset using member methods
offsetObj = dt.getOffset()           // ZoneOffset object
offsetHours = offset(dt)             // Offset in hours (using BIF)
```

### Supported Timezone Formats

* **3-letter codes**: `"EST"`, `"UTC"`, `"PST"`, `"CST"`
* **Full timezone names**: `"America/New_York"`, `"Europe/London"`, `"Asia/Tokyo"`

## DateTime Member Methods

DateTime objects provide numerous member methods for manipulation, formatting, and information retrieval. These methods can be called directly on DateTime instances using dot notation.

### Comparison and Equality Methods

```javascript
dt1 = createDate(2023, 12, 25)
dt2 = createDate(2023, 12, 30)

// Equality comparison
isEqual = dt1.equals(dt2)          // false

// Temporal comparisons  
isAfter = dt2.isAfter(dt1)         // true
isBefore = dt1.isBefore(dt2)       // true
isEqualTime = dt1.isEqual(dt2)     // false
```

### Cloning and Copying

```javascript
dt = now()

// Clone with same timezone
dtCopy = dt.clone()

// Clone with different timezone
dtUTC = dt.clone("UTC")
dtNY = dt.clone("America/New_York")
```

### Conversion and Output Methods

```javascript
dt = now()

// Convert to various formats
isoString = dt.toISOString()         // "2023-12-25T15:30:45-05:00"
epochSeconds = dt.toEpoch()          // 1703534245
epochMillis = dt.toEpochMillis()     // 1703534245123
timeMillis = dt.getTime()            // 1703534245123 (same as toEpochMillis)
epochSecs = dt.toEpochSecond()       // 1703534245 (same as toEpoch)

// Convert to Java types
javaInstant = dt.toInstant()
javaLocalDate = dt.toLocalDate()
javaLocalTime = dt.toLocalTime()
javaDate = dt.toDate()               // java.util.Date
javaZonedDateTime = dt.getWrapped()  // Access underlying ZonedDateTime
```

### Date/Time Component Access

```javascript
dt = now()

// Date components
year = dt.getYear()                  // 2023
month = dt.getMonthValue()           // 12 (1-12)
day = dt.getDayOfMonth()             // 25
dayOfWeek = dt.getDayOfWeek()        // MONDAY (enum)
dayOfYear = dt.getDayOfYear()        // 359

// Time components  
hour = dt.getHour()                  // 15 (24-hour format)
minute = dt.getMinute()              // 30
second = dt.getSecond()              // 45
nano = dt.getNano()                  // 123000000 (nanoseconds)

// Timezone information
zone = dt.getZone()                  // ZoneId object
offset = dt.getOffset()              // ZoneOffset object
```

### Date Manipulation Methods

```javascript
dt = createDate(2023, 12, 25)

// Add/subtract time units
futureDate = dt.plusDays(5)          // Add 5 days
pastDate = dt.minusDays(10)          // Subtract 10 days
nextMonth = dt.plusMonths(1)         // Add 1 month
nextYear = dt.plusYears(1)           // Add 1 year

// Time additions
laterTime = dt.plusHours(3)          // Add 3 hours
earlierTime = dt.minusMinutes(30)    // Subtract 30 minutes
futureTime = dt.plusSeconds(45)      // Add 45 seconds

// Set specific components
newYear = dt.withYear(2024)          // Change year to 2024
newMonth = dt.withMonth(6)           // Change month to June
newDay = dt.withDayOfMonth(15)       // Change day to 15th
newHour = dt.withHour(9)             // Change hour to 9 AM

// Using modify method (similar to dateAdd BIF)
modified = dt.modify("d", 5)         // Add 5 days
modified = dt.modify("h", -3)        // Subtract 3 hours
modified = dt.modify("m", 2)         // Add 2 months
modified = dt.modify("yyyy", 1)      // Add 1 year
```

### Timezone Operations

```javascript
dt = now()

// Convert to different timezone
utcTime = dt.convertToZone("UTC")
nyTime = dt.convertToZone("America/New_York")

// Set timezone (changes zone, keeps local time)
withTZ = dt.setTimezone("Europe/London")

// Check if leap year
isLeap = dt.isLeapYear()             // true/false
```

### Formatting Methods

```javascript
dt = now()

// Custom formatting
formatted = dt.format("yyyy-mm-dd HH:nn:ss")
localized = dt.format("medium")

// Set default format for the DateTime object
dt.setFormat("yyyy-mm-dd HH:nn:ss")
defaultFormatted = dt.toString()     // Uses the set format

// With specific locale
import java.util.Locale
spanishFormat = dt.format(Locale.of("es", "ES"), "EEEE, mmmm d, yyyy")
```

### Advanced Member Method Usage

```javascript
dt = createDateTime(2023, 12, 25, 15, 30, 45)

// Chain operations
result = dt.plusDays(5)
           .withHour(9)
           .withMinute(0)
           .withSecond(0)

// Get first day of month
firstDay = dt.withDayOfMonth(1)

// Get last day of month  
lastDay = dt.withDayOfMonth(dt.getMonth().length(dt.isLeapYear()))

// Beginning of day
startOfDay = dt.withHour(0).withMinute(0).withSecond(0).withNano(0)

// End of day
endOfDay = dt.withHour(23).withMinute(59).withSecond(59).withNano(999999999)
```

### Working with Temporal Units

```javascript
dt1 = createDate(2023, 1, 1)
dt2 = createDate(2023, 12, 31)

// Calculate differences using member methods
daysBetween = dt1.until(dt2, ChronoUnit.DAYS)      // 364
monthsBetween = dt1.until(dt2, ChronoUnit.MONTHS)  // 11
```

### Range and Validation

```javascript
dt = now()

// Check if date supports certain operations
supportsNanos = dt.isSupported(ChronoField.NANO_OF_SECOND)  // true
supportsDay = dt.isSupported(ChronoUnit.DAYS)               // true

// Get valid range for a field
yearRange = dt.range(ChronoField.YEAR)          // ValueRange object
monthRange = dt.range(ChronoField.MONTH_OF_YEAR) // 1-12
```

These member methods provide direct access to the rich functionality of BoxLang's DateTime objects, allowing for fluent and expressive date manipulation code. Most operations return new DateTime instances, supporting method chaining for complex transformations.

## Date Arithmetic and Mathematical Operations

BoxLang supports mathematical operations on dates, converting them to fractional days for calculations:

### Addition and Subtraction

```javascript
dt1 = createDate(2023, 12, 25)
dt2 = createDate(2023, 12, 30)

// Subtract dates to get difference in days
daysDiff = dt2 - dt1  // Returns 5.0

// Add days to a date
futureDate = dt1 + 10  // Adds 10 days

// Add fractional days (hours, minutes)
halfDay = dt1 + 0.5    // Adds 12 hours
quarterDay = dt1 + 0.25 // Adds 6 hours
```

### Multiplication and Division

```javascript
dt = createDate(2023, 1, 1)
timespan = createTimeSpan(5, 12, 30, 0) // 5 days, 12 hours, 30 minutes

// Multiply timespan
doubleSpan = timespan * 2

// Divide timespan
halfSpan = timespan / 2

// Add calculated timespan to date
newDate = dt + (timespan * 1.5)
```

### Using DateAdd for Precision

```javascript
dt = now()

// Add specific units
futureDate = dateAdd("d", 5, dt)     // Add 5 days
futureDate = dateAdd("h", 3, dt)     // Add 3 hours
futureDate = dateAdd("n", 30, dt)    // Add 30 minutes
futureDate = dateAdd("s", 45, dt)    // Add 45 seconds

// Date part units:
// "yyyy" - years
// "q" - quarters  
// "m" - months
// "d" - days
// "w" - weekdays
// "ww" - weeks
// "h" - hours
// "n" - minutes
// "s" - seconds
// "l" - milliseconds
```

## Date Comparison and Differences

```javascript
dt1 = createDate(2023, 12, 25)
dt2 = createDate(2023, 12, 30)

// Compare dates
result = dateCompare(dt1, dt2)  // Returns -1 (dt1 is earlier)

// Get specific differences
daysDiff = dateDiff("d", dt1, dt2)     // 5 days
hoursDiff = dateDiff("h", dt1, dt2)    // 120 hours
minutesDiff = dateDiff("n", dt1, dt2)  // 7200 minutes

// Boolean comparisons
isAfter = dt2.isAfter(dt1)    // true
isBefore = dt1.isBefore(dt2)  // true
isEqual = dt1.isEqual(dt2)    // false
```

## Extracting Date Parts

BoxLang provides numerous BIFs to extract specific parts of dates:

```javascript
dt = now()

// Basic parts
currentYear = year(dt)
currentMonth = month(dt)
currentDay = day(dt)
currentHour = hour(dt)
currentMinute = minute(dt)
currentSecond = second(dt)

// Advanced parts
dayOfWeek = dayOfWeek(dt)               // 1-7 (Sunday=1)
dayOfYear = dayOfYear(dt)               // 1-366
quarter = quarter(dt)                   // 1-4
week = week(dt)                         // Week of year

// String representations
monthName = monthAsString(dt)           // "December"
shortMonth = monthShortAsString(dt)     // "Dec"
dayName = dayOfWeekAsString(dt)         // "Tuesday"
shortDay = dayOfWeekShortAsString(dt)   // "Tue"

// Calculated values
daysInMonth = daysInMonth(dt)           // 28-31
daysInYear = daysInYear(dt)             // 365 or 366
firstDay = firstDayOfMonth(dt)          // First day of month
```

## Utility Functions

### Validation and Information

```javascript
// Check if year is leap year
isLeap = dt.isLeapYear()

// Get numeric date (days since epoch)
numericDate = getNumericDate(dt)

// Get time in milliseconds since epoch
timeMillis = getTime(dt)
epochMillis = dt.toEpochMillis()
epochSeconds = dt.toEpoch()
```

### Creating Time Spans

```javascript
// Create timespan (days, hours, minutes, seconds)
span = createTimeSpan(1, 2, 30, 45)  // 1 day, 2 hours, 30 min, 45 sec

// Use timespan in calculations
futureDate = now() + span
```

## Common Patterns and Examples

#### Working with Business Days

```javascript
function addBusinessDays(date, days) {
    result = date
    remaining = days
    
    while (remaining > 0) {
        result = dateAdd("d", 1, result)
        // Skip weekends (Saturday=7, Sunday=1)
        if (dayOfWeek(result) != 1 && dayOfWeek(result) != 7) {
            remaining--
        }
    }
    
    return result
}
```

#### Date Range Generation

```javascript
function getDateRange(startDate, endDate) {
    dates = []
    current = startDate
    
    while (dateCompare(current, endDate) <= 0) {
        arrayAppend(dates, current)
        current = dateAdd("d", 1, current)
    }
    
    return dates
}
```

#### Age Calculation

```javascript
function calculateAge(birthDate) {
    today = now()
    age = dateDiff("yyyy", birthDate, today)
    
    // Adjust if birthday hasn't occurred this year
    birthdayThisYear = createDate(year(today), month(birthDate), day(birthDate))
    if (dateCompare(today, birthdayThisYear) < 0) {
        age--
    }
    
    return age
}
```

#### Timezone Conversion Utility

```javascript
function convertTimezone(dt, fromTZ, toTZ) {
    // Use member methods for timezone conversion
    return dt.convertToZone(toTZ)
}

function formatInTimezone(dt, mask, timezone) {
    // Format date in specific timezone without changing request timezone
    return dateTimeFormat(dt, mask, timezone)
}
```

## Performance Considerations

* DateTime objects are immutable; operations return new instances
* Use BIFs like `dateAdd()`, `dateDiff()`, `dateFormat()` for most operations
* Cache formatted strings if formatting the same date multiple times with `dateTimeFormat()`
* Be mindful of timezone conversions in loops
* Use `createTimeSpan()` for duration calculations rather than manual arithmetic



### Mathematical Representations

For basic arithmetic operations ( addition, subtraction, multiplication and division ) dates and timespans may be cast as numeric values. In BoxLang the numeric value of a [DateTime](https://boxlang.ortusbooks.com/boxlang-framework/modularity/compat-cfml/reference/types/datetime) object is a representation of the decimal days since the Unix epoch time.&#x20;

A [timespan](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/temporal/createtimespan) or Java [Duration](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/time/Duration.html) object is represented as decimal days for the purpose of mathematical operations.

```javascript
timeNow = now();
// Addition casts the date to a numeric day value 
// ( example: 20241.89415408551756893278841047638 )
originalEpochDays = timeNow + 0;
// Add 2.5 days to the decimal days value
updatedEpochDays = timeNow + 2.5;
```
