# BoxLang Charts Module Documentation

## Component Reference

This documentation provides comprehensive reference information for all components in the BoxLang Charts Module.

## Components

### [bx:chart](components/bx-chart.md)

**Main chart container component**

The primary component that renders interactive charts using Chart.js. Supports responsive design, extensive styling options, and multiple chart types.

### [bx:chartseries](components/bx-chartseries.md)  

**Chart series definition component**

Defines data series within charts, specifying chart type and data sources. Supports component-based, query-based, and array-based data sources.

### [bx:chartdata](components/bx-chartdata.md)

**Individual data point component**

Represents single data points within chart series. Supports standard value-based data and three-dimensional bubble chart coordinates.

## Quick Start

```xml
<bx:chart title="My Chart" chartWidth="400" chartHeight="300">
    <bx:chartseries type="pie" colorlist="FF6384,36A2EB,FFCE56">
        <bx:chartdata item="Item 1" value="100">
        <bx:chartdata item="Item 2" value="200">
        <bx:chartdata item="Item 3" value="150">
    </bx:chartseries>
</bx:chart>
```

## Chart Types Supported

- **pie** - Circular proportional charts
- **bar** - Vertical bar charts  
- **line** - Connected data point charts
- **doughnut** - Pie charts with center holes
- **radar** - Multi-variable circular charts
- **polarArea** - Pie charts with varying radius
- **area** - Line charts with filled areas
- **horizontalbar** - Horizontal bar charts
- **scatter** - X-Y coordinate plots
- **bubble** - Three-dimensional data visualization

## Installation

```bash
box install bx-charts
```

Requires BoxLang 1.0.0+ with web support enabled.

## Module Information

- **Version**: 1.0.0+
- **Author**: Ortus Solutions
- **License**: Apache 2.0
- **Dependencies**: Chart.js (included)
- **BoxLang Version**: 1.0.0+
