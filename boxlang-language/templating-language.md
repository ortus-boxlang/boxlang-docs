---
description: Create dynamic templates with BoxLang's powerful templating language for HTML generation, views, and content rendering
icon: code
---

# Templating Language

BoxLang includes a powerful templating language designed for creating dynamic HTML, views, and content rendering. Template files use the `.bxm` extension and provide a natural way to mix static content with dynamic BoxLang code.

## 📄 Template File Structure

Template files (`.bxm`) are designed for content generation and HTML output. Unlike script files (`.bxs`) or class files (`.bx`), templates default to outputting content directly, making them ideal for views, email templates, and dynamic HTML generation.

```xml
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to BoxLang</title>
</head>
<body>
    <h1>Hello, #name#!</h1>
    <p>Today is #dateFormat( now(), "full" )#</p>
</body>
</html>
```

## 🔤 Output Interpolation

BoxLang templates use the `#` (hash/pound) character for output interpolation. Any expression wrapped in `#` symbols will be evaluated and output to the page.

### Basic Interpolation

```xml
<bx:set greeting = "Hello, World!">
<p>#greeting#</p>
<p>Current time: #now()#</p>
<p>Random number: #randRange( 1, 100 )#</p>
```

### Escaping Hash Symbols

To output a literal `#` character without evaluation, use double hashes `##`:

```xml
<p>Use ## for hash symbols in CSS: ##header { color: blue; }</p>
<p>This outputs: # for hash symbols in CSS: #header { color: blue; }</p>
```

### Complex Expressions

You can use any BoxLang expression within interpolation:

```xml
<bx:set products = [ "Laptop", "Mouse", "Keyboard" ]>
<p>We have #products.len()# products</p>
<p>First product: #products[1]#</p>
<p>Total price: #calculateTotal( products )#</p>
```

## 🏷️ Template Components

BoxLang provides a rich set of template components using the `bx:` prefix. All template components follow XML-like syntax with opening and closing tags or self-closing syntax.

### Common Template Components

#### bx:output

The `bx:output` component enables output of dynamic content and expressions. Within `bx:output`, the `#` interpolation is automatically enabled.

```xml
<bx:output>
    <h1>Welcome, #user.name#!</h1>
    <p>Your account was created on #dateFormat( user.created, "long" )#</p>
</bx:output>
```

#### bx:set

Define variables in templates using `bx:set`:

```xml
<bx:set userName = "Luis Majano">
<bx:set userAge = 25>
<bx:set userInfo = { name: userName, age: userAge }>
```

#### bx:script

Execute BoxLang script code within a template:

```xml
<bx:script>
    users = queryExecute( "SELECT * FROM users" )
    totalUsers = users.recordCount
    activeUsers = users.filter( ( row ) => row.active == true ).len()
</bx:script>

<bx:output>
    <p>Total Users: #totalUsers#</p>
    <p>Active Users: #activeUsers#</p>
</bx:output>
```

#### bx:if, bx:elseif, bx:else

Conditional rendering in templates:

```xml
<bx:set role = "admin">

<bx:if role == "admin">
    <div class="admin-panel">Admin Dashboard</div>
<bx:elseif role == "editor">
    <div class="editor-panel">Editor Dashboard</div>
<bx:else>
    <div class="user-panel">User Dashboard</div>
</bx:if>
```

#### bx:loop

Iterate over arrays, queries, structures, and ranges:

```xml
<!--- Loop over an array --->
<bx:set fruits = [ "Apple", "Banana", "Orange" ]>
<ul>
<bx:loop array="#fruits#" index="fruit">
    <li>#fruit#</li>
</bx:loop>
</ul>

<!--- Loop over a query --->
<bx:set users = queryNew( "id,name", "integer,varchar", [ [1,"John"], [2,"Jane"] ] )>
<table>
<bx:loop query="#users#">
    <tr>
        <td>#users.id#</td>
        <td>#users.name#</td>
    </tr>
</bx:loop>
</table>

<!--- Loop over a range --->
<bx:loop from="1" to="5" index="i">
    <p>Item #i#</p>
</bx:loop>
```

#### bx:include

Include other template files:

```xml
<!--- Include a header template --->
<bx:include template="layouts/header.bxm">

<main>
    <h1>Page Content</h1>
</main>

<!--- Include a footer template --->
<bx:include template="layouts/footer.bxm">
```

