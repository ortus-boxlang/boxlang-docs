# Cache Provider Events

These events involve the higher-level management of cache providers (registration, shutdown, and clear operations).

| Event Name               | Data | Description                           |
| ------------------------ | :--: | ------------------------------------- |
| `afterCacheClearAll`     |      | After all caches have been cleared.   |
| `afterCacheRegistration` |      | After a cache provider is registered. |
| `afterCacheRemoval`      |      | After a cache provider is removed.    |
| `beforeCacheRemoval`     |      | Before a cache provider is removed.   |
| `beforeCacheReplacement` |      | Before a cache provider is replaced.  |
| `beforeCacheShutdown`    |      | Before a cache provider is shut down. |
| `afterCacheShutdown`     |      | After a cache provider has shut down. |
