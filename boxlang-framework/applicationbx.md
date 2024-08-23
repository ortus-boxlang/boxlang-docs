---
icon: rocket-launch
---

# Application.bx

## Introduction

If you are running BoxLang in a [web server like CommandBox](https://commandbox.ortusbooks.com/embedded-server) and a BoxLang page (.bxm/.bx) is requested, the engine will look for a special file called `Application.bx` and if found, it will execute it for you **implicitly**. This file is used to define the following:

1. Application-wide settings, default variables, session/client storages, file mappings, datasources, style settings, ORM settings, and so much more. These are created by placing them in the `this` scope and in the pseudo-constructor of the object.
2. Application **life-cycle** event handlers, which the engine will execute for you implicitly, by you creating the appropriate available methods.

{% hint style="info" %}
Usually, you will place this file in your **webroot**. Any page in the same directory or sub-directories that is requested will execute this file implicitly.
{% endhint %}

### Transient File

This file is created on every request, so make sure that it is optimized accordingly. The `application` scope can be leveraged for global persistence. Also note, that because it is instantiated on every request, you have the potential to change settings and events on a per-request basis if needed. Great use cases for this can be the following:

* Switching datasources
* Lowering session/client timeouts for scopes if a bot is requesting a page
* Increased security
* Stopping requests
* Much More...

{% hint style="warning" %}
Please note that this file is executed for every request, so make sure it is optimized accordingly. The engine will also traverse your directories upwards until it finds this file.
{% endhint %}

### Sample Template

{% code title="Application.bx" %}
```javascript
class{

    this.name = "My Awesome App";
    this.applicationTimeout = createTimeSpan( 30, 0, 0, 0 ); //30 days
    this.sessionStorage = true;
    this.sessionTimeout = createTimeSpan( 0, 0, 60, 0 ); // 1 hour

    function onApplicationStart(){}
    function onApplicationEnd( struct applicationScope ) {}

    function onSessionStart() {}
    function onSessionEnd( struct sessionScope, struct applicationScope ) {}

    function onRequestStart( string targetPage ) {}
    function onRequest( string targetPage ) {
        include arguments.targetPage;
    }
    function onRequestEnd() {}
    function onClassRequest( className, method, struct args) {
        return;
    }

    function onError( any Exception, string EventName ) {}
    function onAbort( required string targetPage ) {}
    function onMissingTemplate( required string targetPage ) {}

}
```
{% endcode %}

{% hint style="info" %}
You can find all the settings and event handlers defined for `Application.bx` in cfdocs: [https://cfdocs.org/application-cfc](https://cfdocs.org/application-cfc).
{% endhint %}

## Life-Cycle Events

The `Application.bx` also acts like a big event listener waiting for the BoxLang server engine to call its methods in a callback fashion. You can listen to when an error occurs, even when a missing template is requested, and much more. If I am missing some here, please refer to the latest documentation for the latest updates: [https://cfdocs.org/application](https://cfdocs.org/application)

* **onApplicationStart**: The first time your application is requested, the `onApplicationStart` event is broadcast. It only happens once, until your application times out, the process is restarted, or the computer is restarted.
* **onSessionStart**: Whenever a NEW user requests any resource in your web application BoxLang will assign them a unique session identifier and call this method for you.
* **onRequestStart**: Executes before every requested resource and receives the targeted page in the arguments. You can decide whether to process the page by returning a boolean variable.
* **onRequest**: This callback allows you to include the requested page or not. Consider the `onRequestStart()` as a before advice and the `onRequest` as an around advice over the request. You must `include` the requested page, or the page will never be processed
* **onRequestEnd**: Also receives the targetPage and executes after onRequestStart() and onRequest() have fired.
* **onSessionEnd**: Once a unique session has expired, the engine will call this method with the session and application scope structure as arguments for you.
* **onApplicationEnd**: Once the application times out or is flushed, you can listen to it. It also accepts the entire application scope as an incoming argument.
* **onError**: Like a big try/catch statement across the application. This will fire whenever an untrapped exception is caught. You will receive the exception struct and the `eventName` that generated the exception.
* **onAbort:** Runs when you execute the abort tag somewhere and you want to know where that pesky abort exists. It receives the `targetPage` that the abort came from.
* **onClassRequest**: Intercepts any HTTP or AMF calls to an application based on a Class request.
* **onMissingTemplate**: Executed whenever a template is requested and does not exist in the server.

{% hint style="info" %}
The [ColdBox HMVC Framework](https://www.coldbox.org) builds heavily on these life-cycle methods to provide a rich event-driven web application architecture. You can create an application with CommandBox just by running: `coldbox create app MyApp`
{% endhint %}

## BoxLang Web Applications

BoxLang differs from other Java web languages because one Java context application (The BoxLang Engine) has been deployed with many servlet definitions. You can still create many BoxLang applications within the running context. All you need is to demarcate them with the `Application.bx`, with a unique name that defines the separate BoxLang applications. **Anything in that directory and sub-directories will be considered part of the application.**

Your BoxLang application is nothing more than a memory space reservation using the `this.name` property as its unique name. It can contain the variables scopes like `application`, `session`, and `client` which are unique per this reservation name. This way, two BoxLang applications can have different persistence variable scopes and can even be embedded between each other:

```
+ webroot
  + admin/
     + Application.bx // Embedded admin app
  + Application.bx // Root public app
```

### Application Longevity

This is why you can't kill the `application` scopes. The application is reserved for a specific duration defined using the `this.applicationTimeout` property or defined in the Administrator. Once it expires, the engine will purge it from memory and recreate it fresh.

{% hint style="success" %}
**Tip** You can force the stopping of the Application scope by leveraging the method `applicationStop()`. Be careful, though, as it stops full execution and restarts it. ([https://cfdocs.org/applicationstop](https://cfdocs.org/applicationstop))
{% endhint %}
