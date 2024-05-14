# Docker

### Docker Images in the AWS ECR

We are using AWS ECR to store the docker images privately while in Pre-Release. Below are the credentials to pull the images, and some code to be able to use `docker run` or `docker compose`

#### AWS CLI <a href="#aws-cli-2" id="aws-cli-2"></a>

You will need to install the AWS CLI to run the following commands. You can find information on getting started with AWS CLI here:

![](https://communitycdn.ortussolutions.com/original/2X/c/c472957d4dae96f47e4f8202d361e26924f8e248.png)[docs.aws.amazon.com](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

#### [Install or update to the latest version of the AWS CLI - AWS Command Line...](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

Instructions to install or update the AWS CLI on your system.

#### Log into AWS ECR to access files <a href="#log-into-aws-ecr-to-access-files-3" id="log-into-aws-ecr-to-access-files-3"></a>

Run the following to get logged into the AWS ECR (Elastic Container Registry)

```sql
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 233317242204.dkr.ecr.us-east-1.amazonaws.com
```

This will attempt to log you in with your AWS Credentials

You can set those credentials with the following commands

**On Mac / Linux**

```bash
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
```

**On Windows**

```bash
set AWS_ACCESS_KEY_ID=
set AWS_SECRET_ACCESS_KEY=

```

#### Pull Images from AWS ECR <a href="#pull-images-from-aws-ecr-6" id="pull-images-from-aws-ecr-6"></a>

We have 2 images

* bx - Just the BX CLI in a container - you can pass expressions, or just run the cli itself
* bx-web - This is a webserver - Remember it is not commandbox (yet) so it’s barebones

```bash
docker pull 233317242204.dkr.ecr.us-east-1.amazonaws.com/tryboxlang:bx
docker pull 233317242204.dkr.ecr.us-east-1.amazonaws.com/tryboxlang:bx-web
```

**Multiple AWS Profiles**

What if you have lots of different AWS Cli Credentials?

You can manage multiple AWS cli profiles in your AWS conf file.

[https://www.simplified.guide/aws/cli/configure-multiple-profiles](https://www.simplified.guide/aws/cli/configure-multiple-profiles)

### Docker Compose for Images <a href="#docker-compose-for-images-8" id="docker-compose-for-images-8"></a>

We have a couple of simple Docker Compose files

#### Docker Compose for bx cli <a href="#docker-compose-for-bx-cli-9" id="docker-compose-for-bx-cli-9"></a>

```yaml
version: "2.1"

services:
  cli:
    image: 233317242204.dkr.ecr.us-east-1.amazonaws.com/tryboxlang:bx
```

**Running a command in a running container**

```bash
docker exec -it CONTAINERID /usr/bin/bx.sh 2+2
```

**Starting a docker container, run a command, and exit**

```bash
docker run 233317242204.dkr.ecr.us-east-1.amazonaws.com/tryboxlang:bx time /usr/bin/bx.sh 2+2
```

#### Docker Compose for bx web server <a href="#docker-compose-for-bx-web-server-12" id="docker-compose-for-bx-web-server-12"></a>

```bash
version: "2.1"

services:
  bxweb:
    image: 233317242204.dkr.ecr.us-east-1.amazonaws.com/tryboxlang:bx-web
    volumes:
      - ./:/app
      - ./build:/root/build
    ports:
      - "8080:8080"
```

We are trying to update these all the time as we update the jar files, we’re working on the automation.

We will be adding versioning soon, for now, they are all pretending they are the one and only images, with version placeholder of 1.0.0 internally.
