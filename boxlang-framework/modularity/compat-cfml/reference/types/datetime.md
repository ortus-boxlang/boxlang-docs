[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Datetime`



## Datetime Methods

<details>
<summary><code>lsWeek(locale=[string], timezone=[string])</code></summary>

Provides the Localized BIF and member functions for time units ( e.g.

different locales have different start days to the week )

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `locale` | `string` | `false` | `null` |
| `timezone` | `string` | `false` | `null` |

</details>
<details>
<summary><code>lsDayOfWeek(locale=[string], timezone=[string])</code></summary>

Provides the Localized BIF and member functions for time units ( e.g.

different locales have different start days to the week )

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `locale` | `string` | `false` | `null` |
| `timezone` | `string` | `false` | `null` |

</details>
<details>
<summary><code>compare(date2=[any], datepart=[string])</code></summary>

nullArguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `date2` | `any` | `true` | `null` |
| `datepart` | `string` | `false` | `null` |

</details>
<details>
<summary><code>compareTo(date2=[any], datepart=[string])</code></summary>

nullArguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `date2` | `any` | `true` | `null` |
| `datepart` | `string` | `false` | `null` |

</details>
<details>
<summary><code>lSDateTimeFormat(mask=[string], locale=[string], timezone=[string])</code></summary>

Formats a date in a locale-specific format

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `null` |
| `locale` | `string` | `false` | `null` |
| `timezone` | `string` | `false` | `null` |

</details>
<details>
<summary><code>lSDateFormat(mask=[string], locale=[string], timezone=[string])</code></summary>

Formats a date in a locale-specific format

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `null` |
| `locale` | `string` | `false` | `null` |
| `timezone` | `string` | `false` | `null` |

</details>
<details>
<summary><code>lSTimeFormat(mask=[string], locale=[string], timezone=[string])</code></summary>

Formats a date in a locale-specific format

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mask` | `string` | `false` | `null` |
| `locale` | `string` | `false` | `null` |
| `timezone` | `string` | `false` | `null` |

</details>
<details>
<summary><code>toLegacyDate()</code></summary>

Takes a BoxLang DateTime object and converts it to the legacy java.util.Date object used by ACF and Lucee.
</details>
<details>
<summary><code>equals(date2=[any])</code></summary>

Provides an overload to the native `equals` method for comparing two date/time values

 This method providers a looser comparison than the native `equals` method, which also adds timezone comparison, in addition to the instant

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `date2` | `any` | `true` | `null` |

</details>
<details>
<summary><code>hash(algorithm=[string], encoding=[string], numIterations=[integer])</code></summary>

Creates an algorithmic hash of an object and returns it in the CFML compat upper case format

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `algorithm` | `string` | `false` | `MD5` |
| `encoding` | `string` | `false` | `utf-8` |
| `numIterations` | `integer` | `false` | `1` |

</details>


## Examples
