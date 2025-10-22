---
description: >-
  This module provides UI layout, grid, and AJAX capabilities to the BoxLang
  language, making it easy to create rich, interactive web applications with
  familiar CFML syntax.
icon: table
---

# Compat UI

### 📋 Table of Contents

* Features
* Installation
* Quick Start
* Components Reference
  * Layout Components
  * Grid Components
  * AJAX Components
  * UI Components
* Built-In Functions (BIFs)
  * AJAX BIFs
  * Grid BIFs
* Examples
  * Layout Examples
  * Grid Examples
  * AJAX Examples
  * Complete Application Examples
* Advanced Features
* Troubleshooting
* Contributing
* Support & Resources
* License

### ✨ Features

* 🎨 **Layout Management**: Tab, accordion, border, hbox, and vbox layouts with nested content areas
* 📊 **Data Grids**: Sortable, editable data grids with pagination and column management
* 🔧 **AJAX Support**: Client-server communication with JavaScript proxy generation and content loading
* 🎯 **Pod Containers**: Flexible content containers with title bars and body areas
* 📱 **Responsive Design**: Components adapt to different screen sizes and containers
* 🔗 **CFML Compatibility**: Familiar syntax for Adobe ColdFusion and Lucee developers
* 💪 **Production Ready**: Built by Ortus Solutions with enterprise-grade quality
* 🚀 **Zero Configuration**: Sensible defaults get you started quickly

### 📦 Installation

#### Requirements

* BoxLang 1.0.0 or higher
* Web support enabled (for HTML generation and AJAX functionality)
* bx-esapi module (automatically installed as a dependency)

#### Install via CommandBox

```bash
box install bx-compat-ui
```

The module will automatically register and be available in your BoxLang applications with the following components:

* `bx:layout`, `bx:layoutarea` - Layout management
* `bx:grid`, `bx:gridcolumn`, `bx:gridrow`, `bx:gridupdate` - Data grids
* `bx:ajaxproxy`, `bx:ajaximport` - AJAX functionality
* `bx:pod`, `bx:div`, `bx:tooltip` - UI containers and elements

#### 🚧 Rewrites CAUTION

If you are using a URL rewriting mechanism (like `.htaccess` for Apache or URL rewrite rules in Nginx), ensure that requests to static assets (JavaScript and CSS files) are properly routed. The module serves assets from the following paths:

```
/bxModules/bxCompatUI/public/
```

Make sure these paths passthrough with no rewrites.

### 🚀 Quick Start

Here's how to create your first UI layout in just a few lines:

```xml
<bx:layout type="tab" fillHeight="true">
    <bx:layoutarea title="Dashboard">
        <h2>Welcome to My App</h2>
        <p>Dashboard content goes here</p>
    </bx:layoutarea>
    <bx:layoutarea title="Data">
        <bx:grid name="myGrid" pageSize="10">
            <bx:gridcolumn name="id" header="ID" width="80" />
            <bx:gridcolumn name="name" header="Name" width="200" />
        </bx:grid>
    </bx:layoutarea>
</bx:layout>
```

That's it! 🎉 You now have a tabbed interface with a dashboard and a data grid.

### 📚 Components Reference

#### Layout Components

**📐 `<bx:layout>` Component**

The main container component for creating structured layouts

**Attributes**

| Attribute     | Type    | Default        | Description                                               |
| ------------- | ------- | -------------- | --------------------------------------------------------- |
| `type`        | string  | **Required**   | Layout type: "tab", "accordion", "border", "hbox", "vbox" |
| `align`       | string  | ""             | Content alignment: "left", "center", "right", "justify"   |
| `fillHeight`  | boolean | false          | Fill available height                                     |
| `fitToWindow` | boolean | false          | Fill entire window viewport                               |
| `height`      | string  | ""             | CSS height value (e.g., "400px", "50%")                   |
| `width`       | string  | ""             | CSS width value (e.g., "600px", "100%")                   |
| `style`       | string  | ""             | Additional CSS styles                                     |
| `id`          | string  | auto-generated | HTML element ID                                           |
| `class`       | string  | ""             | Additional CSS classes                                    |
| `name`        | string  | ""             | Component name identifier                                 |

**Layout Types**

* **tab** - Tabbed interface with clickable headers
* **accordion** - Collapsible panels with headers
* **border** - Five-region layout (top, bottom, left, right, center)
* **hbox** - Horizontal box layout (flex row)
* **vbox** - Vertical box layout (flex column)

