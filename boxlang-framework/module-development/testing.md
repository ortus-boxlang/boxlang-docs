---
description: Test your BoxLang module with TestBox and integrate testing into your CI/CD pipeline
icon: vial
---

# Testing

Test your module using TestBox for BoxLang code, JUnit for Java code, or a combination of both.

## TestBox Testing

TestBox is BoxLang's testing framework. Place tests in your module's `tests/` directory.

### Test Structure

```
my-module/
├── tests/
│   ├── Application.bx        # TestBox test harness
│   ├── specs/
│   │   ├── MyBIFTest.bx      # BDD-style tests
│   │   └── MyComponentTest.bx
│   └── resources/
│       └── fixtures/
```

### BDD-Style Test Example

**File:** `tests/specs/GreetBIFTest.bx`

```js
describe( "Greet BIF", () => {
    beforeEach( () => {
        variables.result = greet( "World" )
    } )

    it( "returns a greeting string", () => {
        expect( variables.result ).toBeString()
    } )

    it( "includes the name in the greeting", () => {
        expect( variables.result ).toInclude( "World" )
    } )

    it( "uses custom greeting when provided", () => {
        var custom = greet( name = "World", greeting = "Hi" )
        expect( custom ).toInclude( "Hi" )
    } )
} )
```

### xUnit-Style Test Example

```js
class {

    function testGreetReturnsString() {
        var result = greet( "World" )
        $assert.isTrue( result.len() > 0 )
    }

    function testGreetIncludesName() {
        var result = greet( "World" )
        $assert.isTrue( result contains "World" )
    }
}
```

## Running Tests

```bash
# Run all TestBox tests
box testbox run

# Run a specific spec
box testbox run tests/specs/GreetBIFTest.bx

# Run with a test runner URL
box testbox run "http://localhost:8080/tests"
```

## JUnit Testing (Java Modules)

For Java-heavy modules, use JUnit 5 with standard Gradle test configuration:

```java
@DisplayName( "Greet BIF Tests" )
class GreetTest {

    @Test
    @DisplayName( "Should return greeting with name" )
    void testGreet() {
        var runtime = BoxRuntime.getInstance();
        // Set up test context
        // Invoke BIF
        // Assert results
    }
}
```

Run JUnit tests:

```bash
./gradlew test
```

## Integration Testing

Test your module loaded in a running BoxLang runtime:

```js
class {

    function beforeAll() {
        // Load the module
        variables.moduleService = getBoxRuntime().getModuleService()
        variables.moduleService.loadModule(
            createObject( "java", "java.nio.file.Paths" )
                .get( expandPath( "../../" ) )
        )
    }

    function testModuleIsLoaded() {
        expect( variables.moduleService.hasModule( "myModule" ) ).toBeTrue()
    }

    function testBIFIsRegistered() {
        expect( () => greet( "Test" ) ).notToThrow()
    }
}
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Module Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup BoxLang
        uses: ortus-boxlang/setup-boxlang@v1
        with:
          boxlang-version: latest

      - name: Setup Java (for Java modules)
        uses: actions/setup-java@v4
        with:
          java-version: 21

      - name: Build (Java modules)
        run: ./gradlew build

      - name: Run Tests
        run: box testbox run
```

## Test Best Practices

{% stepper %}
{% step %}
### Test Module Isolation

Verify your module loads cleanly with no side effects. Test both load and unload cycles.

{% endstep %}

{% step %}
### Test Error Handling

Write tests for invalid inputs, missing dependencies, and edge cases.

{% endstep %}

{% step %}
### Test With Other Modules

Verify compatibility by testing alongside modules your module depends on or commonly coexists with.

{% endstep %}

{% step %}
### Mock External Dependencies

Use MockBox to mock external services in tests:

```js
var mockService = createMock( "models.ExternalService" )
    .$( "call", { status: "ok" } )
```

{% endstep %}
{% endstepper %}

## Next Steps

- [Packaging & Publishing](packaging-publishing.md) — Build and distribute your module
- [Troubleshooting](troubleshooting.md) — Common issues and solutions
