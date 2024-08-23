---
icon: globe-wifi
---

# HTTP/S Calls

BoxLang makes it really **easy** to interact with **any** HTTP/S endpoint via the `http` tag/construct. The `http` call will generate an HTTP/S request and parse the response into a nice BoxLang structure.

```java
http url="https://www.google.com/" result="result" {
    httpparam name="q" type="formfield" value="test";
}
writeDump( result )
```

{% hint style="info" %}
You can use ANY http method in the `http` calls, the default is a `GET` operation.
{% endhint %}

As you can see from the example above, you can pass parameters to the HTTP request by using the child `httpparam` construct. This parameter can be of many different types: `header, body, xml, cgi, file, url, formfield, cookie` depending on the requirements of the http endpoint.

## The Result Structure

The result structure will contain the following keys:

|        Key       | Description                                                                                                                                                               |
| :--------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   `statusCode`   | The HTTP response code and reason string.                                                                                                                                 |
|   `fileContent`  | The body of the HTTP response. Usually a string, but could also be a Byte Array.                                                                                          |
| `responseHeader` | A structure of response headers, the keys are header names and the values are either the header value or an array of values if multiple headers with the same name exist. |
|   `errorDetail`  | An error message if applicable.                                                                                                                                           |
|    `mimeType`    | The mime type returned in the Content-Type response header.                                                                                                               |
|      `text`      | A boolean indicateing if the response body is text or binary                                                                                                              |
|     `charset`    | The character set returned in the Content-Type header.                                                                                                                    |
|     `header`     | All the http response headers as a single string.                                                                                                                         |

## HTTP Arguments

This construct accepts many arguments with different features you can use when executing http/s calls, below we list just the most common ones.

| Argument      | Type    | Default   | Description                                                                                                                                                                                                                                                   |
| ------------- | ------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `url`         | URL     |           | The http/s endpoint to hit                                                                                                                                                                                                                                    |
| `port`        | numeric | 80/443    | The port of the endpoint to hit. 80 for http and 443 for https                                                                                                                                                                                                |
| `method`      | string  | GET       | The http method to use.                                                                                                                                                                                                                                       |
| `username`    | string  |           | An optional server username                                                                                                                                                                                                                                   |
| `password`    | string  |           | An optional server password                                                                                                                                                                                                                                   |
| `useragent`   | string  | BoxLang   | The user agent to simulate for the request                                                                                                                                                                                                                    |
| `charset`     | string  | utf-8     | The encoding to use                                                                                                                                                                                                                                           |
| `resolveUrl`  | boolean | false     | No does not resolve URLs in the response body. As a result, any relative URL links in the response body do not work. Yes resolves URLs in the response body to absolute URLs, including the port number, so that links in a retrieved page remain functional. |
| `redirect`    | boolean | true      | If the response header includes a location field, determines whether to redirect execution to the URL specified in the field.                                                                                                                                 |
| `timeout`     | numeric | unlimited | A value in seconds of the max time to take for the request.                                                                                                                                                                                                   |
| `getAsBinary` | string  | auto      | If **yes**, convert to BoxLang binary type, **No** keep as text, **auto** let BoxLang detect and convert as necessary                                                                                                                                         |
| `result`      | string  | http      | The name of the variable you want the result structured returned into                                                                                                                                                                                         |
| `multipart`   | boolean | false     | Tells BoxLang to send all data specified by httpparam type="formField" tags as multipart form data, with a Content-Type of multipart/form-data.                                                                                                               |

Basically, you can do any type of http/s calls and consume any type of RESTFul webservices with a nice BoxLang syntax!

## HTTPParam

As mentioned before in our example we can use the `httpparam` construct to pass parameters to the http/s endpoint. The parameters can be of different types as we can see in the following table.

```java
httpParam type=""  name=""  value=""  file=""  encoded=""  mimetype="";
```

### Param Types

| Type        | Description                                                                                                                                   |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `header`    | Specifies an HTTP header. Does not URL encode the value                                                                                       |
| `body`      | Specifies that the `value` is the body of the HTTP request.                                                                                   |
| `xml`       | Identifies the request as having a content-type of `text/xml` and specifies that the `value` attribute contains the body of the HTTP request. |
| `cgi`       | Same as `header` but URL encodes the `value` by default.                                                                                      |
| `file`      | Tells BoxLang to send the contents of the specified file.                                                                                     |
| `url`       | Specifies a URL query string name-value pair to append to the http url attribute. URL encodes the value.                                      |
| `formfield` | Specifies a form field to send. URL encodes the value by default.                                                                             |
| `cookie`    | Specifies a cookie to send as an HTTP header. URL encodes the value.                                                                          |

### Param Arguments

The available param arguments to the httpparam construct are:

| Argument   | Type    | Default | Description                                                                                                                                                                                                                                                                                                        |
| ---------- | ------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `type`     | string  |         | The type of data from the available types above                                                                                                                                                                                                                                                                    |
| `name`     | string  |         | The variable name for the data                                                                                                                                                                                                                                                                                     |
| `value`    | string  |         | The value of the variable                                                                                                                                                                                                                                                                                          |
| `file`     | path    |         | Applies to `file` type; ignored for all other types. The absolute path to the file that is sent with the request.                                                                                                                                                                                                  |
| `encoded`  | boolean | false   | Applies to `formfield` and `cgi` types; ignored for all other types. Specifies whether to URLEncode the form field or header.                                                                                                                                                                                      |
| `mimetype` | string  |         | Applies to `file` type; invalid for all other types. Specifies the MIME media type of the file contents. The content type can include an identifier for the character encoding of the file; for example, text/html; charset=ISO-8859-1 indicates that the file is HTML text in the ISO Latin-1 character encoding. |

Here is another example for you:

```java
http url="https://myrestapp.com/user" result="local.result", method="post" {
        httpparam name="x-api-token" type="header" value="123";
        httpparam
                type="body"
                value=serializeJson( '{
                        name : "luis",
                         age : 2
                }' );
        
}
writeDump( result )
```
