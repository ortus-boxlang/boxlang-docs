# Properties

Properties are a way to create attributes/fields/data for your object, which can also adhere to inheritance rules.  They are almost the same as fields in Java. In BoxLang, they can also be used to describe further capabilities for RESTFul/SOAP web services and Hibernate ORM. If `accessors` are enabled, BoxLang will track those properties in the `variables` scope according to their name and create automatic getter and setter methods for those properties. \([https://boxlang.ortusbooks.com/boxlang-language/classes/properties](https://boxlang.ortusbooks.com/boxlang-language/classes/properties)\)

```java
property name="firstName" default="";
property name="lastName" default="";
property name="age" type="numeric" default="0";
property name="address" type="array";
```

The `property` construct can also have different name-value pair attributes that can enhance its functionality. You can find all of them here: [https://boxlang.ortusbooks.com/boxlang-language/classes/properties](https://boxlang.ortusbooks.com/boxlang-language/classes/properties). Below are the most common ones:

* `type` - A valid BoxLang type
* `default` - Default value when the object is created, else defaults to `null`.
* `setter` - Generate a setter method or not, defaults to true
* `getter` - Generate a getter method or not, defaults to true

Please note that in BoxLang you can also declare these attributes via annotations in the comments section, weird, I know!

```java
/**
* The user age
* @type numeric
* @default 0
*/
property name="age"
```
