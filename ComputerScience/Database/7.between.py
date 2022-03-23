from SQLStrategy.main import DB

DB.select_table("""SELECT ENAME FROM EMP WHERE SAL BETWEEN 1000 AND 2000""")
DB.select_table("select ename, sal from emp where sal between 1000 and 2000")
