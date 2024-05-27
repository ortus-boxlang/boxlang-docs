---
description: Containerize all things with BoxLang
---

# Docker

<figure><img src="../../.gitbook/assets/docker.png" alt=""><figcaption></figcaption></figure>

### Docker Images

Two image tags are currently published for BoxLang.

* `ortussolutions/boxlang:cli` - Just the BoxLang CLI in a container - you can pass expressions, or just run the cli itself
* `ortussolutions/boxlang:miniserver` - This is a webserver - Remember it is not commandbox (yet) so it’s barebones

```bash
docker pull ortussolutions/boxlang:cli
docker pull ortussolutions/boxlang:miniserver
```

### Docker Tags <a href="#docker-compose-for-images-8" id="docker-compose-for-images-8"></a>

Both images are tagged with the following tags:

* `latest` - The latest stable release of BoxLang
* `snapshot` - The latest snapshot release of BoxLang
* `alpine-snapshot` - The latest snapshot release of BoxLang on Alpine Linux

### ARM Processors <a href="#docker-compose-for-images-8" id="docker-compose-for-images-8"></a>

We will be building our arm processor support soon.  In the meantime please use this in your commands if you are using ARM based or Apple Silicone processors:

```bash
--platform linux/amd64
```

### **Running Images**

#### **Running a command in a running container**

```bash
docker exec -it CONTAINERID /usr/bin/bx.sh 2+2

# ARM / Apple Silicone
docker exec --platform linux/amd64 -it CONTAINERID /usr/bin/bx.sh 2+2
```

#### **Starting a docker container, run a command, and exit**

<pre class="language-bash"><code class="lang-bash"><strong>docker run ortussolutions/boxlang:cli time /usr/bin/bx.sh 2+2
</strong>
# ARM / Apple Silicone
docker run --platform linux/amd64 ortussolutions/boxlang:cli time /usr/bin/bx.sh 2+2
</code></pre>

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
      - BOXLANG_PORT=8080
      - BOXLANG_WEBROOT=/app
      - BOXLANG_DEBUG=false
      - BOXLANG_HOST=localhost
      # Path to boxlang.json
      #- BOXLANG_CONFIG=/path/to/boxlang.json
      # Where to store the boxlang home
      - BOXLANG_HOME=/opt/boxlang
    volumes:
      - ./test:/app
      - ./test/.engine:/opt/boxlang
      - ./build:/root/build
    ports:
      - "8888:8080"


```
