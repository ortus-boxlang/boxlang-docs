---
description: Boxlang Password Encryption Module
icon: lock
---

# Password Encryption

This module provides secure password encryption and hashing functionality for BoxLang applications using industry-standard algorithms including Argon2, BCrypt, SCrypt, and PBKDF2. These algorithms are specifically designed for secure password storage and verification, protecting against rainbow table attacks, brute force attempts, and other common password cracking techniques.

### Installation

```bash
# For Operating Systems using our Quick Installer
install-bx-module bx-password-encrypt

# Using CommandBox to install for web servers
box install bx-password-encrypt
```

Once installed, several built-in-functions will be available for use in your BoxLang code. You can also check out the module API documentation for more details.

### BCrypt Hashing

BCrypt is a widely-used, battle-tested password hashing function with adaptive cost factor. It's an excellent choice for secure password storage.

This module contributes the following BCrypt BIFs:

* `BCryptHash( string, [rounds] )` - Returns a secure hash of the given string using the BCrypt hashing algorithm. Alias: `GenerateBCryptHash`
* `BCryptVerify( string, hash )` - Performs a BCrypt verification on the given string against the hashed value. Alias: `VerifyBCryptHash`

#### Examples

```java
// Hash a password with default cost factor (10)
hashedPassword = BCryptHash( "mySecurePassword123" );

// Hash with custom cost factor (higher = more secure but slower)
hashedPassword = BCryptHash( "mySecurePassword123", 12 );

// Verify a password
isValid = BCryptVerify( "mySecurePassword123", hashedPassword );

// Using in a user registration workflow
component {
    function createUser( required string username, required string password ) {
        var user = {
            username: arguments.username,
            passwordHash: BCryptHash( arguments.password )
        };
        // Save to database
        queryExecute(
            "INSERT INTO users (username, password_hash) VALUES (:username, :passwordHash)",
            user
        );
    }

    function authenticateUser( required string username, required string password ) {
        var user = queryExecute(
            "SELECT password_hash FROM users WHERE username = :username",
            { username: arguments.username },
            { returntype: "array" }
        );
        
        if( arrayLen( user ) && BCryptVerify( arguments.password, user[1].password_hash ) ) {
            return true;
        }
        return false;
    }
}
```

### Argon2 Hashing

Argon2 is the winner of the Password Hashing Competition and is recommended for new applications. It provides excellent protection against both CPU and GPU-based attacks.

This module contributes the following Argon2 BIFs:

* `ArgonHash( string, [salt], [iterations], [memory], [parallelism] )` - Returns a secure hash of the given string using the Argon2 hashing algorithm. Alias: `GenerateArgon2Hash`
* `ArgonVerify( string, hash )` - Performs an Argon2 verification on the given string against the hashed value. Alias: `Argon2CheckHash`

#### Examples

```java
// Hash a password with default settings
hashedPassword = ArgonHash( "mySecurePassword123" );

// Hash with custom parameters for higher security
hashedPassword = ArgonHash( 
    "mySecurePassword123",
    "",  // auto-generate salt
    10,  // iterations
    65536, // memory in KB
    4    // parallelism
);

// Verify a password
isValid = ArgonVerify( "mySecurePassword123", hashedPassword );

if( isValid ) {
    // Password is correct, proceed with login
    writeOutput( "Login successful!" );
} else {
    // Password is incorrect
    writeOutput( "Invalid credentials" );
}
```

### SCrypt Hashing

SCrypt is designed to be memory-hard, making it resistant to hardware brute-force attacks. It's particularly effective against GPU-based attacks.

This module contributes the following SCrypt BIFs:

* `SCryptHash( string, [cpuCost], [memoryCost], [parallelization], [saltLength], [keyLength] )` - Returns a secure hash of the given string using the SCrypt hashing algorithm. Alias: `GenerateSCryptHash`
* `SCryptVerify( string, hash )` - Performs an SCrypt verification on the given string against the hashed value. Alias: `VerifySCryptHash`

#### Examples

```java
// Hash a password with default settings
hashedPassword = SCryptHash( "mySecurePassword123" );

// Hash with custom parameters for higher security
hashedPassword = SCryptHash( 
    "mySecurePassword123",
    16384, // CPU cost
    8,     // memory cost
    1,     // parallelization
    16,    // salt length
    32     // key length
);

// Verify a password
isValid = SCryptVerify( "mySecurePassword123", hashedPassword );

// Using for API key hashing
function generateAPIKey( required string userId ) {
    var rawKey = createUUID();
    var hashedKey = SCryptHash( rawKey );
    
    queryExecute(
        "INSERT INTO api_keys (user_id, key_hash) VALUES (:userId, :keyHash)",
        { userId: arguments.userId, keyHash: hashedKey }
    );
    
    return rawKey; // Return once to user, then discard
}
```

### PBKDF2 Key Derivation

PBKDF2 (Password-Based Key Derivation Function 2) is a key derivation function that can be used for password hashing and generating cryptographic keys.

This module contributes the following PBKDF2 BIF:

* `GeneratePBKDFKey( password, salt, [iterations], [algorithm], [keyLength] )` - Generates a PBKDF2 key from the given password and salt.
  * `password` - The password to derive the key from
  * `salt` - The salt value (should be unique per password)
  * `iterations` - Number of iterations (default: 10000). Higher is more secure but slower
  * `algorithm` - The HMAC algorithm to use (default: "PBKDF2WithHmacSHA256")
  * `keyLength` - The desired key length in bits (default: 256)

#### Examples

```java
// Generate a PBKDF2 key with default settings
salt = generateSecretKey( "AES", 128 );
key = GeneratePBKDFKey( "mySecurePassword123", salt );

// Generate with custom parameters
key = GeneratePBKDFKey( 
    "mySecurePassword123",
    salt,
    100000, // iterations
    "PBKDF2WithHmacSHA512", // algorithm
    512 // key length in bits
);

// Using PBKDF2 for encryption key derivation
function encryptData( required string data, required string password ) {
    var salt = generateSecretKey( "AES", 128 );
    var key = GeneratePBKDFKey( password, salt, 100000 );
    
    var encryptedData = encrypt( 
        data, 
        key, 
        "AES/CBC/PKCS5Padding",
        "Base64"
    );
    
    return {
        encrypted: encryptedData,
        salt: toBase64( salt )
    };
}
```

### Best Practices

1. **Use Argon2 for new applications** - It provides the best security against modern attacks
2. **Never store passwords in plain text** - Always hash passwords before storing them
3. **Use unique salts** - Let the algorithms generate salts automatically or ensure each password has a unique salt
4. **Adjust cost factors appropriately** - Balance security with performance based on your application's needs
5. **Verify passwords using the corresponding verify function** - Never compare hashed passwords directly
6. **Update hashing parameters over time** - As hardware improves, increase cost factors for new password hashes

### GitHub Repository and Reporting Issues

Visit the [GitHub repository](https://github.com/ortus-boxlang/bx-password-encrypt) for release notes. You can also file a bug report or improvement suggestion via [Jira](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=16100\&issuetype=1).
