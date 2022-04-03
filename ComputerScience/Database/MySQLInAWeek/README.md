# MySQL In A Week

## login

```bash
$ docker -it exec  mysql_container bash

> mysql -u root -p -h 127.0.0.1
```

## Version

```
mysql> select version(), current_date;
+-----------+--------------+
| version() | current_date |
+-----------+--------------+
| 8.0.28    | 2022-04-03   |
+-----------+--------------+
1 row in set (0.00 sec)
```

## show

```
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| db                 |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.01 sec)
```
