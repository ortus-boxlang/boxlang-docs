# SchedulerStats

Get the stats of all schedulers or a specific scheduler by name.

Each stats structure contains the following fields:

* created
* lastExecutionTime
* lastResult
* lastRun
* name
* neverRun
* nextRun
* totalFailures
* totalRuns
* totalSuccess
* ### Method Signature
* ```
  SchedulerStats(name=[string])
  ```
* #### Arguments

| Argument | Type     | Required | Description                                                                   | Default |
| -------- | -------- | -------- | ----------------------------------------------------------------------------- | ------- |
| `name`   | `string` | `false`  | The name of the scheduler to get stats on or if not passed for all schedulers |         |

* ### Examples
* ### Related
* [SchedulerGet](SchedulerGet.md)
* [SchedulerGetAll](SchedulerGetAll.md)
* [SchedulerList](SchedulerList.md)
* [SchedulerRestart](SchedulerRestart.md)
* [SchedulerShutdown](SchedulerShutdown.md)
* [SchedulerStart](SchedulerStart.md)
