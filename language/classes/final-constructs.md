# Final Constructs

BoxLang supports the usage of `final` constructs for three contexts:

* Classes
* Methods
* Variables (Constants)

Final modifiers disallow the modifications to the source code to maintain stricter programming constructs. This would be used when you do not want to allow code to override your class or function or variable. This can be a great asset if you are building libraries, frameworks or APIs that require fine granular control of how they can be extended or used.

## Final Classes

Classes can be declared as final, meaning they cannot be extended (inheritance) by other components. This is the ultimate code reuse blocker! However, a final class CAN extend other components.

{% hint style="success" %}
Final classes can be used to prevent inheritance where it is not allowed. Great for APIs, frameworks, and libraries where the author wants to be strict about the usage of such code templates.
{% endhint %}

```java
final class{}

final class extends="MyService"{}
```

{% hint style="info" %}
Unlike `abstract` a function can be `final` even if the class is not `final`.
{% endhint %}

## Final Functions

Functions within a class can also be declared as `final`. Final methods cannot be overridden by sub-components. Final methods can be used to limit the extent to which sub-classes redefine the behavior of the parent classes.

```java
class BaseUtil{

    final function getFile(){
        return getCurrentTemplatePath();
    }

}

// Throws exception due to final method being overriden.
class extends="BaseUtil"{
    function getFile(){
         return "hijacked";
    }
}
```

{% hint style="success" %}
This may be useful when frameworks/base classes are being developed, to ensure the same implementation is being followed in all derived classes.
{% endhint %}

## Final Variables

Variables declared as final are ensured to be constants for the rest of the execution process. The value of that final variable cannot be modified post-construction of the class. Usually these constructs are used in variables defined in the pseudo-constructor.

```java
class{
    final static CACHE_KEY = "cb_";
    final NAME = "John Majano"
    NAME = "Lui Majano" // Throws a final variable exception

    final DETAILS = { "age" : 1 }
    DETAILS[ "nickname" ] = "Johnny Bravo" // Allowed
    DETAILS = {} // Disallowed

}
```

Usually, final variables should be in uppercase to denote them as contstants as per Java conventions and best practices.

{% hint style="danger" %}
**Important**: The variables that contain references to other objects cannot be re-bound to reference news or other objects. i.e., If a `final` variable holds a reference to an array, the reference may not be updated to a new array – but the contents of the original array itself may be updated. The same should apply to structures.
{% endhint %}
