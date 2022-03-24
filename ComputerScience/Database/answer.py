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
