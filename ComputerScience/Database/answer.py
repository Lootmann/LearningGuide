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

title("GROUP BY")
DB.select_table("SELECT JOB, AVG(SAL) FROM EMP GROUP BY JOB")
DB.select_table("SELECT JOB, AVG(SAL) FROM EMP WHERE DEPTNO <> 10 GROUP BY JOB")
DB.select_table("SELECT DEPTNO, AVG(SAL) FROM EMP GROUP BY DEPTNO")
