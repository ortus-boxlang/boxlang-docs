# HTTP Events

These events are fired during HTTP request and response operations. This only includes code that makes use of  `bx:http` . Other network operations, for example, reading in images via URL in the Image module, will not trigger these events.&#x20;

| Event Name          | Data | Description                                     |
| ------------------- | :--: | ----------------------------------------------- |
| `onHTTPRequest`     |      | Triggered when an HTTP request is made.         |
| `onHTTPRawResponse` |      | Triggered when a raw HTTP response is received. |
| `onHTTPResponse`    |      | Triggered when an HTTP response is processed.   |
