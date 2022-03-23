from SQLStrategy.main import DB

DB.select_table(
    """SELECT SUM(sal), MAX(sal), MIN(sal), AVG(sal), count(SAL) FROM EMP"""
)
