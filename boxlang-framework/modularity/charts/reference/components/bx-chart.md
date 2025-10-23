# bx:chart

## Summary

The main container component that renders charts using Chart.js. This component processes nested `bx:chartseries` and `bx:chartdata` components to build interactive chart visualizations.

## Syntax

```xml
<bx:chart 
    title="string"
    chartWidth="number" 
    chartHeight="number"
    backgroundColor="string"
    showLegend="boolean"
    [additional attributes...]>
    <bx:chartseries type="pie|bar|line|...">
        <bx:chartdata item="string" value="number">
        <!-- additional chartdata components -->
    </bx:chartseries>
    <!-- additional chartseries components -->
</bx:chart>
```

## Attributes

### Core Attributes

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `backgroundColor` | string | No | "#ffffff" | Color of the area between the data background and the chart border, around labels and around the legend. Hexadecimal value or supported named color. For a hex value, use the form: `backgroundColor = "##xxxxxx"`, where x = 0-9 or A-F; use two hash signs or none. |
| `chartHeight` | number | No | 300 | Chart height; integer number of pixels |
| `chartWidth` | number | No | 400 | Chart width; integer number of pixels |
| `title` | string | No | "" | Title of the chart displayed at the top |
| `showLegend` | boolean | No | true | If chart contains more than one data series, display legend |

### Responsive Attributes

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `responsive` | boolean | No | true | Enable responsive behavior. When true, chart resizes with container |
| `maintainAspectRatio` | boolean | No | true | Maintain aspect ratio during resize |
| `aspectRatio` | number | No | 2 | Aspect ratio (width/height) for chart |
| `resizeDelay` | number | No | 0 | Delay in milliseconds before resize update |

### Styling Attributes

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `font` | string | No | - | Font family for chart text |
| `fontBold` | boolean | No | false | Display grid control text in bold |
| `fontItalic` | boolean | No | false | Display grid control text in italics |
| `fontSize` | number | No | 12 | Size of text in pixels |
| `foregroundColor` | string | No | "#333333" | Text color. For a hex value, use the form: `foregroundColor = "##xxxxxx"`, where x = 0-9 or A-F; use two hash signs or none |
| `dataBackgroundColor` | string | No | - | Data area background color. For a hex value, use the form: `dataBackgroundColor = "##xxxxxx"`, where x = 0-9 or A-F; use two hash signs or none |
| `borderColor` | string | No | - | Border color for chart elements like bars, lines, and pie slices. Hexadecimal value or supported named color. For a hex value, use the form: `borderColor = "##xxxxxx"`. Applies to: bar, line, area, pie, doughnut, radar, polarArea, bubble |
| `borderWidth` | number | No | varies | Border width in pixels. Applies to: bar, line, area, pie, doughnut, radar, polarArea, bubble. Default: 1 for bar, 2 for pie/doughnut/polarArea/bubble, 3 for line/area/radar |
| `borderRadius` | number | No | 0 | Border radius in pixels for rounded corners on bars. Applies to: bar, horizontalbar only |

### Axis Configuration

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `xAxisTitle` | string | No | "" | X-axis title |
| `yAxisTitle` | string | No | "" | Y-axis title |
| `showXGridlines` | boolean | No | false | Display X-axis gridlines |
| `showYGridlines` | boolean | No | true | Display Y-axis gridlines |
| `showXLabel` | boolean | No | true | Show the x-axis labels |
| `scaleFrom` | number | No | - | Y-axis minimum value; integer |
| `scaleTo` | number | No | - | Y-axis max value; integer |
| `sortXAxis` | boolean | No | false | Display column labels in alphabetic order along X-axis. Ignored if the xAxisType attribute is scale |

