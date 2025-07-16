---
description: Human, Fluent, Functional Scheduled Tasks with BoxLang
icon: calendars
---

# 🎯 Introduction

The BoxLang async framework provides a powerful and flexible way to schedule tasks and workloads in your applications. Whether you need to run tasks at specific intervals, one-off tasks, or manage complex scheduling scenarios, the async package has you covered.  It allows you to schedule tasks using a human-readable DSL (Domain Specific Language) that is both fluent and functional. This makes it easy to define when and how tasks should run, without getting bogged down in complex configurations.

You have three main approaches to scheduling tasks in BoxLang:

1. **📋 Scheduler Approach**: Create a scheduler and register tasks in it
2. **⚡ Scheduled Executor Approach**: Create a `ScheduledExecutor` and send task objects into it
3. **🖥️ CLI Runner Approach**: Use the `boxlang schedule {path.to.Scheduler.bx}` command to run tasks from the CLI

{% hint style="success" %}
With our scheduled tasks you can run either one-off tasks or periodically tasks.
{% endhint %}

The way to do executor tasks is documented in our [Executors Section](executors.md), this guide focuses on the scheduler runtime and CLI runner approaches.

# 🏗️ Scheduler Service

BoxLang provides a `SchedulerService` that manages all the global, application, and module schedulers.  There is really no need to interact with it, but if you want to you can access it via the `boxRuntime().getSchedulerService()` method. This service is responsible for managing all the schedulers in your application, including starting and stopping them, and providing access to the registered tasks.

# ⚙️ Configuration

The BoxLang configuration file located at `{BoxLangHome}/config/boxlang.json` contains all the necessary configurations and tunings for the scheduled tasks framework.  Here are the main configurations you can set:

```json
// BoxLang Scheduler
// These are managed by the SchedulerService and registered upon startup
// or via a boxlang schedule [scheduler.bx] call
"scheduler": {
    // The default scheduler for all scheduled tasks
    // Each scheduler can have a different executor if needed
    "executor": "scheduled-tasks",
    // The cache to leverage for server fixation or distribution
    "cacheName": "default",
    // An array of BoxLang Schedulers to register upon startup
    // Must be an absolute path to the scheduler file
    // You can use the ${user-dir} or ${boxlang-home} variables or any other environment variable
    // Example: "schedulers": [ "/path/to/Scheduler.bx" ]
    "schedulers": [],
    // You can also define tasks manually here
    // Every task is an object defined by a unique name
    // The task object is a struct with the following properties:
    // - `crontime:string` - The cron time to run the task (optional), defaults to empty string
    // - `eventhandler:path` - The absolute path to the task event handler(optional), defaults to empty string
    // - `exclude:any` - Comma-separated list of dates or date range (d1 to d2) on which to not execute the scheduled task
    // - `file:name` - Name of the log file to store output of the task (optional), defaults to `scheduler`
    // - `group:string` - The group name of the task (optional), defaults to empty string
    "tasks": {}
},
```

## Executor

The `executor` property defines the default executor to use for all scheduled tasks. This can be overridden on a per-scheduler basis. The default executor is `scheduled-tasks`, which is a `ScheduledExecutor` with a default of 20 threads, which can be found in the `executors` section.

## Cache Name

The `cacheName` property defines the cache to use for server fixation or distribution. This is useful if you want to share scheduled tasks across multiple servers in a cluster. The default cache is `default`, which is the default cache defined in the BoxLang configuration.  This can be found in the `caches` section of the configuration file and can be overridden on a per-scheduler basis.

## Schedulers

The `schedulers` property is an array of BoxLang schedulers to register upon startup. Each scheduler is defined by an absolute path to the scheduler class (e.g. `/path/to/Scheduler.bx`). You can use the `${user-dir}` or `${boxlang-home}` variables or any other environment variable to define the path. This allows you to define multiple schedulers that can be registered and managed by the `SchedulerService` at runtime startup.

## Tasks

The `tasks` property is an object that defines the tasks to register upon startup. Each task is defined by a unique name and can have many properties.  This is an experimental feature that is coming soon.

# 📋 Scheduler Class

A `Scheduler` is a self-contained class that can track multiple tasks for you and give you enhanced and fluent approaches to scheduling. It is a powerful tool that allows you to register tasks, configure them, and manage their execution. Each scheduler class inherits from the `BaseScheduler` Java class, giving you access to all of its powerful methods and capabilities.

Let's review the structure of a BoxLang scheduler class:

