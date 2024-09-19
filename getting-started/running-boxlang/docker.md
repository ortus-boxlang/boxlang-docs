---
description: Containerize all things with BoxLang
icon: docker
---

# Docker

<figure><img src="../../.gitbook/assets/docker.png" alt=""><figcaption></figcaption></figure>

### Docker Images

Two distinct image tags have been published for BoxLang, each serving a specific purpose.

* `ortussolutions/boxlang:cli`— This is just the BoxLang CLI in a container. You can pass expressions, run the runtime itself, use it for tooling, cron jobs, and more.
* `ortussolutions/boxlang:miniserver` - This is the BoxLang [MiniServer](miniserver.md) runtime packaged into a docker container.

```bash
docker pull ortussolutions/boxlang:cli
docker pull ortussolutions/boxlang:miniserver
```

### Docker Tags <a href="#docker-compose-for-images-8" id="docker-compose-for-images-8"></a>

Both images are tagged with the following tags:

* `latest` - The latest stable release of BoxLang
* `snapshot` - The latest snapshot release of BoxLang
* `alpine-snapshot` - The latest snapshot release of BoxLang on Alpine Linux

{% hint style="danger" %}
We encourage you to use the `snapshot` version of our images until we go stable.
{% endhint %}

### **Running Images**

#### **Running a command in a running container**

```bash
docker exec -it CONTAINERID /usr/bin/bx.sh 2+2
```

#### **Starting a docker container, run a command, and exit**

<pre class="language-bash"><code class="lang-bash"><strong>docker run ortussolutions/boxlang:cli time /usr/bin/bx.sh 2+2
</strong></code></pre>

#### Starting a MiniServer <a href="#docker-compose-for-images-8" id="docker-compose-for-images-8"></a>

<pre class="language-bash"><code class="lang-bash"><strong>docker run -it \
</strong><strong>   -p 8080:8080 \
</strong><strong>   ortussolutions/boxlang:miniserver
</strong>
# ARM / Apple Silicone
docker run --platform linux/amd64 \
   -it \
   -p 8080:8080 \
   ortussolutions/boxlang:miniserver
</code></pre>

### Docker Compose for Images <a href="#docker-compose-for-images-8" id="docker-compose-for-images-8"></a>

Two example compose files are included below.

#### Docker Compose for BoxLang CLI <a href="#docker-compose-for-bx-cli-9" id="docker-compose-for-bx-cli-9"></a>

```yaml
version: "2.1"

services:
  cli:
    image: ortussolutions/boxlang:cli
```

#### MiniServer <a href="#docker-compose-for-bx-web-server-12" id="docker-compose-for-bx-web-server-12"></a>

```bash
version: "2.1"

services:
  bxweb:
    image: docker pull ortussolutions/boxlang:miniserver
    environment:
      - BOXLANG_DEBUG=true
      - BOXLANG_MODULES=bx-compat-cfml,bx-esapi,bx-mysql
    volumes:
      - .:/app
    ports:
      - 8880:8080
```

For more information on the options available when running the MiniServer container, see the image entry [on Docker Hub](https://hub.docker.com/r/ortussolutions/boxlang).

### Modules

The image has a module installer built in: `/usr/local/bin/install-bx-module` which can be used via the `BOXLANG_MODULES` env variable.  If it detects it, then it will try to download an install those modules into the runtime's home.  We recommend you do this by warming up the server first.

### Runtime Source Code

The runtime source code can be found here: [https://github.com/ortus-boxlang/boxlang-docker](https://github.com/ortus-boxlang/boxlang-docker)

We welcome any pull requests, testing, docs, etc.
