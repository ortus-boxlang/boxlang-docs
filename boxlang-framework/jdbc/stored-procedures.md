---
description: Execute database stored procedures with IN/OUT/INOUT parameters and result set capture
icon: code
---

# 🗂️ Stored Procedures

BoxLang provides comprehensive support for executing database stored procedures through the `bx:storedProc` component. You can pass parameters, capture return values, retrieve multiple result sets, and handle complex procedure logic.

## 📋 Overview

Stored procedure support in BoxLang includes:

- **Parameter Types** - IN, OUT, and INOUT parameters
- **Multiple Result Sets** - Capture all result sets returned by a procedure
- **Return Codes** - Retrieve procedure return status codes
- **NULL Handling** - Proper NULL value support for parameters and results
- **Type Safety** - Strong typing with SQL type declarations
- **Database Agnostic** - Works across MySQL, PostgreSQL, Oracle, SQL Server, and more

## 🔧 Basic Stored Procedure Execution

### Simple Procedure Call

**Script Syntax:**

```js
bx:storedProc
    procedure="sp_GetEmployees"
    datasource="myDB"
    result="procResult" {

    bx:procResult name="employees" resultset="1";
}

// Access the result set
writeOutput( "Found #employees.recordCount# employees" );
```

**Template Syntax:**

You can use  the template syntax within code islands <pre>```</pre> or if you are within a `.bxm` template:

```xml
<bx:storedProc
    procedure="sp_GetEmployees"
    datasource="myDB"
    result="procResult">

    <bx:procResult name="employees" resultset="1" />
</bx:storedProc>

<!-- Access the result set -->
<bx:output>
    Found #employees.recordCount# employees
</bx:output>
```

## 📥 IN Parameters

IN parameters pass values into the stored procedure:

**Script Syntax:**

```js
bx:storedProc
    procedure="sp_GetEmployeesByDept"
    datasource="myDB" {

    bx:procParam
        type="in"
        cfsqltype="varchar"
        value=department;

    bx:procResult name="employees" resultset="1";
}
```

**Template Syntax:**

```xml
<bx:storedProc
    procedure="sp_GetEmployeesByDept"
    datasource="myDB">

    <bx:procParam
        type="in"
        cfsqltype="varchar"
        value="#department#" />

    <bx:procResult name="employees" resultset="1" />
</bx:storedProc>
```

### IN Parameter with NULL

**Script Syntax:**

```js
bx:storedProc procedure="sp_SearchEmployees" datasource="myDB" {
    bx:procParam
        type="in"
        cfsqltype="varchar"
        value=searchTerm
        null=isNull( searchTerm );

    bx:procResult name="results" resultset="1";
}
```

**Template Syntax:**

```xml
<bx:storedProc procedure="sp_SearchEmployees" datasource="myDB">
    <bx:procParam
        type="in"
        cfsqltype="varchar"
        value="#searchTerm#"
        null="#isNull( searchTerm )#" />

    <bx:procResult name="results" resultset="1" />
</bx:storedProc>
```

## 📤 OUT Parameters

OUT parameters retrieve values from the stored procedure:

**Script Syntax:**

```js
bx:storedProc
    procedure="sp_CreateEmployee"
    datasource="myDB"
    result="procResult" {

    // IN parameters
    bx:procParam type="in" cfsqltype="varchar" value=firstName;
    bx:procParam type="in" cfsqltype="varchar" value=lastName;
    bx:procParam type="in" cfsqltype="varchar" value=email;

    // OUT parameter to get new employee ID
    bx:procParam
        type="out"
        cfsqltype="integer"
        variable="newEmployeeId";
}

// Access the OUT parameter value
writeOutput( "New employee created with ID: #newEmployeeId#" );
```

**Template Syntax:**

```xml
<bx:storedProc
    procedure="sp_CreateEmployee"
    datasource="myDB"
    result="procResult">

    <!-- IN parameters -->
    <bx:procParam type="in" cfsqltype="varchar" value="#firstName#" />
    <bx:procParam type="in" cfsqltype="varchar" value="#lastName#" />
    <bx:procParam type="in" cfsqltype="varchar" value="#email#" />

    <!-- OUT parameter to get new employee ID -->
    <bx:procParam
        type="out"
        cfsqltype="integer"
        variable="newEmployeeId" />