**📋 `<bx:layoutarea>` Component**

Defines content areas within a Layout. Must be nested inside `<bx:layout>`.

**Attributes**

| Attribute       | Type    | Default        | Description                                                            |
| --------------- | ------- | -------------- | ---------------------------------------------------------------------- |
| `title`         | string  | ""             | Area title (used for tabs/accordion headers)                           |
| `align`         | string  | ""             | Content alignment within the area                                      |
| `collapsible`   | boolean | true           | Whether area can be collapsed (accordion)                              |
| `initcollapsed` | boolean | false          | Start in collapsed state                                               |
| `source`        | string  | ""             | URL to load content from (AJAX)                                        |
| `position`      | string  | "center"       | Position for border layout: "bottom", "center", "left", "right", "top" |
| `size`          | string  | ""             | CSS size for border layout regions                                     |
| `splitter`      | boolean | true           | Show splitter for border layout                                        |
| `minsize`       | string  | ""             | Minimum size constraint                                                |
| `maxsize`       | string  | ""             | Maximum size constraint                                                |
| `id`            | string  | auto-generated | HTML element ID                                                        |

#### Grid Components

**📊 `<bx:grid>` Component**

Creates a data grid with sorting, editing, and pagination capabilities

**Core Attributes**

| Attribute     | Type    | Default      | Description                                   |
| ------------- | ------- | ------------ | --------------------------------------------- |
| `name`        | string  | **Required** | Grid control name                             |
| `query`       | query   | null         | Query object to populate the grid             |
| `pageSize`    | number  | 25           | Number of rows per page                       |
| `sortable`    | boolean | true         | Enable column sorting                         |
| `editable`    | boolean | false        | Enable cell editing                           |
| `autoWidth`   | boolean | false        | Auto-size columns to fit content              |
| `height`      | string  | ""           | Grid height (CSS value)                       |
| `width`       | string  | ""           | Grid width (CSS value)                        |
| `stripeRows`  | boolean | true         | Alternate row colors                          |
| `showHeaders` | boolean | true         | Show column headers                           |
| `selectMode`  | string  | "single"     | Row selection mode: "none", "single", "multi" |

**Event Attributes**

| Attribute | Type   | Default | Description                                      |
| --------- | ------ | ------- | ------------------------------------------------ |
| `onLoad`  | string | ""      | JavaScript function called when grid loads       |
| `onEdit`  | string | ""      | JavaScript function called when cell is edited   |
| `onSort`  | string | ""      | JavaScript function called when column is sorted |

**Styling Attributes**

| Attribute            | Type    | Default | Description               |
| -------------------- | ------- | ------- | ------------------------- |
| `bgColor`            | string  | ""      | Background color for grid |
| `bold`               | boolean | false   | Bold text formatting      |
| `colHeaderBold`      | boolean | false   | Bold column headers       |
| `colHeaderFont`      | string  | ""      | Column header font family |
| `colHeaderFontSize`  | number  | 12      | Column header font size   |
| `colHeaderItalic`    | boolean | false   | Italic column headers     |
| `colHeaderTextColor` | string  | ""      | Column header text color  |

**Advanced Attributes**

| Attribute     | Type    | Default | Description                          |
| ------------- | ------- | ------- | ------------------------------------ |
| `bind`        | string  | ""      | Data binding expression for AJAX     |
| `bindOnLoad`  | boolean | true    | Whether to bind data on initial load |
| `collapsible` | boolean | false   | Whether grid is collapsible          |
| `delete`      | boolean | false   | Allow delete operations              |
| `appendKey`   | boolean | false   | Append key field to form data        |

**📋 `<bx:gridcolumn>` Component**

Defines a column within a grid. Must be nested inside `<bx:grid>`.

**Attributes**

| Attribute  | Type    | Default      | Description                                       |
| ---------- | ------- | ------------ | ------------------------------------------------- |
| `name`     | string  | **Required** | Column name (maps to query column)                |
| `header`   | string  | name         | Column header text                                |
| `width`    | string  | "auto"       | Column width (CSS value)                          |
| `sortable` | boolean | true         | Enable sorting for this column                    |
| `editable` | boolean | false        | Enable editing for this column                    |
| `type`     | string  | "string"     | Data type: "string", "numeric", "date", "boolean" |
| `format`   | string  | ""           | Display format for values                         |
| `align`    | string  | "left"       | Text alignment: "left", "center", "right"         |