```javascript
class {

	// Properties - These are automatically injected by the BoxLang runtime
	property name="scheduler";       // The BaseScheduler instance this class wraps
	property name="runtime";         // The BoxRuntime instance
	property name="logger";          // A logger instance for this scheduler
	property name="asyncService";    // The AsyncService for executor management
	property name="cacheService";    // The CacheService for distributed scheduling
	property name="interceptorService"; // The InterceptorService for event broadcasting

	/**
	 * The configure method is called by the BoxLang runtime to allow the scheduler to configure itself.
	 *
	 * This is where you define your tasks and setup global configuration.
	 */
	function configure(){
		// Setup Scheduler Properties
		scheduler.setSchedulerName( "My-Scheduler" );
		scheduler.setTimezone( "UTC" );

		// Define a lambda task
		scheduler.task( "My test Task" )
			.call( () -> {
				println( "I am a lambda task: #dateFormat( now(), "full" )#" );
			} )
			.every( 2, "second" );
	}

	/**
	 * --------------------------------------------------------------------------
	 * Life - Cycle Callbacks
	 * --------------------------------------------------------------------------
	 */

	/**
	 * Called after the scheduler has registered all schedules
	 */
	void function onStartup(){
		println( "I have started!" & scheduler.getSchedulerName() );
	}

	/**
	 * Called before the scheduler is going to be shutdown
	 */
	void function onShutdown(){
		println( "I have shutdown!" & scheduler.getSchedulerName() );
	}

	/**
	 * Called whenever ANY task fails
	 *
	 * @task      The task that got executed
	 * @exception The exception object
	 */
	function onAnyTaskError( task, exception ){
		println( "Any task [#task.getName()#] blew up " & exception.getMessage() );
	}

	/**
	 * Called whenever ANY task succeeds
	 *
	 * @task   The task that got executed
	 * @result The result (if any) that the task produced as an Optional
	 */
	function onAnyTaskSuccess( task, result ){
		println( "on any task success [#task.getName()#]" );
		println( "results for task are: " & result.orElse( "No result" ) );
	}

	/**
	 * Called before ANY task runs
	 *
	 * @task The task about to be executed
	 */
	function beforeAnyTask( task ){
		println( "before any task [#task.getName()#]" );
	}

	/**
	 * Called after ANY task runs
	 *
	 * @task   The task that got executed
	 * @result The result (if any) that the task produced as an Optional
	 */
	function afterAnyTask( task, result ){
		println( "after any task completed [#task.getName()#]" );
		println( "results for task are: " & result.orElse( "No result" ) );
	}

}
```

## Scheduler Properties

The scheduler properties are automatically injected by the BoxLang runtime and provide access to various services:

| Property | Description |
|----------|-------------|
| `scheduler` | The `BaseScheduler` instance that your class wraps, providing access to all scheduler methods |
| `runtime` | The `BoxRuntime` instance for access to global services |
| `logger` | A logger instance specifically configured for this scheduler |
| `asyncService` | The `AsyncService` for managing executors and async operations |
| `cacheService` | The `CacheService` for distributed scheduling and state management |
| `interceptorService` | The `InterceptorService` for broadcasting events and interceptors |

## Scheduler Configuration Methods

Your scheduler class has access to all the methods from the `BaseScheduler` class through the `scheduler` property:

| Method | Description |
|--------|-------------|
| `setSchedulerName( name )` | Set the human-readable name for this scheduler |
| `setTimezone( timezone )` | Set the timezone for all tasks (default: system timezone) |
| `setContext( context )` | Set the BoxLang context for task execution |
| `task( name )` | Register a new task with the given name |
| `xtask( name )` | Register a new task but disable it immediately (useful for debugging) |
| `startup()` | Start the scheduler and all its tasks |
| `shutdown()` | Shutdown the scheduler gracefully |
| `restart()` | Restart the scheduler |
| `removeTask( name )` | Remove a task from the scheduler |
| `hasTask( name )` | Check if a task is registered |
| `getTaskRecord( name )` | Get the task record for a specific task |
| `getTaskStats()` | Get statistics for all tasks |
| `getRegisteredTasks()` | Get a list of all registered task names |


## 🚀 Scheduling Tasks

Now that we have seen the capabilities of the scheduler, let's dive deep into scheduling tasks with the `task( name )` method.

### 📝 Registering Tasks

Once you call this method, the scheduler will create a `ScheduledTask` object for you, configure it, and register it. The task object provides a fluent API for configuring when and how the task should run.

```javascript
task( "my-task" )
```

### 🎯 Task Closure/Lambda/Object

You register the callable event via the `call()` method on the task object. You can register a closure/lambda or an object. If you register an object, then we will call the object's `run()` method by default, but you can change it using the `method` argument and call any public method.

```javascript
// Lambda Syntax
task( "my-task" )
    .call( () => runCleanup() )
    .everyHour();

// Closure Syntax
task( "my-task" )
    .call( function(){
        // task here
        println( "Task executed at: " & now() );
    } )
    .everyHourAt( 45 );

// Object with run() method
task( "my-task" )
    .call( createObject( "MyTaskObject" ) )
    .everyDay()

// Object with a custom method
task( "my-task" )
    .call( createObject( "MyTaskObject" ), "reapCache" )
    .everydayAt( "13:00" )
```

