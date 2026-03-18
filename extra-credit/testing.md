---
description: >-
  TestBox is the Behavior/Test Driven Development testing/mocking framework for
  BoxLang.
icon: flask-vial
---

# Testing

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption><p>www.testbox.run</p></figcaption></figure>

### Table of Contents

1. [Why Testing Matters](https://claude.ai/chat/8804f97a-54e8-4212-8dbc-53377a26d039#why-testing-matters)
2. [Introduction to TestBox](https://claude.ai/chat/8804f97a-54e8-4212-8dbc-53377a26d039#introduction-to-testbox)
3. [Installation and Setup](https://claude.ai/chat/8804f97a-54e8-4212-8dbc-53377a26d039#installation-and-setup)
4. [BDD (Behavior Driven Development)](https://claude.ai/chat/8804f97a-54e8-4212-8dbc-53377a26d039#bdd-behavior-driven-development)
5. [TDD (Test Driven Development)](https://claude.ai/chat/8804f97a-54e8-4212-8dbc-53377a26d039#tdd-test-driven-development)
6. [Assertions and Expectations](https://claude.ai/chat/8804f97a-54e8-4212-8dbc-53377a26d039#assertions-and-expectations)
7. [Mocking and Stubbing](https://claude.ai/chat/8804f97a-54e8-4212-8dbc-53377a26d039#mocking-and-stubbing)
8. [Running Tests](https://claude.ai/chat/8804f97a-54e8-4212-8dbc-53377a26d039#running-tests)
9. [Advanced Testing Patterns](https://claude.ai/chat/8804f97a-54e8-4212-8dbc-53377a26d039#advanced-testing-patterns)
10. [Best Practices](https://claude.ai/chat/8804f97a-54e8-4212-8dbc-53377a26d039#best-practices)

### Why Testing Matters

Testing is not just a good practice—it's **imperative** for building reliable, maintainable BoxLang applications. Here's why:

#### **The Cost of Bugs**

* Bugs found in production are **10-100x more expensive** to fix than bugs caught during development
* Poor testing leads to brittle code that breaks with every change
* Manual testing is slow, error-prone, and doesn't scale

#### **Benefits of Automated Testing**

* **Confidence**: Deploy with certainty that your code works
* **Documentation**: Tests serve as living documentation of how your code should behave
* **Refactoring Safety**: Change code fearlessly, knowing tests will catch regressions
* **Faster Development**: Catch issues immediately instead of during manual testing cycles
* **Better Design**: Writing testable code forces better architecture

#### **Real-World Impact**

```javascript
// Without tests: "It works on my machine!"
function calculateDiscount( price, customerType ) {
    if ( customerType == "VIP" ) {
        return price * 0.8  // 20% discount
    }
    return price * 0.95  // 5% discount
}

// What happens when requirements change?
// What if price is negative? Zero? String?
// What about edge cases? You won't know until production!
```

**Bottom Line**: If you're not testing your BoxLang applications, you're essentially using your users as beta testers. TestBox makes testing so easy, there's no excuse not to do it.

### Introduction to TestBox

TestBox is a next-generation testing framework for the BoxLang JVM language, based on BDD (Behavior-Driven Development), providing a clean and obvious syntax for writing tests. It contains not only a testing framework, console/web runner, assertions, and expectations library, but also ships with several mocking utilities.

#### **What TestBox Provides**

**🧪 Testing Frameworks**

* **BDD (Behavior Driven Development)**: Focus on features and user stories
* **xUnit/TDD (Test Driven Development)**: Traditional unit testing approach

**🔍 Assertion Libraries**

* **Assertions**: Traditional boolean-based assertions
* **Expectations**: Fluent, readable assertion syntax

**🎭 Mocking Capabilities**

* Mock objects, methods, and properties
* Stub return values and behavior
* Verify method calls and interactions

**🏃‍♂️ Multiple Test Runners**

* CLI Runner (BoxLang native)
* Web Runner (browser-based)
* IDE Integration
* Continuous Integration support

**📊 Rich Reporting**

* Console output
* JSON, XML, JUnit formats
* HTML reports with visualizations
* Custom report formats

### Installation and Setup

#### **Installing TestBox**

The easiest way to get started with TestBox is through CommandBox, our CLI tool that connects to our package manager directory: [FORGEBOX](https://www.forgebox.io/)

```bash
# For web applications
box install testbox
```

#### **Project Structure**

Organize your tests with a clear structure:

```
/myproject
├── Application.bx
├── models/
│   └── UserService.bx
├── tests/
│   ├── Application.bx
│   ├── specs/
│   │   ├── integration/
│   │   │   └── UserServiceIntegrationSpec.bx
│   │   └── unit/
│   │       └── UserServiceSpec.bx
│   ├── resources/
│   │   └── BaseTest.bx
│   └── runner.bxm
└── box.json
```

#### **Root Application Configuration**

Create your main `Application.bx` at the root of your project:

```cfscript
class {
    /**
     * --------------------------------------------------------------------------
     * Application Properties: Modify as you see fit!
     * --------------------------------------------------------------------------
     */
    this.name                 = "My BoxLang Application"
    this.sessionManagement    = true
    this.sessionTimeout       = createTimespan( 0, 1, 0, 0 )
    this.setClientCookies     = true
    this.setDomainCookies     = true
    this.timezone             = "UTC"
    this.whiteSpaceManagement = "smart"
    
    /**
     * --------------------------------------------------------------------------
     * Java Integration
     * --------------------------------------------------------------------------
     */
    this.javaSettings = {
        loadPaths               : [ expandPath( "./lib/java" ) ],
        loadColdFusionClassPath : true,
        reloadOnChange          : false
    }
    
    /**
     * --------------------------------------------------------------------------
     * Location Mappings
     * --------------------------------------------------------------------------
     */
    this.mappings[ "/root" ]   = getDirectoryFromPath( getCurrentTemplatePath() )
    
    /**
     * --------------------------------------------------------------------------
     * ORM + Datasource Settings
     * --------------------------------------------------------------------------
     */
    this.datasource = "myDatasource"
    
    /**
     * Fires when the application starts
     */
    public boolean function onApplicationStart() {
        return true
    }
    
    /**
     * Fires when the application ends
     *
     * @appScope The app scope
     */
    public void function onApplicationEnd( struct appScope ) {
    }
    
    /**
     * Fires on every request
     *
     * @targetPage The requested page
     */
    public boolean function onRequestStart( string targetPage ) {
        return true
    }
    
    /**
     * Fires on every session start
     */
    public void function onSessionStart() {
    }
    
    /**
     * Fires on session end
     *
     * @sessionScope The session scope
     * @appScope     The app scope
     */
    public void function onSessionEnd( struct sessionScope, struct appScope ) {
    }
    
    /**
     * On missing template handler
     *
     * @template
     */
    public boolean function onMissingTemplate( template ) {
    }
}
```

#### **Basic Configuration**

Create a simple `tests/Application.bx` for your test suite:

```cfscript
class {
    this.name                 = "My Testing Suite"
    this.sessionManagement    = true
    this.setClientCookies     = true
    this.sessionTimeout       = createTimespan( 0, 0, 15, 0 )
    this.applicationTimeout   = createTimespan( 0, 0, 15, 0 )
    this.whiteSpaceManagement = "smart"
    
    /**
     * --------------------------------------------------------------------------
     * Location Mappings
     * --------------------------------------------------------------------------
     * - root : Quick reference to root application
     * - testbox : Where TestBox is installed
     */
    // Create testing mapping
    this.mappings[ "/tests" ]   = getDirectoryFromPath( getCurrentTemplatePath() )
    // The root application mapping
    rootPath                    = reReplaceNoCase( this.mappings[ "/tests" ], "tests(\\|/)", "" )
    this.mappings[ "/root" ]    = rootPath
    this.mappings[ "/testbox" ] = rootPath & "testbox"
    
    /**
     * Fires on every test request. It builds a Virtual application for you
     *
     * @targetPage The requested page
     */
    public boolean function onRequestStart( targetPage ) {
        // Set a high timeout for long running tests
        bx:setting requestTimeout = "9999";
        // Any global request start code
        
        return true
    }
}
```

### BDD (Behavior Driven Development)

BDD stands for Behavioral Driven Development. It is a software development process designed to enhance collaboration among developers, testers, and business stakeholders. BDD involves creating automated tests that are based on the expected behavior of the software, rather than just testing individual code components.

BDD focuses on **what** the software should do, not **how** it does it. You write specifications in human-readable language that describe features and expected behaviors.

#### **BDD Structure**

```cfscript
class extends="testbox.system.BaseSpec"{

    function run(){

        describe( "User Registration Feature", () => {
            
            beforeEach( () => {
                variables.userService = new models.UserService()
                variables.mockDB = createEmptyMock( "database" )
            } )
            
            describe( "When registering a new user", () => {
                
                it( "should create a user with valid data", () => {
                    // Given
                    var userData = {
                        email : "john@example.com",
                        password : "SecurePass123!",
                        firstName : "John",
                        lastName : "Doe"
                    }
                    
                    // When
                    var result = userService.register( userData )
                    
                    // Then
                    expect( result.success ).toBeTrue()
                    expect( result.user.email ).toBe( "john@example.com" )
                    expect( result.user.id ).toBeNumeric()
                } )
                
                it( "should reject invalid email addresses", () => {
                    var userData = {
                        email : "invalid-email",
                        password : "SecurePass123!",
                        firstName : "John",
                        lastName : "Doe"
                    }
                    
                    var result = userService.register( userData )
                    
                    expect( result.success ).toBeFalse()
                    expect( result.errors ).toHaveKey( "email" )
                    expect( result.errors.email ).toContain( "invalid" )
                } )
        
                it( "should hash passwords securely", () => {
                    var userData = {
                        email : "jane@example.com",
                        password : "MyPassword123!",
                        firstName : "Jane",
                        lastName : "Smith"
                    }
                    
                    var result = userService.register( userData )
                    
                    expect( result.user.password ).notToBe( "MyPassword123!" )
                    expect( len( result.user.password ) ).toBeGT( 50 ) // Hashed passwords are long
                } )
            } )
            
            describe( "Password validation", () => {
                
                it( "should require minimum length", () => {
                    expect( () => {
                        userService.validatePassword( "short" )
                    } ).toThrow( "ValidationException" )
                } )
                
                it( "should require special characters", () => {
                    var result = userService.validatePassword( "NoSpecialChars123" )
                    expect( result.valid ).toBeFalse()
                    expect( result.message ).toContain( "special character" )
                } )
            } )
        } )
        
    }

}
```

#### **Given-When-Then Syntax**

For even more readable tests, use the Given-When-Then pattern:

```cfscript
feature( "Shopping Cart Management", () => {
    
    scenario( "Adding items to cart", () => {
        
        given( "I have an empty shopping cart", () => {
            variables.cart = new models.ShoppingCart()
        } )
        
        when( "I add a valid product", () => {
            variables.product = {
                id : 123,
                name : "BoxLang Programming Book",
                price : 29.99
            }
            variables.result = cart.addItem( product, quantity = 2 )
        } )
        
        then( "the item should be in my cart", () => {
            expect( result.success ).toBeTrue()
            expect( cart.getItemCount() ).toBe( 2 )
            expect( cart.getTotal() ).toBe( 59.98 )
        } )
        
        then( "I should be able to remove the item", () => {
            cart.removeItem( product.id )
            expect( cart.getItemCount() ).toBe( 0 )
        } )
    } )
} )
```

#### **Story-Based Testing**

For integration tests, use stories to test complete user journeys:

```cfscript
story( "User can complete a purchase", () => {
    
    given( "a registered user with items in cart", () => {
        variables.user = createTestUser()
        variables.cart = createCartWithItems( user.id )
    } )
    
    given( "valid payment information", () => {
        variables.paymentInfo = {
            cardNumber : "4111111111111111",
            expiryMonth : 12,
            expiryYear : 2025,
            cvv : "123",
            billingAddress : createValidAddress()
        }
    } )
    
    then( "they can successfully complete checkout", () => {
        var result = checkoutService.processPayment( 
            cart = cart,
            paymentInfo = paymentInfo,
            user = user
        )
        
        expect( result.success ).toBeTrue()
        expect( result.orderId ).toBeNumeric()
        expect( result.confirmationEmail ).toHaveBeenSent()
    } )
} )
```

### TDD (Test Driven Development)

xUnit style of testing is the more traditional TDD or test-driven development approach, where you create a test case bundle class that matches the software under test, and for each method in the SUT, you create a test method in the test bundle class.

TDD follows the **Red-Green-Refactor** cycle:

1. **Red**: Write a failing test
2. **Green**: Write minimal code to make it pass
3. **Refactor**: Improve the code while keeping tests green

#### **xUnit Test Structure**

```cfscript
/**
 * Test suite for Calculator class
 * Demonstrates xUnit style testing with TestBox
 */
class extends="testbox.system.BaseSpec" {
    
    // Test subject
    property calculator
    
    /**
     * Setup run before each test
     */
    function setup() {
        calculator = new models.Calculator()
    }
    
    /**
     * Cleanup run after each test  
     */
    function teardown() {
        structDelete( variables, "calculator" )
    }
    
    /**
     * Test addition with positive numbers
     */
    function testAddPositiveNumbers() {
        var result = calculator.add( 5, 3 )
        $assertIsEqual( result, 8 )
    }
    
    /**
     * Test addition with negative numbers
     */
    function testAddNegativeNumbers() {
        var result = calculator.add( -5, -3 )
        $assertIsEqual( result, -8 )
    }
    
    /**
     * Test division by zero throws exception
     */
    @test
    @DisplayName( "Division by zero should throw exception" )
    function divisionByZeroShouldThrow() {
        expect( () => {
            calculator.divide( 10, 0 )
        } ).toThrow( "DivisionByZeroException" )
    }
    
    /**
     * Test complex calculation
     */
    function testComplexCalculation() {
        // Test the order of operations: 2 + 3 * 4 = 14
        var result = calculator.calculate( "2 + 3 * 4" )
        expect( result ).toBe( 14 )
    }
    
    /**
     * This test will be skipped
     */
    function testSkippedExample() skip {
        fail( "This test should not run" )
    }
}
```

#### **TDD Example: Building a URL Shortener**

Let's build a URL shortener using TDD. First, write the tests:

```cfscript
class extends="testbox.system.BaseSpec" {
    
    property urlShortener
    
    function setup() {
        urlShortener = new models.UrlShortener()
    }
    
    function testShortenValidUrl() {
        var longUrl = "https://www.example.com/very/long/path/to/resource"
        var shortCode = urlShortener.shorten( longUrl )
        
        expect( shortCode ).toBeString()
        expect( len( shortCode ) ).toBeLTE( 10 )
        expect( shortCode ).toMatch( "^[a-zA-Z0-9]+$" )
    }
    
    function testExpandShortCode() {
        var longUrl = "https://www.example.com/test"
        var shortCode = urlShortener.shorten( longUrl )
        var expandedUrl = urlShortener.expand( shortCode )
        
        expect( expandedUrl ).toBe( longUrl )
    }
    
    function testInvalidUrlThrowsException() {
        expect( () => {
            urlShortener.shorten( "not-a-valid-url" )
        } ).toThrow( "InvalidUrlException" )
    }
    
    function testNonExistentShortCode() {
        expect( () => {
            urlShortener.expand( "nonexistent" )
        } ).toThrow( "ShortCodeNotFoundException" )
    }
    
    function testDuplicateUrlReturnsSameCode() {
        var url = "https://www.example.com/duplicate"
        var shortCode1 = urlShortener.shorten( url )
        var shortCode2 = urlShortener.shorten( url )
        
        expect( shortCode1 ).toBe( shortCode2 )
    }
}
```

Now implement the `UrlShortener` class to make tests pass:

```cfscript
class {
    
    property urlMap = {}
    property codeMap = {}
    
    function init() {
        return this
    }
    
    function shorten( required string url ) {
        // Validate URL
        if ( !isValid( "url", url ) ) {
            throw( 
                type = "InvalidUrlException",
                message = "The provided URL is not valid: #url#"
            )
        }
        
        // Check if URL already exists
        if ( structKeyExists( urlMap, url ) ) {
            return urlMap[ url ]
        }
        
        // Generate short code
        var shortCode = generateShortCode()
        
        // Store mappings
        urlMap[ url ] = shortCode
        codeMap[ shortCode ] = url
        
        return shortCode
    }
    
    function expand( required string shortCode ) {
        if ( !structKeyExists( codeMap, shortCode ) ) {
            throw(
                type = "ShortCodeNotFoundException", 
                message = "Short code not found: #shortCode#"
            )
        }
        
        return codeMap[ shortCode ]
    }
    
    private function generateShortCode() {
        var chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        var shortCode = ""
        
        for ( var i = 1; i <= 6; i++ ) {
            var randomIndex = randRange( 1, len( chars ) )
            shortCode &= mid( chars, randomIndex, 1 )
        }
        
        // Ensure uniqueness
        if ( structKeyExists( codeMap, shortCode ) ) {
            return generateShortCode()
        }
        
        return shortCode
    }
}
```

#### **Life-Cycle Methods**

xUnit tests support several life-cycle methods:

```cfscript
class extends="testbox.system.BaseSpec" {
    
    /**
     * Run once before all tests in this bundle
     */
    function beforeTests() {
        // Setup expensive resources
        variables.database = connectToTestDatabase()
        variables.testData = loadTestData()
    }
    
    /**
     * Run once after all tests in this bundle
     */
    function afterTests() {
        // Cleanup expensive resources
        database.close()
        cleanupTestFiles()
    }
    
    /**
     * Run before each individual test
     */
    function setup() {
        // Setup for each test
        variables.userService = new models.UserService()
        variables.testUser = createTestUser()
    }
    
    /**
     * Run after each individual test
     */
    function teardown() {
        // Cleanup after each test
        deleteTestUser( testUser.id )
        structClear( variables )
    }
}
```

### Assertions and Expectations

TestBox provides two ways to verify your code behaves correctly: traditional assertions and fluent expectations.

#### **Traditional Assertions**

Assertions use the `$assert` object:

```cfscript
class extends="testbox.system.BaseSpec" {
    
    function testAssertionExamples() {
        var user = { name : "John", age : 30, active : true }
        var numbers = [ 1, 2, 3, 4, 5 ]
        var emptyString = ""
        
        // Basic assertions
        $assertIsTrue( user.active )
        $assertIsFalse( user.age < 18 )
        $assertIsEqual( user.name, "John" )
        $assertIsNotEqual( user.name, "Jane" )
        
        // Type assertions
        $assertIsString( user.name )
        $assertIsNumeric( user.age )
        $assertIsArray( numbers )
        $assertIsStruct( user )
        
        // Null and empty checks
        $assertIsNotNull( user.name )
        $assertIsEmpty( emptyString )
        $assertIsNotEmpty( numbers )
        
        // Collection assertions
        $assertincludes( numbers, 3 )
        $assertNotIncludes( numbers, 10 )
        $assertIncludesWithCase( [ "Monday", "Tuesday" ], "Monday" )
        
        // Custom message
        $assertIsEqual( 
            user.age, 
            30, 
            "User age should be 30 but was #user.age#" 
        )
    }
}
```

#### **Fluent Expectations**

Expectations provide a more readable, chainable syntax:

```cfscript
describe( "Expectations Examples", () => {
    
    it( "demonstrates basic expectations", () => {
        var user = { 
            name : "Alice", 
            email : "alice@example.com",
            age : 25,
            roles : [ "user", "admin" ],
            preferences : { theme : "dark", notifications : true }
        }
        
        // Basic expectations
        expect( user.name ).toBe( "Alice" )
        expect( user.age ).toBeNumeric()
        expect( user.email ).toContain( "@" )
        expect( user.roles ).toHaveLength( 2 )
        
        // Boolean checks
        expect( user.preferences.notifications ).toBeTrue()
        expect( user.banned ).toBeFalsy() // null, false, empty string, etc.
        
        // Type checks
        expect( user ).toBeStruct()
        expect( user.roles ).toBeArray()
        expect( user.name ).toBeString()
        expect( user.age ).toBeInstanceOf( "java.lang.Integer" )
        
        // Collection expectations
        expect( user.roles ).toContain( "admin" )
        expect( user.roles ).notToContain( "guest" )
        expect( user.preferences ).toHaveKey( "theme" )
        expect( user.preferences ).notToHaveKey( "language" )
        
        // Range and comparison
        expect( user.age ).toBeBetween( 18, 65 )
        expect( user.age ).toBeGT( 18 )
        expect( user.age ).toBeLTE( 30 )
        
        // Pattern matching
        expect( user.email ).toMatch( "^\w+@\w+\.\w+$" )
        expect( user.name ).toStartWith( "Al" )
        expect( user.email ).toEndWith( ".com" )
    } )
    
    it( "demonstrates exception expectations", () => {
        var calculator = new models.Calculator()
        
        // Expect exceptions
        expect( () => {
            calculator.divide( 10, 0 )
        } ).toThrow()
        
        expect( () => {
            calculator.divide( 10, 0 )
        } ).toThrow( "DivisionByZeroException" )
        
        expect( () => {
            calculator.sqrt( -4 )
        } ).toThrow( type = "InvalidArgumentException", regex = "negative" )
    } )
    
    it( "demonstrates custom matchers", () => {
        var response = {
            status : 200,
            body : '{"success": true, "data": []}',
            headers : { "content-type" : "application/json" }
        }
        
        // Chain multiple expectations
        expect( response )
            .toHaveKey( "status" )
            .toHaveKey( "body" )
            .toHaveKey( "headers" )
        
        expect( response.status )
            .toBe( 200 )
            .toBeNumeric()
            .toBeBetween( 200, 299 )
    } )
} )
```

#### **Advanced Expectation Patterns**

```cfscript
describe( "Advanced Expectations", () => {
    
    it( "can validate complex objects", () => {
        var apiResponse = {
            success : true,
            data : [
                { id : 1, name : "Item 1", price : 19.99 },
                { id : 2, name : "Item 2", price : 29.99 }
            ],
            pagination : {
                page : 1,
                totalPages : 5,
                totalItems : 47
            }
        }
        
        // Validate structure
        expect( apiResponse )
            .toHaveKey( "success" )
            .toHaveKey( "data" )
            .toHaveKey( "pagination" )
        
        expect( apiResponse.success ).toBeTrue()
        expect( apiResponse.data ).toBeArray().notToBeEmpty()
        
        // Validate each item in array
        apiResponse.data.each( ( item ) => {
            expect( item )
                .toHaveKey( "id" )
                .toHaveKey( "name" )
                .toHaveKey( "price" )
            
            expect( item.id ).toBeNumeric()
            expect( item.name ).toBeString().notToBeEmpty()
            expect( item.price ).toBeNumeric().toBeGT( 0 )
        } )
        
        // Validate pagination
        expect( apiResponse.pagination.page ).toBeLTE( apiResponse.pagination.totalPages )
        expect( apiResponse.pagination.totalItems ).toBeGT( 0 )
    } )
    
    it( "can validate with closures", () => {
        var users = [
            { name : "John", age : 30, active : true },
            { name : "Jane", age : 25, active : true },
            { name : "Bob", age : 40, active : false }
        ]
        
        // Custom validation with closures
        expect( users ).toSatisfy( ( userList ) => {
            return userList.filter( ( user ) => user.active ).len() >= 2
        } )
        
        // Validate specific conditions
        var activeUsers = users.filter( ( user ) => user.active )
        expect( activeUsers ).toHaveLength( 2 )
        
        activeUsers.each( ( user ) => {
            expect( user.age ).toBeGT( 18 )
        } )
    } )
} )
```

### Mocking and Stubbing

TestBox includes MockBox, a powerful mocking framework that lets you create fake objects for testing in isolation.

#### **Creating Mocks**

```cfscript
describe( "User Service with Mocks", () => {
    
    beforeEach( () => {
        // Create mock dependencies
        variables.mockDB = createMock( "models.Database" )
        variables.mockEmailService = createMock( "models.EmailService" )
        variables.mockLogger = createEmptyMock( "Logger" )
        
        // Inject mocks into system under test
        variables.userService = new models.UserService(
            database = mockDB,
            emailService = mockEmailService,
            logger = mockLogger
        )
    } )
    
    it( "should create user and send welcome email", () => {
        // Given
        var userData = {
            email : "test@example.com",
            firstName : "John",
            lastName : "Doe"
        }
        
        var savedUser = {
            id : 123,
            email : "test@example.com",
            firstName : "John",
            lastName : "Doe",
            createdDate : now()
        }
        
        // Setup mock expectations
        mockDB.$( "save", savedUser )
        mockEmailService.$( "sendWelcomeEmail", true )
        mockLogger.$( "info" ) // Void method
        
        // When
        var result = userService.createUser( userData )
        
        // Then
        expect( result.success ).toBeTrue()
        expect( result.user.id ).toBe( 123 )
        
        // Verify mock interactions
        expect( mockDB.$callLog().save ).toHaveLength( 1 )
        expect( mockEmailService.$callLog().sendWelcomeEmail ).toHaveLength( 1 )
        
        // Verify method called with correct arguments
        var saveCall = mockDB.$callLog().save[ 1 ]
        expect( saveCall.args[ 1 ].email ).toBe( "test@example.com" )
        
        var emailCall = mockEmailService.$callLog().sendWelcomeEmail[ 1 ]
        expect( emailCall.args[ 1 ] ).toBe( savedUser )
    } )
} )
```

#### **Stubbing Method Behavior**

```cfscript
describe( "Payment Processing with Stubs", () => {
    
    beforeEach( () => {
        variables.mockPaymentGateway = createMock( "services.PaymentGateway" )
        variables.paymentService = new models.PaymentService( mockPaymentGateway )
    } )
    
    it( "should handle successful payment", () => {
        // Stub successful payment response
        mockPaymentGateway.$( "processPayment" ).$results( {
            success : true,
            transactionId : "txn_123456",
            authCode : "AUTH789"
        } )
        
        var paymentData = {
            amount : 99.99,
            cardNumber : "4111111111111111",
            expiryDate : "12/25"
        }
        
        var result = paymentService.processPayment( paymentData )
        
        expect( result.success ).toBeTrue()
        expect( result.transactionId ).toBe( "txn_123456" )
    } )
    
    it( "should handle payment failure", () => {
        // Stub failed payment response
        mockPaymentGateway.$( "processPayment" ).$results( {
            success : false,
            errorCode : "DECLINED",
            errorMessage : "Card declined"
        } )
        
        var result = paymentService.processPayment( { amount : 99.99 } )
        
        expect( result.success ).toBeFalse()
        expect( result.errorCode ).toBe( "DECLINED" )
    } )
    
    it( "should handle gateway timeout", () => {
        // Stub exception throwing
        mockPaymentGateway.$( "processPayment" ).$throws(
            type = "TimeoutException",
            message = "Gateway timeout"
        )
        
        expect( () => {
            paymentService.processPayment( { amount : 99.99 } )
        } ).toThrow( "TimeoutException" )
    } )
} )
```

#### **Advanced Mocking Patterns**

```cfscript
describe( "Advanced Mocking Scenarios", () => {
    
    it( "can mock with dynamic responses", () => {
        var mockUserRepository = createMock( "repositories.UserRepository" )
        
        // Different responses based on arguments
        mockUserRepository.$( "findById" ).$args( 1 ).$results( { 
            id : 1, name : "John" 
        } )
        mockUserRepository.$( "findById" ).$args( 2 ).$results( { 
            id : 2, name : "Jane" 
        } )
        mockUserRepository.$( "findById" ).$args( 999 ).$throws( "UserNotFoundException" )
        
        var userService = new models.UserService( mockUserRepository )
        
        expect( userService.getUser( 1 ).name ).toBe( "John" )
        expect( userService.getUser( 2 ).name ).toBe( "Jane" )
        expect( () => {
            userService.getUser( 999 )
        } ).toThrow( "UserNotFoundException" )
    } )
    
    it( "can use partial mocks for real objects", () => {
        // Create a partial mock of a real object
        var realCalculator = new models.Calculator()
        var partialMock = prepareMock( realCalculator )
        
        // Mock only specific methods while keeping others real
        partialMock.$( "complexCalculation", 42 )
        
        // Real method works normally
        expect( partialMock.add( 2, 3 ) ).toBe( 5 )
        
        // Mocked method returns stubbed value
        expect( partialMock.complexCalculation( "anything" ) ).toBe( 42 )
    } )
    
    it( "can verify method call sequences", () => {
        var mockService = createMock( "services.WorkflowService" )
        var workflow = new models.OrderWorkflow( mockService )
        
        mockService.$( "validateOrder", true )
        mockService.$( "processPayment", { success : true } )
        mockService.$( "shipOrder", { trackingNumber : "12345" } )
        mockService.$( "sendConfirmation", true )
        
        workflow.processOrder( { orderId : 123 } )
        
        // Verify methods were called in correct order
        var callLog = mockService.$callLog()
        expect( callLog.validateOrder ).toHaveLength( 1 )
        expect( callLog.processPayment ).toHaveLength( 1 )
        expect( callLog.shipOrder ).toHaveLength( 1 )
        expect( callLog.sendConfirmation ).toHaveLength( 1 )
        
        // Verify call order (timestamps should be ascending)
        expect( callLog.validateOrder[ 1 ].timestamp ).toBeLT( callLog.processPayment[ 1 ].timestamp )
        expect( callLog.processPayment[ 1 ].timestamp ).toBeLT( callLog.shipOrder[ 1 ].timestamp )
    } )
    
    it( "can mock static methods and properties", () => {
        var mockConfig = createMock( "utils.Config" )
        
        // Mock static-like behavior
        mockConfig.$( "getSetting" ).$args( "apiUrl" ).$results( "https://test-api.example.com" )
        mockConfig.$( "getSetting" ).$args( "timeout" ).$results( 5000 )
        
        var apiClient = new models.ApiClient( mockConfig )
        
        expect( apiClient.getBaseUrl() ).toContain( "test-api" )
        expect( apiClient.getTimeout() ).toBe( 5000 )
    } )
} )
```

#### **Spy Pattern for Existing Objects**

```cfscript
describe( "Spying on Real Objects", () => {
    
    it( "can spy on method calls while preserving real behavior", () => {
        var realEmailService = new services.EmailService()
        var emailSpy = prepareMock( realEmailService )
        
        var userService = new models.UserService( emailSpy )
        
        // Use real service
        userService.sendPasswordReset( "user@example.com" )
        
        // Verify the real method was called
        expect( emailSpy.$callLog().sendEmail ).toHaveLength( 1 )
        
        var emailCall = emailSpy.$callLog().sendEmail[ 1 ]
        expect( emailCall.args[ 1 ] ).toBe( "user@example.com" )
        expect( emailCall.args[ 2 ] ).toContain( "Password Reset" )
    } )
} )
```

### Running Tests

TestBox offers multiple options for running your tests, including the command line, web browsers, and IDE integration.

#### **BoxLang CLI Runner**

The fastest way to run tests is with the BoxLang CLI runner:

```bash
# Run all tests
./testbox/run

# Run specific test bundle
./testbox/run tests.specs.unit.UserServiceSpec

# Run tests in a directory
./testbox/run --directory=tests.specs.unit

# Run with verbose output (see progress)
./testbox/run --verbose

# Run with specific reporter
./testbox/run --reporter=json

# Filter by labels
./testbox/run --labels=unit,fast

# Exclude slow tests
./testbox/run --excludes=slow,integration

# Generate multiple report formats
./testbox/run --reporter=console --write-json-report=true --write-visualizer=true
```

#### **Advanced CLI Options**

```bash
# Fail fast - stop on first failure
./testbox/run --eager-failure=true

# Custom report path
./testbox/run --reportpath=build/test-results

# Filter specific test names
./testbox/run --filter-specs="should create user,should validate email"

# Run with pattern matching
./testbox/run --bundles-pattern="*Spec*.bx,*Test*.bx"

# Custom properties file
./testbox/run --properties-filename=test-results.properties

# Pass options to test runner
./testbox/run --runner-timeout=30 --runner-debug=true
```

#### **Web Runner**

For browser-based testing and debugging:

```cfscript
// Create /tests/runner.bxm
<bx:script>
param name="url.reporter" default="simple";
param name="url.directory" default="tests.specs";
param name="url.recurse" default="true";

writeOutput(
    new testbox.system.TestBox( 
        directory = url.directory,
        recurse = url.recurse,
        reporter = url.reporter
    ).run()
)
</bx:script>
```

Visit `http://localhost/tests/runner.bxm` to run tests in browser.

#### **CommandBox Integration**

For web applications using CommandBox:

```bash
# Install TestBox
box install testbox

# Run tests
box testbox run

# Run with specific options
box testbox run directory=tests.specs.unit reporter=json

# Watch for changes and auto-run tests
box testbox watch
```

#### **IDE Integration**

Most modern IDEs support TestBox integration:

**VS Code with BoxLang Extension:**

* Install the BoxLang extension
* Use Command Palette: "BoxLang: Run Tests"
* Set breakpoints for debugging
* View test results in integrated terminal

**IntelliJ IDEA:**

* Configure BoxLang runner
* Right-click test files to run individual tests
* Use built-in test runner interface

#### **Continuous Integration**

Example GitHub Actions workflow:

```yaml
name: BoxLang Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup BoxLang
      run: |
        curl -fsSL https://downloads.ortussolutions.com/ortussolutions/boxlang/install-boxlang.sh | bash
        
    - name: Install TestBox
      run: install-bx-module bx-testbox
      
    - name: Run Tests
      run: |
        cd $GITHUB_WORKSPACE
        ./testbox/run --reporter=junit --reportpath=test-results
        
    - name: Publish Test Results
      uses: dorny/test-reporter@v1
      if: always()
      with:
        name: BoxLang Tests
        path: test-results/*.xml
        reporter: java-junit
```

### Best Practices

#### **Test Organization**

```cfscript
// Good: Clear, descriptive test names
describe( "UserService", () => {
    describe( "When creating a new user", () => {
        it( "should save user with valid data" )
        it( "should hash the password securely" )
        it( "should send welcome email" )
        it( "should throw exception for duplicate email" )
    } )
    
    describe( "When updating user profile", () => {
        it( "should update allowed fields only" )
        it( "should validate email format" )
        it( "should maintain audit trail" )
    } )
} )

// Bad: Unclear test names
describe( "UserService", () => {
    it( "test1" )  // What does this test?
    it( "user stuff" )  // Too vague
    it( "should work correctly" )  // Not specific
} )
```

#### **Test Data Management**

```cfscript
// Good: Use factories for test data
class {
    static function createUser( overrides = {} ) {
        var defaultUser = {
            email : "test@example.com",
            firstName : "Test",
            lastName : "User",
            age : 25,
            active : true
        }
        
        return defaultUser.append( overrides )
    }
    
    static function createValidOrder( overrides = {} ) {
        var defaultOrder = {
            userId : createUser().id,
            items : [ createOrderItem() ],
            total : 99.99,
            status : "pending"
        }
        
        return defaultOrder.append( overrides )
    }
}

// Usage in tests
describe( "Order Processing", () => {
    it( "should process valid order", () => {
        var order = TestDataFactory.createValidOrder()
        var result = orderService.process( order )
        expect( result.success ).toBeTrue()
    } )
    
    it( "should reject order with no items", () => {
        var order = TestDataFactory.createValidOrder( { items : [] } )
        expect( () => {
            orderService.process( order )
        } ).toThrow( "EmptyOrderException" )
    } )
} )
```

#### **Assertion Guidelines**

```cfscript
// Good: Specific, meaningful assertions
it( "should create user with proper defaults", () => {
    var user = userService.createUser( { email : "test@example.com" } )
    
    expect( user.id ).toBeNumeric()
    expect( user.email ).toBe( "test@example.com" )
    expect( user.active ).toBeTrue()
    expect( user.createdDate ).toBeDate()
    expect( user.role ).toBe( "user" )
} )

// Bad: Vague or multiple concepts in one test
it( "should work", () => {
    var user = userService.createUser( { email : "test@example.com" } )
    var updatedUser = userService.updateUser( user.id, { firstName : "John" } )
    var deletedUser = userService.deleteUser( user.id )
    
    expect( user ).toBeStruct()  // Too vague
    expect( updatedUser.firstName ).toBe( "John" )  // Different concept
    expect( deletedUser ).toBeTrue()  // Another different concept
} )
```

#### **Mock Usage Guidelines**

```cfscript
// Good: Mock external dependencies only
describe( "EmailService", () => {
    beforeEach( () => {
        // Mock external SMTP service
        variables.mockSmtpClient = createMock( "SmtpClient" )
        variables.emailService = new EmailService( mockSmtpClient )
    } )
    
    it( "should format email correctly", () => {
        mockSmtpClient.$( "send", true )
        
        emailService.sendWelcome( "user@test.com", "John" )
        
        var sentEmail = mockSmtpClient.$callLog().send[ 1 ].args[ 1 ]
        expect( sentEmail.subject ).toBe( "Welcome John!" )
        expect( sentEmail.body ).toContain( "Hello John" )
    } )
} )

// Bad: Mocking everything
describe( "UserService", () => {
    it( "should create user", () => {
        var mockString = createMock( "String" )  // Don't mock primitives
        var mockStruct = createMock( "Struct" )  // Don't mock basic types
        var mockValidator = createMock( "Validator" )  // This is your own code!
        
        // Test becomes meaningless
    } )
} )
```

#### **Test Performance**

```cfscript
// Good: Fast, focused tests
describe( "User Validation", () => {
    it( "should validate email format", () => {
        var validator = new UserValidator()
        
        expect( validator.isValidEmail( "test@example.com" ) ).toBeTrue()
        expect( validator.isValidEmail( "invalid" ) ).toBeFalse()
    } )
} )

// Bad: Slow integration test for simple logic
describe( "User Validation", () => {
    it( "should validate email format", () => {
        // Don't set up entire database for simple validation
        setupTestDatabase()
        var userService = new UserService( getRealDatabase() )
        
        // This is testing validation, not persistence
        var result = userService.createUser( { email : "invalid" } )
        expect( result.errors ).toHaveKey( "email" )
    } )
} )
```

#### **Error Testing**

```cfscript
// Good: Test specific error conditions
describe( "Payment Processing", () => {
    it( "should handle declined card gracefully", () => {
        mockGateway.$( "charge" ).$throws( 
            type = "PaymentDeclinedException",
            message = "Card declined"
        )
        
        var result = paymentService.processPayment( validPaymentData )
        
        expect( result.success ).toBeFalse()
        expect( result.errorType ).toBe( "PAYMENT_DECLINED" )
        expect( result.userMessage ).toBe( "Your card was declined. Please try a different payment method." )
    } )
    
    it( "should handle gateway timeout", () => {
        mockGateway.$( "charge" ).$throws( 
            type = "TimeoutException",
            message = "Gateway timeout"
        )
        
        var result = paymentService.processPayment( validPaymentData )
        
        expect( result.success ).toBeFalse()
        expect( result.errorType ).toBe( "GATEWAY_TIMEOUT" )
        expect( result.shouldRetry ).toBeTrue()
    } )
} )
```

#### **Documentation Through Tests**

```cfscript
// Tests serve as executable documentation
describe( "Shopping Cart Business Rules", () => {
    
    describe( "Discount Calculations", () => {
        it( "should apply 10% discount for orders over $100", () => {
            var cart = new ShoppingCart()
            cart.addItem( { price : 150, quantity : 1 } )
            
            var total = cart.calculateTotal()
            
            expect( total.subtotal ).toBe( 150 )
            expect( total.discount ).toBe( 15 )
            expect( total.final ).toBe( 135 )
        } )
        
        it( "should not apply discount for orders under $100", () => {
            var cart = new ShoppingCart()
            cart.addItem( { price : 50, quantity : 1 } )
            
            var total = cart.calculateTotal()
            
            expect( total.subtotal ).toBe( 50 )
            expect( total.discount ).toBe( 0 )
            expect( total.final ).toBe( 50 )
        } )
        
        it( "VIP customers get 15% discount regardless of order size", () => {
            var cart = new ShoppingCart( customerType = "VIP" )
            cart.addItem( { price : 25, quantity : 1 } )
            
            var total = cart.calculateTotal()
            
            expect( total.discount ).toBe( 3.75 )  // 15% of 25
            expect( total.final ).toBe( 21.25 )
        } )
    } )
} )
```

### Conclusion

Testing is not optional—it's essential for building reliable BoxLang applications. TestBox makes testing approachable and even enjoyable with its intuitive BDD and TDD syntax, powerful mocking capabilities, and flexible test runners.

**Key Takeaways:**

1. **Start Testing Now**: Every day you delay, technical debt is accumulating
2. **Choose Your Style**: BDD for features and behavior, TDD for units and algorithms
3. **Mock Wisely**: Mock external dependencies, not your code
4. **Test the Right Things**: Business logic, edge cases, error conditions
5. **Keep Tests Fast**: Slow tests don't get run
6. **Make Tests Readable**: Their documentation for future developers

**Remember**: The best test is the one you write and run. Start small, build momentum, and soon testing will become second nature in your BoxLang development workflow.

**Next Steps:**

* Set up TestBox in your current project
* Write your first test for existing code
* Gradually increase test coverage
* Integrate testing into your CI/CD pipeline
* Share testing knowledge with your team

Happy testing! 🧪
