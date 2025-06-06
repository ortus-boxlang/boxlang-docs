---
description: >-
  Maven Integration allows BoxLang to seamlessly incorporate Java dependencies
  into your runtime, expanding your application's capabilities with the vast
  Java ecosystem.
icon: magento
---

# Maven Integration

<figure><img src="../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

BoxLang offers seamless integration with [Maven](https://central.sonatype.com/), the widely used Java build and dependency management tool. This integration enables you to easily integrate third-party Java libraries into your BoxLang runtime, providing access to the vast Java ecosystem without requiring complex setup procedures.

## Overview

The Maven integration in BoxLang works through a simple but powerful mechanism:

* **Centralized Dependency Management**: Use Maven's `pom.xml` to declare all your Java dependencies
* **Automatic Download**: Maven handles downloading and resolving dependency conflicts
* **Runtime Integration**: BoxLang automatically loads all JARs from the `lib/` folder
* **Simple Workflow**: Add dependencies, run `mvn install`, and start using Java libraries immediately

## Installing Maven

Before you can use Maven integration, you need to have Maven installed on your system.

{% tabs %}
{% tab title="Windows" %}
**Option 1: Using Chocolatey (Recommended)**

```bash
choco install maven
```

**Option 2: Using Scoop**

```bash
scoop install maven
```

**Option 3: Manual Installation**

1. Download Maven from [maven.apache.org](https://maven.apache.org/download.cgi)
2. Extract to `C:\Program Files\Apache\maven`
3. Add `C:\Program Files\Apache\maven\bin` to your PATH environment variable
{% endtab %}

{% tab title="Mac OS" %}
**Option 1: Using Homebrew (Recommended)**

```bash
brew install maven
```

**Option 2: Using MacPorts**

```bash
sudo port install maven3
```

**Option 3: Using sdkman**

```bash
sdk install maven {version}
```
{% endtab %}

{% tab title="Linux" %}
**Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install maven
```

**CentOS/RHEL/Fedora:**

```bash
sudo yum install maven
# or for newer versions
sudo dnf install maven
```

**Arch Linux:**

```bash
sudo pacman -S maven
```

**SDKMan:**

```bash
sdk install maven {version}
```
{% endtab %}
{% endtabs %}

### Verify Installation

After installation, verify that Maven is working:

```bash
mvn -version
```

You should see output showing the Maven version, Java version, and OS information.

## Getting Started

The BoxLang home by default is located in your user's home directory: `~/.boxlang`

### The BoxLang POM File

BoxLang Home includes a pre-configured `pom.xml` file specifically designed for runtime dependency management:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>io.boxlang</groupId>
    <artifactId>runtime-library</artifactId>
    <version>@build.version@</version>

    <dependencies>
        <!-- Add your Java dependencies here -->
    </dependencies>

    <build>
        <directory>${project.basedir}/.tmp</directory>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-dependency-plugin</artifactId>
                <version>3.1.2</version>
                <executions>
                    <execution>
                        <id>copy-dependencies</id>
                        <phase>install</phase>
                        <goals>
                            <goal>copy-dependencies</goal>
                        </goals>
                        <configuration>
                            <outputDirectory>${project.basedir}/lib</outputDirectory>
                            <includeScope>runtime</includeScope>
                            <excludeScope>test</excludeScope>
                            <excludeScope>provided</excludeScope>
                            <overWriteReleases>true</overWriteReleases>
                            <overWriteSnapshots>true</overWriteSnapshots>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### Basic Workflow

1. **Edit the POM**: Add your desired dependencies to the `<dependencies>` section
2. **Install Dependencies**: Run `mvn install` in the BoxLang Home directory
3. **Use Libraries**: Start using the Java libraries in your BoxLang code immediately

### Adding Dependencies

#### Finding Dependencies

Use [Maven Central](https://central.sonatype.com/) to find the dependencies you need. Simply search for the library and copy the Maven coordinates.

#### Adding a Dependency

Edit the `pom.xml` file and add your dependency inside the `<dependencies>` section:

```xml
<dependencies>
    <!-- Apache Commons Text for string manipulation -->
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-text</artifactId>
        <version>1.12.0</version>
    </dependency>
    
    <!-- QR Code generation -->
    <dependency>
        <groupId>com.google.zxing</groupId>
        <artifactId>core</artifactId>
        <version>3.5.2</version>
    </dependency>
    <dependency>
        <groupId>com.google.zxing</groupId>
        <artifactId>javase</artifactId>
        <version>3.5.2</version>
    </dependency>
    
    <!-- PDF generation with iText -->
    <dependency>
        <groupId>com.itextpdf</groupId>
        <artifactId>itext7-core</artifactId>
        <version>8.0.2</version>
        <type>pom</type>
    </dependency>
</dependencies>
```

#### Installing Dependencies

Navigate to your BoxLang Home directory and run:

```bash
mvn install
```

This command will:

* Download all declared dependencies and their transitive dependencies
* Place all JARs in the `lib/` folder
* Make them available to the BoxLang runtime

#### Cleaning Dependencies

To remove all downloaded dependencies:

```bash
mvn clean
```

This will clear the `lib/` folder of all Maven-managed JARs.

## Practical Examples

### Text Processing with Apache Commons

Add powerful text processing capabilities to your BoxLang applications:

```xml
<!-- Add to pom.xml -->
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-text</artifactId>
    <version>1.12.0</version>
</dependency>
```

```javascript
// Use in BoxLang after mvn install
stringEscapeUtils = new org.apache.commons.text.StringEscapeUtils()
wordUtils = new org.apache.commons.text.WordUtils()

// Escape HTML
safeHTML = stringEscapeUtils.escapeHtml4( "<script>alert('xss')</script>" )
println( "Safe HTML: " & safeHTML )

// Capitalize words
title = wordUtils.capitalizeFully( "the quick brown fox" )
println( "Title: " & title ) // "The Quick Brown Fox"

// Text similarity
similarity = new org.apache.commons.text.similarity.JaroWinklerSimilarity()
score = similarity.apply( "BoxLang", "BoxScript" )
println( "Similarity: " & score )
```

### QR Code Generation

Add QR code generation capabilities to your BoxLang applications:

```xml
<!-- Add to pom.xml -->
<dependency>
    <groupId>com.google.zxing</groupId>
    <artifactId>core</artifactId>
    <version>3.5.2</version>
</dependency>
<dependency>
    <groupId>com.google.zxing</groupId>
    <artifactId>javase</artifactId>
    <version>3.5.2</version>
</dependency>
```

```javascript
// QR Code generator utility
function createQRCodeGenerator() {
    return {
        "generate": ( text, size = 300 ) -> {
            var writer = new com.google.zxing.qrcode.QRCodeWriter()
            var bitMatrix = writer.encode( 
                text, 
                new com.google.zxing.BarcodeFormat().QR_CODE, 
                size, 
                size 
            )
            
            return new com.google.zxing.client.j2se.MatrixToImageWriter()
                .toBufferedImage( bitMatrix )
        },
        
        "saveToFile": ( text, filePath, size = 300 ) -> {
            var image = this.generate( text, size )
            var file = new java.io.File( filePath )
            
            new javax.imageio.ImageIO().write( image, "PNG", file )
            return filePath
        },
        
        "generateDataURL": ( text, size = 300 ) -> {
            var image = this.generate( text, size )
            var baos = new java.io.ByteArrayOutputStream()
            
            new javax.imageio.ImageIO().write( image, "PNG", baos )
            var bytes = baos.toByteArray()
            var encoder = new java.util.Base64().getEncoder()
            
            return "data:image/png;base64," & encoder.encodeToString( bytes )
        }
    }
}

// Usage
qrGenerator = createQRCodeGenerator()

// Generate QR code for a URL
qrFile = qrGenerator.saveToFile( 
    "https://boxlang.ortussolutions.com", 
    "/tmp/boxlang-qr.png", 
    400 
)
println( "QR code saved to: " & qrFile )

// Generate QR code as data URL for web use
dataURL = qrGenerator.generateDataURL( "BoxLang is awesome!" )
println( "Data URL: " & dataURL.left( 50 ) & "..." )
```

### PDF Generation with iText

Create dynamic PDFs programmatically:

```xml
<!-- Add to pom.xml -->
<dependency>
    <groupId>com.itextpdf</groupId>
    <artifactId>itext7-core</artifactId>
    <version>8.0.2</version>
    <type>pom</type>
</dependency>
```

```javascript
// PDF generator utility
function createPDFGenerator() {
    return {
        "createSimplePDF": ( filePath, content ) -> {
            var writer = new com.itextpdf.kernel.pdf.PdfWriter( filePath )
            var pdf = new com.itextpdf.kernel.pdf.PdfDocument( writer )
            var document = new com.itextpdf.layout.Document( pdf )
            
            var paragraph = new com.itextpdf.layout.element.Paragraph( content )
            document.add( paragraph )
            
            document.close()
            return filePath
        },
        
        "createStyledPDF": ( filePath, title, content ) -> {
            var writer = new com.itextpdf.kernel.pdf.PdfWriter( filePath )
            var pdf = new com.itextpdf.kernel.pdf.PdfDocument( writer )
            var document = new com.itextpdf.layout.Document( pdf )
            
            // Add title
            var titleParagraph = new com.itextpdf.layout.element.Paragraph( title )
                .setFontSize( 20 )
                .setBold()
            document.add( titleParagraph )
            
            // Add content
            var contentParagraph = new com.itextpdf.layout.element.Paragraph( content )
                .setFontSize( 12 )
            document.add( contentParagraph )
            
            // Add table
            var table = new com.itextpdf.layout.element.Table( [ 1, 1, 1 ] )
            table.addCell( "Feature" )
            table.addCell( "BoxLang" )
            table.addCell( "Status" )
            table.addCell( "Dynamic Typing" )
            table.addCell( "✓" )
            table.addCell( "Active" )
            table.addCell( "Java Integration" )
            table.addCell( "✓" )
            table.addCell( "Active" )
            
            document.add( table )
            
            document.close()
            return filePath
        }
    }
}

// Usage
pdfGen = createPDFGenerator()

// Simple PDF
simplePDF = pdfGen.createSimplePDF( 
    "/tmp/simple-report.pdf", 
    "This is a PDF generated from BoxLang using iText!" 
)

// Styled PDF with table
styledPDF = pdfGen.createStyledPDF(
    "/tmp/boxlang-features.pdf",
    "BoxLang Feature Report",
    "BoxLang combines the flexibility of dynamic languages with the power of the JVM."
)

println( "PDFs created: " & simplePDF & " and " & styledPDF )
```

### Encryption and Security

Add cryptographic capabilities with Bouncy Castle:

```xml
<!-- Add Bouncy Castle for cryptography -->
<dependency>
    <groupId>org.bouncycastle</groupId>
    <artifactId>bcprov-jdk18on</artifactId>
    <version>1.77</version>
</dependency>
```

```javascript
// Encryption utility
function createEncryptionUtil() {
    // Add Bouncy Castle as security provider
    var provider = new org.bouncycastle.jce.provider.BouncyCastleProvider()
    var security = new java.security.Security()
    security.addProvider( provider )
    
    return {
        "generateKeyPair": () -> {
            var keyGen = new java.security.KeyPairGenerator().getInstance( "RSA", "BC" )
            keyGen.initialize( 2048 )
            return keyGen.generateKeyPair()
        },
        
        "encrypt": ( data, publicKey ) -> {
            var cipher = new javax.crypto.Cipher().getInstance( "RSA/ECB/PKCS1Padding", "BC" )
            cipher.init( new javax.crypto.Cipher().ENCRYPT_MODE, publicKey )
            return cipher.doFinal( data.getBytes() )
        },
        
        "decrypt": ( encryptedData, privateKey ) -> {
            var cipher = new javax.crypto.Cipher().getInstance( "RSA/ECB/PKCS1Padding", "BC" )
            cipher.init( new javax.crypto.Cipher().DECRYPT_MODE, privateKey )
            var decrypted = cipher.doFinal( encryptedData )
            return new java.lang.String( decrypted )
        }
    }
}

// Usage
encryption = createEncryptionUtil()
keyPair = encryption.generateKeyPair()

message = "Secret BoxLang message"
encrypted = encryption.encrypt( message, keyPair.getPublic() )
decrypted = encryption.decrypt( encrypted, keyPair.getPrivate() )

println( "Original: " & message )
println( "Decrypted: " & decrypted )
```

## Advanced Usage Patterns

#### Multi-Module Dependencies

For large applications, organize dependencies by functionality:

```xml
<dependencies>
    <!-- Document Generation -->
    <dependency>
        <groupId>com.itextpdf</groupId>
        <artifactId>itext7-core</artifactId>
        <version>8.0.2</version>
        <type>pom</type>
    </dependency>
    
    <!-- QR Code Generation -->
    <dependency>
        <groupId>com.google.zxing</groupId>
        <artifactId>core</artifactId>
        <version>3.5.2</version>
    </dependency>
    
    <!-- Cryptography -->
    <dependency>
        <groupId>org.bouncycastle</groupId>
        <artifactId>bcprov-jdk18on</artifactId>
        <version>1.77</version>
    </dependency>
</dependencies>
```

#### Version Management

Use properties for easier version management:

```xml
<properties>
    <zxing.version>3.5.2</zxing.version>
    <commons.version>1.12.0</commons.version>
    <itext.version>8.0.2</itext.version>
</properties>

<dependencies>
    <dependency>
        <groupId>com.google.zxing</groupId>
        <artifactId>core</artifactId>
        <version>${zxing.version}</version>
    </dependency>
    
    <dependency>
        <groupId>com.google.zxing</groupId>
        <artifactId>javase</artifactId>
        <version>${zxing.version}</version>
    </dependency>
    
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-text</artifactId>
        <version>${commons.version}</version>
    </dependency>
</dependencies>
```

#### Excluding Transitive Dependencies

Sometimes you need to exclude specific transitive dependencies:

```xml
<dependency>
    <groupId>com.itextpdf</groupId>
    <artifactId>itext7-core</artifactId>
    <version>8.0.2</version>
    <type>pom</type>
    <exclusions>
        <exclusion>
            <groupId>commons-logging</groupId>
            <artifactId>commons-logging</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

## Best Practices

#### 1. Keep Dependencies Updated

Regularly check for newer versions of your dependencies:

```bash
mvn versions:display-dependency-updates
```

#### 2. Use Specific Versions

Always specify exact versions rather than ranges:

```xml
<!-- Good -->
<version>2.16.0</version>

<!-- Avoid -->
<version>[2.0,3.0)</version>
```

#### 3. Document Your Dependencies

Add comments explaining why each dependency is needed:

```xml
<dependencies>
    <!-- Apache Commons Text - Used for advanced string manipulation in templates -->
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-text</artifactId>
        <version>1.12.0</version>
    </dependency>
    
    <!-- ZXing - Required for QR code generation in reports -->
    <dependency>
        <groupId>com.google.zxing</groupId>
        <artifactId>core</artifactId>
        <version>3.5.2</version>
    </dependency>
    
    <!-- iText - PDF generation for invoices and reports -->
    <dependency>
        <groupId>com.itextpdf</groupId>
        <artifactId>itext7-core</artifactId>
        <version>8.0.2</version>
        <type>pom</type>
    </dependency>
    
    <!-- Bouncy Castle - Cryptography for secure operations -->
    <dependency>
        <groupId>org.bouncycastle</groupId>
        <artifactId>bcprov-jdk18on</artifactId>
        <version>1.77</version>
    </dependency>
</dependencies>
```

#### 4. Test After Adding Dependencies

Always test your BoxLang application after adding new dependencies:

```javascript
// Test that dependencies loaded correctly
function testDependencies() {
    try {
        // Test ZXing (QR Codes)
        var qrWriter = new com.google.zxing.qrcode.QRCodeWriter()
        println( "✅ ZXing QR Code library loaded successfully" )
        
        // Test iText (PDF)
        var pdfWriter = new com.itextpdf.kernel.pdf.PdfWriter()
        println( "✅ iText PDF library loaded successfully" )
        
        // Test Bouncy Castle
        var provider = new org.bouncycastle.jce.provider.BouncyCastleProvider()
        println( "✅ Bouncy Castle loaded successfully" )
        
        return true
    } catch ( any e ) {
        println( "❌ Dependency loading failed: " & e.message )
        return false
    }
}

testDependencies()
```

#### 5. Monitor Dependency Size

Keep an eye on the total size of your `lib/` folder:

```bash
# Check total size of dependencies
du -sh lib/

# List individual JAR sizes
ls -lh lib/*.jar
```

## Troubleshooting

#### Dependency Conflicts

If you encounter dependency conflicts, use Maven's dependency tree to investigate:

```bash
mvn dependency:tree
```

#### Class Loading Issues

If classes aren't found after installation:

1. Verify the JAR is in the `lib/` folder
2. Restart the BoxLang runtime
3. Check for package name typos in your BoxLang code

**If you continue to experience class loading issues, we recommend building BoxLang modules for complete isolation.**

#### Version Compatibility

Some dependencies may require specific versions of Java. Check compatibility before adding:

```bash
# Check Java version
java -version

# Check Maven version
mvn -version
```

## Conclusion

Maven integration makes BoxLang incredibly powerful by providing access to the entire Java ecosystem. Whether you need advanced text processing, HTTP clients, database drivers, encryption libraries, or specialized tools, Maven integration makes it simple to add and manage these dependencies.

Key benefits:

* **🚀 Easy Setup**: Simple `mvn install` command to add dependencies
* **🔧 Automatic Management**: Maven handles dependency resolution and conflicts
* **📚 Vast Ecosystem**: Access to thousands of Java libraries
* **🔄 Version Control**: Easy dependency updates and rollbacks
* **🧹 Clean Management**: Simple cleanup with `mvn clean`

With Maven integration, BoxLang applications can leverage decades of Java library development, making it possible to build enterprise-grade applications with minimal setup complexity.
