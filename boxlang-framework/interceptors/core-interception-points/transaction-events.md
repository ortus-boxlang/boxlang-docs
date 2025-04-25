# Transaction Events

These events are triggered during transaction lifecycles such as begin, commit, rollback, and savepoint operations.

| Event Name                  | Data | Description                              |
| --------------------------- | :--: | ---------------------------------------- |
| `onTransactionBegin`        |      | Transaction begins.                      |
| `onTransactionEnd`          |      | Transaction ends.                        |
| `onTransactionAcquire`      |      | Transaction is acquired.                 |
| `onTransactionRelease`      |      | Transaction is released.                 |
| `onTransactionCommit`       |      | Transaction is committed.                |
| `onTransactionRollback`     |      | Transaction is rolled back.              |
| `onTransactionSetSavepoint` |      | A savepoint is set within a transaction. |