**🔄 `<bx:gridrow>` Component**

Defines a data row within a grid (for manual data input)

**🔧 `<bx:gridupdate>` Component**

Handles grid update operations for editable grids

#### AJAX Components

**🔗 `<bx:ajaxproxy>` Component**

Creates JavaScript proxies for server-side components and executes bind expressions

**Attributes**

| Attribute     | Type   | Default  | Description                                                 |
| ------------- | ------ | -------- | ----------------------------------------------------------- |
| `cfc`         | string | ""       | The CFC for which to create a proxy (dot-delimited path)    |
| `jsclassname` | string | cfc name | Name for the JavaScript proxy class                         |
| `bind`        | string | ""       | Bind expression for CFC method, JavaScript function, or URL |
| `onError`     | string | ""       | JavaScript function to execute if bind fails                |
| `onSuccess`   | string | ""       | JavaScript function to execute if bind succeeds             |

**📦 `<bx:ajaximport>` Component**

Imports JavaScript and CSS files required for BoxLang AJAX tags and features

**Attributes**

| Attribute   | Type   | Default             | Description                                                                    |
| ----------- | ------ | ------------------- | ------------------------------------------------------------------------------ |
| `tags`      | string | ""                  | Comma-delimited list of BoxLang AJAX tags for which to import supporting files |
| `cssSrc`    | string | "/bx-compat-ui/css" | URL of the directory containing CSS files                                      |
| `scriptSrc` | string | "/bx-compat-ui/js"  | URL of the directory containing JavaScript files                               |
| `params`    | string | ""                  | Parameters to pass, such as API keys                                           |

#### UI Components

**🎨 `<bx:pod>` Component**

Creates a container with optional title bar and body content

**Attributes**

| Attribute     | Type   | Default | Description                                                                        |
| ------------- | ------ | ------- | ---------------------------------------------------------------------------------- |
| `title`       | string | ""      | Text to display in the pod's title bar                                             |
| `name`        | string | ""      | The name assigned to the pod control                                               |
| `height`      | string | ""      | Height of the control in pixels                                                    |
| `width`       | string | ""      | Width of the control in pixels                                                     |
| `bodyStyle`   | string | ""      | CSS style specification for the pod body                                           |
| `headerStyle` | string | ""      | CSS style specification for the pod header                                         |
| `overflow`    | string | "auto"  | How to display child content that overflows: "auto", "hidden", "scroll", "visible" |
| `source`      | string | ""      | URL that returns the content of the pod                                            |
| `onBindError` | string | ""      | JavaScript function to execute if bind expression results in error                 |

**📦 `<bx:div>` Component**

Creates a flexible content container with AJAX loading capabilities

**💬 `<bx:tooltip>` Component**

Adds interactive tooltips to elements

### 🔧 Built-In Functions (BIFs)

#### AJAX BIFs

**ajaxLink(url)**

Generates a URL that causes link results to display within the current AJAX container rather than replacing the current page content.

**Parameters**

* `url` (string, required) - The URL to load when the link is clicked

**Return Value**

Returns a JavaScript URL that handles AJAX loading into the nearest suitable container.

**Examples**

```boxlang
<bx:script>
ajaxURL = ajaxLink("content/page1.bxm");
</bx:script>

<a href="#ajaxURL#">Load Content</a>

<!-- In a pod or layout -->
<bx:pod name="myPod">
    <a href="#ajaxLink('data.bxm')#">Load Data</a>
</bx:pod>
```

**ajaxOnLoad(functionName)**

Specifies a JavaScript function to run when a page loads in the browser.

**Parameters**

* `functionName` (string, required) - The name of the JavaScript function to execute on page load

**Return Value**

Returns an empty string (outputs JavaScript to the page buffer).

**Examples**

```boxlang
<script>
function initializePage() {
    console.log("Page loaded!");
    // Initialize your UI components here
}
</script>

<bx:script>
ajaxOnLoad("initializePage");
</bx:script>
```

#### Grid BIFs

**queryConvertForGrid(query, page, pageSize)**

Converts a query object to a format suitable for grid display with pagination and sorting.

**Parameters**

* `query` (query, required) - The query object to convert
* `page` (number, optional) - The page number (1-based, default: 1)
* `pageSize` (number, optional) - The number of rows per page (default: 25)

**Return Value**

