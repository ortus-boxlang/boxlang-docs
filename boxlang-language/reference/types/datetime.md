[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Datetime`

The primary DateTime class that represents a date and time object in BoxLang

 All temporal methods in BoxLang operate on this class and all castable date/time representations are cast to this class

## Datetime Methods

<dl>
<dt><code>add(datepart=[string], number=[long])</code></dt><dd>Modifies a date object by date part and integer time unit

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `datepart` | `string` | `true` | `` |
| `number` | `long` | `true` | `` |

</dd>
<dt><code>clone()</code></dt><dd></dd>
<dt><code>compare(date2=[any], datepart=[string])</code></dt><dd>Compares the difference between two dates - returning 0 if equal, -1 if date2 is less than date1 and 1 if the inverse

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `date2` | `any` | `true` | `` |
| `datepart` | `string` | `false` | `` |

</dd>
<dt><code>compareTo(date2=[any], datepart=[string])</code></dt><dd>Compares the difference between two dates - returning 0 if equal, -1 if date2 is less than date1 and 1 if the inverse

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `date2` | `any` | `true` | `` |
| `datepart` | `string` | `false` | `` |

</dd>
<dt><code>dateFormat(mask=[string], timezone=[string])</code></dt><dd>Formats a datetime, date or time

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>dateTimeFormat(mask=[string], timezone=[string])</code></dt><dd>Formats a datetime, date or time

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>day(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>dayOfWeek(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>dayOfWeekAsString(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>dayOfWeekShortAsString(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>dayOfYear(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>daysInMonth(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>daysInYear(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>diff(datepart=[string], date2=[any])</code></dt><dd>Returns the numeric difference in the requested date part between two dates

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `datepart` | `string` | `true` | `` |
| `date2` | `any` | `true` | `` |

</dd>
<dt><code>equals(obj=[any])</code></dt><dd>Indicates whether some other object is "equal to" this one.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `obj` | `any` | `true` | null |

</dd>
<dt><code>firstDayOfMonth(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>format(mask=[string], timezone=[string])</code></dt><dd>Formats a datetime, date or time

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>getTime(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>hash(algorithm=[string], encoding=[string], numIterations=[integer])</code></dt><dd>Creates an algorithmic hash of an object

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `algorithm` | `string` | `false` | `MD5` |
| `encoding` | `string` | `false` | `utf-8` |
| `numIterations` | `integer` | `false` | `1` |

</dd>
<dt><code>hour(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>lSDateFormat(mask=[string], locale=[string], timezone=[string])</code></dt><dd>Formats a date in a locale-specific format

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `` |
| `locale` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>lSDateTimeFormat(mask=[string], locale=[string], timezone=[string])</code></dt><dd>Formats a date in a locale-specific format

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `` |
| `locale` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>lsDayOfWeek(locale=[string], timezone=[string])</code></dt><dd>Provides the Localized BIF and member functions for time units ( e.g.

different locales have different start days to the week )

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `locale` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>lSTimeFormat(mask=[string], locale=[string], timezone=[string])</code></dt><dd>Formats a date in a locale-specific format

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `` |
| `locale` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>lsWeek(locale=[string], timezone=[string])</code></dt><dd>Provides the Localized BIF and member functions for time units ( e.g.

different locales have different start days to the week )

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `locale` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>millisecond(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>minute(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>month(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>monthAsString(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>monthShortAsString(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>nanosecond(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>offset(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>quarter(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>second(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>timeFormat(mask=[string], timezone=[string])</code></dt><dd>Formats a datetime, date or time

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>timezone(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>toEpoch()</code></dt><dd>Returns this date time in epoch time ( seconds )</dd>
<dt><code>toEpochMillis()</code></dt><dd>Returns this date time in epoch milliseconds</dd>
<dt><code>toEpochSecond()</code></dt><dd></dd>
<dt><code>toISOString()</code></dt><dd>Returns the date time representation as a string in the specified format mask</dd>
<dt><code>toODBCDate(timezone=[string])</code></dt><dd>Creates a DateTime object with the format set to ODBC Implicit format

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>toODBCDateTime(timezone=[string])</code></dt><dd>Creates a DateTime object with the format set to ODBC Implicit format

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>toODBCTime(timezone=[string])</code></dt><dd>Creates a DateTime object with the format set to ODBC Implicit format

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>weekOfYear(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>
<dt><code>year(timezone=[string])</code></dt><dd>Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |

</dd>

</dl>

## Examples
