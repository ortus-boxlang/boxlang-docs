---
icon: brackets-curly
description: Discover the BoxLang language
---

# Syntax & Semantics

BoxLang is a dynamic language that is fluent with a low verbosity syntax.  It will feel like a very lean Java syntax.  Check out our quick [style guide](../../getting-started/overview/syntax-style-guide/) if you are a Java/Kotlin/Python/PHP/Ruby/CFML/Rust developer, this will give you a first-hand look at the major semantics of the language.

## Syntax Files

BoxLang can be written in either templates, scripts, or classes. You will write one or more instructions in a file (`.bxm,.bxs,.bx`), then run the file through a BoxLang engine or Command Line Interpreter like our REPL.

<figure><img src="../../.gitbook/assets/image (36).png" alt="" width="375"><figcaption><p>BoxLang File Types</p></figcaption></figure>

* `bxm` - BoxLang markup file, tag syntax is the default and used for creating rich views and templating
* `bxs` - BoxLang scripting file, for a-la-carte scripting
* `bx` - A BoxLang class

## Implicit Behavior

BoxLang also gives you a pre-set of defined headless [components](https://boxlang.ortusbooks.com/boxlang-language/reference/components) and [functions](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions) available to you in any file in which you write your code. These components and functions allow you to extend the typical language constructs with many modern capabilities, from database interaction to PDF generation.&#x20;

Also, note that you can use all the BoxLang types naturally with no imports:

* Structs - (Maps)
* Arrays - (Starting with an index of 1, not 0)
* Strings
* Dates
* Numerics (Floats, shorts, integers, longs, etc)
* XML
* Queries
* Functions

{% hint style="success" %}
**Tip:** Please note that the BoxLang built-in functions (BIFs) are also **first-class functions** so that they can be passed around as arguments to other functions or closures or saved as variables.
{% endhint %}

## Exploring Behavior

Let's start by exploring some behavior in these types of files.  Ensure you are using the [BoxLang IDE](../../getting-started/ide-tooling/) Write the code; remember you can execute any BoxLang file within your editor by right-clicking the file and saying **"BoxLang: Run File"**

<figure><img src="../../.gitbook/assets/image (37).png" alt=""><figcaption><p>Run a File</p></figcaption></figure>

### Scripting

Let's write a simple scripting file that declares and uses a few boxlang types, and then you can print them on the console.  You can run the script via your REPL or via [https://try.boxlang.io](https://try.boxlang.io)

{% tabs %}
{% tab title="myscript.bxs" %}
```java
// let's define an array
a = [ 1,2,3 ]
// A structure of data
user = { name : "boxlang", id : createUUID(), age : 3 }
// create a variable using a BIF
today = now()
// Print out some code
println( "Today is #today#" )
// Print out the array and structure
println( a )
println( "array has" & a.len() & " elements" )
println( user )
println( user.name & " has an id of #user.id#" )

```
{% endtab %}
{% endtabs %}

Now you can run it in the REPL: `boxlang myscript.bxs`

### Templating

I can also use the templating language and build this in an HTML-enabled application. &#x20;

{% hint style="info" %}
If you want to see HTML being produced, then you will need to run the file in our [MiniServer](../../getting-started/running-boxlang/miniserver.md) or [CommandBox](../../getting-started/running-boxlang/commandbox.md) server.  If not, just run the templating file via the REPL `boxlang` binary.
{% endhint %}

{% tabs %}
{% tab title="myprogram.bxm" %}
```markup
<bx:set a = [1,2,3,4]>
<bx:set user = { name : "boxlang", id : createUUID(), age : 3 }>
<bx:set today = now()>
<bx:output>Today is #today#</bx:output>
<bx:output>#a#</bx:output>
<bx:output>#user#</bx:output>
```
{% endtab %}
{% endtabs %}

Run this in the MiniServer or CommandBox or the REPL tool: `boxlang myprogram.bxm`.  You can also leverage scripting in templates by using the `<bx:script>` template:

```markup
<bx:script>
a = [ 1,2,3 ]
user = { name : "boxlang", id : createUUID(), age : 3 }
today = now()
</bx:script>

<bx:output>
Today is #today#
<br>
My array is #a# and it has #a.len()# elements
<br>
My user struct is #user# and has #a.len()# keys
</bx:output>
```

### Classes

{% tabs %}
{% tab title="Sample.bx" %}
```javascript
class{

    function hello(){
       return "Hello, World!";
    }
    
    function main( args = [] ){
       return new Sample().hello();
    }

}
```
{% endtab %}
{% endtabs %}

Please note that no types or visibility scopes you might be used to are present. BoxLang can also infer variable types on more distinct variables like dates, booleans, or numbers.   It also can include a `main()` method that can be invoked for you if you run the class via our REPL tool:

```bash
$> boxlang Sample
Hello, World!
```

However, please note that you can fully leverage types if you like:

{% tabs %}
{% tab title="Sample.bx" %}
```javascript
class{

    public string function hello(){
       return "Hello, World!";
    }

}
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
By default, the return type of every function and/or argument is **any**. Thus, it can be determined at runtime as a dynamic variable.
{% endhint %}

### Semi-Colons

Please note that semi-colons are used to demarcate line endings in BoxLang `;`. They can be optional, however.

## Polyglot References

As we now live in a world of polyglot developers, we have added references below to other languages to see the differences and similarities between BoxLang and other major languages in usage today. Please note that this section is merely academic and to help developers from other language backgrounds to understand the intricacies of the BoxLang syntax.

### PHP Syntax

{% tabs %}
{% tab title="myprogram.php" %}
```php
<?php
    require("Sample.php");
    $s = new Sample();
    echo $s->hello();
?>
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Sample.php" %}
```php
<?php
class Sample
{
    public function hello() {
        return "Hello, World!";
    }
}
?>
```
{% endtab %}
{% endtabs %}

### Ruby Syntax

{% tabs %}
{% tab title="myprogram.rb" %}
```ruby
class Sample
    def hello
        "Hello, World!"
    end
end

s = Sample.new
puts s.hello
```
{% endtab %}
{% endtabs %}

### Java Syntax

{% tabs %}
{% tab title="MyProgram.java" %}
```java
public class MyProgram {

    public String hello(){
        return "Hello, world!";
    }

    public static void main(String[] args) {
        System.out.println( new MyProgram().hello() );
    }

}
```
{% endtab %}
{% endtabs %}

