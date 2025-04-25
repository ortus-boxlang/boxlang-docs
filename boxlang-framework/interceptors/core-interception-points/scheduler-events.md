# Scheduler Events

These events relate to the lifecycle of schedulers and scheduled task execution.

| Event Name                  | Data | Description                            |
| --------------------------- | :--: | -------------------------------------- |
| `onSchedulerStartup`        |      | When a scheduler starts up.            |
| `onSchedulerShutdown`       |      | When a scheduler shuts down.           |
| `onSchedulerRestart`        |      | When a scheduler restarts.             |
| `schedulerBeforeAnyTask`    |      | Before any task is executed.           |
| `schedulerAfterAnyTask`     |      | After any task is executed.            |
| `schedulerOnAnyTaskSuccess` |      | After a task runs successfully.        |
| `schedulerOnAnyTaskError`   |      | When a scheduled task throws an error. |
