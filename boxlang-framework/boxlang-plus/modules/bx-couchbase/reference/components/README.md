# 📚 Components

Complete reference for all Couchbase module Components.

## 🔒 Distributed Locking Components

Components for coordinating operations across multiple servers:

- [**CouchbaseLock**](CouchbaseLock.md) - Execute code with automatic distributed lock management

## 📖 Usage

### CouchbaseLock Component

```js
<bx:CouchbaseLock
    name="user-#userId#-update"
    cache="default"
    timeout="5"
    expires="30">

    // Critical section - only one server executes this at a time
    user = getUser(userId);
    user.balance += amount;
    saveUser(user);

</bx:CouchbaseLock>
```

## 🔗 Related Documentation

- [Distributed Locking Guide](../../distributed-locking.md) - Lock patterns and best practices
- [Built-In Functions](../built-in-functions/README.md) - BIF reference
- [Reference Overview](../README.md) - Configuration and settings