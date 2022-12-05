# tcp_receiver

![Generic badge](https://img.shields.io/badge/python-3.9.2-blue)
![Generic badge](https://img.shields.io/github/license/cameritelabs/oci-emulator)
![Generic badge](https://img.shields.io/badge/code%20style-black-000000.svg)
![Python application](https://github.com/cameritelabs/oci-emulator/workflows/Python%20application/badge.svg)
[![codecov](https://codecov.io/gh/cameritelabs/oci-emulator/branch/main/graph/badge.svg?token=5C8SX1Q6P9)](https://codecov.io/gh/cameritelabs/oci-emulator)

A TCP server to receive messages managed by a http server.

## [DockerHub](https://hub.docker.com/r/cameritelabs/oci-emulator)

tcp-receiver is available on dockerhub. To run it, just execute:

```bash
docker run -d -p 3003:3003 -p 9528:9528 cameritelabs/tcp-receiver:latest
```


## Install 🤘

The following steps covers the setup process

### Using pyenv with pyenv-virtualenv

You also should use virtualenv to build/develop the project and I recommend the use of [pyenv](https://github.com/pyenv/pyenv) with [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to manage multiple python environments.

```bash
pyenv install 3.9.7
pyenv virtualenv 3.9.7 tcp_receiver
pyenv activate tcp_receiver
```

### Installing dependencies (Python 3.9.7)

Open your bash and run the follow command to install all the project dependencies, you just need to run the command one time

```bash
pip install --upgrade pip
pip install -r requirements.txt
```
