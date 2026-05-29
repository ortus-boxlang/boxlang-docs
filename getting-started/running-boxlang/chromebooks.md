---
description: Learn how to code with BoxLang on your Chromebook using Linux development environment!
icon: chrome
---

# Chromebooks

<figure><img src="../../.gitbook/assets/chromebooks.png" alt=""><figcaption></figcaption></figure>

We love Chromebooks! This comprehensive guide will help you run and develop BoxLang applications on both Intel-based and ARM-based Chromebooks. We'll install all prerequisites, set up BoxLang, configure VS Code with the BoxLang extension, and create your first application.

{% embed url="https://www.google.com/chromebook/" %}

<figure><img src="../../.gitbook/assets/CB_Hero_Base.width-1200.format-webp.webp" alt=""><figcaption><p><a href="https://www.google.com/chromebook/">https://www.google.com/chromebook/</a></p></figcaption></figure>

## Requirements

* **Hardware**: 4GB RAM Chromebook minimum (8GB+ recommended for better performance)
* **Operating System**: Chrome OS with Linux development environment enabled
* **Java Runtime**: OpenJDK 21 or higher
* **Storage**: At least 2GB free space for development tools

### Enabling Linux Development Environment

Chromebooks provide excellent development capabilities through their built-in Linux development environment (based on Debian). This allows you to run a full Linux container alongside Chrome OS seamlessly.

**To enable Linux development:**

1. Open **Settings** > **Advanced** > **Developers**
2. Turn on **Linux development environment**
3. Follow the setup wizard to configure your container
4. Choose appropriate storage size (4GB minimum, 8GB+ recommended)

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-23 19.44.51.png" alt=""><figcaption><p>Enable Linux Development Environment</p></figcaption></figure>

{% hint style="info" %}
**Pro Tip**: The Linux environment runs in a secure container that's isolated from Chrome OS, providing a safe development space while maintaining system security.
{% endhint %}

## 📋 Table of Contents

