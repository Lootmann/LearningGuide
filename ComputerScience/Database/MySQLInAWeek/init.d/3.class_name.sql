USE MyDB;

DROP TABLE IF EXISTS class_name;

CREATE TABLE class_name(
    class       char(4) NOT NULL,
    name        varchar(10) NOT NULL
);

INSERT INTO class_name VALUES('text','教科書');
INSERT INTO class_name VALUES('mdvd','マルチメディアDVD');
INSERT INTO class_name VALUES('sftw','ソフトウェア');
INSERT INTO class_name VALUES('sbtx','副読本');
INSERT INTO class_name VALUES('pbbk','問題集');
INSERT INTO class_name VALUES('dict','辞書');
INSERT INTO class_name VALUES('comp','コンピューター');
