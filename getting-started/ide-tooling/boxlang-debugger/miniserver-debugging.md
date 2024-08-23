---
description: Debug code running on the BoxLang MiniServer
---

# MiniServer Debugging

<figure><img src="../../../.gitbook/assets/miniserver.png" alt=""><figcaption><p>Debug the MiniServer</p></figcaption></figure>

One convenient feature of our official BoxLang VS Code extension is the [built-in MiniServer](../../running-boxlang/miniserver.md). The MiniServer is just that, a web server built to be fast and easy to work with. You can use it to spin up a server in any directory within your project and almost instantly test code. We even save your configuration to reuse your server again in the future! Let’s take a quick look at how to configure the MiniServer and some of its features.

## The MiniServer Panel

After installing the BoxLang extension, you should see a new icon featuring the BoxLang logo in the sidebar. Clicking this icon brings up the BoxLang Server Panel. Here you will see a list of the servers you are currently using for the workspace you are currently in. To start configuring a server click the “+” icon at the top right-hand corner.

<figure><img src="../../../.gitbook/assets/image (27).png" alt="" width="563"><figcaption></figcaption></figure>

When you click the “+” icon, you will be prompted with a series of inputs to help configure your server. After filling out the prompts, your new MiniServer will start-up automatically. Once running, a browser window should open to the port the server configures.

### MiniServer Control Icons

Now that your server is configured, it should show up in the list of available servers. You will see information about the status of your server here as well as some icons to be able to interact with it. Hover your mouse over the server to see what options are available.  When the server is stopped you will see something like this:

<figure><img src="../../../.gitbook/assets/image (28).png" alt="" width="563"><figcaption><p>Stopped Controls</p></figcaption></figure>

* Delete
* Edit (The name)
* Run Server

When the server is running you will see something like this:

<figure><img src="../../../.gitbook/assets/image (29).png" alt="" width="563"><figcaption><p>Running controls</p></figcaption></figure>

* Debug
* Open Browser
* Stop

## Trying Out Your App

The BoxLang MiniServer is a real life BoxLang runtime. That means you can configure and run your code just like you would any other web server. The great part is it only took 5 seconds to get setup! This is great for quickly spinning up servers to test out an idea or even locally serve files for whatever reason or run small microservices.

Another advantage of the MiniServer is that it makes debugging your web app very easy. You can spin up a webserver and start debugging your templates almost instantly.  Just go add breakpoints wherever you want, hit your code in the browser and voila! You are now debuging your live MiniServer BoxLang application!

<figure><img src="../../../.gitbook/assets/image (30).png" alt=""><figcaption></figcaption></figure>

## Wrapping Up

In conclusion, the MiniServer is a pretty cool feature provided by the official BoxLang VS Code extension. As a member of the BoxLang community your feedback is always valuable to us. Download the extension, spin up a MiniServer, throw some breakpoints in, and let us know what you think!
