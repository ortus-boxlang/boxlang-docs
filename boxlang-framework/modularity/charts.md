---
description: >-
  The chart module provides chart generation capabilities to the Boxlang
  language.
icon: chart-pie-simple
---

# Charts

> 📊 A comprehensive charting module for BoxLang that brings beautiful, interactive charts to your web applications

This module provides powerful chart generation capabilities to the [BoxLang](https://boxlang.io) language, making it easy to create stunning data visualizations with minimal code.

## 📋 Table of Contents

- [Features](charts#-features)
- [Installation](charts#-installation)
- [Quick Start](charts#-quick-start)
- [Chart Types](charts#-chart-types)
- [Choosing the Right Chart Type](charts#-choosing-the-right-chart-type)
- [Components Reference](charts#-components-reference)
- [Examples](charts#-examples)
  - [Basic Examples](#basic-examples)
  - [Advanced Examples](#advanced-examples)
- [Advanced Features](charts#-advanced-features)
- [Chart.js Integration](charts#-chartjs-integration)
- [Troubleshooting](charts#-troubleshooting)
- [Contributing](charts#-contributing)
- [Support & Resources](charts#-support--resources)
- [License](charts#-license)

## ✨ Features

- 🎨 **10 Chart Types**: pie, bar, line, doughnut, radar, polar area, area, horizontal bar, scatter, and bubble charts
- 📱 **Responsive Design**: Charts automatically adapt to container sizes and screen dimensions
- 🎯 **Easy to Use**: Simple BoxLang component syntax with nested data structure
- 🎭 **Highly Customizable**: Extensive styling options including colors, fonts, axes, and grid lines
- ⚡ **Powered by Chart.js**: Built on the popular Chart.js library for modern, interactive charts
- 📊 **Advanced Features**: Stacked/clustered series, axis titles, custom scales, and tooltips
- 🔧 **Zero Configuration**: Sensible defaults get you started quickly
- 💪 **Production Ready**: Built by Ortus Solutions with enterprise-grade quality

## 📦 Installation

### Requirements

- BoxLang 1.0.0 or higher
- Web support enabled (for `htmlHead()` BIF)

### Install via CommandBox

```bash
box install bx-charts
```

The module will automatically register and be available as `bxcharts` in your BoxLang applications.

### 🚧 Rewrites CAUTION

If you are using a URL rewriting mechanism (like `.htaccess` for Apache or URL rewrite rules in Nginx), ensure that requests to static assets (like JavaScript and CSS files) are properly routed to the `boxlang_modules/bx-charts/assets/` directory. This is crucial for the Chart.js library and any other assets to load correctly.  Also, make sure you are not rewriting the following directory from which assets are delivered from the module:`

```
/bxModules/bxCharts/public/index.bxm
```

The following must passthrough with no rewrites.

### Local Development Setup

For local development and testing of the module itself:

```bash
# Clone the repository
git clone https://github.com/ortus-boxlang/bx-charts.git
cd bx-charts

# Set up local development environment
./setup.sh

# Install dependencies
box install
npm install

# Start the server for testing
box start
```

This creates a symbolic link in `boxlang_modules/bx-charts` for local module development and testing.

## 🚀 Quick Start

Here's how to create your first chart in just a few lines:

```xml
<bx:chart title="My First Chart" chartwidth="400" chartheight="300">
    <bx:chartseries type="pie" colorlist="FF6384,36A2EB,FFCE56">
        <bx:chartdata item="Red" value="300">
        <bx:chartdata item="Blue" value="50">
        <bx:chartdata item="Yellow" value="100">
    </bx:chartseries>
</bx:chart>
```

That's it! 🎉 You now have a beautiful, interactive pie chart.

## 📊 Chart Types

The module supports 10 different chart types, each optimized for specific data visualization needs:

### 🥧 Pie Chart (`type="pie"`)

Perfect for showing proportions and percentages of a whole.

- **Best for**: Market share, budget allocation, survey results
- **Data structure**: Single series with multiple data points

### 📊 Bar Chart (`type="bar"`)

Great for comparing values across categories.

- **Best for**: Comparing quantities, showing rankings, temporal data
- **Features**: Supports stacking and clustering
- **Data structure**: Single or multiple series

### 📈 Line Chart (`type="line"`)

Ideal for showing trends over time.

- **Best for**: Time series, trend analysis, continuous data
- **Features**: Multiple series support, customizable markers
- **Data structure**: One or more series with sequential data points

### 🍩 Doughnut Chart (`type="doughnut"`)

Similar to pie charts but with a hole in the center.

- **Best for**: Proportions with emphasis on total value
- **Visual style**: Modern, clean look with central focus area

### 🕸️ Radar Chart (`type="radar"`)

Shows multivariate data on a circular grid.

- **Best for**: Comparing multiple variables, skill assessments, product comparisons
- **Data structure**: Multiple data points forming a polygon

### 🎯 Polar Area Chart (`type="polarArea"`)

Like a pie chart but with varying radius.

- **Best for**: Showing proportions where magnitude matters
- **Visual style**: Circular sectors with different radii

### 🏔️ Area Chart (`type="area"`)

Line chart with filled area underneath.

- **Best for**: Showing volume over time, cumulative data
- **Features**: Emphasizes magnitude of change

### ↔️ Horizontal Bar Chart (`type="horizontalbar"`)

Bar chart with horizontal orientation.

- **Best for**: Long category names, rankings, comparisons
- **Layout**: Left-to-right instead of bottom-to-top

### 🔵 Scatter Plot (`type="scatter"`)

Shows relationship between two variables.

- **Best for**: Correlation analysis, distribution patterns
- **Data structure**: X-Y coordinate pairs

### 🫧 Bubble Chart (`type="bubble"`)

Shows three-dimensional data using x, y coordinates and bubble size.

- **Best for**: Multi-dimensional data analysis, comparative metrics, portfolio analysis
- **Data structure**: X-Y coordinate pairs with radius (r) for bubble size
- **Usage**: Use `x`, `y`, and `r` attributes in `<bx:chartdata>` instead of just `value`

## 🎯 Choosing the Right Chart Type

Selecting the appropriate chart type is crucial for effective data visualization. Use this guide to choose the best chart for your data:

### 📊 Quick Selection Guide

| **Your Goal** | **Recommended Chart Type** | **Why** |
|--------------|---------------------------|---------|
| Show parts of a whole | **Pie** or **Doughnut** | Best for displaying percentage distribution of 3-6 categories |
| Compare values across categories | **Bar** or **Horizontal Bar** | Clear visual comparison of discrete values |
| Show trends over time | **Line** or **Area** | Excellent for time series and continuous data |
| Compare multiple variables | **Radar** | Perfect for multi-dimensional comparisons (e.g., product features) |
| Show proportions with magnitude | **Polar Area** | Like pie chart but size indicates importance |
| Display correlation | **Scatter** | Shows relationship between two variables |
| Show 3D relationships | **Bubble** | Displays three metrics simultaneously (x, y, size) |
| Compare with long labels | **Horizontal Bar** | Better readability for lengthy category names |
| Emphasize volume/magnitude | **Area** | Highlights total quantity over time |

### 💡 Decision Tree

```
What do you want to visualize?

├─ Parts of a whole (percentages)?
│  ├─ Simple distribution → Pie Chart 🥧
│  └─ Modern look with center space → Doughnut Chart 🍩
│
├─ Comparing values?
│  ├─ Short category names → Bar Chart 📊
│  ├─ Long category names → Horizontal Bar Chart ↔️
│  └─ Multiple variables per item → Radar Chart 🕸️
│
├─ Changes over time?
│  ├─ Single or few metrics → Line Chart 📈
│  └─ Emphasize volume/total → Area Chart 🏔️
│
├─ Relationships between variables?
│  ├─ Two variables (x, y) → Scatter Plot 🔵
│  └─ Three variables (x, y, size) → Bubble Chart 🫧
│
└─ Proportions with varying magnitude?
   └─ Polar Area Chart 🎯
```

### ⚠️ Common Pitfalls to Avoid

| **Don't Use** | **When** | **Use Instead** |
|--------------|---------|-----------------|
| Pie Chart | More than 6 categories | Bar Chart |
| Line Chart | Comparing unrelated categories | Bar Chart |
| 3D Effects | Accuracy is important | 2D charts (all types) |
| Radar Chart | Categories aren't comparable | Bar or Column Chart |
| Bubble Chart | Only 2 dimensions of data | Scatter Plot |

### 📏 Best Practices

1. **Pie/Doughnut Charts**: Limit to 5-6 slices maximum. Order slices by size for better readability.
2. **Bar Charts**: Always start the Y-axis at zero to avoid misleading visualizations.
3. **Line Charts**: Use for continuous data only. Avoid for unrelated categories.
4. **Radar Charts**: Ensure all axes use the same scale and are comparable metrics.
5. **Bubble Charts**: Make sure bubble sizes are clearly distinguishable. Use radius (r) values that create visible differences.
6. **Color Selection**: Use consistent color schemes. Avoid red/green combinations (color blindness).

## 📚 Components Reference

### 📊 `<bx:chart>` Component

The main container component that renders charts using Chart.js.

#### Core Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `title` | string | "" | Chart title displayed at the top |
| `chartWidth` | number | 400 | Chart width in pixels |
| `chartHeight` | number | 300 | Chart height in pixels |
| `backgroundColor` | string | "#ffffff" | Background color (hex or named color) |
| `showLegend` | boolean | true | Display legend for multi-series charts |

#### 📱 Responsive Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `responsive` | boolean | true | Enable responsive resizing |
| `maintainAspectRatio` | boolean | true | Maintain width/height ratio |
| `aspectRatio` | number | 2 | Aspect ratio (width/height) |
| `resizeDelay` | number | 0 | Delay before resize (ms) |

#### 🎨 Styling Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `font` | string | - | Font family for chart text |
| `fontBold` | boolean | false | Bold text |
| `fontItalic` | boolean | false | Italic text |
| `fontSize` | number | 12 | Font size in pixels |
| `foregroundColor` | string | "#333333" | Text color |
| `dataBackgroundColor` | string | - | Data area background color |

#### 📏 Axis Configuration

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `xAxisTitle` | string | "" | X-axis title |
| `yAxisTitle` | string | "" | Y-axis title |
| `showXGridlines` | boolean | false | Show X-axis grid lines |
| `showYGridlines` | boolean | true | Show Y-axis grid lines |
| `showXLabel` | boolean | true | Display X-axis labels |
| `scaleFrom` | number | - | Y-axis minimum value |
| `scaleTo` | number | - | Y-axis maximum value |
| `sortXAxis` | boolean | false | Sort labels alphabetically |

#### 🎯 Display Options

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `showBorder` | boolean | false | Display chart border |
| `showMarkers` | boolean | true | Show data point markers |
| `showTooltip` | boolean | true | Enable tooltips |
| `markerSize` | number | 4 | Marker size in pixels |
| `show3D` | boolean | false | 3D appearance (limited support) |

#### 📐 Advanced Options

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `seriesPlacement` | string | "default" | Series layout: "default", "cluster", "stacked" |
| `labelFormat` | string | "" | Y-axis label format (use `{value}` placeholder) |
| `categoryLabelPositions` | string | "horizontal" | Label rotation: "horizontal", "up_45", "up_90", "down_45", "down_90", "vertical" |
| `url` | string | "" | URL to open when clicking data points |

### 📈 `<bx:chartseries>` Component

Defines a data series within a chart. Must be nested inside `<bx:chart>`.

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `type` | string | ✅ Yes | Chart type: "pie", "bar", "line", "doughnut", "radar", "polarArea", "area", "horizontalbar", "scatter" |
| `colorlist` | string | No | Comma-separated color list (hex or named colors) |
| `serieslabel` | string | No | Label for this data series |

**Example:**

```boxlang
<bx:chartseries type="bar" colorlist="FF6384,36A2EB,FFCE56" serieslabel="Sales Data">
    <!-- chartdata components here -->
</bx:chartseries>
```

### 📍 `<bx:chartdata>` Component

Defines individual data points within a series. Must be nested inside `<bx:chartseries>`.

#### Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `item` | string | ✅ Yes | Data point label/name |
| `value` | number | ✅ Yes* | Data point value (*Required for all chart types except bubble) |
| `x` | number | ⚠️ Bubble | X-coordinate (required for bubble charts) |
| `y` | number | ⚠️ Bubble | Y-coordinate (required for bubble charts) |
| `r` | number | ⚠️ Bubble | Bubble radius (required for bubble charts) |

**Standard Example:**

```boxlang
<bx:chartdata item="Product A" value="150">
<bx:chartdata item="Product B" value="200">
```

**Bubble Chart Example:**

```boxlang
<bx:chartdata item="Product A" x="20" y="30" r="15">
<bx:chartdata item="Product B" x="40" y="10" r="10">
```

## 💡 Examples

### Basic Examples

#### 🥧 Simple Pie Chart

```xml
<bx:chart title="Memory Usage Distribution"
          chartwidth="400" chartheight="300"
          showlegend="true">
    <bx:chartseries type="pie" colorlist="00ff00,0000ff,ff0000,ffff00"
                    serieslabel="Memory Usage">
        <bx:chartdata item="Free Memory" value="512">
        <bx:chartdata item="Used Memory" value="256">
        <bx:chartdata item="Reserved Memory" value="128">
        <bx:chartdata item="Cache Memory" value="64">
    </bx:chartseries>
</bx:chart>
```

**💡 Use Case:** Perfect for showing how a total is divided into parts, like disk space usage or budget allocation.

#### 📊 Bar Chart with Grid Lines

```xml
<bx:chart title="Performance Metrics"
          chartwidth="500" chartheight="350"
          xaxistitle="Metrics" yaxistitle="Count"
          showxgridlines="false" showygridlines="true">
    <bx:chartseries
			type="bar"
			colorlist="131cd7,ED2939,gray,d47f00"
            serieslabel="Performance Data">
        <bx:chartdata item="Hits" value="150">
        <bx:chartdata item="Misses" value="25">
        <bx:chartdata item="Garbage Collections" value="10">
        <bx:chartdata item="Evictions" value="5">
    </bx:chartseries>
</bx:chart>
```

**💡 Use Case:** Great for comparing different categories or metrics at a glance.

#### 📈 Line Chart for Time Series

```xml
<bx:chart title="Website Traffic Over Time"
          chartwidth="600" chartheight="300"
          xaxistitle="Day" yaxistitle="Visitors"
          showygridlines="true">
    <bx:chartseries type="line" colorlist="36A2EB"
                    serieslabel="Daily Visitors">
        <bx:chartdata item="Monday" value="1200">
        <bx:chartdata item="Tuesday" value="1350">
        <bx:chartdata item="Wednesday" value="1100">
        <bx:chartdata item="Thursday" value="1450">
        <bx:chartdata item="Friday" value="1800">
        <bx:chartdata item="Saturday" value="2100">
        <bx:chartdata item="Sunday" value="1900">
    </bx:chartseries>
</bx:chart>
```

**💡 Use Case:** Ideal for displaying trends and patterns over time.

#### 🍩 Doughnut Chart

```xml
<bx:chart title="Browser Market Share"
          chartwidth="400" chartheight="400"
          showlegend="true">
    <bx:chartseries type="doughnut"
                    colorlist="FF6384,36A2EB,FFCE56,4BC0C0,9966FF"
                    serieslabel="Browser Usage">
        <bx:chartdata item="Chrome" value="65">
        <bx:chartdata item="Firefox" value="18">
        <bx:chartdata item="Safari" value="12">
        <bx:chartdata item="Edge" value="4">
        <bx:chartdata item="Others" value="1">
    </bx:chartseries>
</bx:chart>
```

**💡 Use Case:** Similar to pie charts but with a modern look, great for dashboards.

### Advanced Examples

#### 🏔️ Area Chart with Styling

```xml
<bx:chart title="Server Load Over Time"
          chartwidth="600" chartheight="350"
          xaxistitle="Time" yaxistitle="CPU Usage (%)"
          showxgridlines="true" showygridlines="true"
          scalefrom="0" scaleto="100"
          fontsize="14" fontbold="true">
    <bx:chartseries type="area" colorlist="36A2EB"
                    serieslabel="CPU Load">
        <bx:chartdata item="00:00" value="25">
        <bx:chartdata item="04:00" value="15">
        <bx:chartdata item="08:00" value="65">
        <bx:chartdata item="12:00" value="85">
        <bx:chartdata item="16:00" value="75">
        <bx:chartdata item="20:00" value="45">
    </bx:chartseries>
</bx:chart>
```

**💡 Use Case:** Shows volume or magnitude over time with emphasis on total quantity.

#### ↔️ Horizontal Bar Chart

```xml
<bx:chart title="Department Budgets"
          chartwidth="500" chartheight="350"
          xaxistitle="Budget ($1000s)" yaxistitle="Department"
          showygridlines="true">
    <bx:chartseries type="horizontalbar"
                    colorlist="FF6384,36A2EB,FFCE56,4BC0C0"
                    serieslabel="Budget Allocation">
        <bx:chartdata item="IT Department" value="850">
        <bx:chartdata item="Marketing" value="620">
        <bx:chartdata item="Sales" value="950">
        <bx:chartdata item="Human Resources" value="340">
    </bx:chartseries>
</bx:chart>
```

**💡 Use Case:** Perfect when you have long category names or want to emphasize horizontal comparison.

#### 📚 Stacked Bar Chart

```xml
<bx:chart title="Quarterly Sales by Region"
          chartwidth="600" chartheight="400"
          xaxistitle="Quarter" yaxistitle="Sales ($1000s)"
          showygridlines="true"
          seriesplacement="stacked">
    <bx:chartseries type="bar" colorlist="FF6384"
                    serieslabel="North Region">
        <bx:chartdata item="Q1" value="120">
        <bx:chartdata item="Q2" value="135">
        <bx:chartdata item="Q3" value="145">
        <bx:chartdata item="Q4" value="160">
    </bx:chartseries>
    <bx:chartseries type="bar" colorlist="36A2EB"
                    serieslabel="South Region">
        <bx:chartdata item="Q1" value="95">
        <bx:chartdata item="Q2" value="110">
        <bx:chartdata item="Q3" value="105">
        <bx:chartdata item="Q4" value="125">
    </bx:chartseries>
</bx:chart>
```

**💡 Use Case:** Shows both individual values and totals across categories. Perfect for comparing parts of a whole across different groups.

#### 🎯 Radar Chart for Multi-dimensional Data

```xml
<bx:chart title="Skills Assessment"
          chartwidth="500" chartheight="500"
          showlegend="true">
    <bx:chartseries type="radar" colorlist="FF6384"
                    serieslabel="Current Skills">
        <bx:chartdata item="JavaScript" value="85">
        <bx:chartdata item="BoxLang" value="95">
        <bx:chartdata item="Database" value="75">
        <bx:chartdata item="DevOps" value="70">
        <bx:chartdata item="Security" value="80">
    </bx:chartseries>
</bx:chart>
```

**💡 Use Case:** Excellent for showing multiple variables for comparison, like skill assessments or product features.

#### 🔵 Scatter Plot for Correlation

```xml
<bx:chart title="Response Time vs Throughput"
          chartwidth="600" chartheight="400"
          xaxistitle="Response Time (ms)" yaxistitle="Requests/sec"
          showxgridlines="true" showygridlines="true"
          markersize="8">
    <bx:chartseries type="scatter" colorlist="9966FF"
                    serieslabel="Performance Data">
        <bx:chartdata item="Point 1" value="120">
        <bx:chartdata item="Point 2" value="85">
        <bx:chartdata item="Point 3" value="200">
        <bx:chartdata item="Point 4" value="150">
        <bx:chartdata item="Point 5" value="95">
    </bx:chartseries>
</bx:chart>
```

**💡 Use Case:** Shows relationships between two variables, useful for correlation analysis.

#### 🫧 Bubble Chart for Multi-dimensional Analysis

Bubble charts display three dimensions of data using x and y coordinates plus bubble size.

```xml
<bx:chart title="Product Portfolio Analysis"
          chartwidth="600" chartheight="400"
          xaxistitle="Market Share (%)" yaxistitle="Revenue ($M)"
          showxgridlines="true" showygridlines="true">
    <bx:chartseries type="bubble"
                    colorlist="FF6384,36A2EB,FFCE56,4BC0C0"
                    serieslabel="Product Performance">
        <bx:chartdata item="Product A" x="20" y="30" r="15">
        <bx:chartdata item="Product B" x="40" y="10" r="10">
        <bx:chartdata item="Product C" x="30" y="20" r="25">
        <bx:chartdata item="Product D" x="15" y="35" r="8">
    </bx:chartseries>
</bx:chart>
```

**💡 Use Case:** Perfect for displaying three-dimensional data where the third dimension (bubble size) represents metrics like customer satisfaction, investment size, or population.

**Note:** For bubble charts, use `x`, `y`, and `r` attributes instead of `value` in `<bx:chartdata>` components.

#### 📱 Responsive Chart

BoxLang Charts support responsive sizing that adapts to container width and screen sizes. This is ideal for responsive web applications and dashboards.

```xml
<bx:chart title="Responsive Dashboard Chart"
          chartwidth="800" chartheight="400"
          responsive="true"
          maintainAspectRatio="true"
          aspectRatio="2"
          xaxistitle="Month" yaxistitle="Revenue ($)">
    <bx:chartseries type="bar" colorlist="36A2EB"
                    serieslabel="Monthly Revenue">
        <bx:chartdata item="January" value="12000">
        <bx:chartdata item="February" value="15000">
        <bx:chartdata item="March" value="13500">
        <bx:chartdata item="April" value="18000">
    </bx:chartseries>
</bx:chart>
```

**💡 Use Case:** Perfect for dashboards and mobile-friendly layouts where charts need to adapt to different screen sizes.

**Responsive Tips:**

- Charts resize automatically to fit their container width (up to `chartWidth`)
- Use `maintainAspectRatio="false"` to fill specific container heights
- Set custom aspect ratios: `2` for wide (2:1), `1` for square (1:1), `0.5` for tall (1:2)
- Add `resizeDelay` for performance optimization on frequently resizing containers

## 🚀 Advanced Features

### 📊 Series Placement Options

Control how multiple data series are displayed in bar charts:

**Default (Side-by-side):**

```js
seriesplacement="default"  <!-- or omit the attribute -->
```

**Clustered (Grouped bars):**

```js
seriesplacement="cluster"
```

**Stacked (Bars on top of each other):**

```js
seriesplacement="stacked"
```

### 🎨 Color Customization

Colors can be specified in multiple formats:

```xml
<!-- Hex colors (with or without #) -->
colorlist="FF6384,36A2EB,FFCE56"
colorlist="##FF6384,##36A2EB,##FFCE56"

<!-- Named colors -->
colorlist="red,blue,green,yellow"

<!-- RGB values (use hex format) -->
colorlist="rgb(255,99,132),rgb(54,162,235)"
```

**Color Best Practices:**

- Use contrasting colors for better accessibility
- Limit to 5-7 distinct colors for clarity
- Consider colorblind-friendly palettes for inclusive design
- Use [ColorBrewer](https://colorbrewer2.org/) for scientifically-designed palettes

### 📏 Custom Scales and Ranges

Control axis ranges for better data visualization:

```xml
<bx:chart scalefrom="0" scaleto="100"
          yaxistitle="Percentage">
    <!-- chart content -->
</bx:chart>
```

**Tips:**

- Set `scaleFrom="0"` for bar charts to avoid misleading visualizations
- Use custom scales to zoom into specific data ranges
- Combine with `labelFormat` for custom axis labels

### 🔤 Label Formatting and Rotation

Format axis labels and rotate them for better readability:

```xml
<!-- Format Y-axis labels -->
<bx:chart labelFormat="{value}%" yaxistitle="Percentage">

<!-- Rotate category labels for long names -->
<bx:chart categoryLabelPositions="up_45">
```

**Label Position Options:**

- `horizontal` - Standard horizontal labels (default)
- `up_45` - 45° upward rotation
- `up_90` - 90° upward (vertical)
- `down_45` - 45° downward rotation
- `down_90` - 90° downward
- `vertical` - Same as `down_90`

### 🎯 Interactive Features

Make charts interactive with click events:

```xml
<bx:chart url="https://www.example.com/details">
    <!-- Clicking any data point opens this URL -->
</bx:chart>
```

### 🎭 Font and Style Customization

Complete control over text appearance:

```xml
<bx:chart fontBold="true"
          fontItalic="false"
          fontSize="16"
          foregroundColor="##2C3E50"
          dataBackgroundColor="##ECF0F1">
    <!-- Styled chart -->
</bx:chart>
```

### 📍 Marker Control

Customize data point markers for line and scatter charts:

```xml
<bx:chart showMarkers="true"
          markerSize="8">
    <bx:chartseries type="line">
        <!-- Line chart with large markers -->
    </bx:chartseries>
</bx:chart>
```

## 🔧 Chart.js Integration

This module is built on [Chart.js v4.x](https://www.chartjs.org/), one of the most popular JavaScript charting libraries.

### 📚 Chart.js Resources

- **Official Documentation**: [https://www.chartjs.org/docs/latest/](https://www.chartjs.org/docs/latest/)
- **Chart Types Guide**: [https://www.chartjs.org/docs/latest/charts/](https://www.chartjs.org/docs/latest/charts/)
- **Configuration Options**: [https://www.chartjs.org/docs/latest/configuration/](https://www.chartjs.org/docs/latest/configuration/)
- **Samples**: [https://www.chartjs.org/samples/](https://www.chartjs.org/samples/)

### 🎨 Chart.js Features Supported

This module exposes most Chart.js capabilities through BoxLang attributes:

- ✅ All major chart types (pie, bar, line, doughnut, radar, polar area, scatter)
- ✅ Responsive and adaptive sizing
- ✅ Custom colors and styling
- ✅ Axis configuration and grid lines
- ✅ Legends and tooltips
- ✅ Stacked and grouped series
- ✅ Custom scales and ranges
- ✅ Font styling and customization

### 🔌 How It Works

1. **Component Processing**: BoxLang components collect your chart data
2. **Configuration Building**: Data is transformed into Chart.js configuration
3. **Asset Loading**: Chart.js library is automatically included via `htmlHead()`
4. **Rendering**: HTML canvas element is created with inline JavaScript initialization
5. **Interaction**: Chart.js handles all user interactions and animations

### 💡 Chart.js Best Practices

Based on Chart.js documentation, here are some tips:

**Performance:**

- Use `resizeDelay` for charts that resize frequently
- Limit data points to 100-200 for smooth animations
- Disable animations for large datasets

**Accessibility:**

- Always provide axis titles with `xAxisTitle` and `yAxisTitle`
- Use `seriesLabel` to describe each data series
- Ensure color contrasts meet WCAG standards

**Visual Design:**

- Keep charts simple - one message per chart
- Use appropriate chart types for your data
- Add grid lines (`showYGridlines="true"`) for precise reading
- Limit colors to 5-7 for clarity

## ❓ Troubleshooting

### Charts Not Displaying

**Problem:** Chart area is blank or not visible.

**Solutions:**

- ✅ Ensure BoxLang web support is enabled
- ✅ Check that `htmlHead()` BIF is available
- ✅ Verify Chart.js library loads (check browser console)
- ✅ Make sure chart container has width/height

### Colors Not Working

**Problem:** Custom colors not appearing correctly.

**Solutions:**

- ✅ Use hex format without # or with ## (BoxLang escaping): `colorlist="FF6384,36A2EB"`
- ✅ Check color format: hex values should be 6 characters (e.g., `FF0000` not `F00`)
- ✅ Named colors are case-insensitive: `red`, `Red`, `RED` all work

### Responsive Charts Not Resizing

**Problem:** Charts don't adapt to container size changes.

**Solutions:**

- ✅ Set `responsive="true"` (it's default, but verify)
- ✅ Ensure parent container has defined width
- ✅ Use `maintainAspectRatio="false"` if you need to fill specific heights
- ✅ Check for CSS that might be constraining the chart

### Multiple Series Not Stacking

**Problem:** Multiple series appear side-by-side instead of stacked.

**Solutions:**

- ✅ Add `seriesplacement="stacked"` to `<bx:chart>`
- ✅ Ensure all series have the same chart type
- ✅ Stacking only works with `bar`, `line`, and `area` chart types

### Data Not Showing

**Problem:** Chart renders but no data appears.

**Solutions:**

- ✅ Verify all `<bx:chartdata>` components have `item` and `value` attributes
- ✅ Check that values are numeric (not strings)
- ✅ Ensure `<bx:chartdata>` is nested inside `<bx:chartseries>`
- ✅ Verify `<bx:chartseries>` is nested inside `<bx:chart>`

### Labels Overlapping

**Problem:** X-axis labels overlap and are unreadable.

**Solutions:**

- ✅ Use `categoryLabelPositions="up_45"` to rotate labels
- ✅ Increase `chartWidth` to give more space
- ✅ Reduce font size with `fontSize="10"`
- ✅ Consider using `horizontalbar` type for long labels

## 🤝 Contributing

We ❤️ contributions! This project is open source and welcomes your help to make it even better.

### 🐛 Found a Bug?

If you discover a bug, please:

1. **Check existing issues** at [GitHub Issues](https://github.com/ortus-boxlang/bx-charts/issues)
2. **Create a new issue** with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - BoxLang version and environment details
   - Sample code that demonstrates the issue

### 💡 Have an Enhancement Idea?

We'd love to hear your ideas! Please:

1. Open a [Feature Request](https://github.com/ortus-boxlang/bx-charts/issues/new)
2. Describe the feature and its use case
3. Explain how it would benefit users
4. Consider if it aligns with Chart.js capabilities

### 🔧 Want to Contribute Code?

Excellent! Here's how to get started:

#### Development Setup

1. **Fork and Clone:**

   ```bash
   git clone https://github.com/YOUR-USERNAME/bx-charts.git
   cd bx-charts
   ```

2. **Set up Local Development Environment:**

   ```bash
   # Creates symbolic link for local module development
   ./setup.sh
   ```

   This script creates a `boxlang_modules/bx-charts` symbolic link pointing to the current directory, allowing you to test the module locally before publishing.

3. **Install Dependencies:**

   ```bash
   # Install BoxLang dependencies
   box install

   # Install Node.js dependencies (Chart.js)
   npm install
   ```

   The `npm install` command will automatically:
   - Download the latest Chart.js library
   - Copy it to the `public/` folder

4. **Update Chart.js (Optional):**

   To manually update Chart.js to the latest version:

   ```bash
   npm run update-chartjs
   ```

5. **Test the Module Locally:**

   Start a BoxLang server to test your changes:

   ```bash
   # Start the BoxLang server (uses server.json configuration)
   box start

   # Visit test pages in your browser
   # http://localhost:8080/tests/ - Main test index
   # http://localhost:8080/tests/test-charts-enhanced.bxm - Advanced chart examples
   # http://localhost:8080/tests/test-responsive-charts.bxm - Responsive chart tests
   ```

   The test files in `/tests/` directory provide comprehensive examples of all chart types and features.

6. **Build the Module (Optional):**

   To build a distributable version of the module:

   ```bash
   # Build with default version (1.0.0)
   boxlang Build.bx

   # Build with specific version
   boxlang Build.bx --version=1.2.3

   # Built artifacts will be in build/artifacts/
   ```

7. **Start Format Watcher:**

   ```bash
   box run-script format:watch
   ```

#### Pull Request Guidelines

- ✅ Create PRs against the `development` branch (NOT `master`)
- ✅ Follow the existing code style (auto-format with cfformat)
- ✅ Add tests for new features
- ✅ Update documentation as needed
- ✅ Keep commits focused and atomic
- ✅ Link related issues in PR description

#### Code Standards

- **BoxLang/CFML**: Follow [cfformat](.cfformat.json) settings
- **Formatting**: Auto-format with `box run-script format`
- **Coding Standards**: Follow [Ortus Coding Standards](https://github.com/Ortus-Solutions/coding-standards)

### 📚 Improve Documentation

Documentation improvements are always welcome:

- Fix typos or unclear explanations
- Add more examples
- Improve code comments
- Create tutorials or guides

### 💰 Financial Support

You can support BoxLang and all Ortus Solutions open source projects:

- 🌟 [Become a Patron](https://www.patreon.com/ortussolutions)
- 💵 [One-time PayPal Donation](https://www.paypal.com/paypalme/ortussolutions)

Patrons get exclusive benefits like:

- Priority support
- Early access to new features
- FORGEBOX Pro account
- CFCasts account

### 📞 Support Channels

Need help? Don't create an issue—use our support channels:

- 💬 [Ortus Community Discourse](https://community.ortussolutions.com)
- 📱 [Box Team Slack](http://boxteam.ortussolutions.com/)
- 🏢 [Professional Support](https://www.ortussolutions.com/services/support)

### 🏆 Contributors

Thank you to all our amazing contributors! ❤️

<a href="https://github.com/ortus-boxlang/bx-charts/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ortus-boxlang/bx-charts" alt="Contributors"/>
</a>

Made with [contributors-img](https://contrib.rocks)

## 🔐 Security Vulnerabilities

If you discover a security vulnerability:

1. **DO NOT** create a public issue
2. Email [security@ortussolutions.com](mailto:security@ortussolutions.com?subject=security)
3. Report in `#security` channel on [Box Team Slack](http://boxteam.ortussolutions.com/)

All vulnerabilities will be promptly addressed.

## 📄 License

This project is licensed under the **Apache License 2.0**.

```
Copyright 2025 Ortus Solutions, Corp

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

See [LICENSE](LICENSE) file for full details.

## 💼 Support & Resources

### 📖 Documentation

- **Module Docs**: You're reading them! 📚
- **BoxLang Docs**: [https://boxlang.ortusbooks.com/](https://boxlang.ortusbooks.com/)
- **Chart.js Docs**: [https://www.chartjs.org/docs/](https://www.chartjs.org/docs/)

### 🌐 Links

- **BoxLang Website**: [https://boxlang.io](https://boxlang.io)
- **Ortus Solutions**: [https://www.ortussolutions.com](https://www.ortussolutions.com)
- **GitHub Repository**: [https://github.com/ortus-boxlang/bx-charts](https://github.com/ortus-boxlang/bx-charts)
- **Issue Tracker**: [https://github.com/ortus-boxlang/bx-charts/issues](https://github.com/ortus-boxlang/bx-charts/issues)

### 🎓 Learning Resources

- **BoxLang Training**: [https://www.ortussolutions.com/services/training](https://www.ortussolutions.com/services/training)
- **CFCasts**: [https://www.cfcasts.com](https://www.cfcasts.com)
- **Blog**: [https://www.ortussolutions.com/blog](https://www.ortussolutions.com/blog)