### ⏰ Frequencies

There are many many frequency methods in scheduled tasks that will enable the tasks in specific intervals. Every time you see that an argument receives a `timeUnit` the available options are:

* days
* hours
* minutes
* seconds
* **milliseconds (default)**
* microseconds
* nanoseconds

Ok, let's go over the frequency methods:

| Frequency Method                       | Description                                                                  |
| -------------------------------------- | ---------------------------------------------------------------------------- |
| `every( period, timeunit )`            | Run the task every custom period of execution                                |
| `spacedDelay( spacedDelay, timeunit )` | Run the task every custom period of execution but with NO overlaps           |
| `everyMinute()`                        | Run the task every minute from the time it get's scheduled                   |
| `everyHour()`                          | Run the task every hour from the time it get's scheduled                     |
| `everyHourAt( minutes )`               | Set the period to be hourly at a specific minute mark and 00 seconds         |
| `everyDay()`                           | Run the task every day at midnight                                           |
| `everyDayAt( time )`                   | Run the task daily with a specific time in 24 hour format: HH:mm             |
| `everyWeek()`                          | Run the task every Sunday at midnight                                        |
| `everyWeekOn( day, time )`             | Run the task weekly on the given day of the week and time                    |
| `everyMonth()`                         | Run the task on the first day of every month at midnight                     |
| `everyMonthOn( day, time )`            | Run the task every month on a specific day and time                          |
| `onFirstBusinessDayOfTheMonth( time )` | Run the task on the first Monday of every month                              |
| `onLastBusinessDayOfTheMonth( time )`  | Run the task on the last business day of the month                           |
| `everyYear()`                          | Run the task on the first day of the year at midnight                        |
| `everyYearOn( month, day, time )`      | Set the period to be weekly at a specific time at a specific day of the week |
| `onWeekends( time )`                   | Run the task on Saturday and Sunday                                          |
| `onWeekdays( time )`                   | Run the task only on weekdays at a specific time.                            |
| `onMondays( time )`                    | Only on Mondays                                                              |
| `onTuesdays( time )`                   | Only on Tuesdays                                                             |
| `onWednesdays( time )`                 | Only on Wednesdays                                                           |
| `onThursdays( time )`                  | Only on Thursdays                                                            |
| `onFridays( time )`                    | Only on Fridays                                                              |
| `onSaturdays( time )`                  | Only on Saturdays                                                            |
| `onSundays( time )`                    | Only on Sundays                                                              |

{% hint style="success" %}
All `time` arguments are defaulted to midnight (00:00)
{% endhint %}

### 🚫 Preventing Overlaps / Stacking

By default all tasks that have interval rates/periods that will execute on that interval schedule. However, what happens if a task takes longer to execute than the period? Well, by default the task will not execute if the previous one has not finished executing, causing the pending task to execute immediately after the current one completes ( Stacking Tasks ). If you want to prevent this behavior, then you can use the `withNoOverlaps()` method and BoxLang will register the tasks with a _fixed delay_. Meaning the intervals do not start counting until the last task has finished executing.

```javascript
task( "test" )
	.call( () => createObject( "CacheService" ).reap() )
	.everyMinute()
	.withNoOverlaps();
```

{% hint style="success" %}
Spaced delays are a feature of the Scheduled Executors. There is even a `spacedDelay( delay, timeUnit )` method in the Task object.
{% endhint %}

### ⏳ Delaying First Execution

Every task can also have an initial delay of first execution by using the `delay()` method.

```javascript
/**
 * Set a delay in the running of the task that will be registered with this schedule
 *
 * @delay The delay that will be used before executing the task
 * @timeUnit The time unit to use, available units are: days, hours, microseconds, milliseconds, minutes, nanoseconds, and seconds. The default is milliseconds
 */
ScheduledTask function delay( numeric delay, timeUnit = "milliseconds" )
```

The `delay` is numeric and the `timeUnit` can be:

* days
* hours
* minutes
* seconds
* **milliseconds (default)**
* microseconds
* nanoseconds

```javascript
// Lambda Syntax
task( "my-task" )
    .call( () => wirebox.getInstance( "MyObject" ).runcleanup() )
    .delay( "5000" )
    .everyHour();
```

{% hint style="info" %}
Please note that the `delay` pushes the execution of the task into the future only for the first execution.
{% endhint %}

### 🎯 One Off Tasks

Apart from registering tasks that have specific intervals/frequencies you can also register tasks that can be executed **ONCE** **ONLY**. These are great for warming up caches, registering yourself with control planes, setting up initial data collections and so much more.

