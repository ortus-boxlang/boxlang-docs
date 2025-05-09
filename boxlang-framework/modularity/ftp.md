---
description: >-
  The FTP module allows you perform various operations against an FTP or SFTP
  server.
icon: globe
---

# FTP

```
# For Operating Systems using our Quick Installer.
install-bx-module bx-ftp

# Using CommandBox to install for web servers.
box install bx-ftp
```

```javascript
Open connection to FTP server, calling it 'conn'
bx:ftp
    action="open"
    connection="conn"
    server="ftp.server.com"
    port="21"
    username="user"
    password="password"
    passive="true";
    
// List the current directory
bx:ftp
    action="listDir"
    connection="conn"
    name="result";

// Dump the results
bx:dump var="result";
```

### Attributes

Here is the list of available attributes you can use.

| Attribute   | Type    | Description                                                                                                                                                                                                                                     |
| ----------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| action      | string  | <p>The ftp operation you want to perform. Use<br>Values:<br>* open<br>* close<br>* changeDir<br>* createDir<br>* listDir<br>* removeDir<br>* getFile<br>* putFile<br>* rename<br>* remove<br>* getCurrentDir<br>* existsDir<br>* existsFile</p> |
| username    | string  | The username to log in with.                                                                                                                                                                                                                    |
| password    | string  | The password to log in with.                                                                                                                                                                                                                    |
| server      | string  | The FTP server to connect with. Ex. ftp.server.com                                                                                                                                                                                              |
| timeout     | numeric | Number of seconds for the timeout of all operations. This includes data request operations. **Defaults to 0, which indicates no timeout.**                                                                                                      |
| port        | numeric | The FTP server port. **Defaults to port 21.**                                                                                                                                                                                                   |
| connection  | string  | The variable name and reference for an FTP connection. This is required for all bx-ftp commands.                                                                                                                                                |
| stopOnError | boolean | Set to true to halt execution if an FTP error occurs. **Defaults to false.**                                                                                                                                                                    |
| passive     | boolean | Set to true to enable passive mode. Only available for FTP connections, not SFTP.                                                                                                                                                               |
| directory   | string  | Directory on which operation to perform. Used for actions **listDir**, **changeDir**, and **existsDir**.                                                                                                                                        |
| localFile   | string  | Name of file on local system. Used in actions **getFile** and **putFile**.                                                                                                                                                                      |
| remoteFile  | string  | Name of file on the FTP server. Used in actions **existsFile**, **getFile**, and **putFile**.                                                                                                                                                   |
| item        | string  | Name of file or directory. Used in actions **remove**, and **removeDir**.                                                                                                                                                                       |
| open        |         |                                                                                                                                                                                                                                                 |
| putfile     |         |                                                                                                                                                                                                                                                 |
| removeDir   |         |                                                                                                                                                                                                                                                 |
| remove      |         |                                                                                                                                                                                                                                                 |

### Examples

#### Open FTP Connection

```
bx:ftp
    action="open"
    connection="conn"
    username="user"
    password="password"
    server="ftp.server.com"
    port="21"
    passive="true|false";
```

#### Open SFTP Connection

To connect using SFTP, you need to set `secure`equal to `true`.

```
bx:ftp
    action="open"
    connection="conn"
    username="user"
    password="password"
    server="server.com"
    port="22"
    secure="true";
```

#### Close Connection

```
bx:ftp action="close" connection="conn" result="myResult";
```

### GitHub Repository and Reporting Issues <a href="#github-repository-and-reporting-issues" id="github-repository-and-reporting-issues"></a>

Visit the [GitHub repository](https://github.com/ortus-boxlang/bx-ftp) for release notes. You can also file a bug report or improvement suggestion via [Jira](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=13359\&components=27021\&issuetype=1).
