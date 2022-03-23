from SQLStrategy.main import DB

DB.select_table("""SELECT ENAME, JOB, SAL FROM EMP ORDER BY SAL DESC""")
