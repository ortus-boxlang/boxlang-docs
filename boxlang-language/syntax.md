---
description: Script or Tags? Choose wisely!
---

# Syntax & Semantics

There are two ways to write BoxLang code: in **tag** or in **script** syntax. BoxLang will dictate that your view or presentation layers will utilize the **tag** syntax in `bxm` files and the **script** syntax in `bxs` and `bx` files.  Please note `bx` files are specifically for Box Classes, this is where model or business layers should all be done. (MVC comes later). There are no differences in functionality between them; it's pure syntax.

* script Syntax Guide - [https://cfdocs.org/script](https://cfdocs.org/script)

{% hint style="info" %}
In BoxLang tags start with **bx:** vs **cf**. So instead of `<cfoutput>` use `<bx:output>`.
{% endhint %}

## Syntax Files

BoxLang includes a set of instructions you use on pages (`.bxm,.bxs`) or classes (`.bx`). You will write one or more instructions in a file (`.bxm,.bxs,.bx`) then run the file through a BoxLang engine or Command Line Interpreter like CommandBox.

* `bxm` - BoxLang markup file, tag syntax is the default and used for views
* `bxs` - BoxLang script file, script syntax.&#x20;
* `bx` - The default is the BoxLang class file (Class or Object), script syntax.

## Implicit Behavior

BoxLang also gives you a pre-set of defined [tags](https://cfdocs.org/tags) and [functions](https://cfdocs.org/functions) available to you in any file you write your code in. These tags and functions allow you to extend the typical language constructs with many modern capabilities, from database interaction to PDF generation. They are basically automatic imports.

{% hint style="success" %}
**Tip:** Please note that the BoxLang built-in functions are also **first-class functions** so that they can be passed around as arguments to other functions or closures or saved as variables.
{% endhint %}

## Exploring Behavior

Three BoxLang instructions we will use in this section are `bx:set`, `bx:output`, and `bx:dump`.

* `bx:set` is used to create a variable and assign it a value.
* `bx:output` displays a variable's value to the output stream.
* `bx:dump` is used to display the contents of simple and complex variables, objects, classes, user-defined functions, and other elements to the output stream.

We might have a file named _myprogram.bxm_ and _Sample.bx_ like this:

### Tag Syntax

{% tabs %}
{% tab title="myprogram.bxm" %}
```markup
<bx:set s = new Sample()>
<bx:output>#s.hello()#</bx:output>
```
{% endtab %}
{% endtabs %}

### Script Syntax

{% tabs %}
{% tab title="myprogram.bxm" %}
```java
<bx:script>
    s = new Sample();
    writeOutput( s.hello() );
</bx:script>
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tip:** Please note that if you want to write in script in a tag-based file, you must use an opening and closing `<bx:script>` tag.
{% endhint %}

{% tabs %}
{% tab title="Sample.bx" %}
```javascript
class{

    function hello(){
       return "Hello, World!";
    }

}
```
{% endtab %}
{% endtabs %}

Please note that no types and not even any visibility scopes you might be used to are present. BoxLang can also infer variable types on more distinct variables like dates, booleans, or numbers. However, please note that you can fully leverage types if you like:

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

Please note that semi-colons are used to demarcate line endings in BoxLang `;`. They can be optional, however. Also, note the CommandBox REPL does NOT require semi-colons.

### Tags In Script

BoxLang will allow you to write your tags in script syntax. You basically eliminate the starting `<` and ending `>` enclosures and create a block by using the `{` and `}` mustaches.

{% hint style="info" %}
BoxLang uses Lucee's generic tag-in-script syntax
{% endhint %}

```javascript
http method="GET" charset="utf-8" url="https://www.google.com/" result="result" {
    httpparam name="q" type="formfield" value="test";
}
```

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

## Coding Standards

At [Ortus Solutions](https://www.ortussolutions.com), we have developed a set of development standards for many languages. You can find our BoxLang standards here: [https://github.com/Ortus-Solutions/coding-standards](https://github.com/Ortus-Solutions/coding-standards).

{% @github-files/github-code-block url="https://github.com/Ortus-Solutions/coding-standards" %}