Returns a structure containing the converted grid data with pagination information.

**Examples**

```boxlang
<bx:script>
// Convert query for grid display
myQuery = queryNew("id,name,email", "integer,varchar,varchar", [
    [1, "John Doe", "john@example.com"],
    [2, "Jane Smith", "jane@example.com"]
]);

gridData = queryConvertForGrid(myQuery, 1, 10);
</bx:script>

<bx:grid name="userGrid" query="#gridData.query#">
    <bx:gridcolumn name="id" header="ID" width="80" />
    <bx:gridcolumn name="name" header="Name" width="200" />
    <bx:gridcolumn name="email" header="Email" width="250" />
</bx:grid>
```

### 💡 Examples

#### Layout Examples

**📑 Tab Layout**

```xml
<bx:layout type="tab" fillHeight="true">
    <bx:layoutarea title="Home">
        <h2>Welcome</h2>
        <p>This is the home tab content. Perfect for dashboard or overview information.</p>
    </bx:layoutarea>
    <bx:layoutarea title="Profile">
        <h2>User Profile</h2>
        <p>User profile information and settings go here.</p>
    </bx:layoutarea>
    <bx:layoutarea title="Settings">
        <h2>Application Settings</h2>
        <p>Configure your application preferences.</p>
    </bx:layoutarea>
</bx:layout>
```

**💡 Use Case:** Perfect for organizing related content into easily accessible tabs, like user interfaces with multiple sections.

**🎯 Accordion Layout**

```xml
<bx:layout type="accordion">
    <bx:layoutarea title="Getting Started" collapsible="true">
        <h3>Welcome to BoxLang UI</h3>
        <p>This section helps you get started with the basics.</p>
        <ul>
            <li>Installation guide</li>
            <li>First steps</li>
            <li>Basic examples</li>
        </ul>
    </bx:layoutarea>
    <bx:layoutarea title="Advanced Features" initcollapsed="true">
        <h3>Advanced Functionality</h3>
        <p>Learn about advanced features and customization options.</p>
    </bx:layoutarea>
    <bx:layoutarea title="FAQ" initcollapsed="true">
        <h3>Frequently Asked Questions</h3>
        <p>Common questions and their answers.</p>
    </bx:layoutarea>
</bx:layout>
```

**💡 Use Case:** Great for FAQ sections, help documentation, or any content where you want to conserve vertical space.

**🎨 Border Layout**

```xml
<bx:layout type="border" height="500px">
    <bx:layoutarea position="top" size="60px">
        <header style="background: #333; color: white; padding: 15px;">
            <h1>My Application</h1>
        </header>
    </bx:layoutarea>
    <bx:layoutarea position="left" size="200px">
        <nav style="padding: 10px;">
            <h3>Navigation</h3>
            <ul>
                <li><a href="#dashboard">Dashboard</a></li>
                <li><a href="#reports">Reports</a></li>
                <li><a href="#settings">Settings</a></li>
            </ul>
        </nav>
    </bx:layoutarea>
    <bx:layoutarea position="center">
        <main style="padding: 20px;">
            <h2>Main Content Area</h2>
            <p>This is where your primary content goes.</p>
        </main>
    </bx:layoutarea>
    <bx:layoutarea position="right" size="150px">
        <aside style="padding: 10px;">
            <h4>Sidebar</h4>
            <p>Additional information or tools.</p>
        </aside>
    </bx:layoutarea>
    <bx:layoutarea position="bottom" size="40px">
        <footer style="background: #f5f5f5; padding: 10px; text-align: center;">
            © 2024 My Application
        </footer>
    </bx:layoutarea>
</bx:layout>
```

**💡 Use Case:** Ideal for complete application layouts with header, footer, sidebar navigation, and main content areas.

**↔️ Box Layouts (HBox/VBox)**

**Horizontal Box Layout:**

```xml
<bx:layout type="hbox" width="100%" style="gap: 10px;">
    <bx:layoutarea>
        <bx:pod title="Statistics" width="200px">
            <p>Users: 1,234</p>
            <p>Sales: $45,678</p>
        </bx:pod>
    </bx:layoutarea>
    <bx:layoutarea>
        <bx:pod title="Recent Activity" width="300px">
            <ul>
                <li>User registered</li>
                <li>Order placed</li>
                <li>Payment processed</li>
            </ul>
        </bx:pod>
    </bx:layoutarea>
    <bx:layoutarea>
        <bx:pod title="Quick Actions" width="200px">
            <button>Export Data</button>
            <button>Generate Report</button>
        </bx:pod>
    </bx:layoutarea>
</bx:layout>
```

