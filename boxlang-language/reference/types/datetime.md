# datetime

The primary DateTime class that represents a date and time object in BoxLang

All temporal methods in BoxLang operate on this class and all castable date/time representations are cast to this class

## Datetime Methods

<details>

<summary><code>add(datepart=[string], number=[long])</code></summary>

Modifies a date object by date part and integer time unit

Arguments:

</details>

<details>

<summary><code>clone()</code></summary>



</details>

<details>

<summary><code>compare(date2=[any], datepart=[string])</code></summary>

Compares the difference between two dates - returning 0 if equal, -1 if date2 is less than date1 and 1 if the inverse

Arguments:

</details>

<details>

<summary><code>compareTo(date2=[any], datepart=[string])</code></summary>

Compares the difference between two dates - returning 0 if equal, -1 if date2 is less than date1 and 1 if the inverse

Arguments:

</details>

<details>

<summary><code>dateFormat(mask=[string], timezone=[string], locale=[string])</code></summary>

Formats a datetime, date or time

Arguments:

</details>

<details>

<summary><code>dateTimeFormat(mask=[string], timezone=[string], locale=[string])</code></summary>

Formats a datetime, date or time

Arguments:

</details>

<details>

<summary><code>day(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>dayOfWeek(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>dayOfWeekAsString(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>dayOfWeekShortAsString(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>dayOfYear(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>daysInMonth(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>daysInYear(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>diff(datepart=[string], date2=[any])</code></summary>

Returns the numeric difference in the requested date part between two dates

Arguments:

</details>

<details>

<summary><code>equals(obj=[any])</code></summary>

Indicates whether some other object is "equal to" this one.

Arguments:

</details>

<details>

<summary><code>firstDayOfMonth(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>format(mask=[string], timezone=[string], locale=[string])</code></summary>

Formats a datetime, date or time

Arguments:

</details>

<details>

<summary><code>getnumericdate(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>getTime(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>hash(algorithm=[string], encoding=[string], numIterations=[integer])</code></summary>

Creates an algorithmic hash of an object

Arguments:

</details>

<details>

<summary><code>hour(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>len()</code></summary>

Returns the absolute value of a number

</details>

<details>

<summary><code>millisecond(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>minute(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>month(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>monthAsString(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>monthShortAsString(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>nanosecond(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>offset(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>quarter(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>second(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>timeFormat(mask=[string], timezone=[string], locale=[string])</code></summary>

Formats a datetime, date or time

Arguments:

</details>

<details>

<summary><code>timezone(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>toEpoch()</code></summary>

Returns this date time in epoch time ( seconds )

</details>

<details>

<summary><code>toEpochMillis()</code></summary>

Returns this date time in epoch milliseconds

</details>

<details>

<summary><code>toEpochSecond()</code></summary>



</details>

<details>

<summary><code>toISOString()</code></summary>

Returns the date time representation as a string in the specified format mask

</details>

<details>

<summary><code>toODBCDate(timezone=[string])</code></summary>

Creates a DateTime object with the format set to ODBC Implicit format

Arguments:

</details>

<details>

<summary><code>toODBCDateTime(timezone=[string])</code></summary>

Creates a DateTime object with the format set to ODBC Implicit format

Arguments:

</details>

<details>

<summary><code>toODBCTime(timezone=[string])</code></summary>

Creates a DateTime object with the format set to ODBC Implicit format

Arguments:

</details>

<details>

<summary><code>week(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

<details>

<summary><code>year(timezone=[string], locale=[string])</code></summary>

Provides the BIF and member functions for all time unit request with no arguments

Arguments:

</details>

## Examples