Basically, you don't register a frequency just the callable event. Usually, you can also combine them with a delay of execution, if you need them to fire off after certain amount of time has passed.

```javascript
task( "build-up-cache" )
    .call( () => createObject( "MyService" ).buildCache() )
    .delay( 1, "minutes" );

task( "notify-admin-server-is-up" )
    .call( () => createObject( "NotificationService" ).notifyAppIsUp( getServerIP() ) )
    .delay( 30, "seconds" );

task( "register-container" )
    .call( () => createObject( "RegistrationService" ).register() )
    .delay( 30, "seconds" );
```

### 🔄 Life-Cycle Methods

We already saw that a scheduler has life-cycle methods, but a task can also have several useful life-cycle methods:

| Method                | Description                                                   |
| --------------------- | ------------------------------------------------------------- |
| `after( target )`     | Store the closure to execute after the task executes: `function( task, results )` |
| `before( target )`    | Store the closure to execute before the task executes: `function( task )` |
| `onFailure( target )` | Store the closure to execute if there is a failure running the task: `function( task, exception )` |
| `onSuccess( target )` | Store the closure to execute if the task completes successfully: `function( task, results )` |

```javascript
task( "testharness-Heartbeat" )
	.call( function() {
		if ( randRange(1, 5) == 1 ){
			throw( message = "I am throwing up randomly!", type="RandomThrowup" );
		}
		println( "====> I am in a test harness test schedule!" );
	} )
	.every( "5", "seconds" )
	.before( function( task ) {
		println( "====> Running before the task!" );
	} )
	.after( function( task, results ){
		println( "====> Running after the task!" );
	} )
	.onFailure( function( task, exception ){
		println( "====> test schedule just failed!! #exception.message#" );
	} )
	.onSuccess( function( task, results ){
		println( "====> Test scheduler success : Stats: #task.getStats().toString()#" );
	} );
```

### 🌍 Timezone

By default, all tasks will ask the scheduler for the timezone to run in. However, you can override it on a task-by-task basis using the `setTimezone( timezone )` method:

```javascript
setTimezone( "America/Chicago" )
```

{% hint style="success" %}
You can find all valid time zone Id's here: [https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/time/ZoneId.html](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/time/ZoneId.html)
{% endhint %}

{% hint style="warning" %}
Remember that some timezones utilize daylight savings time. When daylight saving time changes occur, your scheduled task may run twice or even not run at all. For this reason, we recommend avoiding timezone scheduling when possible.
{% endhint %}

### ✅ Truth Test Constraints

There are many ways to constrain the execution of a task. However, you can register a `when()` closure that will be executed at runtime and boolean evaluated. If `true`, then the task can run, else it is disabled.

```javascript
task( "my-task" )
    .call( () => createObject( "UserService" ).cleanOldUsers() )
    .daily()
    .when( function(){
        // Can we run this task?
        return true;
    } );
```

### 📅 Start and End Dates

All scheduled tasks support the ability to seed in the **startOnDateTime** and **endOnDateTime** dates via our DSL:

* `startOn( date, time = "00:00" )`
* `endOn( date, time = "00:00" )`

