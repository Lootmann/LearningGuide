# MySQL In A Week

## login

```bash
$ docker -it exec  mysql_container bash
$ mysql -u root -p -h 127.0.0.1

$ docker exec -it mysql_container mysql -u root -p -h 127.0.0.1
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

## commands

### INNER JOIN

```sql
SELECT * FROM resource INNER JOIN class_name ON resource.class = class_name.class;

SELECT code,resource.name,price,class_name.name FROM resource INNER JOIN class_name ON resource.class=class_name.class;
```

### USING

```sql
SELECT * FROM resource INNER JOIN class_name USING(class);

SELECT code,resource.name,price,class_name.name FROM resource INNER JOIN class_name USING(class);
SELECT code,resource.name,price,class_name.name FROM resource INNER JOIN class_name USING(class) WHERE price >= 3000;
```

### CROSS JOIN

`クロス結合` 2 つのテーブルの組合せの全ての組合せを作る結合  
`100 * 100 = 10000` lines になるのでパフォーマンスが著しく低下する必要がある

[CROSS JOIN](https://www.dbonline.jp/sqlite/join/index3.html)

### LEFT OUTER JOIN

```sql
SELECT * FROM purchase_history
  LEFT OUTER JOIN resource
  ON purchase_history.code=resource.code;
```

```sql
SELECT * FROM purchase_history
  RIGHT OUTER JOIN resource
  ON purchase_history.code = resource.code
  ORDER BY purchase_history.date ASC;
```
