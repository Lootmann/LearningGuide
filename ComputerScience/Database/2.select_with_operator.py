"""
You have decided to increase an employee's salary by 2%.

From the EMP table,
show the employee's name (ENAME) and the salary multiplied by 1.02 (SAL). 
"""
from SQLStrategy.main import DB

DB.select_table("SELECT ENAME, SAL * 1.02 FROM EMP")