**Vertical Box Layout:**

```xml
<bx:layout type="vbox" height="400px">
    <bx:layoutarea>
        <h3>Header Section</h3>
    </bx:layoutarea>
    <bx:layoutarea style="flex: 1;">
        <p>This area will expand to fill available space.</p>
    </bx:layoutarea>
    <bx:layoutarea>
        <button>Action Button</button>
    </bx:layoutarea>
</bx:layout>
```

**💡 Use Case:** Perfect for arranging content horizontally or vertically with consistent spacing and alignment.

#### Grid Examples

**📊 Basic Data Grid**

```xml
<bx:script>
// Create sample data
employeeQuery = queryNew("id,name,department,salary", "integer,varchar,varchar,numeric", [
    [1, "John Doe", "Engineering", 75000],
    [2, "Jane Smith", "Marketing", 65000],
    [3, "Bob Johnson", "Sales", 55000],
    [4, "Alice Brown", "Engineering", 80000]
]);
</bx:script>

<bx:grid name="employeeGrid" 
         query="#employeeQuery#" 
         pageSize="10" 
         sortable="true" 
         stripeRows="true">
    <bx:gridcolumn name="id" header="ID" width="60" sortable="false" />
    <bx:gridcolumn name="name" header="Employee Name" width="200" />
    <bx:gridcolumn name="department" header="Department" width="150" />
    <bx:gridcolumn name="salary" header="Salary" width="120" type="numeric" format="currency" align="right" />
</bx:grid>
```

**💡 Use Case:** Perfect for displaying tabular data with sorting and pagination capabilities.

**✏️ Editable Grid with Events**

```xml
<bx:script>
function handleGridEdit(grid, row, col, newValue, oldValue) {
    console.log("Cell edited:", { row, col, newValue, oldValue });
    // Handle the edit - save to database, validate, etc.
}

function handleGridLoad(grid) {
    console.log("Grid loaded successfully");
    // Initialize any additional functionality
}
</bx:script>

<bx:grid name="editableGrid" 
         query="#productQuery#" 
         editable="true"
         pageSize="15"
         onEdit="handleGridEdit"
         onLoad="handleGridLoad"
         selectMode="multi">
    <bx:gridcolumn name="id" header="Product ID" width="80" editable="false" />
    <bx:gridcolumn name="name" header="Product Name" width="250" editable="true" />
    <bx:gridcolumn name="price" header="Price" width="100" type="numeric" format="currency" editable="true" />
    <bx:gridcolumn name="active" header="Active" width="80" type="boolean" editable="true" />
</bx:grid>
```

**💡 Use Case:** Ideal for administrative interfaces where users need to edit data directly in the grid.

#### AJAX Examples

**🔗 AJAX Proxy for Server Communication**

```xml
<bx:ajaximport tags="ajaxproxy" />

<bx:ajaxproxy cfc="components.UserService" 
              jsclassname="UserProxy" />

<script>
// Use the generated JavaScript proxy
var userProxy = new UserProxy();

function loadUserData() {
    userProxy.call("getUsers", {department: "Engineering"}, function(result) {
        console.log("Users loaded:", result);
        // Process the result data
        displayUsers(result);
    });
}

function displayUsers(users) {
    var html = "<ul>";
    users.forEach(function(user) {
        html += "<li>" + user.name + " (" + user.email + ")</li>";
    });
    html += "</ul>";
    document.getElementById("userList").innerHTML = html;
}
</script>

<button onclick="loadUserData()">Load Users</button>
<div id="userList"></div>
```

**💡 Use Case:** Perfect for creating rich client-server interactions without page refreshes.

**🔄 AJAX Content Loading**

```xml
<bx:ajaximport />

<bx:layout type="tab">
    <bx:layoutarea title="Static Content">
        <h2>This content is loaded immediately</h2>
        <p>No AJAX required for static content.</p>
    </bx:layoutarea>
    <bx:layoutarea title="Dynamic Content" source="content/dynamic-data.bxm">
        <p>Loading...</p>
    </bx:layoutarea>
</bx:layout>

<bx:pod title="Navigation" width="250px">
    <ul>
        <li><a href="#ajaxLink('pages/dashboard.bxm')#">Dashboard</a></li>
        <li><a href="#ajaxLink('pages/reports.bxm')#">Reports</a></li>
        <li><a href="#ajaxLink('pages/settings.bxm')#">Settings</a></li>
    </ul>
</bx:pod>
```