</bx:storedProc>

<!-- Access the OUT parameter value -->
<bx:output>
    New employee created with ID: #newEmployeeId#
</bx:output>
```

## 🔄 INOUT Parameters

INOUT parameters can pass values in AND retrieve values out:

**Script Syntax:**

```js
bx:storedProc
    procedure="sp_UpdateInventory"
    datasource="myDB" {

    bx:procParam type="in" cfsqltype="integer" value=productId;

    // INOUT parameter - pass in quantity, get back new total
    bx:procParam
        type="inout"
        cfsqltype="integer"
        value=quantityChange
        variable="newTotal";
}

writeOutput( "New inventory total: #newTotal#" );
```

**Template Syntax:**

```xml
<bx:storedProc
    procedure="sp_UpdateInventory"
    datasource="myDB">

    <bx:procParam type="in" cfsqltype="integer" value="#productId#" />

    <!-- INOUT parameter - pass in quantity, get back new total -->
    <bx:procParam
        type="inout"
        cfsqltype="integer"
        value="#quantityChange#"
        variable="newTotal" />
</bx:storedProc>

<bx:output>
    New inventory total: #newTotal#
</bx:output>
```

## 📊 Multiple Result Sets

Capture multiple result sets returned by a single procedure:

**Script Syntax:**

```js
bx:storedProc
    procedure="sp_GetEmployeeDetails"
    datasource="myDB" {

    bx:procParam type="in" cfsqltype="integer" value=employeeId;

    // First result set: Employee basic info
    bx:procResult name="employeeInfo" resultset="1";

    // Second result set: Employee orders
    bx:procResult name="employeeOrders" resultset="2";

    // Third result set: Employee reviews
    bx:procResult name="employeeReviews" resultset="3";
}

// Access each result set
writeOutput( "<h2>#employeeInfo.firstName# #employeeInfo.lastName#</h2>" );

writeOutput( "<h3>Orders (#employeeOrders.recordCount#)</h3>" );
for ( order in employeeOrders ) {
    writeOutput( "<p>Order #order.orderId#: #order.total#</p>" );
}

writeOutput( "<h3>Reviews (#employeeReviews.recordCount#)</h3>" );
for ( review in employeeReviews ) {
    writeOutput( "<p>Rating: #review.rating# - #review.reviewText#</p>" );
}
```

**Template Syntax:**

```xml
<bx:storedProc
    procedure="sp_GetEmployeeDetails"
    datasource="myDB">

    <bx:procParam type="in" cfsqltype="integer" value="#employeeId#" />

    <!-- First result set: Employee basic info -->
    <bx:procResult name="employeeInfo" resultset="1" />

    <!-- Second result set: Employee orders -->
    <bx:procResult name="employeeOrders" resultset="2" />

    <!-- Third result set: Employee reviews -->
    <bx:procResult name="employeeReviews" resultset="3" />
</bx:storedProc>

<!-- Access each result set -->
<h2>#employeeInfo.firstName# #employeeInfo.lastName#</h2>

