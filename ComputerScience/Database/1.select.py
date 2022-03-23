"""
Show ENAME, JOB, and SAL from EMP table
"""
from SQLStrategy.main import DB

DB.select_table("SELECT ENAME, JOB, SAL FROM EMP")
DB.select_table("SELECT * FROM EMP")
