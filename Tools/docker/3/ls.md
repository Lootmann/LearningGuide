# How to use Docker

0. Find Docker Image from Docker Hub
1. docker run (download and run)
2. docker stop
3. docker rm
4. docker image rm

## docker run

```bash
$ ls
index.html
```

```bash
$ docker run -dit \
  --name my-apache-app \
  -p 8080:80 \
  -v "$PWD":/usr/local/apache2/htdocs/ httpd:2.4
```

```
$ docker container ls

| CONTAINER ID | IMAGE     | COMMAND            | CREATED        | STATUS        | PORTS                                 | NAMES         |
| ------------ | --------- | ------------------ | -------------- | ------------- | ------------------------------------- | ------------- |
| 60b77a7faac2 | httpd:2.4 | "httpd-foreground" | 12 seconds ago | Up 10 seconds | 0.0.0.0:8080->80/tcp, :::8080->80/tcp | my-apache-app |
```

```
❯ http :8080

HTTP/1.1 200 OK
Accept-Ranges: bytes
Connection: Keep-Alive
Content-Length: 242
Content-Type: text/html
Date: Mon, 21 Mar 2022 08:23:25 GMT
ETag: "f2-5dab6296cca78"
Keep-Alive: timeout=5, max=100
Last-Modified: Mon, 21 Mar 2022 08:19:57 GMT
Server: Apache/2.4.53 (Unix)

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>NewDocument</title>
  </head>
  <body>
    <h1>hello world :^)</h1>
  </body>
</html>
```

## docker logs

container が出力するログを取得

```
$ docker logs my-apache-app

172.17.0.1 - - [21/Mar/2022:08:14:59 +0000] "GET / HTTP/1.1" 200 249
172.17.0.1 - - [21/Mar/2022:08:14:59 +0000] "GET /favicon.ico HTTP/1.1" 404 196
172.17.0.1 - - [21/Mar/2022:08:15:01 +0000] "GET /docker-run.sh HTTP/1.1" 200 103
172.17.0.1 - - [21/Mar/2022:08:20:04 +0000] "GET / HTTP/1.1" 200 242
172.17.0.1 - - [21/Mar/2022:08:20:05 +0000] "GET /favicon.ico HTTP/1.1" 404 196
172.17.0.1 - - [21/Mar/2022:08:23:25 +0000] "GET / HTTP/1.1" 200 242
```

## docker stop

コンテナの停止

```
$ docker stop my-apache-app
```

## docker rm

コンテナの破棄 完全に破棄する 復元する方法は無い

## docker image

```
docker image ls
$ docker image rm http:2.4
```
