# Includes

If you've used other scripting environments such as PHP, or dynamic HTML, you would be familiar with the concept of **server side includes**. An **include** is a file that is embedded, or **included** within another file making it part of the execution; simple as that.

This can be very useful when you want multiple BoxLang templates to share the same block of code, scopes and visibility. In modern times, you can call this a **mixin**.

A typical example might be your website's header and footer, or the reuse of included functions. The ColdBox MVC framework even allows you to define mixin helper templates that can be injected at runtime in Controller objects, views, layouts and much more.

## A Stern Warning

Now, even though doing includes/mixins are easy to do in BoxLang, let me give you a **BIG WARNING**. Includes are one of the most abused features in ANY language, that bring confusion and sustainability issues. Easy doesn't mean sustainable or maintainable. Do not go crazy with includes, there are many other design patterns like dependency injection and composition/aggregation that can solve reusability in much better approaches. Think about it not twice, but thrice!

> **Mixin** : In object-oriented programming languages, a mixin is a class that contains methods for use by other classes without having to be the parent class of those other classes; No inheritance needed. - [https://en.wikipedia.org/wiki/Mixin](https://en.wikipedia.org/wiki/Mixin)

## Implementation

BoxLang provides the `<bx:include>` tag and the `include` construct for including files in script - [https://boxlang.ortusbooks.com/boxlang-language/syntax/includes](https://boxlang.ortusbooks.com/boxlang-language/syntax/includes).

```javascript
<bx:include template="" runonce="true|false">

// script
include "template.bxm" runonce=true;
```

The `template` argument is a relative, absolute or BoxLang mapping path to the template to inject.

```javascript
include template="path/to/libraries/mixins.bxm";
```
