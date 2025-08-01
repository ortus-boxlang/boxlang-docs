---
description: BoxLang includes a lightning fast web server powered by Undertow!
icon: jet-fighter-up
---

# MiniServer

<figure><img src="../../.gitbook/assets/miniserver.png" alt=""><figcaption></figcaption></figure>

The **BoxLang MiniServer** runtime is a **lightweight,** **lightning-fast** web server powered by Undertow. It's ideal for fast applications, desktop apps (Electron/JavaFX), embedded web servers, and development. For those who desire a more robust and feature-rich servlet server implementation, we offer our open-source FREE  [CommandBox server](commandbox.md) and [CommandBox PRO](https://boxlang.io/plans) with a BoxLang Subscription.

{% hint style="success" %}
**Tip:** Please note that the BoxLang MiniServer is NOT a servlet server.  **There is no servlet container;** the web server is just a simple, fast, and pure Java Undertow server.
{% endhint %}

{% hint style="danger" %}
CommandBox is our open-source servlet server implementation. However, with a [Boxlang +/++ subscription](https://boxlang.io/plans), it becomes a powerhouse for mission-critical applications.  Check out all that you get with CommandBox Pro: [https://www.ortussolutions.com/products/commandbox-pro](https://www.ortussolutions.com/products/commandbox-pro)
{% endhint %}

### Starting a BoxLang MiniServer <a href="#starting-a-web-server-12" id="starting-a-web-server-12"></a>

The BoxLang core OS runtime doesn't know about a web application. Our web support runtime provides this functionality, a crucial part of the MiniServer and the Servlet (JEE, Jakarta, CommandBox) runtime. This runtime enhances the core boxlang runtime, making it multi-runtime and web deployable.

&#x20;If you use our Windows installer or our Quick Installer, you will have the `boxlang-miniserver` binary installed in your operating system.  You will use this to start servers.  Just navigate to any folder that you want to start a server in and run `boxlang-miniserver`.

{% hint style="success" %}
Please note that our [VSCode BoxLang Extension](../ide-tooling/) can also assist you in managing and starting/stopping servers.
{% endhint %}

{% tabs %}
{% tab title="Mac/Unix" %}
```bash
# Mac / *unix
cd mySite
boxlang-miniserver
```
{% endtab %}

{% tab title="Windows" %}
```powershell
# Windows
cd mySite
boxlang-miniserver.bat
```
{% endtab %}

{% tab title="JAR Execution" %}
```bash
# Native Jar execution
cd mySite
java -jar /usr/local/lib/boxlang-miniserver-1.0.0.jar
```
{% endtab %}
{% endtabs %}

Once you run the command, the following output will appear in your console:

```bash
+ Loaded environment variables from: /path/to/webroot/.env
+ Starting BoxLang Server...
  - Web Root: /home/lmajano/Sites/temp
  - Host: 0.0.0.0
  - Port: 8080
  - Debug: null
  - Config Path: null
  - Server Home: null
  - Health Check: false
  - Health Check Secure: false
+ Starting BoxLang Runtime...
  - BoxLang Version: 1.4.0-snapshot+0 (Built On: 2025-08-01 16:03:36)
  - Runtime Started in 652ms
+ Security protection enabled - blocking access to hidden files (starting with .)
+ WebSocket Server started
+ BoxLang MiniServer started in 818ms at: http://localhost:8080
Press Ctrl+C to stop the server.
```

As you can see from the output, this is the result of the command:

* Use the current **working directory** as the web root.
* Bind to `0.0.0.0:8080` by default (accessible from any network interface)
* **Automatic .env file loading** - Environment variables from `.env` files in the webroot are loaded into system properties
* **Built-in security protection** - Blocks access to hidden files and directories (starting with `.`) for security
* **WebSocket support** enabled by default at `/ws` endpoint
* This configures the web server with some default welcome files and no rewrites.
* BoxLang will process any BoxLang or CFML files
* Uses the user's BoxLang home as the default for configuration and modules: `~/.boxlang`



{% hint style="warning" %}
**ALERT:** The BoxLang Core knows nothing of web or HTTP, so the `form`, `url`, `cookie`, and `cgi` scopes will only exist when running the BoxLang web server (but not in the REPL, etc).
{% endhint %}

That's practically it. This is a very lightweight server that can get the job done. You can also start up servers using our VSCode IDE by opening the command palette and clicking **Start** a BoxLang web server.

<figure><img src="../../.gitbook/assets/ide-tooling-context-minserver.png" alt=""><figcaption><p>Command Palette</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (2) (2).png" alt=""><figcaption><p>Manage your Servers</p></figcaption></figure>

### Arguments <a href="#web-server-args-13" id="web-server-args-13"></a>

These are the supported arguments you can pass into the binary to configure the server.

| Argument | Value |
| --- | --- |
| `--configPath path/boxlang.json`<br>`-c path/boxlang.json` | Relative/Absolute location of the `boxlang.json` to use. By default it uses the `~/.boxlang/boxlang.json` |
| `--debug`<br>`-d`                                                                      | Put the runtime into debug mode. By default we use `false` |
| `--host ip\|domain`                                                                     | Bind the hostname to the mini server. By default we use `0.0.0.0` (all network interfaces) |
| `--port 8080`<br>`-p 8080`                                                    | The port to bind the mini server to. By default we use port `8080` |
| `--rewrites [index.bxm]`<br>`-r [index.bxm]`                       | Enable rewrites for applications using `index.bxm` as the file to use. You can also pass the name of the file to use: `--rewrites myfile.bxm` |
| `--health-check`                                                                       | Enable health check endpoints at `/health`, `/health/ready`, and `/health/live`. These provide detailed server status, readiness, and liveness information in JSON format. |
| `--health-check-secure`                                                         | Restrict detailed health check information to localhost only. When enabled, non-localhost requests receive basic status only, while localhost gets full system details including JVM metrics and memory usage. |
| `--serverHome path/`<br>`-s path/`                                     | The location of the BoxLang home for the miniserver. This is where it will look for the `boxlang.json`, place to put the log files, the compiled classes, load modules, and much more.<br><br>By default, we use the OS home via the `BOXLANG_HOME` environment variable which usually points to the user's home: `~/.boxlang/` |
| `--webroot path/`<br>`-w path/`                                           | The webserver root. By default, we use the directory from where you started the command. |

```bash
# Custom port and webroot
boxlang-miniserver --port 80 --webroot /var/www

# Custom port and server home
boxlang-miniserver --port 80 --serverHome /var/www/servers/myServer

# Custom port and rewrites enabled
boxlang-miniserver --port 80 --rewrites

# Enable health check endpoints for monitoring
boxlang-miniserver --health-check

# Enable secure health checks (detailed info only on localhost)
boxlang-miniserver --health-check --health-check-secure

# Production server with security and monitoring
boxlang-miniserver --port 8080 --host 0.0.0.0 --health-check-secure
```

### Environment Variables

The `boxlang-miniserver` binary will also scan for several environment variables as overrides to the execution process.

| Env Variable                           | Purpose                                                             |
| -------------------------------------- | ------------------------------------------------------------------- |
| `BOXLANG_CONFIG = PATH`                | Override the `boxlang.json`                                         |
| `BOXLANG_DEBUG = boolean`              | Enable or disable debug mode                                        |
| `BOXLANG_HOME = directory`             | Override the server HOME directory                                  |
| `BOXLANG_HOST = ip or domain`          | Override the `0.0.0.0` default to whatever IP or domain you like. |
| `BOXLANG_PORT = 8080`                  | Override the default port                                           |
| `BOXLANG_REWRITES = boolean`           | Enable or disable URL rewrites                                      |
| `BOXLANG_REWRITE_FILE = file.bxm`      | Choose the rewrite file to use. By default, it uses `index.bxm`     |
| `BOXLANG_WEBROOT = path`               | Override the location of the web root                               |
| `BOXLANG_HEALTH_CHECK = boolean`       | Enable or disable health check endpoints                            |
| `BOXLANG_HEALTH_CHECK_SECURE = boolean`| Enable secure health checks (detailed info only on localhost)      |
| `BOXLANG_MINISERVER_OPTS = jvmOptions` | A list of Java options to pass to the startup command               |



{% hint style="danger" %}
Environment variables are scanned first, then the command arguments. Thus, the command arguments take precedence.
{% endhint %}

## 🔒 Security Features

The BoxLang MiniServer includes built-in security features to protect your applications:

### Hidden File Protection

The server automatically blocks access to hidden files and directories (those starting with a dot `.`). This security feature protects sensitive files such as:

* `.env` files containing environment variables
* `.git` directories and configuration
* `.htaccess` and other web server configuration files
* Any custom hidden files or directories

When a request is made for a hidden file, the server returns a `404 Not Found` response for security reasons, without revealing whether the file actually exists.

{% hint style="info" %}
**Security Note:** This protection is enabled by default and cannot be disabled. It's a fundamental security feature designed to prevent accidental exposure of sensitive configuration files.
{% endhint %}

## 🩺 Health Check Endpoints

The MiniServer provides comprehensive health monitoring capabilities through dedicated endpoints:

### Basic Health Checks

Enable health checks with the `--health-check` flag:

```bash
boxlang-miniserver --health-check
```

This enables three endpoints:

* **`/health`** - Complete health information including system metrics, JVM details, and runtime status
* **`/health/ready`** - Readiness probe for load balancers (simple UP/DOWN status)
* **`/health/live`** - Liveness probe for container orchestration (simple UP/DOWN status)

### Secure Health Checks

For production environments, use the `--health-check-secure` flag:

```bash
boxlang-miniserver --health-check --health-check-secure
```

When secure mode is enabled:

* **Localhost requests** receive full detailed health information
* **Remote requests** receive only basic status information
* This prevents sensitive system information from being exposed to external networks

### Health Check Response Format

The `/health` endpoint returns comprehensive JSON information:

```json
{
  "status": "UP",
  "timestamp": "2025-08-01T17:05:47.587438Z",
  "uptime": "1m 47s",
  "uptimeMs": 107245,
  "version": "1.4.0-snapshot+0",
  "buildDate": "2025-08-01 16:03:36",
  "javaVersion": "17.0.2",
  "memoryUsed": 152093696,
  "memoryMax": 4294967296
}
```

The health check provides:

* **Status** - Current server status (UP/DOWN)
* **Timestamp** - Current server time in ISO format
* **Uptime** - Human-readable server uptime
* **UptimeMs** - Server uptime in milliseconds
* **Version** - BoxLang version information
* **Build Date** - When BoxLang was built
* **Java Version** - JVM version information
* **Memory Usage** - Current memory usage in bytes
* **Memory Max** - Maximum available memory in bytes

## 🌍 Environment Variable Loading

The MiniServer automatically loads environment variables from `.env` files located in your webroot directory:

### Automatic .env Loading

When you start the server, it will automatically look for and load a `.env` file in the webroot:

```bash
# If webroot contains a .env file, you'll see:
+ Loaded environment variables from: /path/to/webroot/.env
```

### .env File Format

Your `.env` file should contain key-value pairs:

```bash
# .env file example
DATABASE_URL=jdbc:mysql://localhost:3306/mydb
API_KEY=your-secret-api-key
DEBUG_MODE=true
CUSTOM_SETTING=value
```

### Accessing Loaded Variables

Environment variables loaded from `.env` files are:

1. **Added to Java System Properties** - Accessible via `System.getProperty("key")`
2. **Available in BoxLang** - Accessible through the `server.system.properties` struct
3. **Available to your applications** - Can be used in BoxLang code for configuration

{% hint style="info" %}
**Privacy Note:** Environment variables are NOT exposed through health check endpoints. Health checks only return basic server metrics and status information for security purposes.
{% endhint %}

## 🔌 WebSocket Support

The BoxLang MiniServer includes built-in WebSocket support for real-time communication:

### WebSocket Endpoint

WebSocket connections are available at the `/ws` endpoint:

```javascript
// JavaScript client example
const socket = new WebSocket('ws://localhost:8080/ws');

socket.onopen = function(event) {
    console.log('Connected to BoxLang WebSocket server');
};

socket.onmessage = function(event) {
    console.log('Message from server:', event.data);
};

socket.onclose = function(event) {
    console.log('Disconnected from server');
};
```

### SocketBox - BoxLang WebSocket Library

For enhanced WebSocket functionality in your BoxLang applications, we recommend using **SocketBox** - our companion library specifically designed for BoxLang WebSocket development:

{% hint style="success" %}
**SocketBox** is available on ForgeBox: [https://forgebox.io/view/socketbox](https://forgebox.io/view/socketbox)
{% endhint %}

SocketBox provides:

* **High-level WebSocket abstractions** for BoxLang applications
* **Event-driven architecture** with listeners and handlers
* **Room and namespace management** for organizing connections
* **Built-in authentication and authorization** support
* **Message broadcasting** to multiple clients
* **Connection lifecycle management** with automatic reconnection
* **Integration with BoxLang frameworks** like ColdBox

#### Installing SocketBox

```bash
# Install via CommandBox
box install socketbox

# Or download from ForgeBox
# https://forgebox.io/view/socketbox
```

#### SocketBox Example

```javascript
// BoxLang server-side WebSocket handler using SocketBox
class {

    function onConnect( socket, data ) {
        // Handle new WebSocket connection
        socket.join( "chatRoom" )
        socket.broadcast( "userJoined", { user: data.username } )
    }

    function onMessage( socket, message ) {
        // Handle incoming messages
        socket.to( "chatRoom" ).emit( "newMessage", {
            user: socket.data.username,
            text: message.text,
            timestamp: now()
        })
    }

    function onDisconnect( socket ) {
        // Handle client disconnection
        socket.broadcast( "userLeft", { user: socket.data.username } )
    }
}
```

### WebSocket Features

* **Real-time bidirectional communication** between client and server
* **Automatic connection management** with built-in error handling
* **Integration with BoxLang runtime** for server-side message processing
* **Low latency** communication for interactive applications
* **Enhanced functionality** with SocketBox library for production applications

The WebSocket server is automatically started when the MiniServer launches, as indicated by the console message:

```bash
+ WebSocket Server started
```

{% hint style="info" %}
**WebSocket Note:** The WebSocket endpoint is always enabled and cannot be disabled. This provides a consistent real-time communication channel for all BoxLang applications. For production applications, consider using SocketBox for enhanced features and easier development.
{% endhint %}

## 🏠 Default Welcome Files

The BoxLang MiniServer automatically serves welcome files when a request is made to a directory. The server looks for these files in the following order:

1. `index.bxm` - BoxLang Markup (preferred)
2. `index.bxs` - BoxLang Script
3. `index.cfm` - CFML Markup (legacy compatibility)
4. `index.cfs` - CFML Script (legacy compatibility)
5. `index.htm` - HTML
6. `index.html` - HTML

### Welcome File Behavior

When a request is made to a directory (e.g., `http://localhost:8080/`), the server will:

1. **Check for welcome files** in the order listed above
2. **Serve the first match** found in the directory
3. **Enable directory listing** if no welcome file is found (showing folder contents)
4. **Process BoxLang/CFML files** through the runtime before serving
5. **Serve static files** (HTML) directly without processing

### Example Directory Structure

```
webroot/
├── index.bxm          # ✅ Will be served for /
├── index.html         # ❌ Will be ignored (index.bxm takes precedence)
├── subfolder/
│   ├── index.cfm      # ✅ Will be served for /subfolder/
│   └── page.bxm       # ✅ Available at /subfolder/page.bxm
└── static/
    └── styles.css     # ✅ Available at /static/styles.css
```

{% hint style="success" %}
**Tip:** Use `index.bxm` for your main pages to take advantage of BoxLang's modern syntax and features while maintaining compatibility with legacy CFML files.
{% endhint %}

## 🔀 URL Rewrites

The BoxLang MiniServer supports URL rewrites for creating clean, SEO-friendly URLs and building single-page applications (SPAs):

### Enabling URL Rewrites

Enable URL rewrites with the `--rewrites` flag:

```bash
# Enable rewrites with default file (index.bxm)
boxlang-miniserver --rewrites

# Enable rewrites with custom file
boxlang-miniserver --rewrites app.bxm

# Using environment variable
BOXLANG_REWRITES=true boxlang-miniserver
```

### How URL Rewrites Work

When URL rewrites are enabled:

1. **All requests** are routed to your specified rewrite file (default: `index.bxm`)
2. **Static files** (CSS, JS, images) are served directly without rewriting
3. **BoxLang/CFML files** that exist are served normally (not rewritten)
4. **Non-existent URLs** are routed to your rewrite file for custom handling

### URL Rewrite Examples

```javascript
// In your index.bxm (rewrite handler)
switch( cgi.path_info ) {
    case "/":
        // Home page
        include "views/home.bxm";
        break;

    case "/products":
        // Products listing
        include "views/products.bxm";
        break;

    case "/products/":
        // Individual product (extract ID from URL)
        var productId = listLast( cgi.path_info, "/" );
        request.productId = productId;
        include "views/product-detail.bxm";
        break;

    default:
        // 404 page
        response.setStatus( 404 );
        include "views/404.bxm";
}
```

### Use Cases for URL Rewrites

* **Single Page Applications (SPAs)** - Route all requests to your main app file
* **Clean URLs** - `/products/123` instead of `/product.bxm?id=123`
* **Custom routing** - Implement your own URL routing logic
* **Framework applications** - Perfect for ColdBox, FW/1, or custom frameworks

### Console Output

When rewrites are enabled, you'll see:

```bash
+ Enabling rewrites to /index.bxm
```

{% hint style="info" %}
**Rewrite Note:** URL rewrites work best for dynamic applications and frameworks. Static websites typically don't need URL rewriting enabled.
{% endhint %}

## 🛑 Server Management

### Graceful Shutdown

The BoxLang MiniServer supports graceful shutdown for safe server termination:

```bash
# Stop the server gracefully
Press Ctrl+C
```

When you stop the server, you'll see:

```bash
Shutting down BoxLang Server...
BoxLang Server stopped.
```

The graceful shutdown process:

1. **Stops accepting new requests** immediately
2. **Completes active requests** before shutting down
3. **Closes the BoxLang runtime** properly
4. **Releases all resources** (ports, file handles, etc.)

### Background Execution

For production deployments, you can run the server in the background:

```bash
# Run in background (Unix/Linux/Mac)
nohup boxlang-miniserver > server.log 2>&1 &

# Or using screen/tmux
screen -S boxlang-server
boxlang-miniserver

# Or using systemd (Linux)
# Create a service file for automatic startup
```

{% hint style="warning" %}
**Production Note:** For production deployments, consider using process managers like systemd, supervisor, or Docker containers for better service management and automatic restarts.
{% endhint %}

## ⚡ Performance Features

The BoxLang MiniServer includes several built-in performance optimizations:

### Automatic GZIP Compression

The server automatically compresses responses using GZIP compression for better performance:

* **Automatic compression** for responses larger than 1.5KB
* **Smart content detection** - only compresses suitable content types
* **Client support detection** - only compresses when client supports it
* **Bandwidth savings** - typically 60-80% reduction in transfer size

### Performance Characteristics

* **Fast startup times** - typically under 1 second
* **Low memory footprint** - minimal overhead beyond your application
* **High concurrency** - built on Undertow's high-performance architecture
* **Zero-copy static file serving** - optimized static asset delivery
* **Keep-alive connections** - reduces connection overhead

### Performance Tips

```bash
# Allocate more memory for better performance
BOXLANG_MINISERVER_OPTS="-Xmx2g -Xms512m" boxlang-miniserver

# Enable health checks for monitoring
boxlang-miniserver --health-check

# Use environment variables for configuration
export BOXLANG_PORT=8080
export BOXLANG_HOST=0.0.0.0
boxlang-miniserver
```

{% hint style="success" %}
**Performance Tip:** The MiniServer is optimized for development and light production workloads. For high-traffic applications, consider using CommandBox with load balancing and clustering capabilities.
{% endhint %}

### Using 3rd Party Jars <a href="#using-3rd-party-jars-14" id="using-3rd-party-jars-14"></a>

You can load up custom third-party JARs into the runtime in two ways

1. `BOXLANG_HOME/lib` - You can place all the jars that the runtime will load in this location
   1. Remember, you can use the `--serverHome` to choose the location of the server's home
2. Add via the classpath to your runner.

Please note that if you use the `-cp` approach, then you need to use a full `java -cp` syntax or you can customize the `boxlang-miniserver` shell scripts to do your bidding.

If you want to test 3rd part libs with the web server, you’ll need to use a different syntax that uses the `-cp` (classpath) JVM arg and specifies both the boxlang jar AND a semicolon-delimited list of the jars you want to use. It’s a little annoying, but this is how Java works.

```bash
# Format
java -cp {jarpath;jarpath2} ortus.boxlang.web.MiniServer


# Example
java -cp boxlang-miniserver-1.0.0.jar;/path/to/my.jar;/path/to/another.jar ortus.boxlang.web.MiniServer
```

### Modules

The MiniServer can use any module you install into the OS home via the `install-bx-module` binary.  However, if you choose your own server home using the `server-home` argument or the environment variable.  Then, place the modules inside a `modules` directory inside the server's home.

### JVM Options

You can use the `BOXLANG_MINISERVER_OPTS` env variable to seed the Java arguments the miniserver will start with.

```bash
BOXLANG_MINISERVER_OPTS="-Xmx512m"
boxlang-miniserver
```

### Runtime Source Code

The runtime source code can be found here: [https://github.com/ortus-boxlang/boxlang-miniserver](https://github.com/ortus-boxlang/boxlang-miniserver)

We welcome any pull requests, testing, docs, etc.
