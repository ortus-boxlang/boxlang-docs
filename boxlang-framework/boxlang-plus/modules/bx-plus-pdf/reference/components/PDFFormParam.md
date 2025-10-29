
# Component: `PDFFormParam`

--------------------------------------------------------------------------
 _invoke()
 --------------------------------------------------------------------------
 Provides additional information to the PDFForm component.

 {% hint style="danger" %}
This component is only available to [Boxlang+/++ subscribers only](https://ww.boxlang.io/plans) but can be installed in conjunction with the [`bx-plus` Module](https://forgebox.io/view/bx-plus) with a limited trial.
{% endhint %}

## Component Signature

```
<bx:PDFFormParam name=[string]
value=[string]
index=[integer] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | String - The field name on the PDF form.<br>                 Required. |  |
| `value` | `string` | `true` | String - The value to associate with the field name.<br>                  For interactive fields, specify a ColdFusion variable.<br>                  Required. |  |
| `index` | `integer` | `false` | Integer - Index associated with the field name. If multiple<br>                  fields have the same name, use the index value to locate one of them.<br>                  Applies to forms created in LiveCycle only. Forms created in Acrobat<br>                  cannot contain more than one field with the same name.<br>                  Default: 1 | `1` |

## Examples

### Basic Field Population

```js
<bx:pdfform action="populate" 
            source="employee-form.pdf"
            destination="john-doe-form.pdf">
    <bx:pdfformparam name="firstName" value="John" />
    <bx:pdfformparam name="lastName" value="Doe" />
    <bx:pdfformparam name="employeeId" value="12345" />
    <bx:pdfformparam name="department" value="Engineering" />
    <bx:pdfformparam name="startDate" value="2024-01-15" />
</bx:pdfform>
```

### Dynamic Value Population

```js
<bx:set employee = {
    "id": "67890",
    "name": "Jane Smith", 
    "email": "jane.smith@company.com",
    "phone": "555-0123",
    "hireDate": "2024-02-01"
} />

<bx:pdfform action="populate"
            source="contact-form.pdf" 
            destination="jane-contact-form.pdf">
    <bx:pdfformparam name="employeeId" value="#employee.id#" />
    <bx:pdfformparam name="fullName" value="#employee.name#" />
    <bx:pdfformparam name="email" value="#employee.email#" />
    <bx:pdfformparam name="phoneNumber" value="#employee.phone#" />
    <bx:pdfformparam name="dateHired" value="#dateFormat(employee.hireDate, 'mm/dd/yyyy')#" />
</bx:pdfform>
```

### Checkbox and Boolean Fields

```js
<bx:pdfform action="populate"
            source="preferences-form.pdf"
            destination="user-preferences.pdf">
    <bx:pdfformparam name="newsletter" value="true" />
    <bx:pdfformparam name="notifications" value="false" />
    <bx:pdfformparam name="marketing" value="true" />
    <bx:pdfformparam name="surveys" value="false" />
</bx:pdfform>
```

### Multiple Fields with Same Name (LiveCycle Forms)

```js
<!-- For LiveCycle forms with repeating sections -->
<bx:pdfform action="populate"
            source="invoice-template.pdf"
            destination="customer-invoice.pdf">
    
    <!-- First line item -->
    <bx:pdfformparam name="itemDescription" value="Web Development Services" index="1" />
    <bx:pdfformparam name="itemQuantity" value="40" index="1" />
    <bx:pdfformparam name="itemRate" value="150.00" index="1" />
    
    <!-- Second line item -->
    <bx:pdfformparam name="itemDescription" value="Database Design" index="2" />
    <bx:pdfformparam name="itemQuantity" value="20" index="2" />
    <bx:pdfformparam name="itemRate" value="175.00" index="2" />
    
    <!-- Third line item -->
    <bx:pdfformparam name="itemDescription" value="Testing & QA" index="3" />
    <bx:pdfformparam name="itemQuantity" value="15" index="3" />
    <bx:pdfformparam name="itemRate" value="125.00" index="3" />
</bx:pdfform>
```

### Complex Form with Calculations

```js
<bx:set orderData = {
    "items": [
        {"name": "Laptop", "price": 1299.99, "qty": 2},
        {"name": "Mouse", "price": 29.99, "qty": 3},
        {"name": "Keyboard", "price": 89.99, "qty": 1}
    ],
    "taxRate": 0.08,
    "shipping": 15.00
} />

<bx:set subtotal = 0 />
<bx:loop array="#orderData.items#" index="i" item="product">
    <bx:set subtotal += product.price * product.qty />
</bx:loop>
<bx:set tax = subtotal * orderData.taxRate />
<bx:set total = subtotal + tax + orderData.shipping />

<bx:pdfform action="populate"
            source="order-form.pdf"
            destination="customer-order.pdf">
    
    <!-- Customer info -->
    <bx:pdfformparam name="orderDate" value="#dateFormat(now(), 'mm/dd/yyyy')#" />
    <bx:pdfformparam name="orderNumber" value="ORD-#randRange(10000, 99999)#" />
    
    <!-- Line items -->
    <bx:loop array="#orderData.items#" index="i" item="product">
        <bx:pdfformparam name="itemName" value="#product.name#" index="#i#" />
        <bx:pdfformparam name="itemPrice" value="#dollarFormat(product.price)#" index="#i#" />
        <bx:pdfformparam name="itemQty" value="#product.qty#" index="#i#" />
        <bx:pdfformparam name="lineTotal" value="#dollarFormat(product.price * product.qty)#" index="#i#" />
    </bx:loop>
    
    <!-- Totals -->
    <bx:pdfformparam name="subtotal" value="#dollarFormat(subtotal)#" />
    <bx:pdfformparam name="tax" value="#dollarFormat(tax)#" />
    <bx:pdfformparam name="shipping" value="#dollarFormat(orderData.shipping)#" />
    <bx:pdfformparam name="grandTotal" value="#dollarFormat(total)#" />
</bx:pdfform>
```

### Date and Time Formatting

```js
<bx:pdfform action="populate"
            source="appointment-form.pdf"
            destination="scheduled-appointment.pdf">
    <bx:pdfformparam name="appointmentDate" value="#dateFormat(now(), 'mm/dd/yyyy')#" />
    <bx:pdfformparam name="appointmentTime" value="#timeFormat(now(), 'h:mm tt')#" />
    <bx:pdfformparam name="createdDateTime" value="#dateTimeFormat(now(), 'mm/dd/yyyy h:mm tt')#" />
    <bx:pdfformparam name="expiryDate" value="#dateFormat(dateAdd('d', 30, now()), 'mm/dd/yyyy')#" />
</bx:pdfform>
```

### Conditional Field Population

```js
<bx:set userRole = "admin" />

<bx:pdfform action="populate"
            source="access-request.pdf" 
            destination="user-access-request.pdf">
    
    <bx:pdfformparam name="userName" value="John Administrator" />
    <bx:pdfformparam name="requestDate" value="#dateFormat(now(), 'mm/dd/yyyy')#" />
    
    <!-- Conditional access levels based on role -->
    <bx:if userRole eq "admin">
        <bx:pdfformparam name="systemAccess" value="true" />
        <bx:pdfformparam name="dataAccess" value="true" />
        <bx:pdfformparam name="userManagement" value="true" />
        <bx:pdfformparam name="accessLevel" value="Full Administrative" />
    <bx:elseif userRole eq "manager">
        <bx:pdfformparam name="systemAccess" value="true" />
        <bx:pdfformparam name="dataAccess" value="true" />
        <bx:pdfformparam name="userManagement" value="false" />
        <bx:pdfformparam name="accessLevel" value="Management" />
    <bx:else>
        <bx:pdfformparam name="systemAccess" value="false" />
        <bx:pdfformparam name="dataAccess" value="false" />
        <bx:pdfformparam name="userManagement" value="false" />
        <bx:pdfformparam name="accessLevel" value="Standard User" />
    </bx:if>
</bx:pdfform>
```

## Field Naming Best Practices

- Use consistent, descriptive field names
- Avoid special characters in field names  
- For repeating sections, use index values consistently
- Test field names by reading the form structure first

## Related Components

- [PDFForm](PDFForm.md) - Main PDF form manipulation component
- [PDF](PDF.md) - General PDF manipulation component


