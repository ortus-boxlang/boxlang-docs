# AWS Lambda

## What is AWS Lambda?

AWS Lambda is a serverless computing service provided by Amazon Web Services (AWS) that lets you run code without provisioning or managing servers. It automatically scales applications by running code in response to events and allocates compute resources as needed, allowing developers to focus on writing code rather than managing infrastructure ([https://docs.aws.amazon.com/lambda/](https://docs.aws.amazon.com/lambda/)).

{% embed url="https://docs.aws.amazon.com/lambda/" %}

The BoxLang AWS Runtime allows you to run a `Lambda.bx` function in this ecosystem.  We provide you a nice template so you can work with serverless: [https://github.com/ortus-boxlang/bx-aws-lambda-template](https://github.com/ortus-boxlang/bx-aws-lambda-template)

{% @github-files/github-code-block url="https://github.com/ortus-boxlang/bx-aws-lambda-template" %}

## BoxLang Default Lambda Handler

The runtime provides a handler for lambda already configured to accept JSON in as a BoxLang Struct and then output either by returning a simple or complex object or using our `response` convention struct.  The default handler is:

```
ortus.boxlang.runtime.aws.LambdaRunner::handleRequest
```

You can see the code for the handler here: [https://github.com/ortus-boxlang/boxlang-aws-lambda/blob/development/src/main/java/ortus/boxlang/runtime/aws/LambdaRunner.java#L161](https://github.com/ortus-boxlang/boxlang-aws-lambda/blob/development/src/main/java/ortus/boxlang/runtime/aws/LambdaRunner.java#L161)

The handler is Java, but you can easily build it with BoxLang.  However, we have done the hard parts for you so you can focus on your lambda function.

### Environment Variables

The following are the env variables available in the runtime:

<table><thead><tr><th width="305">Environmeent</th><th>Description</th></tr></thead><tbody><tr><td><code>BOXLANG_LAMBDA_CLASS</code></td><td><p>Absolute path to the lambda to execute. The default path is:</p><pre><code>/var/task/Lambda.bx
</code></pre><p>Which is your lambda deployed within your zip file.</p></td></tr><tr><td><code>BOXLANG_LAMBDA_DEBUGMODE</code></td><td>Turn runtime debug mode or not.</td></tr><tr><td><code>BOXLANG_LAMBDA_CONFIG</code></td><td>Absolute path to a custom <code>boxlang.json</code> configuration for the runtime.</td></tr></tbody></table>

## BoxLang Default Template

The BoxLang default template for AWS lambda can be found here: [https://github.com/ortus-boxlang/bx-aws-lambda-template](https://github.com/ortus-boxlang/bx-aws-lambda-template).  It is a Gradle project for now, it will be migrated to CommandBox soon.  The structure of the project is the following

```
/.vscode - Some useful vscode tasks and settings
/build - Not in source control, where your build and distributions happen
/gradle - The gradle runtime, keep in source control
/src
  + main
    + bx
      + Lambda.bx (Your BoxLang Lambda function)
  + test
    + java
      + com
        + myproject
          + LambdaRunnerTest.java (An integration test for your Lambda)
          + TestContext.java (A testing context for lambda)
          + TestLogger.java (A testing logger for lambda)
/workbench - Tons of AWS lambda utilities
/box.json - Your project's dependency descriptor for CommandBox
/build.gradle - The gradle build
/gradle.properties - Where you store your version and metadata
/gradlew - The gradle shell executor, keep in source control
/gradlew.bat - The gradle shell executor, keep in source control
/settings.gradle - The project settings
```

The BoxLang AWS Lambda runtime will look for a `Lambda.bx` in your project and execute it by default.  Run the following commands to prep for coding:

```bash
# Download the runtime, later it will be automatic via maven
./gradlew downloadBoxLang

# Run the tests
./gradlew test

# Build the project, create the lambda zip
# The location is /build/distributions/boxlang-aws-project-1.0.0.zip
./gradlew build

# Mess up? No problem, remove the /build folder or run
./gradlew clean

```

### Lambda.bx

The Lambda function is a BoxLang class with a single function called `run()`.&#x20;

<pre class="language-groovy" data-title="Lambda.bx" data-line-numbers><code class="lang-groovy"><strong>/**
</strong> * My BoxLang Lambda
 */
class{

	function run( event, context, response ){
		response.body = {
			"error": false,
			"messages": [],
			"data": "====> Incoming event " &#x26; event.toString()
		};
		response.statusCode = 200;
	}
}
</code></pre>

#### Arguments

It accepts three arguments:

<table><thead><tr><th width="137">Argument</th><th width="264">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>event</code></td><td><code>Struct</code></td><td>All the incoming JSON as a BoxLang struct</td></tr><tr><td><code>context</code></td><td><code>com.amazonaws.services.lambda.runtime.Context</code></td><td>The AWS context object.  You can find much <a href="https://docs.aws.amazon.com/lambda/latest/dg/java-context.html">more information here.</a></td></tr><tr><td><code>response</code></td><td><code>Struct</code></td><td>A BoxLang struct convention for a response.</td></tr></tbody></table>

{% hint style="success" %}
You can find more information about the AWS Context object here: [https://docs.aws.amazon.com/lambda/latest/dg/java-context.html](https://docs.aws.amazon.com/lambda/latest/dg/java-context.html)
{% endhint %}

#### Event

The `event` structure is a snapshot of the input to your lambda.  We deserialize the incoming JSON for you and give you a nice struct.

#### Context

This is an Amazon Java class that provides extensive information about the request. For more information, check out the API in the Amazon Docs ([https://docs.aws.amazon.com/lambda/latest/dg/java-context.html](https://docs.aws.amazon.com/lambda/latest/dg/java-context.html))

#### Context methods

* `getRemainingTimeInMillis()` – Returns the number of milliseconds left before the execution times out.
* `getFunctionName()` – Returns the name of the Lambda function.
* `getFunctionVersion()` – Returns the [version](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html) of the function.
* `getInvokedFunctionArn()` – Returns the Amazon Resource Name (ARN) that's used to invoke the function. Indicates if the invoker specified a version number or alias.
* `getMemoryLimitInMB()` – Returns the amount of memory that's allocated for the function.
* `getAwsRequestId()` – Returns the identifier of the invocation request.
* `getLogGroupName()` – Returns the log group for the function.
* `getLogStreamName()` – Returns the log stream for the function instance.
* `getIdentity()` – (mobile apps) Returns information about the Amazon Cognito identity that authorized the request.
* `getClientContext()` – (mobile apps) Returns the client context that's provided to Lambda by the client application.
* `getLogger()` – Returns the [logger object](https://docs.aws.amazon.com/lambda/latest/dg/java-logging.html) for the function.

#### Response

The `response` argument is our convention to help you build a nice return structure.  However, it is completely optional.  You can easily return a simple or complex object from your lambda, and we will convert it to JSON.

```json
response : {
  statusCode : 200,
  headers : {
    content-type :  "application/json",
    access-control-allow-origin : "*",
  },
  body : YourLambda.run() results
}
```

{% code lineNumbers="true" %}
```groovy
/**
 * My BoxLang Lambda Simple Return
 */
class{

  function run( event, context, response ){
    return "Hello World!"
  }
  
}

/**
 * My BoxLang Lambda Complex Return
 */
class{

  function run( event, context, response ){
    return {
      age : 1,
      when : now(),
      data : [ 12,3234,23423 ]
    };
  }
  
}
```
{% endcode %}

Now you can go ahead and build your function.  You can use TestBox to unit test your `Lambda.bx` or we even include a `src/test` folder in Java, that simulates the full life-cycle of the runtime.  Just run `gradle test` or use VSCode BoxLang IDE to run the tests.  Now we go to production!

## Deploy to AWS

Log in to the Lambda Console and click on `Create function` button.

<figure><img src="../../.gitbook/assets/image (14).png" alt=""><figcaption><p>AWS Lambda Console</p></figcaption></figure>

Now let's add the basic information about our deployment:

* Add a function name
* Choose `Java 21` as your runtime
* Choose `x86_64` as your architecture

<figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption><p>Create a function</p></figcaption></figure>

Now, let's upload our test code. You can choose a zip/jar or s3 location. We will do a simple zip from our template:

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption><p>Upload Test Code</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption><p>Code Uploaded</p></figcaption></figure>

Now important, let's choose the AWS Lambda Runtime Handler in the `Edit runtime settings`

<figure><img src="../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

And make sure you use the following handler address: `ortus.boxlang.runtime.aws.LambdaRunner::handleRequest` This is inside the runtime to execute our `Lambda.bx` function.

### Testing in AWS

Now click on the `Test` tab and an event name `MyTestEvent`.  You can also add anything you like in the `Event JSON` to test the input of your lambda.  Then click on `Test` and watch it do its magic.  Now go have some good fun!

<figure><img src="../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>
