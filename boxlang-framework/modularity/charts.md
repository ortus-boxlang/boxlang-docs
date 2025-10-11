---
description: >-
  The chart module provides chart generation capabilities to the Boxlang language.
icon: globe
---

This module provides chart generation capabilities to the Boxlang language

## Components

This module contributes the following Components to the language:

* `chart` - renders charts to the browser using the Chart.js library
  * The following attributes are available to the `mail` component
    * `backgroundColor` - string, optional -  Color of the area between the data background and the chart border, around labels and around the legend. Hexadecimal value or supported named color. For a hex value, use the form: textColor = "##xxxxxx", where x = 0-9 or A-F; use two hash signs or none.
    * `chartHeight` - number, optional -  Chart height; integer number of pixels
    * `chartWidth` - number, optional -  Chart width; integer number of pixels
    * `font` - string, optional -  Font of data in column..
    * `show3D` - boolean, optional -  Display chart with three-dimensional appearance.
    * `showLegend` - boolean, optional -  yes: if chart contains more than one data series, display legend
    * `showXGridlines` - boolean, optional -  yes: display X-axis gridlines
    * `source` - string, optional -  variable name of the source path
    * `showYGridlines` - boolean, optional -  yes: display Y-axis gridlines.
    * `title` - string, optional -  Title of the chart.
    * `xAxisTitle` - string, optional -  text; X-axis title
    * `yAxisTitle` - string, optional -  text; Y-axis title
    * `dataBackgroundColor` - string, optional -  color for control. For a hex value, use the form: textColor = "##xxxxxx", where x = 0-9 or A-F; use two hash signs or none.
    * `fontBold` - boolean, optional -  Yes: displays grid control text in bold.
    * `fontItalic` - boolean, optional -  Yes: displays grid control text in italics.
    * `fontSize` - number, optional -  Size of text in column. Default: 12.
    * `foregroundColor` - string, optional -  color for control. For a hex value, use the form: textColor = "##xxxxxx", where x = 0-9 or A-F; use two hash signs or none. Default: ##333333.
    * `labelFormat` - string, optional -  Format for Y-axis labels. Use {value} placeholder for the actual value.
    * `categoryLabelPositions` - string, optional -  Label position relative to axis: standard, up_45, up_90, down_45, down_90 or horizontal (standard) and vertical (down_90). Default is horizontal.
    * `markerSize` - number, optional -  Size of data point marker in pixels. Integer. Default: 4.
    * `scaleFrom` - number, optional -  Y-axis minimum value; integer.
    * `scaleTo` - number, optional -  Y-axis max value; integer.
    * `showBorder` - boolean, optional -  Whether to display a border around the chart.
    * `showMarkers` - boolean, optional -  Applies to chartseries type attribute values line, curve and scatter. yes: display markers at data points. Default: true.
    * `showXLabel` - boolean, optional -  yes: shows the x-axis labels. Default: true.
    * `showTooltip` - boolean, optional -  show the tooltip or not. Default: true.
    * `sortXAxis` - boolean, optional -  Display column labels in alphabetic order along X-axis. Ignored if the xAxisType attribute is scale.
    * `url` - string, optional -  URL to open if the user clicks item in a data series.
* `chartSeries` - used within the `chart` component. defines the style in which chart data displays: bar, line, pie, etc.
  * this component supports the following attributes:
    * `item` - string, required - The name of the data point.
    * `value` - string, required -The value of the data point.
    * `color` - string, optional  - The color of the data point. Accepts hexadecimal values - e.g., #FF0000`) or named colors.
    * `markerStyle` - string, optional - Specifies the style of the marker for the data point. Possible values: `circle`, `square`, `diamond`, `triangle`, `plus`, `star`, `cross`.
    * `url` - string, optional - The URL to open when the data point is clicked.
    * `tooltip` - string, optional - The text to display as a tooltip for the data point.
    * `seriesLabel` - string, optional - The label for the series to which the data point belongs.
    * `seriesColor` - string, optional - The color of the series to which the data point belongs.
* `chartData` - used within the `chartSeries` component. defines chart data points for the cfchartseries component.
  * this component supports the following attributes:
    * `item` - string, required - data point name
   	* `value` - string, required - data point value

## Examples

### Pie Chart with Axis Titles and Custom Colors

```
<bx:chart format="png" show3d="false" title="Memory Usage Distribution"
			backgroundcolor="##ffffff" chartheight="275" chartwidth="275"
			showlegend="true">
	<bx:chartseries type="pie" colorlist="00ff00, 0000ff, ff0000, ffff00"
					serieslabel="Memory Usage">
		<bx:chartdata item="Free Memory" value="512">
		<bx:chartdata item="Used Memory" value="256">
		<bx:chartdata item="Reserved Memory" value="128">
		<bx:chartdata item="Cache Memory" value="64">
	</bx:chartseries>
</bx:chart>
```

### Bar Chart with Axis Titles and Grid Lines

```
<bx:chart format="png" show3d="false" backgroundcolor="##ffffff"
			chartwidth="400" chartheight="300" showlegend="true"
			title="Performance Metrics"
			xaxistitle="Metrics" yaxistitle="Count"
			showxgridlines="true" showygridlines="true">
	<bx:chartseries type="bar" colorlist="131cd7,ED2939,gray,d47f00"
					serieslabel="Performance Data">
		<bx:chartdata item="Hits" value="150">
		<bx:chartdata item="Misses" value="25">
		<bx:chartdata item="Garbage Collections" value="10">
		<bx:chartdata item="Evictions" value="5">
	</bx:chartseries>
</bx:chart>
```

### Horizontal Bar Chart

```
<bx:chart format="png" title="Department Budgets"
			chartwidth="450" chartheight="300"
			xaxistitle="Budget (thousands)" yaxistitle="Departments"
			showxgridlines="false" showygridlines="true">
	<bx:chartseries type="horizontalbar" colorlist="FF6384,36A2EB,FFCE56,4BC0C0"
					serieslabel="Budget Allocation">
		<bx:chartdata item="IT" value="850">
		<bx:chartdata item="Marketing" value="620">
		<bx:chartdata item="Sales" value="950">
		<bx:chartdata item="HR" value="340">
	</bx:chartseries>
</bx:chart>
```

### Area Chart Example

```
<bx:chart format="png" title="Website Traffic Over Time"
			chartwidth="500" chartheight="300"
			xaxistitle="Time Period" yaxistitle="Visitors"
			showxgridlines="true" showygridlines="true">
	<bx:chartseries type="area" colorlist="36A2EB"
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

### Stacked Bar Chart

```
<bx:chart format="png" title="Quarterly Sales by Region"
			chartwidth="500" chartheight="350"
			xaxistitle="Quarters" yaxistitle="Sales (thousands)"
			showxgridlines="false" showygridlines="true"
			seriesplacement="stacked">
	<bx:chartseries type="bar" colorlist="FF6384,36A2EB,FFCE56"
					serieslabel="North Region">
		<bx:chartdata item="Q1" value="120">
		<bx:chartdata item="Q2" value="135">
		<bx:chartdata item="Q3" value="145">
		<bx:chartdata item="Q4" value="160">
	</bx:chartseries>
</bx:chart>
```
