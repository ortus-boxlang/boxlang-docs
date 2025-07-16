---
description: Here you can configure the global thread executors in BoxLang.
icon: list-tree
---

# Executors

BoxLang allows you to register named executors globally. The JSON object key is the name of the executor and the value is another object with the `type` and a `threads` property, which is optional.  By default, BoxLang pre-configures two executors for you:

{% code title="boxlang.json" %}
```json
// Global Executors for the runtime
// These are managed by the AsyncService and registered upon startup
// The name of the executor is the key and the value is a struct of executor settings
// Types are: cached, fixed, fork_join, scheduled, single, virtual, work_stealing`
// The `threads` property is the number of threads to use in the executor. The default is 20
// Some executors do not take in a `threads` property
"executors": {
	// Use this for IO bound tasks, does not support scheduling
	// This is also the default when requestion an executor service via executorGet()
	"io-tasks": {
		"type": "virtual",
		"description": "Unlimited IO bound tasks using Java Virtual Threads"
	},
	// Use this for CPU bound tasks, supports scheduling
	"cpu-tasks": {
		"type": "scheduled",
		"threads": 20,
		"description": "CPU bound tasks using a fixed thread pool with scheduling capabilities"
	},
	// Used for all scheduled tasks in the runtime
	"scheduled-tasks": {
		"type": "scheduled",
		"threads": 20,
		"description": "Scheduled tasks using a fixed thread pool with scheduling capabilities"
	}
},
```
{% endcode %}

{% hint style="warning" %}
If you omit the `threads`on the executors, we will use the default of 20 threads.
{% endhint %}



### Available Executor Types

The available types of executors you can register in BoxLang are:

<table><thead><tr><th width="203">Type</th><th>Description</th></tr></thead><tbody><tr><td><strong>cached</strong></td><td><p>Creates a thread pool that creates new threads as needed but will reuse previously constructed threads when available.</p><p><strong>Use Case:</strong> Best for applications that execute many short-lived asynchronous tasks.</p></td></tr><tr><td><strong>fixed</strong></td><td><p>Creates a thread pool with a fixed number of threads. If all threads are busy, new tasks will wait in a queue until a thread is available.</p><p><strong>Use Case:</strong> Ideal for situations where you need a consistent number of threads to handle tasks, ensuring that the resource usage remains predictable.</p></td></tr><tr><td><strong>fork_join</strong></td><td><p>Designed for tasks that can be broken down into smaller tasks and executed in parallel. It uses a work-stealing algorithm to optimize throughput.</p><p><strong>Use Case:</strong> Suitable for recursive algorithms, parallel processing, and tasks that can be divided into subtasks.</p></td></tr><tr><td><strong>scheduled</strong></td><td><p>Allows tasks to be scheduled to run after a given delay or to execute periodically with a fixed number of threads.</p><p><strong>Use Case</strong>: Perfect for tasks that need to run at regular intervals or after a specific delay, such as periodic maintenance or monitoring tasks.</p></td></tr><tr><td><strong>single</strong></td><td><p>Creates a single-threaded executor that executes tasks sequentially.</p><p><strong>Use Case</strong>: Useful for scenarios where tasks must be executed in order, ensuring that no two tasks run simultaneously.</p></td></tr><tr><td><strong>virtual</strong></td><td><p>It uses virtual threads, also known as fibers, which are lightweight and managed by the JVM, providing high scalability with low overhead.</p><p><strong>Use Case</strong>: Best for high-concurrency applications where many lightweight tasks need to be managed efficiently.</p></td></tr><tr><td><strong>work_stealing</strong></td><td><p>Creates a pool of threads that attempts to keep all threads busy by stealing tasks from other threads when they have completed their work.</p><p><strong>Use Case:</strong> Excellent for irregular workloads where tasks may vary significantly in complexity and duration, optimizing resource usage and improving performance.</p></td></tr></tbody></table>

As long as they implement the executor services interfaces, you can use them in BoxLang.