<h3>Orders (#employeeOrders.recordCount#)</h3>
<bx:output query="employeeOrders">
    <p>Order #orderId#: #total#</p>
</bx:output>

<h3>Reviews (#employeeReviews.recordCount#)</h3>
<bx:output query="employeeReviews">
    <p>Rating: #rating# - #reviewText#</p>
</bx:output>
```

## 🔢 Return Codes

Capture the return code (status) from a stored procedure:

**Script Syntax:**

```js
bx:storedProc
    procedure="sp_ValidateLogin"
    datasource="myDB"
    returnCode="true"
    result="procResult" {

    bx:procParam type="in" cfsqltype="varchar" value=username;
    bx:procParam type="in" cfsqltype="varchar" value=password;

    bx:procParam type="out" cfsqltype="varchar" variable="message";

    bx:procResult name="userData" resultset="1";
}

// Check the return code
if ( procResult.statusCode == 0 ) {
    writeOutput( "<p>Login successful! Welcome #userData.firstName#</p>" );
} else {
    writeOutput( "<p>Login failed: #message#</p>" );
}
```

**Template Syntax:**

```xml
<bx:storedProc
    procedure="sp_ValidateLogin"
    datasource="myDB"
    returnCode="true"
    result="procResult">

    <bx:procParam type="in" cfsqltype="varchar" value="#username#" />
    <bx:procParam type="in" cfsqltype="varchar" value="#password#" />

    <bx:procParam type="out" cfsqltype="varchar" variable="message" />

    <bx:procResult name="userData" resultset="1" />
</bx:storedProc>

<!-- Check the return code -->
<bx:if condition="#procResult.statusCode == 0#">
    <p>Login successful! Welcome #userData.firstName#</p>
<bx:else>
    <p>Login failed: #message#</p>
</bx:if>
```

## 🎯 Complete Example

Here's a comprehensive example showing all features:

**Script Syntax:**

```js
bx:storedProc
    procedure="sp_ProcessOrder"
    datasource="myDB"
    returnCode="true"
    debug="true"
    result="procInfo" {

    // IN parameters
    bx:procParam type="in" cfsqltype="integer" value=customerId;
    bx:procParam type="in" cfsqltype="decimal" value=orderAmount scale="2";
    bx:procParam type="in" cfsqltype="varchar" value=shippingAddress maxLength="255";
    bx:procParam type="in" cfsqltype="date" value=orderDate;

    // OUT parameters
    bx:procParam type="out" cfsqltype="integer" variable="newOrderId";
    bx:procParam type="out" cfsqltype="varchar" variable="confirmationCode";
    bx:procParam type="out" cfsqltype="varchar" variable="errorMessage";

    // Result sets
    bx:procResult name="orderDetails" resultset="1";
    bx:procResult name="orderItems" resultset="2";
}

// Check execution status
if ( procInfo.statusCode == 0 ) {
    writeOutput( "<h2>Order Confirmed!</h2>" );
    writeOutput( "<p>Order ID: #newOrderId#</p>" );
    writeOutput( "<p>Confirmation Code: #confirmationCode#</p>" );
    writeOutput( "<p>Execution Time: #procInfo.executionTime# ms</p>" );

    writeOutput( "<h3>Order Details</h3>" );
    writeDump( orderDetails );

    writeOutput( "<h3>Order Items</h3>" );
    for ( item in orderItems ) {
        writeOutput( "<p>#item.productName#: #item.quantity# x #item.price#</p>" );
    }
} else {
    writeOutput( "<p class='error'>Order failed: #errorMessage#</p>" );
}
```

**Template Syntax:**

```xml
<bx:storedProc
    procedure="sp_ProcessOrder"
    datasource="myDB"
    returnCode="true"
    debug="true"
    result="procInfo">

    <!-- IN parameters -->
    <bx:procParam type="in" cfsqltype="integer" value="#customerId#" />
    <bx:procParam type="in" cfsqltype="decimal" value="#orderAmount#" scale="2" />
    <bx:procParam type="in" cfsqltype="varchar" value="#shippingAddress#" maxLength="255" />
    <bx:procParam type="in" cfsqltype="date" value="#orderDate#" />

    <!-- OUT parameters -->
    <bx:procParam type="out" cfsqltype="integer" variable="newOrderId" />
    <bx:procParam type="out" cfsqltype="varchar" variable="confirmationCode" />
    <bx:procParam type="out" cfsqltype="varchar" variable="errorMessage" />

    <!-- Result sets -->
    <bx:procResult name="orderDetails" resultset="1" />
    <bx:procResult name="orderItems" resultset="2" />
</bx:storedProc>

<!-- Check execution status -->
<bx:if condition="#procInfo.statusCode == 0#">
    <h2>Order Confirmed!</h2>
    <p>Order ID: #newOrderId#</p>
    <p>Confirmation Code: #confirmationCode#</p>
    <p>Execution Time: #procInfo.executionTime# ms</p>

    <h3>Order Details</h3>
    <bx:dump var="#orderDetails#" />

    <h3>Order Items</h3>
    <bx:output query="orderItems">
        <p>#productName#: #quantity# x #price#</p>
    </bx:output>
<bx:else>
    <p class="error">Order failed: #errorMessage#</p>
</bx:if>
```

## 🛠️ Component Attributes

### bx:storedProc Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `procedure` | string | Yes | Name of the stored procedure to execute |
| `datasource` | string | No | Datasource name (uses default if not specified) |
| `result` | string | No | Variable name to store execution metadata (default: "bxstoredproc") |
| `returnCode` | boolean | No | Capture procedure return code (default: false) |
| `debug` | boolean | No | Enable debug output (default: false) |
| `username` | string | No | Override datasource username |
| `password` | string | No | Override datasource password |

### bx:procParam Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `type` | string | Yes | Parameter type: "in", "out", or "inout" |
| `cfsqltype` | string | Yes | SQL data type |
| `value` | any | Conditional | Parameter value (required for IN and INOUT) |
| `variable` | string | Conditional | Variable name for OUT/INOUT results |
| `null` | boolean | No | Set to true for NULL values (default: false) |
| `maxLength` | integer | No | Maximum length for string types |
| `scale` | integer | No | Decimal scale for numeric types |

### bx:procResult Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Variable name to store result set |
| `resultset` | integer | Yes | Result set number (1-based) |

## 📝 SQL Data Types

Common `cfsqltype` values for parameters:

| SQL Type | Description | BoxLang Type |
|----------|-------------|--------------|
| `varchar` | Variable-length string | String |
| `char` | Fixed-length string | String |
| `integer` | 32-bit integer | Numeric |
| `bigint` | 64-bit integer | Numeric |
| `decimal` | Fixed-point number | Numeric |
| `numeric` | Fixed-point number | Numeric |
| `float` | Floating-point number | Numeric |
| `double` | Double precision float | Numeric |
| `bit` | Boolean value | Boolean |
| `date` | Date only | Date/DateTime |
| `time` | Time only | Date/DateTime |
| `timestamp` | Date and time | Date/DateTime |
| `binary` | Binary data | Binary |
| `blob` | Large binary object | Binary |
| `clob` | Large character object | String |

## 🗄️ Database-Specific Examples

### MySQL

**Script Syntax:**

```js
bx:storedProc procedure="sp_GetCustomerOrders" datasource="mysqlDB" {
    bx:procParam type="in" cfsqltype="integer" value=customerId;
    bx:procResult name="orders" resultset="1";
}
```

**Template Syntax:**

```xml
<bx:storedProc procedure="sp_GetCustomerOrders" datasource="mysqlDB">
    <bx:procParam type="in" cfsqltype="integer" value="#customerId#" />
    <bx:procResult name="orders" resultset="1" />
</bx:storedProc>
```

### PostgreSQL

**Script Syntax:**

```js
bx:storedProc procedure="get_employee_stats" datasource="postgresDB" {
    bx:procParam type="in" cfsqltype="integer" value=departmentId;
    bx:procParam type="out" cfsqltype="integer" variable="totalEmployees";
    bx:procParam type="out" cfsqltype="decimal" variable="avgSalary";
    bx:procResult name="stats" resultset="1";
}
```

**Template Syntax:**

```xml
<bx:storedProc procedure="get_employee_stats" datasource="postgresDB">
    <bx:procParam type="in" cfsqltype="integer" value="#departmentId#" />
    <bx:procParam type="out" cfsqltype="integer" variable="totalEmployees" />
    <bx:procParam type="out" cfsqltype="decimal" variable="avgSalary" />
    <bx:procResult name="stats" resultset="1" />
</bx:storedProc>
```

### SQL Server

**Script Syntax:**

```js
bx:storedProc
    procedure="sp_UpdateInventory"
    datasource="mssqlDB"
    returnCode="true"
    result="procResult" {

    bx:procParam type="in" cfsqltype="integer" value=productId;
    bx:procParam type="in" cfsqltype="integer" value=quantity;
    bx:procParam type="out" cfsqltype="integer" variable="newQuantity";
    bx:procParam type="out" cfsqltype="varchar" variable="statusMessage";
}

if ( procResult.statusCode == 0 ) {
    writeOutput( "<p>Inventory updated: #statusMessage#</p>" );
    writeOutput( "<p>New quantity: #newQuantity#</p>" );
}
```

**Template Syntax:**

```xml
<bx:storedProc
    procedure="sp_UpdateInventory"
    datasource="mssqlDB"
    returnCode="true"
    result="procResult">

    <bx:procParam type="in" cfsqltype="integer" value="#productId#" />
    <bx:procParam type="in" cfsqltype="integer" value="#quantity#" />
    <bx:procParam type="out" cfsqltype="integer" variable="newQuantity" />
    <bx:procParam type="out" cfsqltype="varchar" variable="statusMessage" />
</bx:storedProc>

<bx:if condition="#procResult.statusCode == 0#">
    <p>Inventory updated: #statusMessage#</p>
    <p>New quantity: #newQuantity#</p>
</bx:if>
```

### Oracle

**Script Syntax:**

```js
bx:storedProc
    procedure="pkg_orders.process_order"
    datasource="oracleDB"
    returnCode="true" {

    bx:procParam type="in" cfsqltype="integer" value=orderId;
    bx:procParam type="inout" cfsqltype="varchar" value=status variable="newStatus";
    bx:procParam type="out" cfsqltype="integer" variable="errorCode";

    bx:procResult name="orderDetails" resultset="1";
}
```

**Template Syntax:**

```xml
<bx:storedProc
    procedure="pkg_orders.process_order"
    datasource="oracleDB"
    returnCode="true">

    <bx:procParam type="in" cfsqltype="integer" value="#orderId#" />
    <bx:procParam type="inout" cfsqltype="varchar" value="#status#" variable="newStatus" />
    <bx:procParam type="out" cfsqltype="integer" variable="errorCode" />

    <bx:procResult name="orderDetails" resultset="1" />
</bx:storedProc>
```

## 💡 Best Practices

### Security
- ✅ **Use stored procedures** for complex business logic
- ✅ **Validate parameters** before passing to procedures
- ✅ **Limit database permissions** to only required procedures
- ✅ **Handle OUT parameters** carefully to avoid information disclosure

### Error Handling
- ✅ **Always check return codes** when `returnCode="true"`
- ✅ **Wrap procedure calls** in try/catch blocks
- ✅ **Capture error messages** via OUT parameters
- ✅ **Log procedure execution** for debugging

### Performance
- ✅ **Use procedures** for complex multi-query operations
- ✅ **Minimize result sets** - only return needed data
- ✅ **Index procedure parameters** in the database
- ✅ **Monitor execution time** with `result` metadata

### Code Quality
- ✅ **Document parameter purpose** with comments
- ✅ **Use consistent naming** for variables
- ✅ **Handle NULL values** explicitly
- ✅ **Test with edge cases** (empty results, NULLs, errors)

## 🚫 Common Pitfalls

❌ **Forgetting to specify resultset numbers**
```xml
<!-- BAD - missing resultset attribute -->
<bx:procResult name="data" />

<!-- GOOD -->
<bx:procResult name="data" resultset="1" />
```

❌ **Not handling NULL values**
```xml
<!-- BAD - will fail if variable is null -->
<bx:procParam type="in" cfsqltype="varchar" value="#maybeNull#" />

<!-- GOOD -->
<bx:procParam
    type="in"
    cfsqltype="varchar"
    value="#maybeNull#"
    null="#isNull( maybeNull )#" />
```

❌ **Ignoring return codes**
```xml
<!-- BAD - no error checking -->
<bx:storedProc procedure="sp_CriticalOperation" returnCode="true">
    ...
</bx:storedProc>

<!-- GOOD - check for errors -->
<bx:storedProc
    procedure="sp_CriticalOperation"
    returnCode="true"
    result="procResult">
    ...
</bx:storedProc>

<bx:if condition="#procResult.statusCode != 0#">
    <bx:throw message="Procedure failed with code: #procResult.statusCode#" />
</bx:if>
```

## 🔗 Related Documentation

- [Datasources](datasources.md) - Configure database connections
- [Querying](querying.md) - Execute SQL queries
- [Transactions](transactions.md) - Manage database transactions
- [bx:storedProc Component](../../boxlang-language/reference/components/jdbc/StoredProc.md) - Complete reference
- [bx:procParam Component](../../boxlang-language/reference/components/jdbc/ProcParam.md) - Parameter reference
- [bx:procResult Component](../../boxlang-language/reference/components/jdbc/ProcResult.md) - Result capture reference
