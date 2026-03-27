---
description: >-
  Complete reference for the LDAP component - perform directory operations
  including query, add, modify, delete, and connection management
icon: address-book
---

# LDAP

The `<bx:ldap>` component provides comprehensive LDAP (Lightweight Directory Access Protocol) operations for directory services integration. It supports querying, adding, modifying, and deleting directory entries, as well as connection management for efficient multi-operation workflows.

## Syntax

### Template Syntax

```xml
<bx:ldap
    action="query"
    server="ldap.example.com"
    port="389"
    result="queryResults"
    start="dc=example,dc=org"
    filter="(objectClass=person)"
/>
```

### Script Syntax

```javascript
bx:ldap
    action="query"
    server="ldap.example.com"
    port="389"
    result="queryResults"
    start="dc=example,dc=org"
    filter="(objectClass=person)";
```

## Supported Actions

The LDAP component supports seven core operations:

### query

Search the directory with filters, scopes, and attribute selection.

* **Use Case**: Find users, groups, or any directory objects
* **Returns**: BoxLang Query object with results (contains matched LDAP entries as rows with their attributes as columns)
* **Features**: Filtering, sorting, pagination, scope control
* **Empty Results**: Returns a Query with `recordCount=0` if no entries match (no exception thrown)

### add

Create new entries in the directory.

* **Use Case**: Add new users, groups, organizational units
* **Supports**: Multi-valued attributes, all attribute types
* **Returns**: Boolean `true` on success
* **Error Handling**: Throws exception if entry already exists or DN is invalid

### modify

Update existing directory entries.

* **Use Case**: Update user information, group memberships
* **Operations**: Replace, add, or delete attributes
* **Returns**: Boolean `true` on success
* **Flexibility**: Modify multiple attributes in one operation
* **Error Handling**: Throws exception if entry does not exist or modification type is invalid

### delete

Remove entries from the directory.

* **Use Case**: Delete obsolete users, groups, or objects
* **Returns**: Boolean `true` on success
* **Safety**: Validates entry exists before deletion (throws exception if not found)
* **Note**: Cannot delete entries with children (delete children first)
* **Error Handling**: Throws exception if entry has subordinate entries or does not exist

### modifydn

Rename entries or move them within the directory tree.

* **Use Case**: Rename users, reorganize directory structure
* **Returns**: Boolean `true` on success
* **Operations**: Rename (change RDN) or move to different parent
* **Flexibility**: Supports both rename and move operations
* **Error Handling**: Throws exception if new DN is invalid or already exists

### open

Create and store a named connection for reuse across multiple operations.

* **Use Case**: Establish a connection with credentials that can be reused without repetition
* **Required Attributes**: `connection` (connection name), `server`, plus authentication details
* **Returns**: Connection object if `result` attribute is specified, otherwise ignored
* **Benefits**: Simplifies multi-operation workflows by eliminating credential repetition
* **Note**: Connection remains open until explicitly closed or application terminates

### close

Close and release a named connection.

* **Use Case**: Explicitly close a named connection to free resources
* **Required Attributes**: `connection` (connection name to close)
* **Returns**: Boolean `true` on success
* **Benefits**: Allows proper resource management for long-running applications
* **Note**: Once closed, connection can be reopened with same name if needed

## Attributes

### Core Attributes

| Attribute    | Type   | Required       | Default           | Description                                                                                                                                                      |
| ------------ | ------ | -------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `action`     | string | ✅ Yes          | -                 | LDAP operation: "query", "add", "modify", "delete", "modifydn", "open", "close"                                                                                  |
| `server`     | string | ⚠️ Conditional | -                 | LDAP server hostname or IP address. Required if `connection` is not provided.                                                                                    |
| `connection` | string | ⚠️ Conditional | -                 | Named connection to an LDAP server (previously created). Required if `server` is not provided. Allows reusing connection credentials across multiple operations. |
| `port`       | number | No             | 389 (636 for SSL) | LDAP server port                                                                                                                                                 |
| `result`     | string | ⚠️ Query       | -                 | Variable name to store query results (primary attribute for result handling)                                                                                     |
| `name`       | string | No             | -                 | **Deprecated**: Use `result` instead. Maintained for backwards compatibility with query actions only                                                             |
| `start`      | string | ✅ Yes          | -                 | Starting DN (Distinguished Name) for search or operation                                                                                                         |

