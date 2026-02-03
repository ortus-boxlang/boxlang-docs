[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SchedulerStats`

Get the stats of all schedulers or a specific scheduler by name.

<p>
 Each stats structure contains the following fields:
 <ul>
 <li>created</li>
 <li>lastExecutionTime</li>
 <li>lastResult</li>
 <li>lastRun</li>
 <li>name</li>
 <li>neverRun</li>
 <li>nextRun</li>
 <li>totalFailures</li>
 <li>totalRuns</li>
 <li>totalSuccess</li>
 <ul>

## Method Signature

```
SchedulerStats(name=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `false` | The name of the scheduler to get stats on or if not passed for all schedulers |  |

## Examples



## Related

  * [SchedulerGet](./SchedulerGet.md)
  * [SchedulerGetAll](./SchedulerGetAll.md)
  * [SchedulerList](./SchedulerList.md)
  * [SchedulerRestart](./SchedulerRestart.md)
  * [SchedulerShutdown](./SchedulerShutdown.md)
  * [SchedulerStart](./SchedulerStart.md)
