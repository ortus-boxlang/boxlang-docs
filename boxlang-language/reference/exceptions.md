[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# BoxLang Exception Types

BoxLang, like Java, has an exception hierarchy, in addition to [the ability to declare custom runtime exceptions](https://boxlang.ortusbooks.com/boxlang-language/syntax/exception-management).  The following are common exceptions thrown by the BoxLang Runtime.

<details>
<summary><code>ScopeNotFoundException</code></summary>

This exception is thrown when a scope is requested that does not exist in the current runtime build

 This exception might be encountered, for example, in a non-web runtime when attempting to access web-specific scopes like `URL` or `FORM`
</details>

<details>
<summary><code>MissingIncludeException</code></summary>

This exception is thrown when a an included template file cannot be located.
</details>

<details>
<summary><code>DatabaseException</code></summary>

This exception is the base exception for all database-related errors in the BoxLang runtime.
</details>

<details>
<summary><code>ConfigurationException</code></summary>

This exception is thrown when an error is encountered during the configuration of the BoxLang runtime or its modules
</details>

<details>
<summary><code>NoFieldException</code></summary>

This exception is thrown when a field is requested on a Java class that does not exist.
</details>

<details>
<summary><code>ClassNotFoundBoxLangException</code></summary>

This exception is thrown when a class cannot be found in the BoxLang runtime.

It is most often encountered when attempting to use a struct that has not been declared or is not avaialable in the current scope
</details>

<details>
<summary><code>LockException</code></summary>

This exception is thrown when a locking operation fails - either with a failure to obtain the lock or due to a timeout
</details>

<details>
<summary><code>NoConstructorException</code></summary>

This exception is thrown when no constructor is found on a Dynamic Object

 It is most often encountered when attempting to construct a Java class with arguments that do not match any of the constructors
</details>

<details>
<summary><code>ParseException</code></summary>

This exception is encountered when parsing of a source file fails.
</details>

<details>
<summary><code>CustomException</code></summary>

This is the base exception class for all custom exceptions thrown by the user.

All dynamically declared exceptions will extend this class
</details>

<details>
<summary><code>ExpressionException</code></summary>

This is the base exception for all expression or evaluation errors in the BoxLang runtime.
</details>

<details>
<summary><code>BoxRuntimeException</code></summary>

This is the base exception thrown by the BoxLang runtime.

It is a runtime exception, so it does not need to be declared in the method signature of classes or methods which throw it
</details>

<details>
<summary><code>KeyNotFoundException</code></summary>

The exception thrown when a key cannot be located within a struct
</details>

<details>
<summary><code>BoxIOException</code></summary>

This exception is thrown when an IO operation fails.

The underlying Java IOException exception is parsed and is used to provide a more user-friendly message.
</details>

<details>
<summary><code>NoMethodException</code></summary>

This exception is thrown when attempting to access a method on a java class that does not exist, is not accessible or does not match the arguments
</details>

<details>
<summary><code>BoxCastException</code></summary>

This exception is thrown when an attempt to cast a value to a specific Java type fails.

Most often it is seen when strongly typed arguments or attributes are used in a way that is not compatible with the expected type.
</details>

<details>
<summary><code>AbstractClassException</code></summary>

This exception is thrown when an abstract class is instantiated.
</details>

<details>
<summary><code>NoElementException</code></summary>

This exception is thrown when a variable is accessed that does not exist
</details>

<details>
<summary><code>UnmodifiableException</code></summary>

This exception is thrown when a modification attempt is made upon an unmodifiable (e.g.

final) object
</details>

<details>
<summary><code>BoxValidationException</code></summary>

This is exception is thrown when an attempt to validate inbound attributes or arguments fails.

Validation upon these attributes or arguments is declared within the respective component or BIF.
</details>
