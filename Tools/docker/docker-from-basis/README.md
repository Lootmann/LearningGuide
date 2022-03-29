# Docker

- Docker
- Docker Engine
- Docker Container
- Docker Image

## Basic

```
docker run -dit --name my-apache-app \
  -p 8080:80 \
  -v "$PWD":/usr/local/apache2/htdocs/ httpd:2.4
```

-d : detach
-i : interactive
-t : 疑似端末(pseudo-tty)を割り当てる

## separate

は以下の３つのコマンドに分解できる

```bash
# download Docker Image from Docker Hub
docker pull httpd:2.4
```

```bash
# create Docker Container from Image
# -p host-port:container-port
docker create --name my-apache-app \
  -p 8080:80 \
  -v "$PWD":/usr/local/apache2/htdocs/ httpd:2.4
```

### --name

--name : 作ったコンテナにコンテナ名を付ける

### -p

```
-p <host-port>:<container-port>
```

host-port : アプリ側でつなげるポート
container-port : コンテナ内で動くアプリのポート

### -v

コンテナ内の特定のディレクトリに
ホストのディレクトリをマウントする設定

```
-v <host>:<container>

host: ホストのディレクトリ
container: コンテナのディレクトリ
```

マウント：あるディレクトリに対して、別のディレクトリの内容が
見えるようになる設定

## Docker start, stop

```bash
# run Docker Container
docker start <container-name>
docker stop <container-name>
```
