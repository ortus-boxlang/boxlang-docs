---
description: This module allows you to read and write INI files in a very easy way.
icon: sliders-up
---

# INI Files

```
# For Operating Systems using our Quick Installer.
install-bx-module bx-ini

# Using CommandBox to install for web servers.
box install bx-ini
```



```ini
[General]
appName=MyApplication
version=1.2.3
author=John Doe
boxlang=rocks

[Database]
host=localhost
port=5432
username=dbuser
password=dbpass
dbname=mydatabase

[Logging]
logLevel=DEBUG
logFile=/var/log/myapp.log
maxFileSize=10MB

[Features]
enableFeatureX=true
enableFeatureY=false
maxConnections=100
```

### Contributed Functions

Here are the contributed functions in this module:

* `getIniFile( file )` : Reads an ini file and returns the IniFile object. If the file does not exist, it will create it.
* `getProfileSection( iniFile, section )` : Gets a section from the ini file as a struct
* `getProfileSections( iniFile )` : Gets all the sections from the ini file as a struct of structs
* `getProfileString( iniFile, section, entry )` : Gets an entry from a section in the ini file, if it does not exist, it will return an empty string
* `setProfileString( iniFile, section, entry, value )` : Sets an entry in a section in the ini file, if the section does not exist, it will create it
* `removeProfileSection( iniFile, section )` : Removes a section from the ini file
* `removeProfileString( iniFile, section, entry )` : Removes an entry from a section in the ini file

The `IniFile` object is a fluent object that allows you to work with ini files in a very easy way. Here is an example of how to use it:

```java

// Get the ini file
var iniFile = getIniFile( "test.ini" );
iniFile.createSection( "mySettings" );
// Set a string
iniFile.setEntry( "section1", "entry1", "value1" );
// Get a string
var value = iniFile.getEntry( "section1", "entry1" );
// Remove a string
iniFile.removeEntry( "section1", "entry1" );
// Remove a section
iniFile.removeSection( "section1" );
```
