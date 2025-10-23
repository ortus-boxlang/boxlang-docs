# BoxLang Charts Module - Component Reference

## Overview

The BoxLang Charts Module provides three main components for creating interactive, responsive charts in your BoxLang applications:

- **[bx:chart](components/bx-chart.md)** - Main chart container component
- **[bx:chartseries](components/bx-chartseries.md)** - Chart series definition component
- **[bx:chartdata](components/bx-chartdata.md)** - Individual data point component

## Quick Reference

### Component Hierarchy

```xml
<bx:chart>
    <bx:chartseries>
        <bx:chartdata>
        <!-- Additional chartdata components -->
    </bx:chartseries>
    <!-- Additional chartseries components -->
</bx:chart>
```

### Supported Chart Types

| Type | Description | Component |
|------|-------------|-----------|
| `pie` | Circular proportional chart | [bx:chartseries](components/bx-chartseries.md) |
| `bar` | Vertical bar chart | [bx:chartseries](components/bx-chartseries.md) |
| `line` | Connected data points | [bx:chartseries](components/bx-chartseries.md) |
| `doughnut` | Pie chart with center hole | [bx:chartseries](components/bx-chartseries.md) |
| `radar` | Multi-variable circular chart | [bx:chartseries](components/bx-chartseries.md) |
| `polarArea` | Pie chart with varying radius | [bx:chartseries](components/bx-chartseries.md) |
| `area` | Line chart with filled area | [bx:chartseries](components/bx-chartseries.md) |
| `horizontalbar` | Horizontal bar chart | [bx:chartseries](components/bx-chartseries.md) |
| `scatter` | X-Y coordinate plot | [bx:chartseries](components/bx-chartseries.md) |
| `bubble` | Three-dimensional data visualization | [bx:chartseries](components/bx-chartseries.md) |

### Data Source Options

The module supports multiple ways to provide data to charts:

1. **Component-based**: Using nested `bx:chartdata` components
2. **Query-based**: Using BoxLang query objects
3. **Array-based**: Using arrays of structs or arrays

## Examples

### Basic Usage

```xml
<bx:chart title="Sales Data" chartWidth="500" chartHeight="400">
    <bx:chartseries type="pie" colorlist="FF6384,36A2EB,FFCE56">
        <bx:chartdata item="Product A" value="150">
        <bx:chartdata item="Product B" value="200">
        <bx:chartdata item="Product C" value="100">
    </bx:chartseries>
</bx:chart>
```

### Multi-Series Chart

```xml
<bx:chart title="Performance Comparison" seriesPlacement="cluster">
    <bx:chartseries type="bar" serieslabel="2023" colorlist="##FF6384">
        <bx:chartdata item="Q1" value="100">
        <bx:chartdata item="Q2" value="120">
        <bx:chartdata item="Q3" value="110">
        <bx:chartdata item="Q4" value="140">
    </bx:chartseries>
    <bx:chartseries type="bar" serieslabel="2024" colorlist="##36A2EB">
        <bx:chartdata item="Q1" value="110">
        <bx:chartdata item="Q2" value="135">
        <bx:chartdata item="Q3" value="125">
        <bx:chartdata item="Q4" value="155">
    </bx:chartseries>
</bx:chart>
```

### Query-Based Chart

```xml
<cfquery name="salesData" datasource="myDB">
    SELECT product_name as item, SUM(sales_amount) as value
    FROM sales 
    GROUP BY product_name
    ORDER BY value DESC
</cfquery>

<bx:chart title="Product Sales">
    <bx:chartseries type="bar" 
                    query="#salesData#" 
                    serieslabel="Total Sales">
    </bx:chartseries>
</bx:chart>
```

### Bubble Chart with Three-Dimensional Data

```xml
<bx:chart title="Portfolio Analysis" 
          xAxisTitle="Risk Level" 
          yAxisTitle="Expected Return">
    <bx:chartseries type="bubble" serieslabel="Investments">
        <bx:chartdata item="Bonds" x="2" y="4" r="10">
        <bx:chartdata item="Stocks" x="6" y="8" r="15">
        <bx:chartdata item="Crypto" x="9" y="15" r="5">
    </bx:chartseries>
</bx:chart>
```

## Component Documentation

### [bx:chart](components/bx-chart.md)

The main container component that renders the chart. Supports extensive configuration options for styling, responsive behavior, axes, and display options.

**Key Features:**

- Responsive design with configurable aspect ratios
- Comprehensive styling options (fonts, colors, borders)
- Axis configuration and grid line control
- Multiple series support with stacking/clustering options

### [bx:chartseries](components/bx-chartseries.md)

Defines a data series within a chart. Specifies the chart type and can source data from components, queries, or arrays.

**Key Features:**

- 10 different chart types supported
- Multiple data source options
- Per-series styling overrides
- Border and color customization

### [bx:chartdata](components/bx-chartdata.md)

Represents individual data points within a chart series. Supports standard value-based data points and three-dimensional bubble chart coordinates.

**Key Features:**

- Simple item/value pairs for most charts
- Three-coordinate system (x,y,r) for bubble charts
- Automatic data validation and type conversion
- Flexible labeling system

## Installation & Setup

```bash
box install bx-charts
```

Requires BoxLang 1.0.0+ with web support enabled.

## Module Structure

```
bx-charts/
├── components/
│   ├── Chart.bx           # Main chart component
│   ├── ChartSeries.bx     # Chart series component
│   └── ChartData.bx       # Data point component
├── docs/
│   └── components/        # Component documentation
├── public/
│   └── chart.min.js       # Chart.js library
└── ModuleConfig.bx        # Module configuration
```

## Getting Started

1. **Install the module**: `box install bx-charts`
2. **Include in your template**: Use the `bx:chart` component
3. **Add data**: Use nested `bx:chartseries` and `bx:chartdata` components
4. **Customize**: Apply styling and configuration attributes as needed

For complete attribute references and advanced usage examples, see the individual component documentation pages.
