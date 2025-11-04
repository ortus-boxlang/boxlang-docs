---
title: BoxCache Stores
---

Object stores are the foundational storage layer of the BoxLang cache engine. They provide the actual mechanism for storing, retrieving, and managing cached objects. While cache providers coordinate user interactions and act as a service layer, object stores handle the low-level data persistence and retrieval operations.

| Type                             | Description                                               |
| -------------------------------- | --------------------------------------------------------- |
| **BlackHoleStore**               | Mocking store, just simulates a store, nothing is stored. |
| **ConcurrentSoftReferenceStore** | Memory-sensitive storage leveraging Java Soft References. |
| **ConcurrentStore**              | Leverages concurrent hashmaps for storage.                |
| **FileSystemStore**              | Stores the cache items in a serialized fashion on disk    |
| **JDBCStore**                    | Distributed cache store backed by JDBC databases for multi-instance cache sharing |

Each store can have different configuration properties as well.
