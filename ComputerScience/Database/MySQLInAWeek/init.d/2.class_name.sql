USE MyDB;
DROP TABLE IF EXISTS class_name;

CREATE TABLE class_name (
    class   char(4)     NOT NULL,
    name    varchar(24) NOT NULL
);

INSERT INTO class_name (class, name) VALUES ('text','教科書');
INSERT INTO class_name (class, name) VALUES ('mdvd','マルチメディアDVD');
INSERT INTO class_name (class, name) VALUES ('sftw','ソフトウェア');
INSERT INTO class_name (class, name) VALUES ('sbtx','副読本');
INSERT INTO class_name (class, name) VALUES ('pbbk','問題集');
INSERT INTO class_name (class, name) VALUES ('dict','辞書');
INSERT INTO class_name (class, name) VALUES ('comp','コンピューター');
