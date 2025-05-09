---
description: >-
  The UI Forms module adds a collection of BoxLang Components/BIFS that will
  create semantic HTML components that can be used in your applications.  We do
  not skin the components, that will be your job.
icon: html5
---

# UI Forms

```
# For Operating Systems using our Quick Installer.
install-bx-module bx-ui-forms

# Using CommandBox to install for web servers.
box install bx-ui-forms
```

## Components

This module contributes the following Components to the language:

* `form` - the wrapping HTML `<form...></form>` component and other [HTML form tag](https://www.w3schools.com/tags/tag_form.asp) components. Produces an HTML form.
* `input` - the [`<input.../>` HTML form component](https://www.w3schools.com/tags/tag_input.asp)
* `select` - the [`<select ... ></select>` HTML form component](https://www.w3schools.com/tags/tag_select.asp)
* `slider` - generates an [HTML 5 input range slider](https://www.w3schools.com/tags/att_input_type_range.asp)
* `textarea` - the [`<textarea>...</textarea>` HTML form component](https://www.w3schools.com/tags/tag_textarea.asp)

{% hint style="info" %}
Most attributes of these components serve as pass-through attributes of the generated HTML tag.&#x20;
{% endhint %}

### `form`

* `format` - this attribute will throw an error if present and is anything other than `HTML`. XML and Flash forms will not be supported.
* `passthrough` - this is a list of passthrough attributes that will be added to the form tag.
* `scriptsrc` - this defines an external location for the custom forms javascript file, which is sourced into the HTML output
* `preservedata` - When the form action returns to the page containing the form, this attribute determines whether to override the control values with the submitted values.

```xml
<bx:form format="HTML" action="http://www.example.com" method="post" preservedata="true">
    <bx:input type="text" name="name" label="Name" />
    <bx:input type="text" name="email" label="Email" />
    <bx:input type="submit" value="Submit" />
</bx:form>
```

**Unsupported `form` Component Attributes**

The following attributes are unsupported and generate a warning log message if used.

* `enablecab`
* `skin`
* `preloader`
* `timeout`
* `wmode`
* `accessible`
* `archive`
* `codebase`

***

### `input`

* `label` - if provided, will generate an HTML `label` tag before the generated `input` tag
* `message` - can be provided as a custom message if validation fails
* `passthrough` - this is a list of passthrough attributes which will be added to the form tag.

```xml
<bx:input type="text" name="name" label="Name" />
```

**Planned `input` Component Attributes supported**

The following have not yet been implemented in the `input` component but are planned for development in the near-term.

* `autosuggest` - Valid only for `type="text"`. Specifies entry completion suggestions to display as the user types into a text input. The user can select a suggestion to complete the text entry. The valid value can be either of the following:
  * A string consisting of the suggestion values separated by the delimiter specified by the delimiter attribute.
  * A bind expression that gets the suggestion values based on the current input text.
* `autosuggestbinddelay` - Valid only for `type="text"`. The minimum time between autosuggest bind expression invocations, in seconds. Use this attribute to limit the number of requests that are sent to the server when a user types.
* `autosuggestminlength` - Valid only for `type="text"`. The minimum number of characters required in the text box before invoking a bind expression to return items for suggestion.
* `delimiter` - Optional delimiter which informs the `autosuggest` attribute
* `maxresultsdisplayed` - Optional numeric value which informs the max result displayed by the autosuggest
* `onbinderror` - The name of a JavaScript function to execute if evaluating a bind expression, including an autosuggest bind expression, results in an error. The function must take two attributes: an HTTP status code and a message.
* `showautosuggestloadingicon` - A Boolean value that specifies whether to display an animated icon when loading an autosuggest value for a text input.
* `typeahead` - A Boolean value that specifies whether the autosuggest feature should automatically complete a user's entry with the first result in the suggestion list.
* `validate` - A limited subset of the accepted values for `validate` will be supported in a future release. It is highly encouraged to use HTML 5 validation, including `min`, `max` and `mask` attributes, however.

**Unsupported `input` Component Attributes**

* `bind` - this attribute is unsupported and will throw an error if used
* `validateAt` - Since the `validate` attribute passes through to an HTML5 `type` attribute on the tag, this attribute is not supported

***

### `slider`

The slider component creates a [`type="range"` input](https://www.w3schools.com/tags/att_input_type_range.asp) component but access the following additional attributes:

* `increment` - specifies the `step` value of the slider
* `bgColor` - specifies the background color of the slider body
* `color` - specifes the color of the slider control
* `vertical` - Optional boolean attribute. When `true`, the slider will have a vertical orientation

```xml
<bx:slider name="slider" min="0" max="100" increment="5" bgColor="#f1f1f1" color="#4CAF50" />
```

***

### `textarea`

* `passthrough` - this is a list of passthrough attributes which will be added to the form tag.
* `message` - can be provided as a custom message if validation fails
* `passthrough` - this is a list of passthrough attributes which will be added to the form tag.

```xml
<bx:textarea name="message" label="Message" />
```

**Unsupported `textarea` Component Attributes**

The following attributes are not supported and will be ignored if provided:

* `stylesXML`
* `templatesXML`
* `richtext`
* `toolbar`
* `toolbarOnFocus`

### GitHub Repository and Reporting Issues <a href="#github-repository-and-reporting-issues" id="github-repository-and-reporting-issues"></a>

Visit the [GitHub repository](https://github.com/ortus-boxlang/bx-ui-forms) for release notes. You can also file a bug report or improvement suggestion via [Jira](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=13359\&components=27027\&issuetype=1).