- [Requirements](#requirements)
- [Accessing the Linux Terminal](#accessing-the-linux-terminal)
- [Installing Java](#installing-java)
- [Installing BoxLang](#installing-boxlang)
- [Installing VS Code](#installing-vs-code)
- [Creating Your First App](#creating-your-first-app)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)

## Accessing the Linux Terminal

You'll interact with the Linux development environment through the **Terminal** application, which provides full command-line access to your Debian container.

**To open the terminal:**

1. Press **Alt + Shift + T** (keyboard shortcut)
2. Or search for "Terminal" in the launcher
3. Or use the **Everything** button and search for "Terminal"

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-23 19.51.21.png" alt=""><figcaption><p>Terminal Application</p></figcaption></figure>

Click on the **Penguin** tab to access your Linux environment:

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-23 19.45.53 (1).png" alt=""><figcaption><p>Linux Terminal Environment</p></figcaption></figure>

## Setting Up the Development Environment

{% stepper %}

{% step %}
### System Updates and Essential Tools

Start by updating your system and installing essential development tools:

```bash
# Update package lists and upgrade system
sudo apt update && sudo apt full-upgrade -y

# Install essential development tools
sudo apt install -y \
    curl \
    wget \
    git \
    zip \
    unzip \
    build-essential \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    gnome-keyring
```

{% endstep %}

{% step %}
### Installing Java 21

Modern Debian distributions now include OpenJDK 21. Try the simple installation first:

```bash
# Try the easy installation first
sudo apt install -y openjdk-21-jdk

# Verify installation
java -version
```

If OpenJDK 21 isn't available in your distribution's repositories, install it manually:

#### Manual Java Installation

If the package manager installation didn't work, install Java manually:

```bash
# Determine your architecture
ARCH=$(dpkg --print-architecture)
echo "Architecture: $ARCH"

# Download OpenJDK 21 based on architecture
if [ "$ARCH" = "amd64" ]; then
    # For x64/Intel Chromebooks
    wget https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.4%2B7/OpenJDK21U-jdk_x64_linux_hotspot_21.0.4_7.tar.gz
    TAR_FILE="OpenJDK21U-jdk_x64_linux_hotspot_21.0.4_7.tar.gz"
    JDK_DIR="jdk-21.0.4+7"
elif [ "$ARCH" = "arm64" ] || [ "$ARCH" = "aarch64" ]; then
    # For ARM Chromebooks
    wget https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.4%2B7/OpenJDK21U-jdk_aarch64_linux_hotspot_21.0.4_7.tar.gz
    TAR_FILE="OpenJDK21U-jdk_aarch64_linux_hotspot_21.0.4_7.tar.gz"
    JDK_DIR="jdk-21.0.4+7"
else
    echo "Unsupported architecture: $ARCH"
    exit 1
fi

# Extract and install
tar -xzf $TAR_FILE
sudo mkdir -p /usr/lib/jvm
sudo mv $JDK_DIR /usr/lib/jvm/

# Set up environment variables
echo "export JAVA_HOME=/usr/lib/jvm/$JDK_DIR" >> ~/.bashrc
echo "export PATH=\$PATH:\$JAVA_HOME/bin" >> ~/.bashrc

# Add to sudo PATH
echo "Defaults secure_path=\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/jvm/$JDK_DIR/bin\"" | sudo tee /etc/sudoers.d/java

# Reload environment
source ~/.bashrc

# Verify installation
java -version
```

{% hint style="success" %}
**Modern Note**: Most current Debian-based distributions now include OpenJDK 21 in their repositories, making the simple `apt install` method the preferred approach.
{% endhint %}

{% endstep %}

{% step %}
### Installing BoxLang

BoxLang installation is straightforward with the official installer script:

```bash
# Run the BoxLang installer
sudo /bin/bash -c "$(curl -fsSL https://downloads.ortussolutions.com/ortussolutions/boxlang/install-boxlang.sh)"
```

**Verify the installation:**

```bash
# Check BoxLang version
boxlang --version

# Test the REPL
boxlang
```

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>BoxLang REPL on Chromebook</p></figcaption></figure>

The REPL (Read-Eval-Print Loop) opens, allowing you to start coding immediately, run BoxLang files, start web servers, and much more!

{% endstep %}

## Setting Up VS Code with BoxLang

{% step %}
### Installing Visual Studio Code

VS Code provides excellent BoxLang development support with syntax highlighting, debugging, and integrated development features.

**Download and install VS Code:**

1. Visit the [VS Code download page](https://code.visualstudio.com/download)
2. Choose the **Linux** version and select the **.deb** package appropriate for your architecture:
   * **Intel/AMD64**: Download the x64 .deb package
   * **ARM**: Download the ARM64 .deb package

{% hint style="info" %}
**Architecture Check**: If unsure about your Chromebook's processor type, run `dpkg --print-architecture` in the terminal to verify.
{% endhint %}

**Install the downloaded package:**

```bash
# Navigate to Downloads folder
cd ~/Downloads

# Install VS Code (replace with your downloaded filename)
sudo dpkg -i code_*.deb

# Fix any missing dependencies
sudo apt-get install -f
```

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>VS Code Installation</p></figcaption></figure>

{% endstep %}

{% step %}
### Installing the BoxLang Extension

1. **Open VS Code** from your applications menu
2. **Access Extensions**: Click the Extensions icon (⬜) or press `Ctrl+Shift+X`
3. **Search for BoxLang**: Type "BoxLang" in the search box
4. **Install the extension**: Click "Install" on the official BoxLang extension by Ortus Solutions

<figure><img src="../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption><p>VS Code Extensions Marketplace</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption><p>BoxLang Extension Installation</p></figcaption></figure>

The BoxLang extension provides:

* **Syntax Highlighting**: Full BoxLang syntax support
* **Code Completion**: Intelligent IntelliSense for BoxLang
* **Debugging Support**: Set breakpoints and debug your applications
* **Integrated Terminal**: Run BoxLang commands directly
* **Web Server Integration**: Start and manage BoxLang web servers
* **REPL Integration**: Interactive BoxLang development

{% endstep %}

## Creating Your First BoxLang Application

{% step %}
### Your First BoxLang Class

Let's create your first BoxLang application to test everything is working correctly.

**Create a new file:**

1. **Create a project folder**:

   ```bash
   mkdir ~/boxlang-projects
   cd ~/boxlang-projects
   ```

2. **Open VS Code in this folder**:

   ```bash
   code .
   ```

3. **Create a new file** called `Hello.bx`

**Add the following code:**

```javascript
class {

    function main( args = [] ) {
        println( "🚀 Hello from Chromebook and BoxLang! " );
        println( "📅 Current time: #now()#" );
        println( "💻 System architecture: #createObject( 'java', 'java.lang.System' ).getProperty( 'os.arch' )#" );

        return "BoxLang is running perfectly on your Chromebook! 🎉";
    }

}
```

<figure><img src="../../.gitbook/assets/image (4) (1).png" alt=""><figcaption><p>BoxLang Hello World Class</p></figcaption></figure>

**Run your application:**

* **Method 1**: Right-click in the editor and select **"BoxLang: Run File"**
* **Method 2**: Use the command palette (`Ctrl+Shift+P`) and search for "BoxLang: Run File"
* **Method 3**: Use the terminal: `boxlang Hello.bx`

**Expected output:**
```
🚀 Hello from Chromebook and BoxLang!
📅 Current time: {ts '2024-05-23 18:27:33'}
💻 System architecture: aarch64
BoxLang is running perfectly on your Chromebook! 🎉
```

{% endstep %}

{% step %}
### Creating a Web Application

Now let's create a web application using BoxLang's templating system.

**Create a template file** called `index.bxm`:

```xml
<bx:output>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BoxLang on Chromebook</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
        }
        .container {
            background: rgba(255,255,255,0.1);
            padding: 2rem;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        h1 { color: #fff; text-align: center; }
        .info { background: rgba(255,255,255,0.1); padding: 1rem; margin: 1rem 0; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 BoxLang Web Server on Chromebook!</h1>

        <div class="info">
            <h3>📅 Server Information</h3>
            <p><strong>Current Time:</strong> #now()#</p>
            <p><strong>BoxLang Version:</strong> #server.boxlang.version#</p>
            <p><strong>Server Host:</strong> #cgi.server_name#:#cgi.server_port#</p>
        </div>

        <div class="info">
            <h3>💻 System Details</h3>
            <p><strong>OS:</strong> #createObject( 'java', 'java.lang.System' ).getProperty( 'os.name' )#</p>
            <p><strong>Architecture:</strong> #createObject( 'java', 'java.lang.System' ).getProperty( 'os.arch' )#</p>
            <p><strong>Java Version:</strong> #createObject( 'java', 'java.lang.System' ).getProperty( 'java.version' )#</p>
        </div>

        <div class="info">
            <h3>🎯 Next Steps</h3>
            <ul>
                <li>Explore the <a href="https://boxlang.ortusbooks.com/" target="_blank">BoxLang Documentation</a></li>
                <li>Try building REST APIs with BoxLang</li>
                <li>Create dynamic web applications</li>
                <li>Integrate with databases and external services</li>
            </ul>
        </div>
    </div>
</body>
</html>
</bx:output>
```

{% endstep %}

{% step %}
### Starting the BoxLang Web Server

**Start the integrated web server:**

1. **Open Command Palette**: Press `Ctrl+Shift+P`
2. **Search for BoxLang**: Type "BoxLang" to see available commands
3. **Select "BoxLang: Start Web Server"**

<figure><img src="../../.gitbook/assets/image (5) (1).png" alt=""><figcaption><p>BoxLang VS Code Commands</p></figcaption></figure>

**You'll see output in the debug console:**
```
🚀 Starting BoxLang Server...
📁 Web Root: /home/username/boxlang-projects
🌐 Host: localhost
🔌 Port: 8080
🐛 Debug: false
⚙️  Config Path: null
🏠 Server Home: null
🚀 Starting BoxLang Runtime...
✅ Runtime Started in 2043ms
✅ BoxLang MiniServer started in 2135ms
🌐 BoxLang MiniServer available at: http://localhost:8080
Press Ctrl+C to stop the server.
```

**Access your web application:**

VS Code will automatically open your browser, or you can manually navigate to `http://localhost:8080`

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption><p>BoxLang Web Application Running</p></figcaption></figure>

Congratulations! 🎉 You've successfully created and deployed your first BoxLang web application on a Chromebook!

{% endstep %}
{% endstepper %}

## Next Steps and Development Tips

### Performance Optimization for Chromebooks

**Memory Management:**

* Close unused browser tabs when developing
* Use `boxlang --help` to see memory configuration options
* Monitor system resources in Chrome OS Task Manager

**Development Best Practices:**

* Use the integrated VS Code terminal for BoxLang commands
* Leverage VS Code's built-in Git support for version control
* Take advantage of VS Code's IntelliSense for BoxLang development

### Useful BoxLang Commands for Development

```bash
# Check BoxLang version and help
boxlang --version
boxlang --help

# Run BoxLang files directly
boxlang myScript.bx

# Start REPL for interactive development
boxlang

# Start web server with custom port
boxlang --server-port 9090

# Start server with debug mode
boxlang --server-debug true
```

### Additional Resources

* 📚 **[BoxLang Documentation](https://boxlang.ortusbooks.com/)** - Complete language reference
* 🌐 **[BoxLang GitHub](https://github.com/ortus-boxlang/boxlang)** - Source code and issues
* 💬 **[Community Discord](https://discord.gg/ortussolutions)** - Get help from the community
* 🎓 **[BoxLang Examples](https://github.com/ortus-boxlang/boxlang-examples)** - Sample applications and tutorials

### Troubleshooting Common Issues

**Java-related issues:**

```bash
# Verify Java installation
java -version
echo $JAVA_HOME

# If Java isn't found, source your profile
source ~/.bashrc
```

**BoxLang server issues:**

```bash
# Check if port is in use
netstat -tulpn | grep :8080

# Stop any running BoxLang processes
pkill -f boxlang
```

**VS Code extension issues:**

* Restart VS Code if BoxLang commands aren't working
* Check the Output panel for BoxLang extension logs
* Ensure the BoxLang binary is in your PATH

## Conclusion

You've successfully set up a complete BoxLang development environment on your Chromebook! This setup provides:

✅ **Full Java 21 development environment**
✅ **BoxLang runtime with REPL support**
✅ **VS Code with BoxLang extension**
✅ **Integrated web server capabilities**
✅ **Modern development workflow**

Your Chromebook is now ready for professional BoxLang development. Whether you're building web applications, APIs, or exploring the language features, you have everything needed to create amazing BoxLang applications.

{% hint style="success" %}
**Pro Tip**: This entire guide was written and tested on a Lenovo Duet 5 Chromebook, proving that Chromebooks are excellent development machines for BoxLang! 💻✨
{% endhint %}

Happy coding with BoxLang on your Chromebook! 🚀
