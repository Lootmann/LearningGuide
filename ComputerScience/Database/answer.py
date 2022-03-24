def title(msg: str, c: int = 8):
    print("~~~" * c + f" {msg} " + "~~~" * c)


"""
Show ENAME, JOB, and SAL from EMP table
"""
from SQLStrategy.main import DB

title("SELECT")
DB.select_table("SELECT ENAME, JOB, SAL FROM EMP")
DB.select_table("SELECT * FROM EMP")
DB.select_table("SELECT ENAME, SAL * 1.02 FROM EMP")

title("ORDER BY")
DB.select_table("""SELECT ENAME, JOB, SAL FROM EMP ORDER BY SAL DESC""")

title("Aggregate")
DB.select_table(
    """SELECT SUM(sal), MAX(sal), MIN(sal), AVG(sal), count(SAL) FROM EMP"""
)

title("BETWEEN")
DB.select_table("""SELECT ENAME FROM EMP WHERE SAL BETWEEN 1000 AND 2000""")
DB.select_table("select ename, sal from emp where sal between 1000 and 2000")

title("LIKE")
DB.select_table("select ename from emp where ename like '%A%'")
DB.select_table("select ename from emp where ename like '%?_%' ESCAPE '?'")

"""Group By
指定したカラム毎にグループ化し、集合関数の計算結果を取得することができる
グループ化の方法はグループ化するカラム 'group by' と記述する
"""
title("GROUP BY")
DB.select_table("SELECT JOB, AVG(SAL) FROM EMP GROUP BY JOB")
DB.select_table("SELECT JOB, AVG(SAL) FROM EMP WHERE DEPTNO <> 10 GROUP BY JOB")
DB.select_table("SELECT DEPTNO, AVG(SAL) FROM EMP GROUP BY DEPTNO")

"""Having
HavingはGroup Byに対してチュ出場権を設定することが出来る
Where条件が Group By でグループ化される前のレコード抽出段階の条件に対して
Havingはグループ化した”後”の条件になる
"""
title("HAVING")
DB.select_table("SELECT job FROM EMP GROUP BY JOB HAVING AVG(SAL) >= 2500")
DB.select_table("SELECT DEPTNO, COUNT(*) FROM EMP GROUP BY DEPTNO HAVING COUNT(*) >= 4")

"""DISTINCT
抽出したレコードから重複した行を排除する
SELECT の直後に配置する
SELECTで抽出されたレコードの重複行を削除する
"""
title("DISTINCT")
DB.select_table("SELECT DISTINCT JOB FROM EMP")
DB.select_table("SELECT DISTINCT DEPTNO FROM EMP")
DB.select_table("SELECT DISTINCT JOB, SAL FROM EMP")

"""INSERT
INSERT INTO EMP_TEMP
SELECT *
FROM   EMP
WHERE  JOB = 'SALESMAN'
"""

"""UPDATE
UPDATE EMP
SET    SAL = SAL * 1.5
WHERE  EMPNO = 7369
"""

"""DELETE
# Delete all records
DELETE FROM EMP

# Delete WHERE
DELETE FROM EMP
WHERE  EMPNO = 7369
"""

"""条件結合
複数の表からのQueryを行う
"""

title("条件結合")
sql = """
SELECT EMP.EMPNO, EMP.ENAME, DEPT.DEPTNO, DEPT.DNAME
FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO
"""
DB.select_table(sql)

sql = """
SELECT EMP.EMPNO, EMP.ENAME, DEPT.DEPTNO, DEPT.DNAME
FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO AND EMP.SAL >= 1500
"""
DB.select_table(sql)

sql = """
SELECT EMP.ENAME, DEPT.DNAME
FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO
"""
DB.select_table(sql)

"""ALIAS 別名
条件結合とやっていることは全く同じ
表のカラムに別名をつけて、記述を簡素化しみやすくするためのもの
"""

title("ALIAS")
sql = """
SELECT E.ENAME, E.DEPTNO, D.DNAME, D.DEPTNO
FROM EMP E, DEPT D
WHERE E.DEPTNO = D.DEPTNO
"""
DB.select_table(sql)

"""Subquery 副問合せ
SELECT文の結果を利用して 問い合わせを行う
WHERE 句が複数のレコードを返すと当然エラーになる
"""
title("subquery")
sql = """
SELECT *
FROM EMP
WHERE EMP.DEPTNO = (
        SELECT MIN(DEPT.DEPTNO)
        FROM DEPT
    )
"""
DB.select_table(sql)

"""IN
DEPTNO IN (10, 30)
DEPTNO = 10 OR DEPTNO = 30

DEPTNO NOT IN (10, 30)
DEPTNO != 10 OR DEPTNO != 30
"""

title("IN")
sql = """
SELECT *
FROM EMP
WHERE DEPTNO IN (10, 30)
"""
DB.select_table(sql)

title("IN subquery")
sql = """
SELECT *
FROM EMP
WHERE DEPTNO IN (
    SELECT DEPTNO
    FROM DEPT
    WHERE DNAME LIKE '%S%'
)
"""
DB.select_table(sql)

"""
EXISTS 句の中に書いてあるSQLで抽出されるレコードがある場合は真
真のときのみ外側のWHERE条件が成立して、レコードが抽出される
"""
title("EXISTS")

sql = """
SELECT ENAME, SAL
FROM EMP EA
WHERE NOT EXISTS(
        SELECT * FROM EMP EB
        WHERE EB.SAL > EA.SAL
      )
"""
DB.select_table(sql)
