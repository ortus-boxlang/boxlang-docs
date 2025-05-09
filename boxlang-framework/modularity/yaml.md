---
icon: yammer
---

# Yaml

### Welcome to the BoxLang YAML Module

This module provides a YAML parser and emitter for BoxLang. It is based on the [SnakeYAML](https://bitbucket.org/asomov/snakeyaml) library and provides a simple way to parse and emit YAML content in BoxLang.

```
# For Operating Systems using our Quick Installer.
install-bx-module bx-yaml

# Using CommandBox to install for web servers.
box install boxlang-yaml
```

### Usage

This module registers the following BIFS:

* `yamlSerialize( content, [filepath], [charset=utf8] ):yaml` : Serialize a BoxLang variable into a YAML string. You can also serialize to a file if you provide a file path.
* `yamlDeserialize( content ):any` : Deserialize a YAML string into a BoxLang variable.
* `yamlDeserializeFile( filepath, [charset=utf8] ):any` : Deserialize a YAML file into a BoxLang variable.

Here is a simple example:

```java
// Serialize a BoxLang structure into a YAML string
yaml = yamlSerialize( { name="Luis", age=21, city="Orlando" } );
// Serialize a more complex structure
yaml = yamlSerialize( { name="Luis", age=21, city="Orlando", address={ street="1234", city="Orlando", state="FL" } } );

// Deserialize a YAML string into a BoxLang structure
data = yamlDeserialize( yaml );

// Deserialize a YAML file into a BoxLang structure
data = yamlDeserializeFile( "data.yml" );
```

### BoxLang Class Serialization

BoxLang classes will be serialized as a structure according to its properties. However it must adhere to the following rules:

* The class must have a `serializable = true` annotation. or none at all, that is the default.
* The property must have a `serializable = true` annotation or none at all, that is the default.
* The property must NOT exist in the `yamlExclude` list in the class or the parent class.
* The property must NOT have a `yamlExclude` annotation.

### BoxLang Class Custom Serialization

If you are serializing BoxLang classes, you can implement the `toYAML()` method in your classes to provide a custom serialization. Here is an example:

```java
class {

	function init( required name="", required age=0, required city="" ){
		variables.name = arguments.name;
		variables.age = arguments.age;
		variables.city = arguments.city;
		return this;
	}

	function toYAML(){
		return { name=variables.name, city=variables.city } );
	}

}
```

### GitHub Repository and Reporting Issues <a href="#github-repository-and-reporting-issues" id="github-repository-and-reporting-issues"></a>

Visit the [GitHub repository](https://github.com/ortus-boxlang/bx-yaml) for release notes. You can also file a bug report or improvement suggestion via [Jira](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=13359\&components=27031\&issuetype=1).
