# ok

## build instructions

Build Image

```bash
docker image build -t ok . 
```

Push to dockerhub

```bash
docker image tag ok dcbove/ok:alpha
docker login --username=dcbove
docker image push dcbove/ok:alpha
```

## local test

```bash
docker container run -p 5051:5051 -e FOO=test -e PORT=5051 ok
docker container stop <name>
```