This means that you can tell the scheduler when the task will become active on a specific date and time (using the scheduler's timezone), and when the task will become disabled.

```javascript
task( "restricted-task" )
  .call( () => createObject( "MaintenanceService" ).performMaintenance() )
  .everyHour()
  .startOn( "2022-01-01", "00:00" )
  .endOn( "2022-04-01" )
```

### 🕐 Start and End Times

All scheduled tasks support the ability to seed in the **startTime** and **endTime** dates via our DSL:

* `startOnTime( time = "00:00" )`
* `endOnTime( time = "00:00" )`
* `between( startTime = "00:00", endTime "00:00" )`

This means that you can tell the scheduler to restrict the execution of the task after and/or before a certain time (using the scheduler's timezone).

```javascript
task( "restricted-task" )
  .call( () => createObject( "ReportService" ).generateReport() )
  .everyMinute()
  .between( "09:00", "17:00" )
```

### ⏸️ Disabling/Pausing Tasks

Every task is runnable from registration according to the frequency you set. However, you can manually disable a task using the `disable()` method:

```javascript
task( "my-task" )
    .call( () => createObject( "SecurityService" ).cleanOldUsers() )
    .daily()
    .disable();
```

Once you are ready to enable the task, you can use the `enable()` method:

```javascript
myTask.enable()
```

{% hint style="warning" %}
Registering a task as disabled can lead to a task continuing to execute if it was later enabled and then removed via `removeTask( name )` and not disabled again before doing so.
{% endhint %}

### 📊 Task Stats

All tasks keep track of themselves and have lovely metrics. You can use the `getStats()` method to get a a snapshot `structure` of the stats in time. Here is what you get in the stats structure:

| Metric          | Description                                               |
| --------------- | --------------------------------------------------------- |
| `created`       | The timestamp of when the task was created in memory      |
| `inetHost`      | The hostname of the machine this task is registered with  |
| `lastRun`       | The last time the task ran                                |
| `lastResult`    | The last result the task callable produced                |
| `localIp`       | The ip address of the server this task is registered with |
| `neverRun`      | A boolean flag indicating if the task has NEVER been ran  |
| `nextRun`       | When the task will run next                               |
| `totalFailures` | How many times the task has failed execution              |
| `totalRuns`     | How many times the task has run                           |
| `totalSuccess`  | How many times the task has run and succeeded             |

```javascript
/**
 * Called after ANY task runs
 *
 * @task The task that got executed
 * @result The result (if any) that the task produced
 */
function afterAnyTask( required task, result ){
	logger.info( "task #task.getName()# just ran. Metrics: #task.getStats().toString()#" );
}
```

### 🛠️ Task Helpers

We have created some useful methods that you can use when working with asynchronous tasks:

| Method                     | Description                                                                                                                                                                          |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `debug( boolean )`         | Enable / disable debug output stream                                                                                                                                                 |
| `err( var )`               | Send output to the error stream                                                                                                                                                      |
| `hasScheduler()`           | Verifies if the task is assigned a scheduler or not                                                                                                                                  |
| `isDisabled()`             | Verifies if the task has been disabled by bit                                                                                                                                        |
| `isConstrained()`          | Verifies if the task has been constrained to run by dayOfMonth, dayOfWeek, firstBusinessDay, lastBusinessDay, weekdays, weekends, startOnDateTime, endOnDateTime, startTime, endTime |
| `out( var )`               | Send output to the output stream                                                                                                                                                     |
| `start()`                  | This kicks off the task into the scheduled executor manually. This method is called for you by the scheduler upon application startup or module loading.                             |
| `setMeta( struct )`        | Set the meta struct of the task. This is a placeholder for any data you want to be made available to you when working with a task.                                                   |
| `setMetaKey( key, value )` | Set a key on the custom meta struct.                                                                                                                                                 |
| `deleteMetaKey( key )`     | Delete a key from the custom meta struct.                                                                                                                                            |


## 🌐 Global Schedulers

The global schedulers are the default schedulers that are registered upon startup. These are defined in the `schedulers` property of the configuration file we have seen above. You can define multiple global schedulers that can be used throughout your application.

## 📱 Per-Application Schedulers

The per-application schedulers are the schedulers that are registered for a specific application using the `Application.bx`.  Just use the `this.schedulers` property to define the schedulers you want to register for your application. This is useful if you want to have different schedulers for different applications in your BoxLang environment.

```javascript
class{

    this.schedulers = [
        "config/YourAppScheduler.bx",
        "/myMapping/YourAppScheduler.bx"
    ]

}
```

Please note that you do not need to register absolute paths for schedulers in your application, you can use relative paths or even per-app mappings. The `SchedulerService` will automatically resolve the paths for you.  Once your application starts, the `SchedulerService` will register all the schedulers defined in the `this.schedulers` property.  Once the application stops, the `SchedulerService` will automatically shutdown all the schedulers and their associated executors.

## 💻 CLI Runner

You can also run schedulers from the command line using the BoxLang CLI. This is useful for running scheduled tasks in CI/CD pipelines, containerized environments, system cron jobs, or for testing purposes. The CLI runner provides a standalone way to execute scheduler files directly from the operating system level.

### Command Syntax

```bash
# Using BoxLang binary
boxlang schedule <SCHEDULER_FILE>

# Using Java JAR
java -jar boxlang.jar schedule <SCHEDULER_FILE>
```

### Requirements

* **File Extension**: Must be a `.bx` (BoxLang) file
* **File Content**: Should contain a BoxLang component with scheduler definitions
* **File Path**: Can be absolute or relative to current directory

### Lifecycle

When you run a scheduler via the CLI, BoxLang follows this lifecycle:

1. **🔍 File Validation**: The file is checked for existence and proper `.bx` extension
2. **⚙️ Compilation**: File is compiled and validated for syntax errors
3. **🏗️ Instantiation**: Scheduler component is instantiated with injected dependencies
4. **📋 Registration**: Scheduler is registered with the BoxLang SchedulerService
5. **🚀 Startup**: All configured tasks begin execution according to their schedules
6. **⏳ Blocking**: Process runs continuously until manually stopped
7. **🛑 Graceful Shutdown**: Press `Ctrl+C` to gracefully shutdown all tasks

### Examples

```bash
# ⏰ Run a basic scheduler
boxlang schedule ./schedulers/MainScheduler.bx

# 📁 Run scheduler with absolute path
boxlang schedule /opt/myapp/schedulers/TaskRunner.bx

# 🔧 Run scheduler in project directory
cd /my/project && boxlang schedule schedulers/CronJobs.bx

# 🐛 Run with debug mode enabled
boxlang --bx-debug schedule ./MyScheduler.bx

# ⚙️ Run with custom configuration
boxlang --bx-config ./custom.json schedule ./MyScheduler.bx
```

### CLI Help

You can get detailed help for the schedule command:

```bash
boxlang schedule --help
# or
boxlang schedule -h
```

This displays comprehensive usage information, requirements, and examples.

### Error Handling

The CLI runner provides clear error messages for common issues:

```bash
# ❌ Wrong file extension
boxlang schedule myfile.txt
# Error: Scheduler must be a .bx file, found: myfile.txt

# ❌ File not found
boxlang schedule nonexistent.bx
# Error: The template [nonexistent.bx] does not exist.

# ❌ Missing file argument
boxlang schedule
# Error: schedule command requires a scheduler file path. Use: boxlang schedule --help
```

### Integration with System Services

The CLI runner is perfect for integration with system-level schedulers and process managers:

#### **Systemd Service (Linux)**

```ini
# /etc/systemd/system/myapp-scheduler.service
[Unit]
Description=MyApp Scheduler Service
After=network.target

[Service]
Type=simple
User=myapp
WorkingDirectory=/opt/myapp
ExecStart=/usr/local/bin/boxlang schedule schedulers/MainScheduler.bx
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

#### **Docker Container**

```dockerfile
FROM ortussolutions/boxlang:latest

COPY schedulers/ /app/schedulers/
WORKDIR /app

# Run the scheduler
CMD ["boxlang", "schedule", "schedulers/MainScheduler.bx"]
```

#### **Cron Job (OS Level)**

```bash
# Run scheduler every hour via cron
0 * * * * /usr/local/bin/boxlang schedule /opt/myapp/schedulers/HourlyTasks.bx

# Run scheduler at system boot
@reboot /usr/local/bin/boxlang schedule /opt/myapp/schedulers/StartupTasks.bx
```

### Environment Variables

You can use BoxLang environment variables with the CLI runner:

```bash
# Set debug mode
export BOXLANG_DEBUG=true
boxlang schedule MyScheduler.bx

# Custom configuration
export BOXLANG_CONFIG=/path/to/config.json
boxlang schedule MyScheduler.bx

# Custom runtime home
export BOXLANG_HOME=/opt/boxlang
boxlang schedule MyScheduler.bx
```

### Logging and Monitoring

The CLI runner integrates with BoxLang's logging system:

```javascript
// In your scheduler class
class {
    property name="scheduler";
    property name="logger";

    function configure(){
        // Log scheduler startup
        logger.info( "CLI Scheduler starting up..." );

        scheduler.task( "monitoring-task" )
            .call( () => {
                logger.info( "Monitoring task executed at: " & now() );
                // Your monitoring logic here
            })
            .every( 30, "seconds" );
    }

    void function onStartup(){
        logger.info( "✅ CLI Scheduler [#scheduler.getSchedulerName()#] is now running" );
    }

    void function onShutdown(){
        logger.info( "🛑 CLI Scheduler [#scheduler.getSchedulerName()#] has been stopped" );
    }
}
```

### Process Management

When running via CLI, you can manage the process using standard OS tools:

```bash
# Run in background
nohup boxlang schedule MyScheduler.bx > /var/log/myapp/scheduler.log 2>&1 &

# Get process ID
ps aux | grep "boxlang schedule"

# Stop gracefully (sends SIGTERM)
kill <PID>

# Force stop (sends SIGKILL)
kill -9 <PID>
```

### Use Cases

The CLI runner is ideal for:

* **🐳 Containerized Applications**: Run schedulers in Docker/Kubernetes
* **☁️ Cloud Functions**: Execute scheduled tasks in serverless environments
* **🔄 CI/CD Pipelines**: Run maintenance tasks during deployments
* **🖥️ System Administration**: Replace traditional cron jobs with BoxLang schedulers
* **🧪 Development & Testing**: Quickly test scheduler configurations
* **📊 Data Processing**: Run ETL jobs and data synchronization tasks
* **🔍 Monitoring**: Execute health checks and system monitoring tasks

This will instantiate the scheduler, configure it, start it, and run it until it's manually stopped or all tasks complete (for one-off tasks).

# 🎛️ Scheduler Management BIFs

BoxLang provides several Built-In Functions (BIFs) for managing schedulers at runtime. These functions allow you to interact with the scheduler service programmatically and manage schedulers dynamically.

## 🚀 schedulerStart()

Creates, registers, and starts a scheduler with the given instantiation class path.

**Syntax:**
```javascript
schedulerStart( className, [name], [force] )
```

**Parameters:**
- `className` (required): The class name to instantiate (e.g., "models.myapp.MyScheduler")
- `name` (optional): Override the scheduler name defined in the class
- `force` (optional): Force start the scheduler (default: true)

**Returns:** The scheduler object

**Example:**
```javascript
// Start a scheduler
myScheduler = schedulerStart( "config.MyScheduler" );

// Start with custom name
myScheduler = schedulerStart( "config.MyScheduler", "CustomName" );
```

## 🔍 schedulerGet()

Get a specific scheduler by name from the scheduler service.

**Syntax:**
```javascript
schedulerGet( name )
```

**Parameters:**
- `name` (required): The name of the scheduler to retrieve

**Returns:** The scheduler object

**Throws:** `IllegalArgumentException` if scheduler not found

**Example:**
```javascript
try {
    myScheduler = schedulerGet( "MyScheduler" );
    println( "Found scheduler: " & myScheduler.getSchedulerName() );
} catch( any e ) {
    println( "Scheduler not found: " & e.message );
}
```

## 📦 schedulerGetAll()

Get all registered schedulers as a struct.

**Syntax:**
```javascript
schedulerGetAll()
```

**Returns:** A struct containing all registered schedulers (key = scheduler name, value = scheduler object)

**Example:**
```javascript
allSchedulers = schedulerGetAll();
for( schedulerName in allSchedulers ) {
    println( "Scheduler: " & schedulerName );
    println( "Tasks: " & allSchedulers[ schedulerName ].getRegisteredTasks().toString() );
}
```

## 📋 schedulerList()

List all the scheduler names registered in the system.

**Syntax:**
```javascript
schedulerList()
```

**Returns:** An array of scheduler names

**Example:**
```javascript
schedulerNames = schedulerList();
println( "Available schedulers: " & schedulerNames.toString() );
```

## 🛑 schedulerShutdown()

Shutdown a scheduler by name gracefully or forcefully.

**Syntax:**
```javascript
schedulerShutdown( name, [force], [timeout] )
```

**Parameters:**
- `name` (required): The name of the scheduler to shutdown
- `force` (optional): Force shutdown the scheduler (default: false)
- `timeout` (optional): Timeout in seconds to wait for graceful shutdown (default: 30)

**Example:**
```javascript
// Graceful shutdown
schedulerShutdown( "MyScheduler" );

// Force shutdown with custom timeout
schedulerShutdown( "MyScheduler", true, 60 );
```

## 🔄 schedulerRestart()

Restart a scheduler by name (shutdown then startup).

**Syntax:**
```javascript
schedulerRestart( name, [force], [timeout] )
```

**Parameters:**
- `name` (required): The name of the scheduler to restart
- `force` (optional): Force restart the scheduler (default: false)
- `timeout` (optional): Timeout in seconds to wait for shutdown (default: 30)

**Example:**
```javascript
// Graceful restart
schedulerRestart( "MyScheduler" );

// Force restart with custom timeout
schedulerRestart( "MyScheduler", true, 60 );
```

## 📊 schedulerStats()

Get statistics for all schedulers or a specific scheduler.

**Syntax:**
```javascript
schedulerStats( [name] )
```

**Parameters:**
- `name` (optional): The name of the scheduler to get stats for (if not provided, returns stats for all schedulers)

**Returns:** Stats struct(s) containing:
- `created`: When the task was created
- `lastExecutionTime`: Duration of last execution
- `lastResult`: Result of last execution
- `lastRun`: When the task last ran
- `name`: Task name
- `neverRun`: Boolean indicating if task has never run
- `nextRun`: When the task will run next
- `totalFailures`: Number of failed executions
- `totalRuns`: Total number of executions
- `totalSuccess`: Number of successful executions

**Example:**
```javascript
// Get stats for all schedulers
allStats = schedulerStats();

// Get stats for specific scheduler
myStats = schedulerStats( "MyScheduler" );
for( taskName in myStats ) {
    task = myStats[ taskName ];
    println( "Task: #taskName# - Runs: #task.totalRuns# - Failures: #task.totalFailures#" );
}
```

## 💡 Example: Dynamic Scheduler Management

Here's a practical example of how you might use these BIFs to manage schedulers dynamically:

```javascript
// Check if scheduler exists
schedulerNames = schedulerList();
if( !arrayContains( schedulerNames, "MaintenanceScheduler" ) ) {
    // Start the scheduler if it doesn't exist
    maintenanceScheduler = schedulerStart( "schedulers.MaintenanceScheduler", "MaintenanceScheduler" );
    println( "Started maintenance scheduler" );
} else {
    // Get existing scheduler
    maintenanceScheduler = schedulerGet( "MaintenanceScheduler" );
    println( "Using existing maintenance scheduler" );
}

// Get and display stats
stats = schedulerStats( "MaintenanceScheduler" );
println( "Scheduler stats: " & serializeJSON( stats ) );

// Restart scheduler if needed
if( someCondition ) {
    println( "Restarting scheduler..." );
    schedulerRestart( "MaintenanceScheduler", false, 60 );
}
```

## 📄 Task Records

When tasks are registered in a scheduler, they are wrapped in a `TaskRecord` object that contains metadata about the task's lifecycle and execution state. You can access task records through the scheduler:

```javascript
// Get a specific task record
taskRecord = scheduler.getTaskRecord( "my-task" );

// Access task record properties
println( "Task name: " & taskRecord.name );
println( "Task group: " & taskRecord.group );
println( "Registered at: " & taskRecord.registeredAt );
println( "Scheduled at: " & taskRecord.scheduledAt );
println( "Is disabled: " & taskRecord.disabled );
println( "Has error: " & taskRecord.error );
if( taskRecord.error ) {
    println( "Error message: " & taskRecord.errorMessage );
}
```

### TaskRecord Properties

| Property | Description |
|----------|-------------|
| `name` | The task name |
| `group` | The task group |
| `task` | The actual ScheduledTask object |
| `future` | The ScheduledFuture object for the task |
| `scheduledAt` | When the task was scheduled |
| `registeredAt` | When the task was registered |
| `disabled` | Whether the task is disabled |
| `error` | Whether the task had an error during scheduling |
| `errorMessage` | The error message if any |
| `stacktrace` | The full stacktrace if any |
| `inetHost` | The hostname where the task is running |
| `localIp` | The IP address of the server |

## 💎 Best Practices

Here are some best practices when working with BoxLang scheduled tasks:

### 🎯 Task Design
* **Keep tasks focused**: Each task should have a single responsibility
* **Handle errors gracefully**: Use `onFailure()` callbacks to handle exceptions
* **Use appropriate timing**: Consider system load when scheduling frequent tasks
* **Leverage constraints**: Use time and date constraints to avoid unnecessary executions

### 🔧 Configuration
* **Use groups**: Organize related tasks into groups for better management
* **Set meaningful names**: Use descriptive task names for easier debugging
* **Configure metadata**: Store relevant information in task metadata
* **Choose appropriate executors**: Match executor types to your workload patterns

### 📊 Monitoring
* **Track statistics**: Use `getStats()` to monitor task performance
* **Implement logging**: Use life-cycle callbacks for comprehensive logging
* **Monitor for failures**: Set up alerts for task failures
* **Review execution times**: Watch for tasks that run longer than expected

### 🚀 Performance
* **Avoid overlaps**: Use `withNoOverlaps()` for long-running tasks
* **Optimize frequencies**: Don't schedule tasks more frequently than necessary
* **Use virtual executors**: For I/O-bound tasks, consider virtual thread executors
* **Clean up resources**: Ensure tasks properly clean up any resources they use

### 🔒 Reliability
* **Handle timezone changes**: Be aware of daylight saving time impacts
* **Plan for restarts**: Design tasks to handle application restarts gracefully
* **Use constraints wisely**: Combine multiple constraints to achieve desired scheduling
* **Test thoroughly**: Test your schedulers in different scenarios and environments

```javascript
// Example of a well-designed scheduler
class {
    property name="scheduler";
    property name="logger";

    function configure(){
        // Configure scheduler
        scheduler.setSchedulerName( "ProductionScheduler" );
        scheduler.setTimezone( "UTC" );

        // High-frequency monitoring task
        scheduler.task( "health-check", "monitoring" )
            .call( () => performHealthCheck() )
            .every( 30, "seconds" )
            .setMeta({ "critical": true })
            .onFailure( function( task, exception ) {
                logger.error( "Health check failed: " & exception.getMessage() );
                alertingService.sendAlert( "CRITICAL", "Health check failure" );
            });

        // Daily maintenance task
        scheduler.task( "daily-cleanup", "maintenance" )
            .call( () => performDailyCleanup() )
            .everyDayAt( "02:00" )
            .withNoOverlaps()
            .setMeta({ "department": "ops", "notification": true })
            .before( function( task ) {
                logger.info( "Starting daily cleanup..." );
            })
            .after( function( task, result ) {
                logger.info( "Daily cleanup completed. Duration: " & task.getStats().lastExecutionTime );
            });

        // Business day report
        scheduler.task( "business-report", "reports" )
            .call( () => generateBusinessReport() )
            .weekdays( "17:00" )
            .when( function() {
                // Only run if we have data to process
                return hasDataToProcess();
            })
            .setMeta({ "type": "report", "priority": "medium" });
    }
}
```

This comprehensive guide covers all the essential aspects of BoxLang's scheduled tasks framework. Whether you're building simple cron-like jobs or complex distributed scheduling systems, BoxLang's scheduler provides the tools and flexibility you need.