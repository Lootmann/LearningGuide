USE MyDB;
DROP TABLE IF EXISTS purchase_history;

CREATE TABLE purchase_history (
    date DATE NOT NULL,
    code CHAR(6) NOT NULL,
    num INT NOT NULL
);
 
INSERT INTO purchase_history (date, code, num) VALUES ('2013/1/13','100001',100);
INSERT INTO purchase_history (date, code, num) VALUES ('2013/1/17','100002',20);
INSERT INTO purchase_history (date, code, num) VALUES ('2013/2/1','100103',31);
INSERT INTO purchase_history (date, code, num) VALUES ('2013/2/3','100101',5);
INSERT INTO purchase_history (date, code, num) VALUES ('2013/3/5','100203',31);
INSERT INTO purchase_history (date, code, num) VALUES ('2013/3/12','100003',13);
INSERT INTO purchase_history (date, code, num) VALUES ('2013/4/30','100201',24);
INSERT INTO purchase_history (date, code, num) VALUES ('2013/5/9','100001',50);
INSERT INTO purchase_history (date, code, num) VALUES ('2013/7/19','100C02',10);
INSERT INTO purchase_history (date, code, num) VALUES ('2013/8/25','100102',5);