### Authentication Attributes

| Attribute            | Type           | Required | Default        | Description                                                                                                          |
| -------------------- | -------------- | -------- | -------------- | -------------------------------------------------------------------------------------------------------------------- |
| `username`           | string         | No       | "" (anonymous) | Bind DN for authentication (e.g., "cn=admin,dc=example,dc=org")                                                      |
| `password`           | string         | No       | "" (anonymous) | Password for authentication                                                                                          |
| `secure`             | boolean/string | No       | false          | Security mode: `false` (no SSL), `true` (SSL), "CFSSL\_BASIC" (server auth only), "CFSSL\_CLIENT\_AUTH" (mutual TLS) |
| `useTls`             | boolean        | No       | false          | Whether to use StartTLS extension to initiate SSL/TLS over normal port                                               |
| `clientCert`         | string         | No       | -              | Full path to keystore file containing client certificate                                                             |
| `clientCertPassword` | string         | No       | -              | Password for client certificate keystore                                                                             |
| `timeout`            | integer        | No       | 60000          | Operation timeout in milliseconds                                                                                    |

### Query-Specific Attributes

| Attribute       | Type   | Required | Default            | Description                                                         |
| --------------- | ------ | -------- | ------------------ | ------------------------------------------------------------------- |
| `filter`        | string | No       | "(objectClass=\*)" | LDAP search filter (e.g., "(uid=jdoe)")                             |
| `scope`         | string | No       | "onelevel"         | Search scope: "base", "onelevel", "subtree"                         |
| `attributes`    | string | No       | "\*"               | Comma-separated list of attributes to return                        |
| `sort`          | string | No       | -                  | Attribute name to sort results by                                   |
| `sortDirection` | string | No       | "asc"              | Sort direction: "asc" or "desc"                                     |
| `maxrows`       | number | No       | -                  | Maximum number of results to return                                 |
| `startRow`      | number | No       | 1                  | Starting row for pagination                                         |
| `returnFormat`  | string | No       | "query"            | Result format: "query" (Query object) or "array" (Array of structs) |

### Modify-Specific Attributes

| Attribute    | Type   | Required | Default   | Description                                                     |
| ------------ | ------ | -------- | --------- | --------------------------------------------------------------- |
| `dn`         | string | ✅ Yes    | -         | Distinguished Name of entry to modify                           |
| `attributes` | struct | ✅ Yes    | -         | Struct of attributes to modify (key=attribute, value=new value) |
| `modifyType` | string | No       | "replace" | Modification type: "replace", "add", "delete"                   |

### Add-Specific Attributes

| Attribute    | Type   | Required | Default | Description                        |
| ------------ | ------ | -------- | ------- | ---------------------------------- |
| `dn`         | string | ✅ Yes    | -       | Distinguished Name for new entry   |
| `attributes` | struct | ✅ Yes    | -       | Struct of attributes for new entry |

### Delete-Specific Attributes

| Attribute | Type   | Required | Default | Description                           |
| --------- | ------ | -------- | ------- | ------------------------------------- |
| `dn`      | string | ✅ Yes    | -       | Distinguished Name of entry to delete |

### ModifyDN-Specific Attributes

| Attribute    | Type   | Required | Default | Description                                       |
| ------------ | ------ | -------- | ------- | ------------------------------------------------- |
| `dn`         | string | ✅ Yes    | -       | Current Distinguished Name                        |
| `attributes` | struct | ✅ Yes    | -       | Struct with "newRDN" and optionally "newParentDN" |

## Examples

### Query Operations

#### Simple Query

Find all users in a directory:

```javascript
ldap
    action="query"
    server="ldap.example.com"
    port="389"
    result="users"
    start="ou=users,dc=example,dc=org"
    filter="(objectClass=person)";

println( "Found #users.recordCount# users" );
```

#### Filtered Search

Search for a specific user with attribute selection:

```javascript
ldap
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

#### Complex Filter Query

Use advanced LDAP filter syntax:

```javascript
// Find active users in IT department created after a date
ldap
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

#### Paginated Query

Handle large result sets efficiently:

