---
icon: camera
---

# Image Manipulation

BoxLang has an extensive and awesome image manipulation library that allows you to create and manipulate images with easy syntax. We cannot see every detail about image manipulation, but it is necessary to understand that this functionality is easy in BoxLang and exists.

Apart from core image functions, all functions can be applied to an image object as member functions. Yes, BoxLang allows you to deal with image objects natively.

```
# For Operating Systems using our Quick Installer.
install-bx-module bx-image

# Using CommandBox to install for web servers.
box install bx-image
```

```java
imgObj = imageRead("https://example.com/company-logo.png");
imgObj.resize(50,50);
bx:image action="writeToBrowser" source=imgObj;

imgObj = imageRead("https://example.com/company-logo.png");
imgObj.blur(5);
bx:image action="writeToBrowser" source=imgObj;

imgObj = imageRead("https://example.com/company-logo.png");
imgObj.rotate(90);
bx:image action="writeToBrowser" source=imgObj;

imgObj = imageRead("https://example.com/company-logo.png");
info = imgObj.info();
writeDump(info);
```

### Contributed Functions/Components

The image module has a wide variety of BIFs to aid in manipulating images. You can find individual BIF documentation by following the below link.

{% content-ref url="image-manipulation/reference/built-in-functions/" %}
[built-in-functions](image-manipulation/reference/built-in-functions/)
{% endcontent-ref %}

{% content-ref url="image-manipulation/reference/components/" %}
[components](image-manipulation/reference/components/)
{% endcontent-ref %}

### GitHub Repository and Reporting Issues <a href="#github-repository-and-reporting-issues" id="github-repository-and-reporting-issues"></a>

Visit the [GitHub repository](https://github.com/ortus-boxlang/bx-image) for release notes. You can also file a bug report or improvement suggestion via [Jira](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=13359\&components=27022\&issuetype=1).
