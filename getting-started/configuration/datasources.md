---
icon: database
description: Here, you can configure the global data sources in the runtime.
---

# Datasources

## Datasources

Here is where you can register datasources globally in the runtime. You can override them at runtime via:

* `Application.bx|cfc` - For the application
* A-la-carte via query execution calls

{% code title="boxlang.json" %}
```json
// The registered global datasources in the language
// The key is the name of the datasource and the value is a struct of the datasource settings
"datasources": {
	"testDB": {
		"driver": "derby",
		"connectionString": "jdbc:derby:memory:testDB;create=true"
	}
	"testdatasource": {
	 	  "driver": "derby",
	 	  "host": "localhost",
	 	  "port": 3306,
	 	  "database": "test"
	}
},
```
{% endcode %}

The key is the name of the datasource and the value is a struct of configuration for the JDBC connection. Most of the items can be different depending on the JDBC module and driver used. However, at the end of the day we need to know at least either the `driver` , the `connectionString` or individual items of the connection. Check out our guide on [defining datasources here](../../boxlang-language/datasources.md).

## Default Datasource

The name of the datasource in the `datasources` configuration struct, which will act as the default one for the entire runtime.

{% code title="boxlang.json" %}
```json
// You can assign a global default datasource to be used in the language
"defaultDatasource": "main",
"datasources" : {
    "main" : {...}
}
```
{% endcode %}
