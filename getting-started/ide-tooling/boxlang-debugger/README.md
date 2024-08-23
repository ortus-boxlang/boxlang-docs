---
description: Learn how to debug with BoxLang and the BoxLang IDE
icon: spider
---

# BoxLang Debugger

## What is a Debugger?

Have you used a debugger before? Have you used one regularly? If you have great! Hopefully, BoxLang’s debugger will make you feel at home. Let me introduce the concept if you are unfamiliar with using a debugger as part of your development process.

<figure><img src="../../../.gitbook/assets/image (32).png" alt="The BoxLang Debugger"><figcaption><p>The BoxLang Debugger</p></figcaption></figure>

Debuggers are a program that runs and controls the execution of the software you are developing. As the debugger is in control of the execution of every instruction, it can freeze the program and provide the developer a chance to inspect the state of their software as if they could freeze time. Often, debuggers will give the developer the power to inspect and change variables within their program and move execution back and forth.

As developers familiar with CFML or Java, we are all familiar with the `writeDump()` or `System.out.println()` style of development. While outputting your application state to the browser or to a file has its place, a debugger offers several benefits over a logging-based debugging approach. Here are just a few of them:

* Add/remove breakpoints as your programming executes instead of having to re-run the request
* Inspect variables at each iteration of a loop
* Create watchers for specific variables and values
* Modify the value of a variable and continue execution
* Step through each method of a call stack to see the different levels of an application
* So much more

Getting started can be daunting if you have never used a debugger before. We have put much effort into making the BoxLang debugger as easy to start as possible. Let’s take a look at how to use it.

## Debugging BoxLang Classes & Scripts

Let's say you have a `.bxs` file. This is BoxLang’s CLI script extension. With a `.bxs` you can execute your file on the command line just like any other scripting language. Our VS Code extension makes it even easier. We provide a right-click option to run BoxLang files or via the command pallete as well.

{% code title="task.bxs" %}
```java
task = new Task();
invoke( task, "setFoo", { foo : "bar" } );
result = invoke( task, "getFoo" );

println( result );
```
{% endcode %}

<figure><img src="../../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

You can also run `bx` files which are BoxLang classes, as long as they have a `main()` method on them, in the same manner as above:

{% code title="Hello.bx" %}
```java
class inject hello="word"{

	property foo;
	property firstName;
	property lastName;
	property numeric age default=1;

	function main( args = {} ){
		test = new Person();
		println( test.toJson() )

		println( this.$bx.getMeta().keyArray() )
		println( this.$bx.getMeta().annotations )
	}

	function onMissingMethod( missingMethodName, missingMethodArgs ){
		println( "Missing method: " & missingMethodName );
		println( "missingMethodArgs: " & missingMethodArgs.toString() );
	}

}

```
{% endcode %}

<figure><img src="../../../.gitbook/assets/image (33).png" alt=""><figcaption><p>Command Pallete</p></figcaption></figure>

Once you click the `BoxLang: Run Script` option. Your program will execute. The debug console will auto-focus and you will see the console output of your program. “Great!” You might say, “But what about debugging! Fair enough! Let’s look at that next.

If you want to debug a script you will need to set a breakpoint. To set a breakpoint simply hover your cursor over the gutter to the left of the file’s line numbers. When you see a red dot appear, “click” and you will set a breakpoint at that line. Now that you have a breakpoint go and ahead and use our right-click `BoxLang: Run Script` option to kick off a debug session. This time your script will pause at your breakpoint.

### Debug Controls

Now that we are debugging, what special actions can we take? We’ll briefly look at 3 features of our debugger: variables, the call stack, and debugger controls.

#### Variables

The Variables Panel gives you information about the state of your program. You can view and even edit variables by looking at the data presented by this panel. This is where much of the value of the debugger comes from. At every breakpoint you hit you will see an up-to-date snapshot of your application state.

<figure><img src="../../../.gitbook/assets/image (24).png" alt=""><figcaption><p>Variables</p></figcaption></figure>

#### Call Stack

The Call Stack Panel lets you see the entire call stack of your current location in the code. This feature is a little more advanced than the variables panel but can provide vital information that helps you understand the flow of code in your app.

<figure><img src="../../../.gitbook/assets/image (25).png" alt="" width="375"><figcaption><p>Call Stack</p></figcaption></figure>

#### Controls

Finally, we get to the debugger controls. These controls are the unsung hero of every debug session, you’ll use them often as you incorporate the debugger into your workflow.

<figure><img src="../../../.gitbook/assets/image (26).png" alt="" width="375"><figcaption><p>Controls</p></figcaption></figure>

* `Play/Pause` - Resume execution if paused/pause execution of a running program.
* `Step Over` - Move to the next pausable location without moving down the call stack
* `Step In` - Move into a deeper stackframe if able or Step Over
* `Step Out` - Move to the parent stack frame
* `Stop` - Stop debugging

The controls mostly speak for themselves. The best way to get familiar with them is to jump in and play around. After just a few minutes of playing around with them, using them as part of your debug process will become second nature.

## Conclusion

I hope you will agree that the BoxLang Debugger is a powerful addition to the set of tools we at Ortus have built to help you develop BoxLang applications.  Now code some Box!