```javascript
// Get 50 users at a time
pageSize = 50;
currentPage = 1;
startRow = ((currentPage - 1) * pageSize) + 1;

ldap
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

#### Query Results as Array

Return results as an array of structs instead of a Query object:

```javascript
// Query returning array format
ldap
    action="query"
    server="ldap.example.com"
    port="389"
    result="userArray"
    start="ou=users,dc=example,dc=org"
    filter="(objectClass=person)"
    returnFormat="array"
    sort="cn";

// Iterate over array results
userArray.each( ( user ) => {
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

### Add Operations

#### Add New User

Create a new directory entry:

```javascript
newUser = {
    "objectClass": ["inetOrgPerson", "organizationalPerson", "person", "top"],
    "cn": "John Doe",
    "sn": "Doe",
    "uid": "jdoe",
    "mail": "john.doe@example.com",
    "userPassword": "SecurePassword123"
};

ldap
    action="add"
    server="ldap.example.com"
    port="389"
    username="cn=admin,dc=example,dc=org"
    password="adminpass"
    dn="uid=jdoe,ou=users,dc=example,dc=org"
    attributes=newUser;

println( "User created successfully!" );
```

#### Add Entry with Multiple Values

Create an entry with multi-valued attributes:

```javascript
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

ldap
    action="add"
    server="ldap.example.com"
    port="389"
    username="cn=admin,dc=example,dc=org"
    password="adminpass"
    dn="cn=Developers,ou=groups,dc=example,dc=org"
    attributes=newGroup;

println( "Group created with multiple members!" );
```

### Modify Operations

#### Modify User Attributes

Update an existing entry:

```javascript
updates = {
    "mail": "john.newemail@example.com",
    "telephoneNumber": "+1-555-0123"
};

ldap
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

#### Add Attribute Values

Add values to existing multi-valued attributes:

```javascript
// Add new members to existing group
newMembers = {
    "member": [
        "uid=bmiller,ou=users,dc=example,dc=org",
        "uid=kchen,ou=users,dc=example,dc=org"
    ]
};

ldap
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

#### Delete Attribute Values

Remove specific values from multi-valued attributes:

```javascript
// Remove a member from group
removeMember = {
    "member": "uid=jsmith,ou=users,dc=example,dc=org"
};

ldap
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

### Delete Operations

#### Delete User

Remove an entry from the directory:

```javascript
ldap
    action="delete"
    server="ldap.example.com"
    port="389"
    username="cn=admin,dc=example,dc=org"
    password="adminpass"
    dn="uid=jdoe,ou=users,dc=example,dc=org";

println( "User deleted successfully!" );
```

### ModifyDN Operations

#### Rename Entry

Change an entry's RDN (Relative Distinguished Name):

```javascript
renameOp = {
    "newRDN": "uid=johnd"
};

ldap
    action="modifydn"
    server="ldap.example.com"
    port="389"
    username="cn=admin,dc=example,dc=org"
    password="adminpass"
    dn="uid=jdoe,ou=users,dc=example,dc=org"
    attributes=renameOp;

println( "User renamed from jdoe to johnd!" );
```

#### Move Entry to Different OU

Move an entry to a different organizational unit:

```javascript
moveOp = {
    "newRDN": "uid=jdoe",
    "newParentDN": "ou=contractors,dc=example,dc=org"
};

ldap
    action="modifydn"
    server="ldap.example.com"
    port="389"
    username="cn=admin,dc=example,dc=org"
    password="adminpass"
    dn="uid=jdoe,ou=employees,dc=example,dc=org"
    attributes=moveOp;

println( "User moved from employees to contractors!" );
```

### Connection Management

#### Define and Reuse Named Connections

Create a named connection once and reuse it across multiple operations:

```javascript
// Define a connection once with all credentials
ldap
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
ldap
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

ldap
    action="add"
    connection="myLdapConn"
    dn="cn=developers,ou=groups,dc=example,dc=org"
    attributes=newGroup;

println( "Group created successfully using reused connection" );
```

#### Explicitly Open a Named Connection

Establish a connection with the `open` action for later reuse:

```javascript
// Explicitly open a named connection
ldap
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
ldap
    action="query"
    connection="prodLdap"
    start="ou=users,dc=prod,dc=org"
    filter="(department=IT)"
    result="itUsers";

// Add operation
ldap
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
ldap
    action="modify"
    connection="prodLdap"
    dn="uid=newuser,ou=users,dc=prod,dc=org"
    attributes={"mail": "newuser@production.com"}
    modifyType="replace";
```

#### Close a Named Connection

Explicitly close a connection to free resources:

```javascript
// Close a named connection
ldap
    action="close"
    connection="prodLdap";

println( "Connection 'prodLdap' closed and resources released" );
```

### Secure Connections

#### SSL/TLS Secure Connection

Connect securely with SSL:

```javascript
ldap
    action="query"
    server="ldaps.example.com"
    port="636"
    secure="true"
    result="secureUsers"
    start="dc=example,dc=org"
    filter="(objectClass=person)";

println( "Secure query returned #secureUsers.recordCount# users" );
```

#### Mutual TLS Authentication

Use client certificates for authentication:

```javascript
ldap
    action="query"
    server="ldaps.example.com"
    port="636"
    secure="CFSSL_CLIENT_AUTH"
    clientCert="/path/to/client.keystore"
    clientCertPassword="keystorepass"
    username="cn=app,dc=example,dc=org"
    password="apppass"
    result="users"
    start="dc=example,dc=org";

println( "Authenticated with client certificate" );
```

## LDAP Filter Syntax

The LDAP filter attribute supports standard LDAP filter operators:

### Filter Operators

* `&` - AND (all conditions must match)
* `|` - OR (any condition matches)
* `!` - NOT (negation)
* `=` - Equals
* `>=` - Greater than or equal
* `<=` - Less than or equal
* `=*` - Presence check (attribute exists)
* `=value*` - Starts with
* `=*value` - Ends with
* `=*value*` - Contains

### Example Filters

```javascript
// Single condition
filter="(uid=jdoe)"

// AND operation (all must match)
filter="(&(objectClass=person)(department=IT))"

// OR operation (any can match)
filter="(|(department=IT)(department=Engineering))"

// NOT operation (negation)
filter="(!(accountStatus=disabled))"

// Complex combination
filter="(&(objectClass=person)(|(department=IT)(department=Engineering))(!(accountStatus=disabled)))"

// Substring matching
filter="(cn=John*)"           // Starts with John
filter="(cn=*Smith)"          // Ends with Smith
filter="(cn=*John*)"          // Contains John

// Presence check
filter="(mail=*)"             // Has mail attribute

// Greater than or equal
filter="(createTimestamp>=20240101000000Z)"
```

## Error Handling

### Understanding Empty Results

**Important:** LDAP queries return **empty Query objects** (recordCount=0) instead of throwing exceptions when:

* Entry does not exist
* Filter matches no entries
* Insufficient permissions (sometimes)
* Entry was deleted

```javascript
ldap
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

```javascript
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

| Error                | Cause                   | Solution                                                |
| -------------------- | ----------------------- | ------------------------------------------------------- |
| Connection timeout   | Server unreachable      | Check server hostname, port, firewall                   |
| Invalid credentials  | Wrong username/password | Verify bind DN and password                             |
| Entry already exists | Duplicate DN in add     | Use unique DN or modify existing entry                  |
| No such object       | DN doesn't exist        | Verify DN syntax and entry existence                    |
| Insufficient access  | Permission denied       | Check ACLs and bind user permissions                    |
| Invalid DN syntax    | Malformed DN            | Validate DN format: `uid=user,ou=org,dc=example,dc=org` |

## Event Handling

The LDAP component announces events at key points in the connection lifecycle:

### onLDAPConnectionOpen

Announced when an LDAP connection is successfully opened.

**Event Payload:**

```javascript
{
    "context": context,           // BoxLang context
    "connection": connection,     // The opened LDAP connection object
    "result": connectionName,     // Named connection reference (if used)
    "attributes": attributes      // Original component attributes
}
```

### onLDAPConnectionClose

Announced when an LDAP connection is closed.

**Event Payload:**

```javascript
{
    "context": context,           // BoxLang context
    "result": connectionName,     // Named connection being closed
    "returnValue": true,          // Success flag
    "attributes": attributes      // Original component attributes
}
```

## Related

* [LDAP Module Overview](../../)