## 🔄 Mixing Scripts and Templates

BoxLang allows seamless mixing of script and template syntax within the same file.

### Scripts in Templates

Use `<bx:script>` to embed BoxLang script code within a template:

```xml
<h1>User Report</h1>

<bx:script>
    // Fetch data using script syntax
    users = queryExecute( "SELECT * FROM users WHERE active = ?", [ true ] )
    
    // Process data
    stats = {
        total: users.recordCount,
        admins: 0,
        users: 0
    }
    
    users.each( ( row ) => {
        if( row.role == "admin" ) {
            stats.admins++
        } else {
            stats.users++
        }
    } )
</bx:script>

<bx:output>
    <p>Total: #stats.total#</p>
    <p>Admins: #stats.admins#</p>
    <p>Users: #stats.users#</p>
</bx:output>
```

### Templates in Scripts

In script files (`.bxs`), you can embed template code using template island notation with triple backticks (` ``` `):

````javascript
// This is a .bxs script file
users = [
    { name: "John", age: 30 },
    { name: "Jane", age: 25 }
]

// Now switch to template syntax
```
<h1>Users List</h1>
<bx:output>
    <ul>
    <bx:loop array="#users#" item="user">
        <li>#user.name# - #user.age# years old</li>
    </bx:loop>
    </ul>
</bx:output>
```

// Back to script syntax
println( "Template rendered successfully" )
````

## 🎯 Component Execution

BoxLang templates can execute any BoxLang component using the `bx:` prefix followed by the component name. The runtime automatically resolves and executes the component.

### Built-in Components

BoxLang includes many built-in components for common tasks:

```xml
<!--- Query database --->
<bx:query name="users" datasource="myDB">
    SELECT id, name, email FROM users WHERE active = 1
</bx:query>

<!--- HTTP request --->
<bx:http url="https://api.example.com/data" method="GET" result="apiResponse">

<!--- File operations --->
<bx:file action="read" file="/path/to/file.txt" variable="fileContent">

<!--- Directory listing --->
<bx:directory action="list" directory="/uploads" name="files" recurse="true">

<!--- Thread for async execution --->
<bx:thread action="run" name="backgroundTask">
    // Long running task here
</bx:thread>
```

### Custom Components

You can also invoke your own custom components in templates:

```xml
<!--- Assuming you have a custom component at models/EmailService.bx --->
<bx:set emailService = new models.EmailService()>
<bx:invoke component="#emailService#" method="sendWelcomeEmail" user="#currentUser#">
```

## 💡 Practical Examples

### Dynamic HTML Page

```xml
<!DOCTYPE html>
<html>
<head>
    <title>#pageTitle#</title>
</head>
<body>
    <bx:set currentDate = now()>
    <bx:set userName = session.userName ?: "Guest">
    
    <header>
        <h1>Welcome, #userName#!</h1>
        <p>Today is #dateFormat( currentDate, "full" )#</p>
    </header>
    
    <bx:if structKeyExists( session, "userId" )>
        <nav>
            <ul>
                <li><a href="/dashboard">Dashboard</a></li>
                <li><a href="/profile">Profile</a></li>
                <li><a href="/logout">Logout</a></li>
            </ul>
        </nav>
    <bx:else>
        <nav>
            <ul>
                <li><a href="/login">Login</a></li>
                <li><a href="/register">Register</a></li>
            </ul>
        </nav>
    </bx:if>
    
    <main>
        <bx:include template="content/#page#.bxm">
    </main>
    
    <footer>
        <p>&copy; #year( currentDate )# My Company. All rights reserved.</p>
    </footer>
</body>
</html>
```

### Data Table with Query

```xml
<bx:script>
    // Fetch products from database
    products = queryExecute(
        "SELECT id, name, price, category FROM products WHERE active = :active ORDER BY name",
        { active: true }
    )
</bx:script>

<h1>Product Catalog</h1>

<bx:if products.recordCount GT 0>
    <table class="table">
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Category</th>
                <th>Price</th>
            </tr>
        </thead>
        <tbody>
            <bx:loop query="#products#">
                <tr>
                    <td>#products.id#</td>
                    <td>#products.name#</td>
                    <td>#products.category#</td>
                    <td>#dollarFormat( products.price )#</td>
                </tr>
            </bx:loop>
        </tbody>
    </table>
    <p>Showing #products.recordCount# products</p>
<bx:else>
    <p>No products found.</p>
</bx:if>
```

### Email Template

```xml
<!--- email/welcome.bxm --->
<bx:set userName = arguments.user.name>
<bx:set userEmail = arguments.user.email>
<bx:set activationLink = arguments.activationLink>

<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; }
        .button { 
            background-color: ##007bff; 
            color: white; 
            padding: 10px 20px; 
            text-decoration: none; 
        }
    </style>
