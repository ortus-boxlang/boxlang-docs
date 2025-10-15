---
description: >-
  🔐 A comprehensive LDAP module for BoxLang that brings full-featured LDAP
  directory access to your applications!
icon: address-book
---

# LDAP +

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://www.boxlang.io/plans)&#x20;
{% endhint %}

This module provides powerful LDAP (Lightweight Directory Access Protocol) capabilities to the [BoxLang](https://boxlang.io) language, making it easy to query, modify, and manage directory services with minimal code.

### ✨ Features

* 🔍 **Query**: Search LDAP directories with filters, scopes, and pagination
* ➕ **Add**: Create new directory entries with multi-valued attributes
* ✏️ **Modify**: Update existing entries (replace/add/delete attributes)
* 🗑️ **Delete**: Remove directory entries
* 🔄 **ModifyDN**: Rename entries or move within directory tree
* 🔒 **Secure**: SSL/TLS support with certificate validation
* 🔑 **Authentication**: Simple bind and anonymous access
* 🎯 **Flexible Filtering**: Complex LDAP filters with boolean logic
* 📄 **Pagination**: Handle large result sets efficiently
* 🔌 **Connection Pooling**: Automatic connection management
* 🏢 **Enterprise Grade**: Built and Supported by Ortus Solutions

### 📦 Installation

#### Requirements

* BoxLang 1.6+
* Access to an LDAP server (Active Directory, OpenLDAP, etc.)

#### Install via CommandBox

If you are using CommandBox for your web applications, simply run:

```bash
box install bx-ldap@ortus
```

#### Install via BoxLang OS Binary

If you are using the BoxLang OS Binary, simply run:

```bash
install-bx-module bx-ldap@ortus
```

The module will automatically register and be available as `bxldap` in your BoxLang applications.

### 🚀 Quick Start

Here's how to query an LDAP directory in just a few lines:

```java
bx:ldap
    action="query"
    server="ldap.example.com"
    port="389"
    name="result"
    start="dc=example,dc=org"
    filter="(objectClass=person)";

println( "Found #result.recordCount# users" );
```

That's it! 🎉 You now have LDAP query results in a BoxLang Query object.

### 🔧 LDAP Actions

The module supports five core LDAP operations:

#### 🔍 Query

Search the directory with filters, scopes, and attribute selection.

* **Use Case**: Find users, groups, or any directory objects
* **Returns**: BoxLang Query object with results
* **Features**: Filtering, sorting, pagination, scope control

#### ➕ Add

Create new entries in the directory.

* **Use Case**: Add new users, groups, organizational units
* **Supports**: Multi-valued attributes, all attribute types
* **Returns**: Success/failure indication

#### ✏️ Modify

Update existing directory entries.

* **Use Case**: Update user information, group memberships
* **Operations**: Replace, add, or delete attributes
* **Flexibility**: Modify multiple attributes in one operation

#### 🗑️ Delete

Remove entries from the directory.

* **Use Case**: Delete obsolete users, groups, or objects
* **Safety**: Validates entry exists before deletion
* **Note**: Cannot delete entries with children (delete children first)

#### 🔄 ModifyDN

Rename entries or move them within the directory tree.

* **Use Case**: Rename users, reorganize directory structure
* **Operations**: Rename (change RDN) or move to different parent
* **Flexibility**: Supports both rename and move operations

### 📚 Component Reference

#### 🔐 `<bx:ldap>` Component

The main component for all LDAP operations.

**Core Attributes**

| Attribute | Type   | Required | Description                                                    |
| --------- | ------ | -------- | -------------------------------------------------------------- |
| `action`  | string | ✅ Yes    | LDAP operation: "query", "add", "modify", "delete", "modifydn" |
| `server`  | string | ✅ Yes    | LDAP server hostname or IP address                             |
| `port`    | number | ✅ Yes    | LDAP server port (389 standard, 636 SSL)                       |
| `name`    | string | ⚠️ Query | Variable name for query results (required for query action)    |
| `start`   | string | ✅ Yes    | Starting DN (Distinguished Name) for search or operation       |

**Authentication Attributes**

| Attribute  | Type    | Default | Description                                                     |
| ---------- | ------- | ------- | --------------------------------------------------------------- |
| `username` | string  | -       | Bind DN for authentication (e.g., "cn=admin,dc=example,dc=org") |
| `password` | string  | -       | Password for authentication                                     |
| `secure`   | boolean | false   | Security mode: true or false (default)                          |

**Query-Specific Attributes**

| Attribute       | Type   | Default            | Description                                  |
| --------------- | ------ | ------------------ | -------------------------------------------- |
| `filter`        | string | "(objectClass=\*)" | LDAP search filter (e.g., "(uid=jdoe)")      |
| `scope`         | string | "onelevel"         | Search scope: "base", "onelevel", "subtree"  |
| `attributes`    | string | "\*"               | Comma-separated list of attributes to return |
| `sort`          | string | -                  | Attribute name to sort results by            |
| `sortDirection` | string | "asc"              | Sort direction: "asc" or "desc"              |
| `maxrows`       | number | -                  | Maximum number of results to return          |
| `startRow`      | number | 1                  | Starting row for pagination                  |
| `timeout`       | number | 60000              | Operation timeout in milliseconds            |

**Modify-Specific Attributes**

| Attribute    | Type   | Required  | Description                                                     |
| ------------ | ------ | --------- | --------------------------------------------------------------- |
| `dn`         | string | ✅ Yes     | Distinguished Name of entry to modify                           |
| `attributes` | struct | ✅ Yes     | Struct of attributes to modify (key=attribute, value=new value) |
| `modifyType` | string | "replace" | Modification type: "replace", "add", "delete"                   |

**Add-Specific Attributes**

| Attribute    | Type   | Required | Description                        |
| ------------ | ------ | -------- | ---------------------------------- |
| `dn`         | string | ✅ Yes    | Distinguished Name for new entry   |
| `attributes` | struct | ✅ Yes    | Struct of attributes for new entry |

**Delete-Specific Attributes**

| Attribute | Type   | Required | Description                           |
| --------- | ------ | -------- | ------------------------------------- |
| `dn`      | string | ✅ Yes    | Distinguished Name of entry to delete |

**ModifyDN-Specific Attributes**

| Attribute    | Type   | Required | Description                                       |
| ------------ | ------ | -------- | ------------------------------------------------- |
| `dn`         | string | ✅ Yes    | Current Distinguished Name                        |
| `attributes` | struct | ✅ Yes    | Struct with "newRDN" and optionally "newParentDN" |

### 💡 Examples

#### Basic Examples

**🔍 Simple Query**

Find all users in a directory:

```java
bx:ldap
    action="query"
    server="ldap.example.com"
    port="389"
    name="users"
    start="ou=users,dc=example,dc=org"
    filter="(objectClass=person)";

println( "Found #users.recordCount# users" );
```

**💡 Use Case:** Quick directory lookup to list all users.

**🔎 Filtered Search**

Search for a specific user:

```java
bx:ldap
    action="query"
    server="ldap.example.com"
    port="389"
    name="user"
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

**➕ Add New User**

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

**✏️ Modify User**

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

**🗑️ Delete User**

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

**🔄 Rename User**

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

#### Advanced Examples

**🔍 Complex Filter Query**

Use advanced LDAP filter syntax:

```java
// Find active users in IT department created after a date
bx:ldap
    action="query"
    server="ldap.example.com"
    port="389"
    name="itUsers"
    start="dc=example,dc=org"
    scope="subtree"
    filter="(&(objectClass=person)(department=IT)(!(accountStatus=disabled))(createTimestamp>=20240101000000Z))"
    sort="cn"
    sortDirection="asc";

println( "Found #itUsers.recordCount# active IT users" );
```

**💡 Use Case:** Department reporting, audit queries, compliance checks.

**Filter Operators:**

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

**📄 Paginated Query**

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
    name="pagedUsers"
    start="ou=users,dc=example,dc=org"
    filter="(objectClass=person)"
    maxrows="#pageSize#"
    startRow="#startRow#"
    sort="cn";

println( "Showing #pagedUsers.recordCount# users (Page #currentPage#)" );
```

**💡 Use Case:** User management interfaces, large directory browsing.

**🔒 SSL/TLS Secure Connection**

Connect securely with SSL:

```java
bx:ldap
    action="query"
    server="ldaps.example.com"
    port="636"
    secure="false"
    name="secureUsers"
    start="dc=example,dc=org"
    filter="(objectClass=person)";

println( "Secure query returned #secureUsers.recordCount# users" );
```

**💡 Use Case:** Production environments, sensitive data access, compliance requirements.

**🔐 Mutual TLS Authentication**

Use client certificates for authentication:

```java
bx:ldap
    action="query"
    server="ldaps.example.com"
    port="636"
    secure="true"
    username="cn=app,dc=example,dc=org"
    password="apppass"
    name="users"
    start="dc=example,dc=org";

println( "Authenticated with client certificate" );
```

**💡 Use Case:** High-security environments, API integrations, service accounts.

**➕ Add Entry with Multiple Values**

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

**✏️ Add Attribute Values**

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

**🗑️ Delete Attribute Values**

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

**🔄 Move Entry to Different OU**

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

### ⚠️ Error Handling

#### Understanding Empty Results

**Important:** LDAP queries return **empty Query objects** (recordCount=0) instead of throwing exceptions when:

* Entry does not exist
* Filter matches no entries
* Insufficient permissions (sometimes)
* Entry was deleted

```java
bx:ldap
    action="query"
    server="ldap.example.com"
    port="389"
    name="user"
    start="dc=example,dc=org"
    filter="(uid=nonexistent)";

// Check for empty results
if( user.recordCount == 0 ){
    println( "User not found" );
} else {
    println( "Found user: #user.cn#" );
}
```

#### Exception Handling

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

#### Common Error Scenarios

| Error                | Cause                   | Solution                                                |
| -------------------- | ----------------------- | ------------------------------------------------------- |
| Connection timeout   | Server unreachable      | Check server hostname, port, firewall                   |
| Invalid credentials  | Wrong username/password | Verify bind DN and password                             |
| Entry already exists | Duplicate DN in add     | Use unique DN or modify existing entry                  |
| No such object       | DN doesn't exist        | Verify DN syntax and entry existence                    |
| Insufficient access  | Permission denied       | Check ACLs and bind user permissions                    |
| Invalid DN syntax    | Malformed DN            | Validate DN format: `uid=user,ou=org,dc=example,dc=org` |

### 🎯 Best Practices

#### Security

* ✅ **Always use SSL/TLS in production** (`secure="true"`)
* ✅ **Never hardcode credentials** - use environment variables or secure vaults
* ✅ **Use least privilege** - bind with minimum required permissions
* ✅ **Validate user input** - sanitize filter parameters to prevent LDAP injection
* ✅ **Implement connection timeouts** - prevent hanging operations
* ✅ **Use service accounts** - dedicated accounts for application access
* ✅ **Rotate passwords regularly** - follow security policies
* ✅ **Log security events** - audit all modify/add/delete operations

#### Performance

* ✅ **Use specific filters** - narrow searches with precise LDAP filters
* ✅ **Limit attribute retrieval** - only request needed attributes
* ✅ **Implement pagination** - use `maxrows` and `startRow` for large result sets
* ✅ **Choose appropriate scope** - use "base" or "onelevel" when possible
* ✅ **Cache results** - cache frequently accessed data
* ✅ **Use indexed attributes** - filter on indexed attributes for speed
* ✅ **Connection pooling** - automatically handled by Apache Directory API

#### Filter Optimization

* ✅ **Put most restrictive filters first** - in AND operations
* ✅ **Use equality over substring** - `(uid=jdoe)` faster than `(uid=*jdoe*)`
* ✅ **Avoid leading wildcards** - `(cn=John*)` faster than `(cn=*John)`
* ✅ **Combine filters efficiently** - use `(&(attr1=val1)(attr2=val2))` not multiple queries

#### Directory Structure

* ✅ **Follow DN conventions** - consistent naming schemes
* ✅ **Use organizational units** - logical grouping (ou=users, ou=groups)
* ✅ **Plan DN hierarchy** - consider future growth and reorganization
* ✅ **Document schema** - maintain documentation of custom attributes

### ❓ Troubleshooting

#### Connection Issues

**Problem:** Cannot connect to LDAP server.

**Solutions:**

* ✅ Verify server hostname and port (389 standard, 636 SSL)
* ✅ Check firewall rules allow LDAP traffic
* ✅ Test connectivity with `telnet ldap.example.com 389`
* ✅ Verify DNS resolution of hostname
* ✅ Check LDAP server is running and accepting connections
* ✅ Review LDAP server logs for connection attempts

#### Authentication Failures

**Problem:** Invalid credentials or bind failure.

**Solutions:**

* ✅ Verify bind DN format: `cn=admin,dc=example,dc=org`
* ✅ Confirm password is correct (no extra spaces)
* ✅ Check if account is locked or disabled
* ✅ Verify user has appropriate permissions
* ✅ For Active Directory: use `user@domain.com` or `DOMAIN\user` format
* ✅ Test credentials with LDAP browser tool (Apache Directory Studio)

#### Query Returns No Results

**Problem:** Query completes but returns 0 results.

**Solutions:**

* ✅ Verify `start` DN exists in directory
* ✅ Check filter syntax is correct
* ✅ Confirm scope is appropriate ("base" vs "onelevel" vs "subtree")
* ✅ Verify bind user has read permissions on entries
* ✅ Test filter with LDAP browser tool
* ✅ Check for typos in attribute names
* ✅ Confirm entries actually exist in search base

#### SSL/TLS Issues

**Problem:** SSL handshake failure or certificate errors.

**Solutions:**

* ✅ Verify port 636 is used for LDAPS (not 389)
* ✅ Check server certificate is valid and not expired
* ✅ Import server certificate into Java truststore
* ✅ For self-signed certs: add to trusted certificates
* ✅ Verify certificate hostname matches server hostname
* ✅ Check for certificate chain issues

#### Modify/Add/Delete Failures

**Problem:** Write operations fail or return errors.

**Solutions:**

* ✅ Verify bind user has write permissions
* ✅ Check DN exists (for modify/delete) or parent exists (for add)
* ✅ Confirm attribute syntax matches schema requirements
* ✅ For add: ensure all required attributes are provided
* ✅ For modify: verify attributes exist before deleting
* ✅ Check for constraints (unique attributes, referential integrity)
* ✅ Cannot delete entries with children (delete children first)

#### Performance Problems

**Problem:** Queries are slow or timeout.

**Solutions:**

* ✅ Add indexes to frequently filtered attributes on LDAP server
* ✅ Use more specific filters to reduce result set size
* ✅ Implement pagination for large result sets
* ✅ Limit attributes retrieved with `attributes` parameter
* ✅ Use appropriate scope (avoid "subtree" when possible)
* ✅ Increase `timeout` value for complex queries
* ✅ Check LDAP server performance and load

### 🤝 Contributing

We ❤️ contributions! This project is open source and welcomes your help to make it even better.

#### 🐛 Found a Bug?

If you discover a bug, please:

1. **Check existing issues** at [GitHub Issues](https://github.com/ortus-solutions-private/bx-ldap/issues)
2. **Create a new issue** with:
   * Clear title and description
   * Steps to reproduce
   * Expected vs actual behavior
   * BoxLang version, LDAP server type and version
   * Sample code that demonstrates the issue

#### 💡 Have an Enhancement Idea?

We'd love to hear your ideas! Please:

1. Open a [Feature Request](https://github.com/ortus-solutions-private/bx-ldap/issues/new)
2. Describe the feature and its use case
3. Explain how it would benefit users
4. Consider if it aligns with LDAP standards

#### 🔧 Want to Contribute Code?

Excellent! Here's how to get started:

**Development Setup**

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/ortus-solutions-private/bx-ldap.git
    cd bx-ldap
    ```
2.  **Build the Project:**

    ```bash
    # Compile Java code
    ./gradlew compileJava

    # Run tests (starts Docker LDAP container)
    ./gradlew test

    # Full build
    ./gradlew build
    ```
3.  **Test the Module:**

    The test suite uses Testcontainers with OpenLDAP in Docker for integration testing:

    ```bash
    # Run all tests
    ./gradlew test

    # Run specific test class
    ./gradlew test --tests "ortus.boxlang.ldap.components.LDAPTest"
    ```
4.  **Code Formatting:**

    ```bash
    # Auto-format code to Ortus standards
    ./gradlew spotlessApply

    # Check formatting
    ./gradlew spotlessCheck
    ```

**Pull Request Guidelines**

* ✅ Create PRs against the `development` branch (NOT `master`)
* ✅ Follow existing code style (use `spotlessApply`)
* ✅ Add tests for new features
* ✅ Update documentation as needed
* ✅ Keep commits focused and atomic
* ✅ Link related issues in PR description

**Code Standards**

* **Java**: Follow Ortus Java coding standards
* **BoxLang**: Follow BoxLang best practices
* **Testing**: All tests must pass before PR merge
* **Documentation**: Update README and Javadocs

#### 📚 Improve Documentation

Documentation improvements are always welcome:

* Fix typos or unclear explanations
* Add more examples
* Improve code comments
* Create tutorials or guides

### 📄 License

This project is licensed under the **Apache License 2.0**.

```
Copyright 2025 Ortus Solutions, Corp

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

See LICENSE file for full details.

### 💼 Support & Resources

#### 📖 Documentation

* **Module Docs**: You're reading them! 📚
* **BoxLang Docs**: [https://boxlang.ortusbooks.com/](https://boxlang.ortusbooks.com/)
* **Apache Directory LDAP API**: [https://directory.apache.org/api/](https://directory.apache.org/api/)

#### 🌐 Links

* **BoxLang Website**: [https://boxlang.io](https://boxlang.io)
* **Ortus Solutions**: [https://www.ortussolutions.com](https://www.ortussolutions.com)
* **GitHub Repository**: [https://github.com/ortus-solutions-private/bx-ldap](https://github.com/ortus-solutions-private/bx-ldap)
* **Issue Tracker**: [https://github.com/ortus-solutions-private/bx-ldap/issues](https://github.com/ortus-solutions-private/bx-ldap/issues)

#### 🎓 Learning Resources

* **BoxLang Training**: [https://www.ortussolutions.com/services/training](https://www.ortussolutions.com/services/training)
* **LDAP Tutorial**: [https://ldap.com/learn-about-ldap/](https://ldap.com/learn-about-ldap/)
* **Blog**: [https://www.ortussolutions.com/blog](https://www.ortussolutions.com/blog)

#### 💬 Community Support

* **Ortus Community Discourse**: [https://community.ortussolutions.com](https://community.ortussolutions.com)
* **Box Team Slack**: [http://boxteam.ortussolutions.com/](http://boxteam.ortussolutions.com/)

#### 💰 Financial Support

You can support BoxLang and all Ortus Solutions open source projects:

* 🌟 [Become a Patron](https://www.patreon.com/ortussolutions)
* 💵 [One-time PayPal Donation](https://www.paypal.com/paypalme/ortussolutions)

Patrons get exclusive benefits like:

* Priority support
* Early access to new features
* FORGEBOX Pro account
* CFCasts account

#### 🔐 Security Vulnerabilities

If you discover a security vulnerability:

1. **DO NOT** create a public issue
2. Email [security@ortussolutions.com](mailto:security@ortussolutions.com?subject=security)
3. Report in `#security` channel on [Box Team Slack](http://boxteam.ortussolutions.com/)

All vulnerabilities will be promptly addressed.
