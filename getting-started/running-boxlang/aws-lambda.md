---
description: BoxLang Runtime for AWS Lambda! Serverless for the win!
icon: aws
---

# AWS Lambda

<figure><img src="../../.gitbook/assets/lambda.png" alt=""><figcaption></figcaption></figure>

## What is AWS Lambda?

<figure><img src="../../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

AWS Lambda is a serverless computing service provided by Amazon Web Services (AWS) that lets you run code without provisioning or managing servers. It automatically scales applications by running code in response to events and allocates compute resources as needed, allowing developers to focus on writing code rather than managing infrastructure ([https://docs.aws.amazon.com/lambda/](https://docs.aws.amazon.com/lambda/)).

The **BoxLang AWS Runtime** allows you to code in BoxLang and create Lambda functions in this ecosystem.  We provide you a nice template so you can work with serverless: [https://github.com/ortus-boxlang/bx-aws-lambda-template](https://github.com/ortus-boxlang/bx-aws-lambda-template). This template will give you a turnkey application with features like:

* Unit and Integration Testing
* Java dependency management
* BoxLang depenency management
* Automatic shading and packaging
* GitHub actions to: test, build and release automatically to AWS

{% @github-files/github-code-block url="https://github.com/ortus-boxlang/bx-aws-lambda-template" %}

## BoxLang Lambda Handler

<figure><img src="../../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

Our BoxLang AWS Handler acts as a front controller to all incoming Lambda executions.  It provides you with:

* Automatic request management to an `event`structure
* Automatic logging and tracing
* Execution of your Lambda classes by convention
* Automatic error management
* Automatic response management and serialization
* Life-Cycle Events via our `Application.bx`

The BoxLang AWS runtime provides a pre-built Java handler for Lambda already configured to accept JSON in as a BoxLang Struct and then output either by returning a simple or complex object or using our `response` convention struct.  Our runtime will automatically convert your results to JSON. &#x20;

The default handler you configure your lambda with is:

```
ortus.boxlang.runtime.aws.LambdaRunner::handleRequest
```

{% hint style="info" %}
You can see the code for the handler here: [https://github.com/ortus-boxlang/boxlang-aws-lambda/blob/development/src/main/java/ortus/boxlang/runtime/aws/LambdaRunner.java#L161](https://github.com/ortus-boxlang/boxlang-aws-lambda/blob/development/src/main/java/ortus/boxlang/runtime/aws/LambdaRunner.java#L161)
{% endhint %}

The handler will look for a `Lambda.bx`in your package and execute the `run()`method by convention.

{% code title="Lambda.bx" %}
```java
class {

    function run( event, context, response ){
    
    
    }

}
```
{% endcode %}



## Environment Variables

The following are all the environment variables the Lambda runtime can read and detect.  If they are set by you or the AWS Lambda runner, then it will use those values to alter operations.  This doesn't mean that they will exist at runtime, it just means you can set them to alter behavior.

<table><thead><tr><th width="305">Environmeent</th><th>Description</th></tr></thead><tbody><tr><td><code>BOXLANG_LAMBDA_CLASS</code></td><td><p>Absolute path to the lambda to execute. The default path is:</p><pre><code>/var/task/Lambda.bx
</code></pre><p>Which is your lambda deployed within your zip file.</p></td></tr><tr><td><code>BOXLANG_LAMBDA_DEBUGMODE</code></td><td>Turn runtime debug mode or not.</td></tr><tr><td><code>BOXLANG_LAMBDA_CONFIG</code></td><td>Absolute path to a custom <code>boxlang.json</code> configuration for the runtime.</td></tr></tbody></table>

You can also leverage ANY env variable to configure the BoxLang runtime using our runtime [environment conventions](../configuration.md).

## BoxLang AWS Template

The BoxLang default template for AWS lambda can be found here: [https://github.com/ortus-boxlang/bx-aws-lambda-template](https://github.com/ortus-boxlang/bx-aws-lambda-template).  The structure of the project is the following

```
/.vscode - Some useful vscode tasks and settings
/gradle - The gradle runtime, keep in source control
/src
  + main
    + bx
      + Application.bx (Your life-cycle class)
      + Lambda.bx (Your BoxLang Lambda function)
  + resources
    + boxlang.json (A custom BoxLang configuration file)
    + boxlang_modules (Where you will install BoxLang modules using CommandBox, don't put in source control )
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

The BoxLang AWS Lambda runtime will look for a `Lambda.bx` in your package by convention and execute the `run()`method for you.&#x20;

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

## Lambda.bx

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

### Arguments

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



## Multiple Functions Header

The runtime also allows you to create other functions inside of your Lambda that can be targeted if your AWS Lambda is exposed as an URL, which we recommend.  You will be able to target different functions in your `Lambda.bx`by using the following header when executing your lambda:

```bash
x-bx-function=methodName
```

This makes it incredibly flexible where you can respond to that incoming header in a different function than the one by convention.

## Lambda Modules

You can use any BoxLang module with the BoxLang Lambda runtime by just installing them to the `src/resources/boxlang_modules` folder.  All modules placed there when running your build script, will be packaged up into your lambda package.

```bash
# Using the install-bx-module you can cd to the folder and install modules
cd src/resources
install-bx-module {names} --local

# Or use CommandBox and add them to the box.json
box install id=bx-module directory=src/resources/boxlang_modules
```

## Deploy to AWS

You can deploy your lambda by manually uploading the build package or using our GitHub Action in your template.  Below is the action that does an automatic update.

{% hint style="danger" %}
Please note that you MUST create the lambda function in the AWS console **FIRST** for this to work.  This does not create; it only updates.
{% endhint %}

```yaml
- name: Update AWS Lambda Function
  uses: kazimanzurrashid/aws-lambda-update-action@v2.0.3
  with:
    zip-file: "./build/distributions/${{ env.PROJECT_NAME }}-${{ env.VERSION }}-all.zip"
    lambda-name: ${{ env.PROJECT_NAME }}-${{ env.DEPLOY_TIER }}
  env:
    AWS_REGION: ${{ secrets.AWS_REGION }}
    AWS_ACCESS_KEY_ID: ${{ secrets.AWS_PUBLISHER_KEY_ID }}
    AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_PUBLISHER_KEY }}
```

Our automated approach will require storing your credentials in your repository's secrets. &#x20;

* `AWS_REGION`- The region to deploy to
* `AWS_PUBLISHER_KEY_ID`- The AWS access key
* `AWS_SECRET_PUBLISHER_KEY`- The AWS secret key

When creating the lambdas, make sure you create two lambdas:

* `{projectName}-staging` - A staging lambda based on the `development`branch
* `{projectName}-production` - A production lambda based on the `main`branch

Please also note that our build process allows you to have a `development`branch and a `master/main`production branch.  This will enable you to have a deployment of a `staging`and a `production`tier function in the lambdas console in AWS.

{% hint style="success" %}
The `{projectName}`comes from the `settings.gradle`file in your root project.
{% endhint %}



<figure><img src="../../.gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>

Log in to the Lambda Console and click on `Create function` button.

<figure><img src="../../.gitbook/assets/image (14).png" alt=""><figcaption><p>AWS Lambda Console</p></figcaption></figure>

Now let's add the basic information about our deployment:

* Add a function name: `{projectName}-staging or production`
* Choose `Java 21` as your runtime
* Choose `x86_64` as your architecture

{% hint style="success" %}
TIP: If you choose ARM processors, you can save some money.
{% endhint %}



<figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption><p>Create a function</p></figcaption></figure>

Now, let's upload our test code. You can choose a zip/jar or s3 location. We will do a simple zip from our template:

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption><p>Upload Test Code</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption><p>Code Uploaded</p></figcaption></figure>

Now important, let's choose the AWS Lambda Runtime Handler in the `Edit runtime settings`

<figure><img src="../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

And make sure you use the following handler address: `ortus.boxlang.runtime.aws.LambdaRunner::handleRequest` This is inside the runtime to execute our `Lambda.bx` function.

{% hint style="danger" %}
Please note that the RAM you chose for your lambda determines your CPU as well. So make sure you increase the RAM accordingly.  We have seen great results with 4GB+.
{% endhint %}



### Testing in AWS

Now click on the `Test` tab and an event name `MyTestEvent`.  You can also add anything you like in the `Event JSON` to test the input of your lambda.  Then click on `Test` and watch it do its magic.  Now go have some good fun!

<figure><img src="../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

## Runtime Source Code

The AWS Runtime source code can be found here: [https://github.com/ortus-boxlang/boxlang-aws-lambda](https://github.com/ortus-boxlang/boxlang-aws-lambda)

We welcome any pull requests, testing, docs, etc.
