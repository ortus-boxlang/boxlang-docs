# bx:chartseries

## Summary

Defines a data series within a chart component. This component specifies the chart type, styling options, and data source for one series of data. It must be nested within a `bx:chart` component and can contain `bx:chartdata` components or use query/array data sources.

## Syntax

```xml
<!-- Using chartdata components -->
<bx:chartseries type="pie|bar|line|..." colorlist="red,blue,green" serieslabel="Series Name">
    <bx:chartdata item="Label 1" value="100">
    <bx:chartdata item="Label 2" value="200">
</bx:chartseries>

<!-- Using query data source -->
<bx:chartseries type="bar" query="#myQuery#" itemColumn="category" valueColumn="amount">
</bx:chartseries>

<!-- Using array data source -->
<bx:chartseries type="pie" data="#arrayData#" serieslabel="Sales Data">
</bx:chartseries>
```

## Attributes

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `type` | string | Yes | - | Chart type: `pie`, `bar`, `line`, `doughnut`, `radar`, `polarArea`, `area`, `horizontalbar`, `scatter`, `bubble` |
| `colorlist` | string | No | - | Comma-separated list of colors (hex or named colors) for chart data points. Example: "red,##FF6384,blue" |
| `serieslabel` | string | No | chart type | Label for this data series, used in legends |
| `borderColor` | string | No | - | Border color for this series (hex or named color). Overrides chart-level `borderColor`. Not applicable for scatter charts |
| `borderWidth` | number | No | - | Border width in pixels for this series. Not applicable for scatter charts. Overrides chart-level `borderWidth` |
| `borderRadius` | number | No | - | Border radius in pixels for this series. Only applicable for bar and horizontalbar charts. Overrides chart-level `borderRadius` |
| `query` | query | No | - | Query object to use as data source. When provided, no child `chartdata` components are required |
| `itemColumn` | string | No | "item" | Name of the query column containing labels. Used with `query` attribute |
| `valueColumn` | string | No | "value" | Name of the query column containing values. Used with `query` attribute |
| `data` | array | No | - | Array data source. Can be array of structs `[{item:"x",value:123}]` or array of arrays `[["x",123]]`. For bubble charts use `x`, `y`, `r` instead of `value` |

## Chart Types

### Supported Chart Types

| Type | Description | Best For |
|------|-------------|----------|
| `pie` | Circular chart showing proportions | Market share, budget allocation, survey results |
| `bar` | Vertical bar chart | Comparing quantities, showing rankings, temporal data |
| `line` | Connected data points | Time series, trend analysis, continuous data |
| `doughnut` | Pie chart with hole in center | Proportions with emphasis on total value |
| `radar` | Multivariate data on circular grid | Comparing multiple variables, skill assessments |
| `polarArea` | Pie chart with varying radius | Proportions where magnitude matters |
| `area` | Line chart with filled area | Showing volume over time, cumulative data |
| `horizontalbar` | Horizontal bar chart | Long category names, rankings |
| `scatter` | X-Y coordinate plot | Correlation analysis, distribution patterns |
| `bubble` | Three-dimensional data (x, y, size) | Multi-dimensional data analysis, portfolio analysis |

## Data Sources

### Using ChartData Components

```xml
<bx:chartseries type="pie" colorlist="FF6384,36A2EB,FFCE56">
    <bx:chartdata item="Product A" value="150">
    <bx:chartdata item="Product B" value="200">
    <bx:chartdata item="Product C" value="100">
</bx:chartseries>
```

### Using Query Object

```xml
<bx:chartseries type="bar" 
                query="#getSalesData()#" 
                itemColumn="product_name" 
                valueColumn="total_sales"
                serieslabel="Q4 Sales">
</bx:chartseries>
```

### Using Array of Structs

```xml
<bx:chartseries type="pie"
    data="#[
        {item:'Product A', value:100},
        {item:'Product B', value:200},
        {item:'Product C', value:150}
    ]#"
    serieslabel="Sales Data">
</bx:chartseries>
```

### Using Array of Arrays (Positional)

```xml
<bx:chartseries type="bar"
    data="#[
        ['Product A', 100],
        ['Product B', 200],
        ['Product C', 150]
    ]#"
    serieslabel="Sales Data">
</bx:chartseries>
```

### Bubble Chart Data

For bubble charts, use `x`, `y`, and `r` coordinates:

```xml
<!-- With chartdata components -->
<bx:chartseries type="bubble" serieslabel="Portfolio Analysis">
    <bx:chartdata item="Stock A" x="20" y="15" r="10">
    <bx:chartdata item="Stock B" x="40" y="25" r="15">
</bx:chartseries>

<!-- With array data -->
<bx:chartseries type="bubble"
    data="#[
        {item:'Stock A', x:20, y:15, r:10},
        {item:'Stock B', x:40, y:25, r:15}
    ]#"
    serieslabel="Portfolio Analysis">
</bx:chartseries>
```

## Examples

### Multi-Series Bar Chart

```xml
<bx:chart title="Server Performance" seriesPlacement="cluster">
    <bx:chartseries type="bar" colorlist="##FF6384" serieslabel="CPU Usage">
        <bx:chartdata item="Server 1" value="65">
        <bx:chartdata item="Server 2" value="78">
        <bx:chartdata item="Server 3" value="45">
    </bx:chartseries>
    <bx:chartseries type="bar" colorlist="##36A2EB" serieslabel="Memory Usage">
        <bx:chartdata item="Server 1" value="42">
        <bx:chartdata item="Server 2" value="56">
        <bx:chartdata item="Server 3" value="33">
    </bx:chartseries>
</bx:chart>
```

### Styled Line Chart

```xml
<bx:chartseries type="line" 
                colorlist="##FF6384" 
                serieslabel="Response Time"
                borderColor="##FF6384"
                borderWidth="3">
    <bx:chartdata item="Jan" value="200">
    <bx:chartdata item="Feb" value="180">
    <bx:chartdata item="Mar" value="165">
    <bx:chartdata item="Apr" value="170">
</bx:chartseries>
```

### Query-Based Chart

```xml
<cfquery name="salesQuery" datasource="myDB">
    SELECT product_name as item, SUM(sales_amount) as value
    FROM sales 
    WHERE sale_date >= #CreateDate(2024,1,1)#
    GROUP BY product_name
    ORDER BY value DESC
</cfquery>

<bx:chart title="Product Sales">
    <bx:chartseries type="bar" 
                    query="#salesQuery#" 
                    serieslabel="2024 Sales"
                    colorlist="##36A2EB">
    </bx:chartseries>
</bx:chart>
```

## Notes

- The `type` attribute is required and determines how the data will be visualized
- Color values can be specified as hex codes (with ## prefix) or named colors (red, blue, etc.)
- When using `query` data source, the query must have columns that match `itemColumn` and `valueColumn` values
- For array data sources, use structs for named properties or arrays for positional data
- Border styling attributes at series level override chart-level settings
- Bubble charts require three-dimensional data: x, y coordinates and radius (r)

## Related Components

- [bx:chart](bx-chart.md) - Main chart container component  
- [bx:chartdata](bx-chartdata.md) - Individual data point component