**💡 Use Case:** Great for loading content dynamically while maintaining the overall page structure.

#### Complete Application Examples

**🏢 Enterprise Dashboard**

```xml
<!DOCTYPE html>
<html>
<head>
    <title>Enterprise Dashboard</title>
    <bx:ajaximport tags="layout,grid,pod" />
</head>
<body>
    <bx:layout type="border" fitToWindow="true">
        <bx:layoutarea position="top" size="70px">
            <header style="background: #2c3e50; color: white; padding: 15px; display: flex; justify-content: space-between; align-items: center;">
                <h1>Enterprise Dashboard</h1>
                <nav>
                    <a href="#ajaxLink('logout.bxm')" style="color: white;">Logout</a>
                </nav>
            </header>
        </bx:layoutarea>
        
        <bx:layoutarea position="left" size="280px">
            <bx:layout type="accordion">
                <bx:layoutarea title="Navigation">
                    <ul style="list-style: none; padding: 10px;">
                        <li><a href="#ajaxLink('dashboard/overview.bxm')#">📊 Overview</a></li>
                        <li><a href="#ajaxLink('dashboard/analytics.bxm')#">📈 Analytics</a></li>
                        <li><a href="#ajaxLink('dashboard/users.bxm')#">👥 Users</a></li>
                        <li><a href="#ajaxLink('dashboard/reports.bxm')#">📋 Reports</a></li>
                    </ul>
                </bx:layoutarea>
                <bx:layoutarea title="Quick Stats" initcollapsed="false">
                    <div style="padding: 10px;">
                        <bx:pod title="Today's Stats">
                            <p><strong>Active Users:</strong> 1,234</p>
                            <p><strong>Revenue:</strong> $45,678</p>
                            <p><strong>Orders:</strong> 89</p>
                        </bx:pod>
                    </div>
                </bx:layoutarea>
                <bx:layoutarea title="Tools" initcollapsed="true">
                    <div style="padding: 10px;">
                        <button onclick="exportData()">📤 Export Data</button><br><br>
                        <button onclick="generateReport()">📊 Generate Report</button><br><br>
                        <button onclick="backupSystem()">💾 Backup System</button>
                    </div>
                </bx:layoutarea>
            </bx:layout>
        </bx:layoutarea>
        
        <bx:layoutarea position="center">
            <bx:layout type="tab" fillHeight="true">
                <bx:layoutarea title="📊 Overview">
                    <div style="padding: 20px;">
                        <h2>System Overview</h2>
                        <bx:layout type="hbox" style="gap: 20px;">
                            <bx:layoutarea>
                                <bx:pod title="Revenue Metrics" height="300px">
                                    <p>Monthly Revenue: $123,456</p>
                                    <p>Growth: +15.3%</p>
                                    <!-- Chart would go here -->
                                </bx:pod>
                            </bx:layoutarea>
                            <bx:layoutarea>
                                <bx:pod title="User Activity" height="300px">
                                    <p>Active Sessions: 456</p>
                                    <p>New Users: 23</p>
                                    <!-- Activity graph would go here -->
                                </bx:pod>
                            </bx:layoutarea>
                        </bx:layout>
                    </div>
                </bx:layoutarea>
                <bx:layoutarea title="📋 Data Management">
                    <div style="padding: 20px;">
                        <h2>User Management</h2>
                        <bx:grid name="userManagementGrid" 
                                 pageSize="15" 
                                 sortable="true" 
                                 editable="true"
                                 selectMode="multi">
                            <bx:gridcolumn name="id" header="ID" width="60" editable="false" />
                            <bx:gridcolumn name="username" header="Username" width="150" />
                            <bx:gridcolumn name="email" header="Email" width="250" />
                            <bx:gridcolumn name="role" header="Role" width="120" />
                            <bx:gridcolumn name="lastLogin" header="Last Login" width="150" type="date" />
                            <bx:gridcolumn name="active" header="Active" width="80" type="boolean" />
                        </bx:grid>
                    </div>
                </bx:layoutarea>
                <bx:layoutarea title="📈 Analytics">
                    <div style="padding: 20px;">
                        <h2>Performance Analytics</h2>
                        <p>Detailed analytics and reporting tools will be displayed here.</p>
                        <!-- Analytics charts and reports would go here -->
                    </div>
                </bx:layoutarea>
            </bx:layout>
        </bx:layoutarea>
        
        <bx:layoutarea position="bottom" size="50px">
            <footer style="background: #ecf0f1; padding: 15px; text-align: center; border-top: 1px solid #bdc3c7;">
                <p>&copy; 2024 Enterprise Dashboard | Built with BoxLang UI Compatibility Module</p>
            </footer>
        </bx:layoutarea>
    </bx:layout>

    <script>
    function exportData() {
        alert("Exporting data...");
        // Implement export functionality
    }
    
    function generateReport() {
        alert("Generating report...");
        // Implement report generation
    }
    
    function backupSystem() {
        alert("Starting system backup...");
        // Implement backup functionality
    }
    </script>
</body>
</html>
```