### Display Options

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `showBorder` | boolean | No | false | Whether to display a border around the chart |
| `showMarkers` | boolean | No | true | Display markers at data points. Applies to chartseries type attribute values line, curve and scatter |
| `showTooltip` | boolean | No | true | Show the tooltip or not |
| `markerSize` | number | No | 4 | Size of data point marker in pixels. Integer |
| `show3D` | boolean | No | false | Display chart with three-dimensional appearance |

### Advanced Options

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `seriesPlacement` | string | No | "default" | Series layout: "default", "cluster", "stacked" |
| `labelFormat` | string | No | "" | Format for Y-axis labels. Use `{value}` placeholder for the actual value |
| `categoryLabelPositions` | string | No | "horizontal" | Label position relative to axis: "horizontal", "up_45", "up_90", "down_45", "down_90", "vertical" |
| `url` | string | No | "" | URL to open when clicking data points. Variables will be substituted: `$SERIESLABEL$`, `$ITEMLABEL$`, `$VALUE$` |

### Legacy/Not Implemented Attributes

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `format` | string | No | - | File format in which to save graph. **Not implemented** (web charts only support canvas/HTML) |
| `name` | string | No | - | Page variable name. **Not implemented** (not applicable to web charts) |
| `pieSliceStyle` | string | No | - | Applies to chartseries type attribute value pie. **Not implemented** |
| `source` | string | No | - | Variable name of the source path. **Not implemented** |
| `xOffset` | number | No | - | Applies if `show3D="yes"`. Number of units by which to display the chart as angled, horizontally. **Not implemented** |
| `yOffset` | number | No | - | Applies if `show3D="yes"`. Number of units by which to display the chart as angled, horizontally. **Not implemented** |
| `base64` | boolean | No | false | Render chart inline using a base64 data url. **Not implemented** |

## Examples

### Basic Pie Chart

```xml
<bx:chart title="Sales Distribution" chartWidth="400" chartHeight="300">
    <bx:chartseries type="pie" colorlist="FF6384,36A2EB,FFCE56">
        <bx:chartdata item="Product A" value="150">
        <bx:chartdata item="Product B" value="200">
        <bx:chartdata item="Product C" value="100">
    </bx:chartseries>
</bx:chart>
```

### Stacked Bar Chart with Styling

```xml
<bx:chart title="Resource Usage" 
          xAxisTitle="Servers" 
          yAxisTitle="Usage %" 
          seriesPlacement="stacked" 
          showYGridlines="true"
          borderColor="##333333"
          borderWidth="2">
    <bx:chartseries type="bar" serieslabel="CPU Usage">
        <bx:chartdata item="Server 1" value="30">
        <bx:chartdata item="Server 2" value="45">
    </bx:chartseries>
    <bx:chartseries type="bar" serieslabel="Memory Usage">
        <bx:chartdata item="Server 1" value="25">
        <bx:chartdata item="Server 2" value="35">
    </bx:chartseries>
</bx:chart>
```

### Responsive Line Chart

```xml
<bx:chart title="Performance Trends" 
          responsive="true" 
          maintainAspectRatio="true"
          aspectRatio="2.5"
          showMarkers="true"
          markerSize="6">
    <bx:chartseries type="line" colorlist="##FF6384" serieslabel="Response Time">
        <bx:chartdata item="Jan" value="200">
        <bx:chartdata item="Feb" value="180">
        <bx:chartdata item="Mar" value="165">
    </bx:chartseries>
</bx:chart>
```

## Notes

- The `bx:chart` component must contain at least one `bx:chartseries` component
- Color values can be specified as hex codes (with ## prefix) or named colors
- The component automatically includes Chart.js library and generates responsive, interactive charts
- Charts are rendered using HTML5 Canvas element with unique IDs to support multiple charts per page
- Border attributes (`borderColor`, `borderWidth`, `borderRadius`) can be set at chart level and overridden at series level

## Related Components

- [bx:chartseries](bx-chartseries.md) - Defines chart series and data source
- [bx:chartdata](bx-chartdata.md) - Defines individual data points
