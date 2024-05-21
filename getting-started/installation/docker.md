---
description: Run BoxLang on containers
---

# Docker

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption><p>Containerize all Box things!</p></figcaption></figure>

### Docker Images

#### Pull Images from Docker Hub <a href="#pull-images-from-aws-ecr-6" id="pull-images-from-aws-ecr-6"></a>

Two image tags are currently published:

* `ortussolutions/boxlang:cli` - Just the BoxLang CLI in a container - you can pass expressions, or just run the cli itself
* `ortussolutions/boxlang:miniserver` - This is a webserver - Remember it is not commandbox (yet) so it’s barebones

```bash
docker pull ortussolutions/boxlang:cli
docker pull ortussolutions/boxlang:miniserver
```

### Docker Compose for Images <a href="#docker-compose-for-images-8" id="docker-compose-for-images-8"></a>

Two example compose files are included below

#### Docker Compose for BoxLang CLI <a href="#docker-compose-for-bx-cli-9" id="docker-compose-for-bx-cli-9"></a>

```yaml
version: "2.1"

services:
  cli:
    image: ortussolutions/boxlang:cli
```

**Running a command in a running container**

```bash
docker exec -it CONTAINERID /usr/bin/bx.sh 2+2
```

**Starting a docker container, run a command, and exit**

```bash
docker run ortussolutions/boxlang:cli time /usr/bin/bx.sh 2+2
```

#### Docker Compose for bx web server <a href="#docker-compose-for-bx-web-server-12" id="docker-compose-for-bx-web-server-12"></a>

```bash
version: "2.1"

services:
  bxweb:
    image: ortussolutions/boxlang:miniserver
    volumes:
      - ./:/app
      - ./build:/root/build
    ports:
      - "8080:8080"
```
