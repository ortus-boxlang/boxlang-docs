# bx:chartdata

## Summary

Defines individual data points within a chart series. This component must be nested within a `bx:chartseries` component and represents a single data point with a label and value(s). For most chart types, only `item` and `value` are needed. For bubble charts, use `x`, `y`, and `r` coordinates instead.

## Syntax

```xml
<!-- Standard data point -->
<bx:chartdata item="Label" value="100">

<!-- Bubble chart data point -->
<bx:chartdata item="Label" x="10" y="20" r="5">
```

## Attributes

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `item` | string | Yes | - | Data point label/name displayed in tooltips and legends |
| `value` | number | Conditional | - | Data point value. Required for all chart types except bubble charts |
| `x` | number | Conditional | - | X-coordinate. Required for bubble charts, ignored for other chart types |
| `y` | number | Conditional | - | Y-coordinate. Required for bubble charts, ignored for other chart types |
| `r` | number | Conditional | - | Bubble radius. Required for bubble charts, ignored for other chart types |

## Usage by Chart Type

### Standard Charts (pie, bar, line, doughnut, radar, polarArea, area, horizontalbar, scatter)

For all standard chart types, use `item` and `value`:

```xml
<bx:chartseries type="pie">
    <bx:chartdata item="Product A" value="150">
    <bx:chartdata item="Product B" value="200">
    <bx:chartdata item="Product C" value="100">
</bx:chartseries>
```

### Bubble Charts

For bubble charts, use `item`, `x`, `y`, and `r`:

```xml
<bx:chartseries type="bubble">
    <bx:chartdata item="Investment A" x="20" y="15" r="10">
    <bx:chartdata item="Investment B" x="40" y="25" r="15">
    <bx:chartdata item="Investment C" x="30" y="10" r="8">
</bx:chartseries>
```

Where:

- `x` represents the horizontal position (e.g., risk level)
- `y` represents the vertical position (e.g., return rate)
- `r` represents the bubble size (e.g., investment amount)

## Examples

### Pie Chart Data Points

```xml
<bx:chart title="Market Share">
    <bx:chartseries type="pie" colorlist="FF6384,36A2EB,FFCE56,4BC0C0">
        <bx:chartdata item="Company A" value="35">
        <bx:chartdata item="Company B" value="28">
        <bx:chartdata item="Company C" value="22">
        <bx:chartdata item="Others" value="15">
    </bx:chartseries>
</bx:chart>
```

### Bar Chart Data Points

```xml
<bx:chart title="Sales by Region" xAxisTitle="Region" yAxisTitle="Sales ($)">
    <bx:chartseries type="bar" serieslabel="Q4 2024">
        <bx:chartdata item="North" value="125000">
        <bx:chartdata item="South" value="98000">
        <bx:chartdata item="East" value="142000">
        <bx:chartdata item="West" value="156000">
    </bx:chartseries>
</bx:chart>
```

### Line Chart Time Series

```xml
<bx:chart title="Website Traffic" xAxisTitle="Month" yAxisTitle="Visitors">
    <bx:chartseries type="line" serieslabel="2024 Traffic">
        <bx:chartdata item="Jan" value="15420">
        <bx:chartdata item="Feb" value="18340">
        <bx:chartdata item="Mar" value="22150">
        <bx:chartdata item="Apr" value="19800">
        <bx:chartdata item="May" value="25600">
    </bx:chartseries>
</bx:chart>
```

### Bubble Chart Portfolio Analysis

```xml
<bx:chart title="Investment Portfolio" 
          xAxisTitle="Risk Level" 
          yAxisTitle="Expected Return (%)">
    <bx:chartseries type="bubble" serieslabel="Investments">
        <bx:chartdata item="Bonds" x="2" y="4" r="500000">
        <bx:chartdata item="Blue Chip Stocks" x="5" y="8" r="300000">
        <bx:chartdata item="Growth Stocks" x="8" y="12" r="150000">
        <bx:chartdata item="Crypto" x="15" y="25" r="50000">
    </bx:chartseries>
</bx:chart>
```

### Radar Chart Multi-Variable Comparison

```xml
<bx:chart title="Product Comparison">
    <bx:chartseries type="radar" serieslabel="Product A">
        <bx:chartdata item="Price" value="7">
        <bx:chartdata item="Quality" value="9">
        <bx:chartdata item="Features" value="8">
        <bx:chartdata item="Support" value="6">
        <bx:chartdata item="Reliability" value="9">
    </bx:chartseries>
</bx:chart>
```

### Multi-Series Data Comparison

```xml
<bx:chart title="Server Performance Comparison" seriesPlacement="cluster">
    <bx:chartseries type="bar" serieslabel="CPU Usage %" colorlist="##FF6384">
        <bx:chartdata item="Server 1" value="65">
        <bx:chartdata item="Server 2" value="78">
        <bx:chartdata item="Server 3" value="45">
    </bx:chartseries>
    <bx:chartseries type="bar" serieslabel="Memory Usage %" colorlist="##36A2EB">
        <bx:chartdata item="Server 1" value="42">
        <bx:chartdata item="Server 2" value="56">
        <bx:chartdata item="Server 3" value="33">
    </bx:chartseries>
</bx:chart>
```

## Data Validation

The component automatically validates data based on the parent series chart type:

- **Standard charts**: Requires `item` and `value` attributes
- **Bubble charts**: Requires `item`, `x`, `y`, and `r` attributes
- **Value types**: Numeric values are automatically converted to numbers
- **Missing data**: Missing required attributes will throw validation errors

## Notes

- The `item` attribute provides the label shown in tooltips, legends, and axis labels
- Numeric values are automatically converted to appropriate types for Chart.js
- For bubble charts, the `r` value determines the relative size of bubbles
- Data points are rendered in the order they appear in the component tree
- Empty or invalid numeric values may cause rendering issues

## Related Components

- [bx:chart](bx-chart.md) - Main chart container component
- [bx:chartseries](bx-chartseries.md) - Chart series container that holds chartdata components
