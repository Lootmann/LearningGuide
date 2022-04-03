DROP SCHEMA IF EXISTS MyDB;
CREATE DATABASE MyDB;
USE MyDB;

DROP TABLE IF EXISTS resource;


CREATE TABLE resource
(
    code        char(6) primary key,
    name        varchar(40) NOT NULL,
    class       char(4) NOT NULL,
    price       int NOT NULL
);
  

INSERT INTO resource VALUES('100001','英語テキスト','text',2500);
INSERT INTO resource VALUES('100002','数学テキスト','text',2700);
INSERT INTO resource VALUES('100003','国語テキスト','text',3000);
INSERT INTO resource VALUES('100101','英語DVD','mdvd',3000);
INSERT INTO resource VALUES('100102','数学学習ソフト','sftw',4900);
INSERT INTO resource VALUES('100103','英語学習ソフト','sftw',5400);
INSERT INTO resource VALUES('100201','国語副読本','sbtx',1200);
INSERT INTO resource VALUES('100202','英語問題集','pbbk',2500);
INSERT INTO resource VALUES('100203','数学問題集','pbbk',2800);
INSERT INTO resource VALUES('100C01','英語辞書','dict',8200);
