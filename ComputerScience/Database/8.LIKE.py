from SQLStrategy.main import DB

DB.select_table("select ename from emp where ename like '%A%'")
DB.select_table("select ename from emp where ename like '%?_%' ESCAPE '?'")
