docker run \
  --rm -v "$PWD":/usr/src/myapp \
  -w /usr/src/myapp \
  golang:1.13 go build -v