</head>
<body>
    <h1>Welcome to Our Platform, #userName#!</h1>
    
    <p>Thank you for registering with email: <strong>#userEmail#</strong></p>
    
    <p>Please activate your account by clicking the button below:</p>
    
    <p>
        <a href="#activationLink#" class="button">Activate Account</a>
    </p>
    
    <p>Or copy this link: #activationLink#</p>
    
    <p>
        Best regards,<br>
        The Team
    </p>
</body>
</html>
```

### Form Processing

```xml
<h1>Contact Form</h1>

<bx:if structKeyExists( form, "submit" )>
    <bx:script>
        // Process form submission
        result = {
            success: false,
            message: ""
        }
        
        // Validate inputs
        if( len( trim( form.name ) ) == 0 || len( trim( form.email ) ) == 0 ) {
            result.message = "Name and email are required"
        } else if( !isValid( "email", form.email ) ) {
            result.message = "Please enter a valid email address"
        } else {
            // Save to database or send email
            queryExecute(
                "INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
                [ form.name, form.email, form.message ]
            )
            result.success = true
            result.message = "Thank you for contacting us!"
        }
    </bx:script>
    
    <bx:if result.success>
        <div class="alert alert-success">#result.message#</div>
    <bx:else>
        <div class="alert alert-error">#result.message#</div>
    </bx:if>
</bx:if>

<form method="post">
    <div>
        <label>Name:</label>
        <input type="text" name="name" value="#form.name ?: ''#" required>
    </div>
    <div>
        <label>Email:</label>
        <input type="email" name="email" value="#form.email ?: ''#" required>
    </div>
    <div>
        <label>Message:</label>
        <textarea name="message" required>#form.message ?: ''#</textarea>
    </div>
    <button type="submit" name="submit">Send Message</button>
</form>
```

## 🔒 Security Considerations

When outputting user-generated content or data from external sources, always encode the output to prevent XSS attacks:

```xml
<!--- Bad: No encoding --->
<p>#user.name#</p>

<!--- Good: HTML encoding --->
<p>#encodeForHTML( user.name )#</p>

<!--- For JavaScript context --->
<script>
    var userName = '#encodeForJavaScript( user.name )#'
</script>

<!--- For URL parameters --->
<a href="/profile?name=#encodeForURL( user.name )#">Profile</a>

<!--- Automatic encoding with bx:output encodefor attribute --->
<bx:output query="users" encodefor="html">
    <p>#users.name#</p>
    <p>#users.bio#</p>
</bx:output>
```

## 📚 Component Reference

For a complete list of available template components, see:

- [Components Reference](reference/components/)
- [Output Component](reference/components/system/Output.md)
- [Loop Component](reference/components/system/Loop.md)
- [Query Component](reference/components/jdbc/Query.md)
- [Include Component](reference/components/system/Include.md)

## 🎓 Best Practices

1. **Use templates for views**: Template files (`.bxm`) are ideal for HTML generation and views
2. **Keep logic in scripts**: Use `<bx:script>` or separate script files for complex business logic
3. **Encode output**: Always encode user-generated content using `encodeForHTML()` and related functions
4. **Organize includes**: Store reusable template fragments in a common directory structure
5. **Comment your templates**: Use `<!--- BoxLang comments --->` for documentation
6. **Use meaningful variable names**: Make your templates readable and maintainable

## 🔗 Related Documentation

- [Program Structure](program-structure.md)
- [Syntax & Semantics](syntax.md)
- [Components](reference/components/)
- [Built-in Functions](reference/built-in-functions/)
- [Variables and Scopes](variable-scopes.md)