**💡 Use Case:** Complete enterprise application interface with navigation, data management, and analytics all in one unified interface.

**🛒 E-commerce Admin Panel**

```xml
<bx:layout type="border" fitToWindow="true">
    <bx:layoutarea position="top" size="80px">
        <header style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px;">
            <h1>🛒 E-commerce Admin Panel</h1>
        </header>
    </bx:layoutarea>
    
    <bx:layoutarea position="left" size="250px">
        <bx:pod title="Quick Actions" height="200px">
            <div style="padding: 10px;">
                <button style="width: 100%; margin: 5px 0; padding: 8px;">➕ Add Product</button>
                <button style="width: 100%; margin: 5px 0; padding: 8px;">📦 Process Orders</button>
                <button style="width: 100%; margin: 5px 0; padding: 8px;">👥 Manage Users</button>
                <button style="width: 100%; margin: 5px 0; padding: 8px;">📊 View Reports</button>
            </div>
        </bx:pod>
    </bx:layoutarea>
    
    <bx:layoutarea position="center">
        <bx:layout type="tab" fillHeight="true">
            <bx:layoutarea title="📦 Products">
                <div style="padding: 15px;">
                    <bx:grid name="productGrid" 
                             pageSize="20" 
                             sortable="true" 
                             editable="true">
                        <bx:gridcolumn name="id" header="ID" width="60" />
                        <bx:gridcolumn name="name" header="Product Name" width="250" />
                        <bx:gridcolumn name="category" header="Category" width="120" />
                        <bx:gridcolumn name="price" header="Price" width="100" type="numeric" format="currency" />
                        <bx:gridcolumn name="stock" header="Stock" width="80" type="numeric" />
                        <bx:gridcolumn name="active" header="Active" width="80" type="boolean" />
                    </bx:grid>
                </div>
            </bx:layoutarea>
            <bx:layoutarea title="📋 Orders">
                <div style="padding: 15px;">
                    <bx:grid name="orderGrid" 
                             pageSize="15" 
                             sortable="true">
                        <bx:gridcolumn name="orderNumber" header="Order #" width="120" />
                        <bx:gridcolumn name="customerName" header="Customer" width="180" />
                        <bx:gridcolumn name="orderDate" header="Date" width="120" type="date" />
                        <bx:gridcolumn name="total" header="Total" width="100" type="numeric" format="currency" />
                        <bx:gridcolumn name="status" header="Status" width="100" />
                    </bx:grid>
                </div>
            </bx:layoutarea>
            <bx:layoutarea title="👥 Customers">
                <div style="padding: 15px;">
                    <bx:grid name="customerGrid" 
                             pageSize="20" 
                             sortable="true">
                        <bx:gridcolumn name="id" header="ID" width="60" />
                        <bx:gridcolumn name="name" header="Name" width="200" />
                        <bx:gridcolumn name="email" header="Email" width="250" />
                        <bx:gridcolumn name="city" header="City" width="120" />
                        <bx:gridcolumn name="totalOrders" header="Orders" width="80" type="numeric" />
                        <bx:gridcolumn name="totalSpent" header="Total Spent" width="120" type="numeric" format="currency" />
                    </bx:grid>
                </div>
            </bx:layoutarea>
        </bx:layout>
    </bx:layoutarea>
</bx:layout>
```

**💡 Use Case:** Perfect for e-commerce administration interfaces with product management, order processing, and customer management all in one place.

### 🚀 Advanced Features

#### 📊 Dynamic Data Loading

Components support AJAX data loading through the `source` attribute:

