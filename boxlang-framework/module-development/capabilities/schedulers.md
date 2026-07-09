---
description: Register scheduled tasks in your BoxLang module (Java only)
icon: clock
---

# Schedulers

{% hint style="warning" %}
Schedulers require **Java**. There is no BoxLang-only mechanism for registering module-level schedulers.
{% endhint %}

Schedulers provide cron-like scheduled task execution. They integrate with BoxLang's `SchedulerService`.

## Creating a Scheduler

Implement the `IScheduler` interface and register via ServiceLoader:

**File:** `src/main/java/ortus/boxlang/modules/mymodule/schedulers/CleanupScheduler.java`

```java
import ortus.boxlang.runtime.async.tasks.IScheduler;
import ortus.boxlang.runtime.async.tasks.BaseScheduler;
import ortus.boxlang.runtime.async.tasks.ScheduledTask;

public class CleanupScheduler extends BaseScheduler {

    @Override
    public void configure() {
        // Schedule a task every hour
        ScheduledTask task = task( "cleanup-temp-files" )
            .call( () -> {
                System.out.println( "Cleaning up temp files..." );
                // Cleanup logic
            })
            .everyHour()
            .onFailure( ( task, exception ) -> {
                getLogger().error( "Cleanup failed", exception );
            });

        register( task );
    }
}
```

**ServiceLoader Config:** `src/main/resources/META-INF/services/ortus.boxlang.runtime.async.tasks.IScheduler`

```
ortus.boxlang.modules.mymodule.schedulers.CleanupScheduler
```

## Scheduler Naming

Schedulers are automatically registered with the name `{schedulerName}@{moduleName}`. For example, a `CleanupScheduler` in a module named `myModule` is registered as `CleanupScheduler@myModule`.

## Available Patterns

The `BaseScheduler` provides a fluent API for common scheduling patterns:

```java
// Every 5 minutes
task( "my-task" )
    .call( () -> doWork() )
    .everyMinute( 5 );

// Daily at 2 AM
task( "daily-task" )
    .call( () -> doWork() )
    .daily( 2, 0 );

// Cron expression
task( "cron-task" )
    .call( () -> doWork() )
    .cron( "0 0 * * *" );
```

## Next Steps

- [Services](services.md) — Global runtime services (Java only)
- [Cache Providers](cache-providers.md) — Custom caching backends (Java only)
- [JDBC Drivers](jdbc-drivers.md) — Database driver registration (Java only)
