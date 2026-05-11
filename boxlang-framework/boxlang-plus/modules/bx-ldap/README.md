---
description: >-
  🔐 A comprehensive LDAP module for BoxLang that brings full-featured LDAP
  directory access to your applications!
icon: address-book
---

# LDAP +

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://ww.boxlang.io/plans) but can be installed in conjunction with the [`bx-plus` Module](../bx-plus/) with a limited trial.
{% endhint %}

This module provides powerful LDAP (Lightweight Directory Access Protocol) capabilities to the [BoxLang](https://boxlang.io) language, making it easy to query, modify, and manage directory services with minimal code.

## ✨ Features

- 🔍 **Query**: Search LDAP directories with filters, scopes, and pagination
- ➕ **Add**: Create new directory entries with multi-valued attributes
- ✏️ **Modify**: Update existing entries (replace/add/delete attributes)
- 🗑️ **Delete**: Remove directory entries
- 🔄 **ModifyDN**: Rename entries or move within directory tree
- 🔒 **Secure**: SSL/TLS support with certificate validation
- 🔑 **Authentication**: Simple bind and anonymous access
- 🎯 **Flexible Filtering**: Complex LDAP filters with boolean logic
- 📄 **Pagination**: Handle large result sets efficiently
- 🔌 **Connection Pooling**: Automatic connection management
- 🏢 **Enterprise Grade**: Built and Supported by Ortus Solutions

## 📦 Installation

### Requirements

- BoxLang 1.6+
- Access to an LDAP server (Active Directory, OpenLDAP, etc.)

### Install via CommandBox

If you are using CommandBox for your web applications, simply run:

```bash
box install bx-ldap@ortus
```

### Install via BoxLang OS Binary

If you are using the BoxLang OS Binary, simply run:

```bash
install-bx-module bx-ldap@ortus
```

The module will automatically register and be available as `bxldap` in your BoxLang applications.

## 🚀 Quick Start

Here's how to query an LDAP directory in just a few lines:

```java
bx:ldap
    action="query"
    server="ldap.example.com"
    port="389"
    result="users"
    start="dc=example,dc=org"
    filter="(objectClass=person)";

println( "Found #users.recordCount# users" );
```

That's it! 🎉 You now have LDAP query results in a BoxLang Query object.

## 🔧 LDAP Actions

The module supports seven core operations:

### 🔍 Query

Search the directory with filters, scopes, and attribute selection.

- **Use Case**: Find users, groups, or any directory objects
- **Returns**: BoxLang Query object with results (contains matched LDAP entries as rows with their attributes as columns)
- **Features**: Filtering, sorting, pagination, scope control
- **Empty Results**: Returns a Query with `recordCount=0` if no entries match (no exception thrown)

### ➕ Add

Create new entries in the directory.

- **Use Case**: Add new users, groups, organizational units
- **Supports**: Multi-valued attributes, all attribute types
- **Returns**: Boolean `true` on success
- **Error Handling**: Throws exception if entry already exists or DN is invalid

### ✏️ Modify

Update existing directory entries.

- **Use Case**: Update user information, group memberships
- **Operations**: Replace, add, or delete attributes
- **Returns**: Boolean `true` on success
- **Flexibility**: Modify multiple attributes in one operation
- **Error Handling**: Throws exception if entry does not exist or modification type is invalid

### 🗑️ Delete

Remove entries from the directory.

- **Use Case**: Delete obsolete users, groups, or objects
- **Returns**: Boolean `true` on success
- **Safety**: Validates entry exists before deletion (throws exception if not found)
- **Note**: Cannot delete entries with children (delete children first)
- **Error Handling**: Throws exception if entry has subordinate entries or does not exist

### 🔄 ModifyDN

Rename entries or move them within the directory tree.

- **Use Case**: Rename users, reorganize directory structure
- **Returns**: Boolean `true` on success
- **Operations**: Rename (change RDN) or move to different parent
- **Flexibility**: Supports both rename and move operations
- **Error Handling**: Throws exception if new DN is invalid or already exists

### 🔓 Open

Create and store a named connection for reuse across multiple operations.

- **Use Case**: Establish a connection with credentials that can be reused without repetition
- **Required Attributes**: `connection` (connection name), `server`, plus authentication details
- **Returns**: Connection object if `result` attribute is specified, otherwise ignored
- **Benefits**: Simplifies multi-operation workflows by eliminating credential repetition
- **Note**: Connection remains open until explicitly closed or application terminates

### 🔐 Close

Close and release a named connection.

- **Use Case**: Explicitly close a named connection to free resources
- **Required Attributes**: `connection` (connection name to close)
- **Returns**: Boolean `true` on success
- **Benefits**: Allows proper resource management for long-running applications
- **Note**: Once closed, connection can be reopened with same name if needed

## 📚 Component Reference

### 🔐 `<bx:ldap>` Component

The main component for all LDAP operations.

#### Core Attributes

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `action` | string | ✅ Yes | - | LDAP operation: "query", "add", "modify", "delete", "modifydn", "open", "close" |
| `server` | string | ⚠️ Conditional | - | LDAP server hostname or IP address. Required if `connection` is not provided. |
| `connection` | string | ⚠️ Conditional | - | Named connection to an LDAP server (previously created). Required if `server` is not provided. Allows reusing connection credentials across multiple operations. |
| `port` | number | - | 389 (636 for SSL) | LDAP server port |
| `result` | string | ⚠️ Query | - | Variable name to store query results (primary attribute for result handling) |
| `name` | string | - | - | **Deprecated**: Use `result` instead. Maintained for backwards compatibility with query actions only |
| `start` | string | ✅ Yes | - | Starting DN (Distinguished Name) for search or operation |

#### Authentication Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `username` | string | "" (anonymous) | Bind DN for authentication (e.g., "cn=admin,dc=example,dc=org") |
| `password` | string | "" (anonymous) | Password for authentication |
| `secure` | boolean/string | false | Security mode: `false` (no SSL), `true` (SSL), "CFSSL_BASIC" (server auth only), "CFSSL_CLIENT_AUTH" (mutual TLS) |
| `useTls` | boolean | false | Whether to use StartTLS extension to initiate SSL/TLS over normal port |
| `clientCert` | string | - | Full path to keystore file containing client certificate |
| `clientCertPassword` | string | - | Password for client certificate keystore |
| `timeout` | integer | 60000 | Operation timeout in milliseconds |

#### Query-Specific Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `filter` | string | "(objectClass=*)" | LDAP search filter (e.g., "(uid=jdoe)") |
| `scope` | string | "onelevel" | Search scope: "base", "onelevel", "subtree" |
| `attributes` | string | "*" | Comma-separated list of attributes to return |
| `sort` | string | - | Attribute name to sort results by |
| `sortDirection` | string | "asc" | Sort direction: "asc" or "desc" |
| `maxrows` | number | - | Maximum number of results to return |
| `startRow` | number | 1 | Starting row for pagination |
| `returnFormat` | string | "query" | Result format: "query" (Query object) or "array" (Array of structs) |

#### Modify-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `dn` | string | ✅ Yes | Distinguished Name of entry to modify |
| `attributes` | struct | ✅ Yes | Struct of attributes to modify (key=attribute, value=new value) |
| `modifyType` | string | "replace" | Modification type: "replace", "add", "delete" |

#### Add-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `dn` | string | ✅ Yes | Distinguished Name for new entry |
| `attributes` | struct | ✅ Yes | Struct of attributes for new entry |

#### Delete-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `dn` | string | ✅ Yes | Distinguished Name of entry to delete |

#### ModifyDN-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `dn` | string | ✅ Yes | Current Distinguished Name |
| `attributes` | struct | ✅ Yes | Struct with "newRDN" and optionally "newParentDN" |

## 💡 Examples

### Basic Examples

#### 🔍 Simple Query

Find all users in a directory:

```java
bx:ldap
    action="query"
    server="ldap.example.com"
    port="389"
    result="users"
    start="ou=users,dc=example,dc=org"
    filter="(objectClass=person)";

println( "Found #users.recordCount# users" );
```

**💡 Use Case:** Quick directory lookup to list all users.

#### 🔎 Filtered Search

Search for a specific user:

```java
bx:ldap
    action="query"
    server="ldap.example.com"
    port="389"
    result="user"
    start="dc=example,dc=org"
    scope="subtree"
    filter="(uid=jdoe)"
    attributes="cn,mail,telephoneNumber";

if( user.recordCount > 0 ){
    println( "Name: #user.cn#, Email: #user.mail#" );
} else {
    println( "User not found" );
}
```

**💡 Use Case:** User lookup with specific attributes for profile display.

#### ➕ Add New User

Create a new directory entry:

```java
newUser = {
    "objectClass": ["inetOrgPerson", "organizationalPerson", "person", "top"],
    "cn": "John Doe",
    "sn": "Doe",
    "uid": "jdoe",
    "mail": "john.doe@example.com",
    "userPassword": "SecurePassword123"
};

bx:ldap
    action="add"
    server="ldap.example.com"
    port="389"
    username="cn=admin,dc=example,dc=org"
    password="adminpass"
    dn="uid=jdoe,ou=users,dc=example,dc=org"
    attributes=newUser;

println( "User created successfully!" );
```

**💡 Use Case:** User registration or bulk user import.

#### ✏️ Modify User

Update an existing entry:

```java
updates = {
    "mail": "john.newemail@example.com",
    "telephoneNumber": "+1-555-0123"
};

bx:ldap
    action="modify"
    server="ldap.example.com"
    port="389"
    username="cn=admin,dc=example,dc=org"
    password="adminpass"
    dn="uid=jdoe,ou=users,dc=example,dc=org"
    modifyType="replace"
    attributes=updates;

println( "User updated successfully!" );
```

**💡 Use Case:** Profile updates, contact information changes.

#### 🗑️ Delete User

Remove an entry from the directory:

```java
bx:ldap
    action="delete"
    server="ldap.example.com"
    port="389"
    username="cn=admin,dc=example,dc=org"
    password="adminpass"
    dn="uid=jdoe,ou=users,dc=example,dc=org";

println( "User deleted successfully!" );
```

**💡 Use Case:** Account deactivation, cleanup of obsolete entries.

#### 🔄 Rename User

Change an entry's RDN (Relative Distinguished Name):

```java
renameOp = {
    "newRDN": "uid=johnd"
};

bx:ldap
    action="modifydn"
    server="ldap.example.com"
    port="389"
    username="cn=admin,dc=example,dc=org"
    password="adminpass"
    dn="uid=jdoe,ou=users,dc=example,dc=org"
    attributes=renameOp;

println( "User renamed from jdoe to johnd!" );
```

**💡 Use Case:** Username changes, standardizing naming conventions.

### Connection Management Examples

#### 🔌 Define and Reuse Named Connections

Create a named connection once and reuse it across multiple operations:

```java
// Define a connection once with all credentials
bx:ldap
    action="query"
    connection="myLdapConn"
    server="ldap.example.com"
    port="389"
    username="cn=admin,dc=example,dc=org"
    password="adminpass"
    start="dc=example,dc=org"
    filter="(objectClass=person)"
    result="users";

println( "Initial query found #users.recordCount# users" );

// Reuse the same named connection for subsequent operations
// No need to pass server, username, password again
bx:ldap
    action="query"
    connection="myLdapConn"
    start="ou=groups,dc=example,dc=org"
    filter="(objectClass=groupOfNames)"
    result="groups";

println( "Found #groups.recordCount# groups" );

// Use the connection for add operations
newGroup = {
    "objectClass": ["groupOfNames"],
    "cn": "developers",
    "member": "uid=jdoe,ou=users,dc=example,dc=org"
};

bx:ldap
    action="add"
    connection="myLdapConn"
    dn="cn=developers,ou=groups,dc=example,dc=org"
    attributes=newGroup;

println( "Group created successfully using reused connection" );
```

**💡 Use Case:** Simplifies code when performing multiple LDAP operations. Credentials are passed once, then the connection is reused by its name.

#### 🔓 Explicitly Open a Named Connection

Establish a connection with the `open` action for later reuse:

```java
// Explicitly open a named connection
bx:ldap
    action="open"
    connection="prodLdap"
    server="ldap.production.com"
    port="389"
    username="cn=service,dc=prod,dc=org"
    password="servicepass"
    timeout="30000";

println( "Connection 'prodLdap' opened and ready for reuse" );

// Now use the connection for various operations
// No need to pass credentials again

// Query operation
bx:ldap
    action="query"
    connection="prodLdap"
    start="ou=users,dc=prod,dc=org"
    filter="(department=IT)"
    result="itUsers";

// Add operation
bx:ldap
    action="add"
    connection="prodLdap"
    dn="uid=newuser,ou=users,dc=prod,dc=org"
    attributes={
        "objectClass": ["inetOrgPerson", "person"],
        "uid": "newuser",
        "cn": "New User",
        "sn": "User"
    };

// Modify operation
bx:ldap
    action="modify"
    connection="prodLdap"
    dn="uid=newuser,ou=users,dc=prod,dc=org"
    attributes={"mail": "newuser@production.com"}
    modifyType="replace";
```

**💡 Use Case:** Use `open` when you need explicit connection lifecycle management. Useful in microservices or long-running applications.

#### 🔐 Close a Named Connection

Explicitly close a connection to free resources:

```java
// Close a named connection
bx:ldap
    action="close"
    connection="prodLdap";

println( "Connection 'prodLdap' closed and resources released" );
```

**💡 Use Case:** Important for resource management in applications that maintain many connections or run for extended periods.

### Advanced Examples

#### 🔍 Complex Filter Query

Use advanced LDAP filter syntax:

```java
// Find active users in IT department created after a date
bx:ldap
    action="query"
    server="ldap.example.com"
    port="389"
    result="itUsers"
    start="dc=example,dc=org"
    scope="subtree"
    filter="(&(objectClass=person)(department=IT)(!(accountStatus=disabled))(createTimestamp>=20240101000000Z))"
    sort="cn"
    sortDirection="asc";

println( "Found #itUsers.recordCount# active IT users" );
```

**💡 Use Case:** Department reporting, audit queries, compliance checks.

**Filter Operators:**

- `&` - AND (all conditions must match)
- `|` - OR (any condition matches)
- `!` - NOT (negation)
- `=` - Equals
- `>=` - Greater than or equal
- `<=` - Less than or equal
- `=*` - Presence check (attribute exists)
- `=value*` - Starts with
- `=*value` - Ends with
- `=*value*` - Contains

#### 📄 Paginated Query

Handle large result sets efficiently:

```java
// Get 50 users at a time
pageSize = 50;
currentPage = 1;
startRow = ((currentPage - 1) * pageSize) + 1;

bx:ldap
    action="query"
    server="ldap.example.com"
    port="389"
    result="pagedUsers"
    start="ou=users,dc=example,dc=org"
    filter="(objectClass=person)"
    maxrows="#pageSize#"
    startRow="#startRow#"
    sort="cn";

println( "Showing #pagedUsers.recordCount# users (Page #currentPage#)" );
```

**💡 Use Case:** User management interfaces, large directory browsing.

#### � Query Results as Array

Return results as an array of structs instead of a Query object:

```java
// Query returning array format
bx:ldap
    action="query"
    server="ldap.example.com"
    port="389"
    result="userArray"
    start="ou=users,dc=example,dc=org"
    filter="(objectClass=person)"
    returnFormat="array"
    sort="cn";

// Iterate over array results
userArray.each( user () => {
    println( "User: #user.cn# (Email: #user.mail#)" );
} );

// Or serialize to JSON for API responses
apiResponse = {
    "success": true,
    "users": userArray,
    "count": userArray.len()
};

println( jsonSerialize( apiResponse ) );
```

**💡 Use Case:** JSON API responses, data transformation, modern data handling patterns.

**Supported Formats:**

- `"query"` - Returns BoxLang Query object (default) - good for compatibility with traditional CFML patterns
- `"array"` - Returns Array of Structs - better for JSON APIs and modern applications

#### �🔒 SSL/TLS Secure Connection

Connect securely with SSL:

```java
bx:ldap
    action="query"
    server="ldaps.example.com"
    port="636"
    secure="false"
    result="secureUsers"
    start="dc=example,dc=org"
    filter="(objectClass=person)";

println( "Secure query returned #secureUsers.recordCount# users" );
```

**💡 Use Case:** Production environments, sensitive data access, compliance requirements.

#### 🔐 Mutual TLS Authentication

Use client certificates for authentication:

```java
bx:ldap
    action="query"
    server="ldaps.example.com"
    port="636"
    secure="true"
    username="cn=app,dc=example,dc=org"
    password="apppass"
    result="users"
    start="dc=example,dc=org";

println( "Authenticated with client certificate" );
```

**💡 Use Case:** High-security environments, API integrations, service accounts.

#### ➕ Add Entry with Multiple Values

Create an entry with multi-valued attributes:

```java
newGroup = {
    "objectClass": ["groupOfNames", "top"],
    "cn": "Developers",
    "member": [
        "uid=jdoe,ou=users,dc=example,dc=org",
        "uid=jsmith,ou=users,dc=example,dc=org",
        "uid=alee,ou=users,dc=example,dc=org"
    ],
    "description": "Development Team"
};

bx:ldap
    action="add"
    server="ldap.example.com"
    port="389"
    username="cn=admin,dc=example,dc=org"
    password="adminpass"
    dn="cn=Developers,ou=groups,dc=example,dc=org"
    attributes=newGroup;

println( "Group created with multiple members!" );
```

**💡 Use Case:** Group management, access control lists, distribution lists.

#### ✏️ Add Attribute Values

Add values to existing multi-valued attributes:

```java
// Add new members to existing group
newMembers = {
    "member": [
        "uid=bmiller,ou=users,dc=example,dc=org",
        "uid=kchen,ou=users,dc=example,dc=org"
    ]
};

bx:ldap
    action="modify"
    server="ldap.example.com"
    port="389"
    username="cn=admin,dc=example,dc=org"
    password="adminpass"
    dn="cn=Developers,ou=groups,dc=example,dc=org"
    modifyType="add"
    attributes=newMembers;

println( "New members added to group!" );
```

**💡 Use Case:** Group membership management, role assignments.

#### 🗑️ Delete Attribute Values

Remove specific values from multi-valued attributes:

```java
// Remove a member from group
removeMember = {
    "member": "uid=jsmith,ou=users,dc=example,dc=org"
};

bx:ldap
    action="modify"
    server="ldap.example.com"
    port="389"
    username="cn=admin,dc=example,dc=org"
    password="adminpass"
    dn="cn=Developers,ou=groups,dc=example,dc=org"
    modifyType="delete"
    attributes=removeMember;

println( "Member removed from group!" );
```

**💡 Use Case:** Membership revocation, access control updates.

#### 🔄 Move Entry to Different OU

Move an entry to a different organizational unit:

```java
moveOp = {
    "newRDN": "uid=jdoe",
    "newParentDN": "ou=contractors,dc=example,dc=org"
};

bx:ldap
    action="modifydn"
    server="ldap.example.com"
    port="389"
    username="cn=admin,dc=example,dc=org"
    password="adminpass"
    dn="uid=jdoe,ou=employees,dc=example,dc=org"
    attributes=moveOp;

println( "User moved from employees to contractors!" );
```

**💡 Use Case:** Organizational restructuring, employee status changes.

## ⚠️ Error Handling

### Understanding Empty Results

**Important:** LDAP queries return **empty Query objects** (recordCount=0) instead of throwing exceptions when:

- Entry does not exist
- Filter matches no entries
- Insufficient permissions (sometimes)
- Entry was deleted

```java
bx:ldap
    action="query"
    server="ldap.example.com"
    port="389"
    result="user"
    start="dc=example,dc=org"
    filter="(uid=nonexistent)";

// Check for empty results
if( user.recordCount == 0 ){
    println( "User not found" );
} else {
    println( "Found user: #user.cn#" );
}
```

### Exception Handling

Handle connection and operation errors:

```java
try {
    ldap
        action="modify"
        server="ldap.example.com"
        port="389"
        username="cn=admin,dc=example,dc=org"
        password="adminpass"
        dn="uid=jdoe,ou=users,dc=example,dc=org"
        attributes=updates;

    println( "Operation successful!" );

} catch( any e ) {
    println( "Error: #e.message#" );
    println( "Detail: #e.detail#" );
}
```

### Common Error Scenarios

| Error | Cause | Solution |
|-------|-------|----------|
| Connection timeout | Server unreachable | Check server hostname, port, firewall |
| Invalid credentials | Wrong username/password | Verify bind DN and password |
| Entry already exists | Duplicate DN in add | Use unique DN or modify existing entry |
| No such object | DN doesn't exist | Verify DN syntax and entry existence |
| Insufficient access | Permission denied | Check ACLs and bind user permissions |
| Invalid DN syntax | Malformed DN | Validate DN format: `uid=user,ou=org,dc=example,dc=org` |

## 🎯 Best Practices

### Security

- ✅ **Always use SSL/TLS in production** (`secure="true"`)
- ✅ **Never hardcode credentials** - use environment variables or secure vaults
- ✅ **Use least privilege** - bind with minimum required permissions
- ✅ **Validate user input** - sanitize filter parameters to prevent LDAP injection
- ✅ **Implement connection timeouts** - prevent hanging operations
- ✅ **Use service accounts** - dedicated accounts for application access
- ✅ **Rotate passwords regularly** - follow security policies
- ✅ **Log security events** - audit all modify/add/delete operations

### Performance

- ✅ **Use specific filters** - narrow searches with precise LDAP filters
- ✅ **Limit attribute retrieval** - only request needed attributes
- ✅ **Implement pagination** - use `maxrows` and `startRow` for large result sets
- ✅ **Choose appropriate scope** - use "base" or "onelevel" when possible
- ✅ **Cache results** - cache frequently accessed data
- ✅ **Use indexed attributes** - filter on indexed attributes for speed
- ✅ **Connection pooling** - automatically handled by Apache Directory API

### Filter Optimization

- ✅ **Put most restrictive filters first** - in AND operations
- ✅ **Use equality over substring** - `(uid=jdoe)` faster than `(uid=*jdoe*)`
- ✅ **Avoid leading wildcards** - `(cn=John*)` faster than `(cn=*John)`
- ✅ **Combine filters efficiently** - use `(&(attr1=val1)(attr2=val2))` not multiple queries

### Directory Structure

- ✅ **Follow DN conventions** - consistent naming schemes
- ✅ **Use organizational units** - logical grouping (ou=users, ou=groups)
- ✅ **Plan DN hierarchy** - consider future growth and reorganization
- ✅ **Document schema** - maintain documentation of custom attributes

## 📢 Event Handling

The LDAP module announces events at key points in the connection lifecycle, allowing you to monitor, audit, and react to connection operations. These events are dispatched through BoxLang's interception system.

### Available Events

#### `onLDAPConnectionOpen`

Announced when an LDAP connection is successfully opened (either new or from pool).

**Event Payload:**

```java
{
    "context": context,           // BoxLang context
    "connection": connection,     // The opened LDAP connection object
    "result": connectionName,     // Named connection reference (if used)
    "attributes": attributes      // Original component attributes
}
```

**Example Interceptor:**

```java
class {
    function onLDAPConnectionOpen( struct eventData ) {
        var connectionName = eventData.result;
        if ( connectionName.len() ) {
            logger.info( "Named LDAP connection opened: #connectionName#" );
        } else {
            logger.info( "Anonymous LDAP connection opened to #eventData.attributes.server#" );
        }
    }
}
```

#### `onLDAPConnectionClose`

Announced when an LDAP connection is closed or removed from the pool.

**Event Payload:**

```java
{
    "context": context,           // BoxLang context
    "result": connectionName,     // Named connection being closed
    "returnValue": true,          // Success flag
    "attributes": attributes      // Original component attributes
}
```

**Example Interceptor:**

```java
class {
    function onLDAPConnectionClose( struct eventData ) {
        if ( eventData.returnValue ) {
            writeLog( text:"LDAP connection closed: #eventData.result#" , log: "ldap");
        } else {
            writeLog( text:"Failed to close LDAP connection: #eventData.result#" , log: "ldap");
        }
    }
}
```

### Connection Monitoring Example

Create an interceptor to monitor all connection lifecycle events:

```java
// Interceptor.bx
class {

    function onLDAPConnectionOpen( struct eventData ) {
        var conn = eventData.result ?: "default";
        writeLog( text:"LDAP Connection opened: #conn#" , log: "ldap");
    }

    function onLDAPConnectionClose( struct eventData ) {
        var conn = eventData.result;
        var status = eventData.returnValue ? "success" : "failed";
        writeLog( text:"LDAP Connection closed (#status#): #conn#" , log: "ldap");
    }
}
```

## ❓ Troubleshooting

### Connection Issues

**Problem:** Cannot connect to LDAP server.

**Solutions:**

- ✅ Verify server hostname and port (389 standard, 636 SSL)
- ✅ Check firewall rules allow LDAP traffic
- ✅ Test connectivity with `telnet ldap.example.com 389`
- ✅ Verify DNS resolution of hostname
- ✅ Check LDAP server is running and accepting connections
- ✅ Review LDAP server logs for connection attempts

### Authentication Failures

**Problem:** Invalid credentials or bind failure.

**Solutions:**

- ✅ Verify bind DN format: `cn=admin,dc=example,dc=org`
- ✅ Confirm password is correct (no extra spaces)
- ✅ Check if account is locked or disabled
- ✅ Verify user has appropriate permissions
- ✅ For Active Directory: use `user@domain.com` or `DOMAIN\user` format
- ✅ Test credentials with LDAP browser tool (Apache Directory Studio)

### Query Returns No Results

**Problem:** Query completes but returns 0 results.

**Solutions:**

- ✅ Verify `start` DN exists in directory
- ✅ Check filter syntax is correct
- ✅ Confirm scope is appropriate ("base" vs "onelevel" vs "subtree")
- ✅ Verify bind user has read permissions on entries
- ✅ Test filter with LDAP browser tool
- ✅ Check for typos in attribute names
- ✅ Confirm entries actually exist in search base

### SSL/TLS Issues

**Problem:** SSL handshake failure or certificate errors.

**Solutions:**

- ✅ Verify port 636 is used for LDAPS (not 389)
- ✅ Check server certificate is valid and not expired
- ✅ Import server certificate into Java truststore
- ✅ For self-signed certs: add to trusted certificates
- ✅ Verify certificate hostname matches server hostname
- ✅ Check for certificate chain issues

### Modify/Add/Delete Failures

**Problem:** Write operations fail or return errors.

**Solutions:**

- ✅ Verify bind user has write permissions
- ✅ Check DN exists (for modify/delete) or parent exists (for add)
- ✅ Confirm attribute syntax matches schema requirements
- ✅ For add: ensure all required attributes are provided
- ✅ For modify: verify attributes exist before deleting
- ✅ Check for constraints (unique attributes, referential integrity)
- ✅ Cannot delete entries with children (delete children first)

### Performance Problems

**Problem:** Queries are slow or timeout.

**Solutions:**

- ✅ Add indexes to frequently filtered attributes on LDAP server
- ✅ Use more specific filters to reduce result set size
- ✅ Implement pagination for large result sets
- ✅ Limit attributes retrieved with `attributes` parameter
- ✅ Use appropriate scope (avoid "subtree" when possible)
- ✅ Increase `timeout` value for complex queries
- ✅ Check LDAP server performance and load