[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Datetime`

The primary DateTime class that represents a date and time object in BoxLang

 All temporal methods in BoxLang operate on this class and all castable date/time representations are cast to this class

## Datetime Methods

<details>
<summary><code>add(datepart=[string], number=[long])</code></summary>
Modifies a date object by date part and integer time unit

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `datepart` | `string` | `true` | `` |
| `number` | `long` | `true` | `` |


</details>
<details>
<summary><code>clone()</code></summary>

</details>
<details>
<summary><code>compare(date2=[any], datepart=[string])</code></summary>
Compares the difference between two dates - returning 0 if equal, -1 if date2 is less than date1 and 1 if the inverse

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `date2` | `any` | `true` | `` |
| `datepart` | `string` | `false` | `` |


</details>
<details>
<summary><code>compareTo(date2=[any], datepart=[string])</code></summary>
Compares the difference between two dates - returning 0 if equal, -1 if date2 is less than date1 and 1 if the inverse

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `date2` | `any` | `true` | `` |
| `datepart` | `string` | `false` | `` |


</details>
<details>
<summary><code>dateFormat(mask=[string], timezone=[string])</code></summary>
Formats a datetime, date or time

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>dateTimeFormat(mask=[string], timezone=[string])</code></summary>
Formats a datetime, date or time

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>day(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>dayOfWeek(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>dayOfWeekAsString(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>dayOfWeekShortAsString(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>dayOfYear(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>daysInMonth(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>daysInYear(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>diff(datepart=[string], date2=[any])</code></summary>
Returns the numeric difference in the requested date part between two dates

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `datepart` | `string` | `true` | `` |
| `date2` | `any` | `true` | `` |


</details>
<details>
<summary><code>equals(obj=[any])</code></summary>
Indicates whether some other object is "equal to" this one.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `obj` | `any` | `true` | null |


</details>
<details>
<summary><code>firstDayOfMonth(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>format(mask=[string], timezone=[string])</code></summary>
Formats a datetime, date or time

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>getTime(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>hash(algorithm=[string], encoding=[string], numIterations=[integer])</code></summary>
Creates an algorithmic hash of an object

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `algorithm` | `string` | `false` | `MD5` |
| `encoding` | `string` | `false` | `utf-8` |
| `numIterations` | `integer` | `false` | `1` |


</details>
<details>
<summary><code>hour(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>lSDateFormat(mask=[string], locale=[string], timezone=[string])</code></summary>
Formats a date in a locale-specific format

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `` |
| `locale` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>lSDateTimeFormat(mask=[string], locale=[string], timezone=[string])</code></summary>
Formats a date in a locale-specific format

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `` |
| `locale` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>lsDayOfWeek(locale=[string], timezone=[string])</code></summary>
Provides the Localized BIF and member functions for time units ( e.g.

different locales have different start days to the week )

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `locale` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>lSTimeFormat(mask=[string], locale=[string], timezone=[string])</code></summary>
Formats a date in a locale-specific format

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `` |
| `locale` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>lsWeek(locale=[string], timezone=[string])</code></summary>
Provides the Localized BIF and member functions for time units ( e.g.

different locales have different start days to the week )

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `locale` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>millisecond(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>minute(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>month(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>monthAsString(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>monthShortAsString(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>nanosecond(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>offset(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>quarter(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>second(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>timeFormat(mask=[string], timezone=[string])</code></summary>
Formats a datetime, date or time

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `` |
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>timezone(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


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

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>toODBCDateTime(timezone=[string])</code></summary>
Creates a DateTime object with the format set to ODBC Implicit format

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>toODBCTime(timezone=[string])</code></summary>
Creates a DateTime object with the format set to ODBC Implicit format

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>weekOfYear(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>
<details>
<summary><code>year(timezone=[string])</code></summary>
Provides the BIF and member functions for all time unit request with no arguments

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `timezone` | `string` | `false` | `` |


</details>


## Examples
