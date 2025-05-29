---
description: Containerize all things with BoxLang
icon: docker
---

# Docker

<figure><img src="../../.gitbook/assets/docker.png" alt=""><figcaption></figcaption></figure>



You can find all our published images and tags here: https://hub.docker.com/r/ortussolutions/boxlang. Please see the Environment Variables section for more information on how to configure the images for runtime and deployment.

* CLI Images : [ortussolutions/boxlang:cli](https://hub.docker.com/r/ortussolutions/boxlang/tags?page=1\&name=cli)
* MiniServer Images : [ortussolutions/boxlang:miniserver](https://hub.docker.com/r/ortussolutions/boxlang/tags?page=1\&name=miniserver)

We also have an experimental image for the BoxLang MiniServer with Nginx included.

* MiniServer with Nginx : [ortussolutions/boxlang:miniserver-nginx](https://hub.docker.com/r/ortussolutions/boxlang/tags?page=1\&name=miniserver-nginx)

## CLI Images

This image contains the BoxLang CLI, which allows you to run BoxLang scripts, CLI applications, commands, schedulers and any OS integrations.

* `ortussolutions/boxlang:cli` - The latest BoxLang CLI image based on Debian Linux
* `ortussolutions/boxlang:cli-alpine` - The latest snapshot of the BoxLang CLI image based on Alpine Linux
* `ortussolutions/boxlang:cli-snapshot` - The latest snapshot of the BoxLang CLI image
* `ortussolutions/boxlang:cli-alpine-snapshot` - The latest snapshot of the BoxLang CLI image on Alpine Linux

```bash
# Pull the latest BoxLang CLI image
docker pull ortussolutions/boxlang:cli
# Run the BoxLang CLI version
docker run --rm -it ortussolutions/boxlang:cli boxlang --version
# Run the BoxLang REPL
docker run --rm -it ortussolutions/boxlang:cli boxlang
# Run a quick code snippet
docker run --rm -it ortussolutions/boxlang:cli boxlang --bx-code "print('Hello, BoxLang!')"
# Run a Task.bx script
docker run --rm -it -v $(pwd):/app ortussolutions/boxlang:cli boxlang /app/Task.bx
# Run a Scheduler.bx script
docker run --rm -it -v $(pwd):/app ortussolutions/boxlang:cli boxlang /app/Scheduler.bx
```

## MiniServer Images

This image contains the BoxLang MiniServer, which is a lightweight web server that can run BoxLang applications, APIs and services. It is designed to be fast, lightweight, and easy to use.

* `ortussolutions/boxlang:miniserver` - The latest BoxLang MiniServer image based on Debian Linux
* `ortussolutions/boxlang:miniserver-alpine` - The latest snapshot of the BoxLang MiniServer image based on Alpine Linux
* `ortussolutions/boxlang:miniserver-snapshot` - The latest snapshot of the BoxLang MiniServer image
* `ortussolutions/boxlang:miniserver-alpine-snapshot` - The latest snapshot of the BoxLang MiniServer image on Alpine Linux

The MiniServer will load the `/app` as the root directory of the server, so you can mount your BoxLang applications and services there. The MiniServer will also automatically load the `index.bxm` file as the default file to serve. Rewrites are enabled by default, and you can configure them using the `REWRITES_FILE` environment variable.

```bash
# Pull the latest BoxLang MiniServer image
docker pull ortussolutions/boxlang:miniserver
# Run the BoxLang MiniServer with Rewrites Enabled
docker run --rm -it -p 8080:8080 ortussolutions/boxlang:miniserver
# Run the BoxLang MiniServer in debug mode
docker run --rm -it -p 8080:8080 -e BOXLANG_DEBUG=true ortussolutions/boxlang:miniserver
# Load a custom boxlang.json configuration file
docker run --rm -it -p 8080:8080 -v $(pwd)/boxlang.json:/root/.boxlang/config/boxlang.json ortussolutions/boxlang:miniserver
```

### Health Check

The Docker images include a health check that will ping the MiniServer's root endpoint to ensure it is running. The health check can be configured using the `HEALTHCHECK_URI` environment variable, which defaults to `http://127.0.1:${PORT}/`. The health check will run on an interval of 20 seconds, timeout of 30 seconds and 15 retries before marking the container as unhealthy.

## Modules

The image has a module installer built in: `/usr/local/bin/install-bx-module` which can be used via the `BOXLANG_MODULES` env variable. If it detects it, then it will try to download an install those modules into the runtime's home. We recommend you do this by warming up the server first.

Example:

```dockerfile
version: "2.1"

services:
  bxweb:
    image: ortussolutions/boxlang:miniserver
    environment:
      - BOXLANG_DEBUG=true
      - BOXLANG_MODULES=bx-compat-cfml,bx-esapi,bx-mysql
    volumes:
      - .:/app
    ports:
      - 8880:8080
```

## Environment Variables

The following environment variables can be used to configure the BoxLang Docker images:

* `BOXLANG_CONFIG_PATH` - The path to the BoxLang configuration file. Default: `/root/.boxlang/config/boxlang.json`
* `BOXLANG_DEBUG` - Enable debugging. Default: `false`
* `BOXLANG_HOME` - The home directory of the BoxLang installation. Default: `/root/.boxlang`
* `BOXLANG_HOST` - The host the MiniServer will listen on. Default: `0.0.0.0`
* `BOXLANG_MODULES` - A comma-separated list of modules to install. Default: \`\`. Example: `bx-compat-cfml,bx-esapi,bx-mysql`
* `BOXLANG_PORT` - The port the MiniServer will listen on. Default: `8080`
* `DEBUG` - Enable debug mode. Default: `false`
* `JAVA_OPTS` - Java options for the MiniServer. Default is `-Djava.awt.headless=true`
* `HEALTHCHECK_URI` - The URI for the health check endpoint. Default: `http://127.0.0.1:${PORT}/`
* `HOST` - The host the MiniServer will listen on. Default: `0.0.0.0`
* `MAX_MEMORY:512m` - The maximum memory allocated to the BoxLang process. Default: `-Xmx512m`
* `MIN_MEMORY:512m` - The minimum memory allocated to the BoxLang process. Default: `-Xms512m`
* `PORT` - The port the MiniServer will listen on. Default: `8080`
* `REWRITES` - Enable URL rewrites. Default: `true`
* `REWRITES_FILE` - The file containing the URL rewrites. Default: `index.bxm`

### BoxLang Environment Variables

Please note that BoxLang has the capacity to override any configuration setting via environment variables using the `BOXLANG_` prefix. Click here for more information: https://boxlang.ortusbooks.com/getting-started/configuration#environment-variable-substitution

Example:

```bash
BOXLANG_DEBUGMODE=true
```

## Experimental: MiniServer with Nginx

This image combines the BoxLang MiniServer with Nginx to provide a lightweight web server that can serve static files and proxy requests to the MiniServer. This is an experimental image and is not recommended for production use just yet. Here are the available environment variables:

* `NGINX_PORT` - The port Nginx will listen on. Default: `80`
* `NGINX_SSL_PORT` - The SSL port Nginx will listen on. Default: `443`

Nginx has been configured to do rewrites for BoxLang applications, fine-tuned for production use and a self-signed SSL certificate is included. You can mount your own SSL certificate and key to the `/etc/nginx/ssl` directory.

```
openssl req -x509 -nodes -newkey rsa:2048 \
    -days 365 \
    -subj "/CN=localhost" \
    -keyout /etc/nginx/ssl/selfsigned.key \
    -out /etc/nginx/ssl/selfsigned.crt
```
