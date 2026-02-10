---
description: >-
  Deploy a modern, cloud-native BoxLang application to DigitalOcean App Platform
  in minutes!
icon: water-arrow-up
---

# DigitalOcean App

## 🥊 BoxLang Starter for DigitalOcean

**Deploy a modern, cloud-native BoxLang application to DigitalOcean App Platform in minutes!**

{% embed url="https://github.com/ortus-boxlang/boxlang-starter-digitalocean" %}

This starter kit provides everything you need to run a **production-ready BoxLang application** on [DigitalOcean's App Platform](https://www.digitalocean.com/?refcode=4d60357dfb31\&utm_campaign=Referral_Invite\&utm_medium=Referral_Program). Built with the powerful **BoxLang MiniServer**, this template showcases BoxLang's modern language features, beautiful UI components, and seamless cloud deployment workflow.

**✨ What You Get:**

* 🚀 Pre-configured BoxLang MiniServer with optimal settings
* 🎨 Beautiful, responsive landing page with Phosphor icons
* 🐳 Multi-stage Docker build for efficient deployments
* ⚡ Auto-compile and hot-reload in development
* 🔄 Automatic redeployment on code changes (when forked)
* 📦 Ready for DigitalOcean App Platform one-click deployment



**⚠️ Note:** Following these steps may result in charges for the use of DigitalOcean services.

### 📋 Requirements

* A DigitalOcean account. If you don't have one, [sign up here](https://cloud.digitalocean.com/registrations/new?refcode=4d60357dfb31).
* (Optional) A GitHub account to fork this repository for automatic deployments.

### 🚀 Deploy the App

Click the button below to deploy this app to DigitalOcean App Platform. If you're not logged in, you'll be prompted to authenticate.

[![Deploy to DigitalOcean](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/ortus-boxlang/boxlang-starter-digitalocean/tree/main\&refcode=4d60357dfb31)

#### 🍴 Fork for Automatic Redeployments (Recommended)

The one-click deploy button above deploys directly from our template repository, which means you won't get automatic redeployments when you make changes. **We recommend forking this repository** to your own GitHub account first.

**To fork this repository:**

1. Navigate to the [repository on GitHub](https://github.com/ortus-boxlang/boxlang-starter-digitalocean)
2. Click the **Fork** button in the top-right corner
3. Follow the on-screen instructions ([Learn more about forking](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo))

**To deploy your forked repository:**

1. Visit the [DigitalOcean Apps control panel](https://cloud.digitalocean.com/apps?refcode=4d60357dfb31)
2. Click **Create App**
3. Under **Service Provider**, select **GitHub**
4. Under **Repository**, select your forked repo (e.g., `<your-username>/boxlang-starter-digitalocean`)
5. Ensure **Branch** is set to `main` and **Autodeploy** is checked ✅
6. Click **Next**

#### ⚙️ Configuration Steps

After clicking the deploy button or connecting your forked repository:

1. **Configure your app** (Optional)
   * Add environment variables
   * Configure HTTP routes
   * Add databases or other services
   * For this starter, default settings work perfectly!
2. **Name and Region**
   * Provide a name for your app
   * Select your preferred deployment region
   * App Platform automatically selects the closest region
   * All apps are routed through a global CDN for optimal performance 🌍
3. **Review Settings**
   * Leave default fields as-is
   * Click **Next**
4. **Launch Your App** 🎉
   * Review your plan (Basic/Pro)
   * Confirm the number of containers
   * Click **Launch Basic/Pro App**

#### 📊 Monitor Your Deployment

After launching, you'll see a **"Building..."** progress indicator. Click **View Logs** to watch the build process in real-time.

The build typically takes **2-3 minutes**. Once complete:

* Click the **Live App** link in the header
* Your BoxLang application will open in a new tab! 🎊

### ✏️ Make Changes to Your App

If you forked the repository, you can now customize your BoxLang application:

1. Make changes to files in your forked repo (e.g., edit `/app/index.bxm`)
2. Commit and push to the `main` branch
3. App Platform automatically redeploys with **zero downtime** ⚡

No manual steps required—just push and watch it deploy!

### 📚 Learn More

Want to dive deeper into App Platform features?

* [DigitalOcean App Platform Documentation](https://www.digitalocean.com/docs/app-platform/?refcode=4d60357dfb31)
* [BoxLang Documentation](https://boxlang.ortusbooks.com)
* [BoxLang MiniServer Guide](https://boxlang.ortusbooks.com/getting-started/running-boxlang/miniserver)

### 🗑️ Delete the App

When you're done testing or no longer need this application:

1. Visit the [Apps control panel](https://cloud.digitalocean.com/apps)
2. Select your app
3. Go to the **Settings** tab
4. Click **Destroy**
5. Confirm the deletion

**⚠️ Important:** If you don't delete your app, charges for DigitalOcean services will continue to accrue.

### 🥊 BoxLang MiniServer App

This starter uses the **BoxLang MiniServer**—a lightweight, embedded web server perfect for containerized deployments and rapid development.

#### What's Included

**📦 Application Structure:**

```
boxlang-starter-digitalocean/
├── app/                      # Your BoxLang application
│   ├── Application.bx        # Application configuration
│   ├── index.bxm             # Main landing page
│   └── includes/             # Assets (images, CSS, JS)
├── boxlang.json              # BoxLang runtime configuration
├── miniserver.json           # MiniServer settings
├── Dockerfile                # Multi-stage Docker build
└── README.md                 # You are here!
```

**⚙️ MiniServer Configuration:**

* **Port:** 8080 (production), 9090 (local development)
* **Host:** 0.0.0.0 (container), 127.0.0.1 (local)
* **Web Root:** `./app` directory
* **Auto-compile:** Enabled for BoxLang files
* **Health Check:** Built-in health endpoint
* **URL Rewrites:** Enabled with fallback to `index.bxm`

#### 🏃 Running Locally

Want to test your BoxLang app on your local machine? Here's how:

**Prerequisites**

* [Docker](https://www.docker.com/get-started) installed on your machine
* OR [BoxLang](https://boxlang.ortusbooks.com/getting-started/installation) installed

**Option 1: Run with Docker (Recommended)**

```bash
# Clone or navigate to your project directory
cd boxlang-starter-digitalocean

# Build the Docker image
docker build -t boxlang-digitalocean .

# Run the container
docker run -p 9090:8080 boxlang-digitalocean

# Visit http://localhost:9090 in your browser 🎉
```

**Hot Reload Development Mode:**

```bash
# Mount your app directory for live changes
docker run -p 9090:8080 \
  -v $(pwd)/app:/app/app \
  boxlang-digitalocean

# Edit files in ./app and refresh your browser!
```

**Option 2: Run with BoxLang CLI**

```bash
# Install BoxLang CLI if you haven't already
# Visit: https://boxlang.ortusbooks.com/getting-started/installation

# Navigate to your project directory
cd boxlang-starter-digitalocean

# Start the MiniServer
boxlang miniserver

# Visit http://localhost:9090 in your browser 🎉
```

The MiniServer will automatically read `miniserver.json` and start with all configured settings.

#### 🔧 Customization Tips

**Update the Port:**

Edit `miniserver.json` to change the default port:

```json
{
  "port": 3000  // Change to your preferred port
}
```

**Environment Variables:**

Set environment-specific configurations in `boxlang.json`:

```json
{
  "runtime": {
    "debug": true,
    "timezone": "UTC"
  }
}
```

**Add BoxLang Modules:**

Install community modules using the BoxLang CLI:

```bash
boxlang module install <module-name>
```

#### 📖 Additional Resources

* [BoxLang Language Documentation](https://boxlang.ortusbooks.com/boxlang-language)
* [BoxLang Framework & Modules](https://boxlang.ortusbooks.com/boxlang-framework)
* [MiniServer Configuration](https://boxlang.ortusbooks.com/getting-started/running-boxlang/miniserver)
* [BoxLang on GitHub](https://github.com/ortus-boxlang/boxlang)

***

#### 💬 Need Help?

* **Community:** Join the [BoxLang Community](https://community.ortussolutions.com)
* **Documentation:** [BoxLang Docs](https://boxlang.ortusbooks.com)
* **Professional Support:** [BoxLang +/++](https://www.boxlang.io/plans)

**Happy Coding with BoxLang! 🥊**