```xml
<bx:layoutarea title="Dynamic Content" source="api/get-content.bxm">
    <p>Loading content...</p>
</bx:layoutarea>

<bx:pod title="Live Data" source="api/get-stats.bxm">
    <p>Fetching latest statistics...</p>
</bx:pod>
```

#### 🎨 CSS Integration

All components generate semantic CSS classes for easy styling:

```css
/* Layout styling */
.bx-layout-tab .bx-tab-header.active {
    background-color: #3498db;
    color: white;
}

/* Grid styling */
.bx-grid .bx-grid-row:nth-child(even) {
    background-color: #f8f9fa;
}

/* Pod styling */
.bx-pod .bx-pod-title {
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    color: white;
}
```

#### 🔗 Event Handling

Components support comprehensive JavaScript event handling:

```xml
<bx:grid name="myGrid" 
         onLoad="handleGridLoad"
         onEdit="handleCellEdit"
         onSort="handleColumnSort">
    <!-- grid columns -->
</bx:grid>

<script>
function handleGridLoad(grid) {
    console.log("Grid loaded:", grid.name);
}

function handleCellEdit(grid, row, col, newValue, oldValue) {
    // Validate and save changes
    if (validateValue(newValue)) {
        saveToServer(row, col, newValue);
    }
}

function handleColumnSort(grid, column, direction) {
    console.log("Sorted by:", column, direction);
}
</script>
```

#### 📱 Responsive Design

Layouts automatically adapt to different screen sizes:

```xml
<bx:layout type="border" fitToWindow="true">
    <!-- Content automatically adjusts to viewport -->
</bx:layout>

<bx:grid name="responsiveGrid" autoWidth="true">
    <!-- Columns resize based on content and container -->
</bx:grid>
```

### ❓ Troubleshooting

#### Components Not Rendering

**Problem:** Components appear as raw tags or don't render properly.

**Solutions:**

* ✅ Ensure the module is installed: `box install bx-compat-ui`
* ✅ Verify BoxLang web support is enabled
* ✅ Check that component tags use the correct `bx:` prefix
* ✅ Ensure required attributes are provided (e.g., `type` for layouts, `name` for grids)

#### AJAX Functionality Not Working

**Problem:** AJAX links or content loading fails.

**Solutions:**

* ✅ Include `<bx:ajaximport />` or `<bx:ajaximport tags="layout,grid" />` in your page
* ✅ Ensure URLs are accessible and return valid content
* ✅ Check browser console for JavaScript errors
* ✅ Verify that the BoxLang AJAX namespace is initialized

#### Layout Areas Not Displaying

**Problem:** Layout areas don't appear or appear incorrectly.

**Solutions:**

* ✅ Ensure `<bx:layoutarea>` components are nested inside `<bx:layout>`
* ✅ Check that `position` attributes are valid for border layouts
* ✅ Verify `title` attributes are provided for tab and accordion layouts
* ✅ Include appropriate CSS for styling (or use default CSS)

#### Grid Not Showing Data

**Problem:** Grid renders but shows no data or incorrect data.

**Solutions:**

* ✅ Verify the query object has data: `query.recordCount > 0`
* ✅ Check that column names in `<bx:gridcolumn>` match query column names
* ✅ Ensure the query is properly passed to the grid's `query` attribute
* ✅ Use `queryConvertForGrid()` if pagination is needed

#### Styling Issues

**Problem:** Components don't look right or lack styling.

**Solutions:**

* ✅ Include component CSS files or create custom styles
* ✅ Check for CSS conflicts with existing stylesheets
* ✅ Use browser developer tools to inspect generated HTML and classes
* ✅ Verify CSS classes are being applied correctly

#### JavaScript Errors

**Problem:** Interactive features not working, console shows errors.

**Solutions:**

* ✅ Ensure `<bx:ajaximport />` is included before using AJAX features
* ✅ Check that JavaScript function names are spelled correctly in event attributes
* ✅ Verify that referenced JavaScript functions are defined before components load
* ✅ Use `ajaxOnLoad()` to ensure initialization happens at the right time

#### Performance Issues

**Problem:** Large grids or complex layouts are slow.

**Solutions:**

* ✅ Use pagination with reasonable page sizes (25-50 rows)
* ✅ Consider lazy loading for layout areas with `source` attribute
* ✅ Optimize database queries that populate grids
* ✅ Use `autoWidth="false"` for grids with many columns

###
