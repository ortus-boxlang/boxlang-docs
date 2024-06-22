[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Datetime`

The primary DateTime class that represents a date and time object in BoxLang

 All temporal methods in BoxLang operate on this class and all castable date/time representations are cast to this class

## Datetime Methods

<details>
<summary><code>add(datepart=[string], number=[long])</code></summary>
<p>Modifies a date object by date part and integer time unit
</p></details>
<details>
<summary><code>clone()</code></summary>
<p>
</p></details>
<details>
<summary><code>compare(date2=[any], datepart=[string])</code></summary>
<p>Compares the difference between two dates - returning 0 if equal, -1 if date2 is less than date1 and 1 if the inverse
</p></details>
<details>
<summary><code>compareTo(date2=[any], datepart=[string])</code></summary>
<p>Compares the difference between two dates - returning 0 if equal, -1 if date2 is less than date1 and 1 if the inverse
</p></details>
<details>
<summary><code>dateFormat(mask=[string], timezone=[string])</code></summary>
<p>Formats a datetime, date or time
</p></details>
<details>
<summary><code>dateTimeFormat(mask=[string], timezone=[string])</code></summary>
<p>Formats a datetime, date or time
</p></details>
<details>
<summary><code>day(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>dayOfWeek(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>dayOfWeekAsString(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>dayOfWeekShortAsString(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>dayOfYear(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>daysInMonth(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>daysInYear(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>diff(datepart=[string], date2=[any])</code></summary>
<p>Returns the numeric difference in the requested date part between two dates
</p></details>
<details>
<summary><code>equals(obj=[any])</code></summary>
<p>Indicates whether some other object is "equal to" this one.
</p></details>
<details>
<summary><code>firstDayOfMonth(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>format(mask=[string], timezone=[string])</code></summary>
<p>Formats a datetime, date or time
</p></details>
<details>
<summary><code>getTime(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>hash(algorithm=[string], encoding=[string], numIterations=[integer])</code></summary>
<p>Creates an algorithmic hash of an object
</p></details>
<details>
<summary><code>hour(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>lSDateFormat(mask=[string], locale=[string], timezone=[string])</code></summary>
<p>Formats a date in a locale-specific format
</p></details>
<details>
<summary><code>lSDateTimeFormat(mask=[string], locale=[string], timezone=[string])</code></summary>
<p>Formats a date in a locale-specific format
</p></details>
<details>
<summary><code>lsDayOfWeek(locale=[string], timezone=[string])</code></summary>
<p>Provides the Localized BIF and member functions for time units ( e.g.

different locales have different start days to the week )
</p></details>
<details>
<summary><code>lSTimeFormat(mask=[string], locale=[string], timezone=[string])</code></summary>
<p>Formats a date in a locale-specific format
</p></details>
<details>
<summary><code>lsWeek(locale=[string], timezone=[string])</code></summary>
<p>Provides the Localized BIF and member functions for time units ( e.g.

different locales have different start days to the week )
</p></details>
<details>
<summary><code>millisecond(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>minute(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>month(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>monthAsString(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>monthShortAsString(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>nanosecond(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>offset(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>quarter(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>second(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>timeFormat(mask=[string], timezone=[string])</code></summary>
<p>Formats a datetime, date or time
</p></details>
<details>
<summary><code>timezone(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>toEpoch()</code></summary>
<p>Returns this date time in epoch time ( seconds )
</p></details>
<details>
<summary><code>toEpochMillis()</code></summary>
<p>Returns this date time in epoch milliseconds
</p></details>
<details>
<summary><code>toEpochSecond()</code></summary>
<p>
</p></details>
<details>
<summary><code>toISOString()</code></summary>
<p>Returns the date time representation as a string in the specified format mask
</p></details>
<details>
<summary><code>toODBCDate(timezone=[string])</code></summary>
<p>Creates a DateTime object with the format set to ODBC Implicit format
</p></details>
<details>
<summary><code>toODBCDateTime(timezone=[string])</code></summary>
<p>Creates a DateTime object with the format set to ODBC Implicit format
</p></details>
<details>
<summary><code>toODBCTime(timezone=[string])</code></summary>
<p>Creates a DateTime object with the format set to ODBC Implicit format
</p></details>
<details>
<summary><code>weekOfYear(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>
<details>
<summary><code>year(timezone=[string])</code></summary>
<p>Provides the BIF and member functions for all time unit request with no arguments
</p></details>


## Examples
