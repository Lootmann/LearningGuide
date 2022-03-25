import sqlite3


class DB:
    """
    EMP
        EMPNO       従業員番号  int
        ENAME       従業員名    str
        JOB         仕事        str
        MGR         マネージャー int
        HIREDATE    採用日付    date
        SAL         給料        int
        COMM        歩合給      int
        DEPTNO      部署番号    int

    DEPT
        DEPTNO  部署番号    int
        DNAME   部署名      str
        LOC     所在地      str
    """

    DB_NAME = "test.db"

    EMP_TABLE = """
    CREATE TABLE IF NOT EXISTS EMP (
        EMPNO INTEGER,
        ENAME TEXT,
        JOB TEXT,
        MGR INTEGER,
        HIREDATE TEXT,
        SAL INTEGER,
        COMM INTEGER,
        DEPTNO INTEGER)
    """

    DEPT_TABLE = """
    CREATE TABLE IF NOT EXISTS DEPT (
        DEPTNO INTEGER,
        DNAME TEXT,
        LOC TEXT)
    """

    @staticmethod
    def create_table():
        with sqlite3.connect(DB.DB_NAME) as db:
            cur = db.cursor()

            cur.execute(DB.EMP_TABLE)
            cur.execute(DB.DEPT_TABLE)

            db.commit()
            cur.close()

    @staticmethod
    def insert_table(filename: str, sql: str):
        records = []
        with open(filename, "r") as f:
            records = [line.strip() for line in f.readlines()]

        with sqlite3.connect(DB.DB_NAME) as db:
            cur = db.cursor()

            for record in records:
                cur.execute(sql, tuple(record.split("\t")))

            db.commit()
            cur.close()

    @staticmethod
    def select_table(sql: str):
        with sqlite3.connect(DB.DB_NAME) as db:
            cur = db.cursor()
            print(">>> {}".format(sql))
            for row in cur.execute(sql):
                print(row)
            print()
            cur.close()


def main():
    DB.create_table()

    # EMP
    DB.insert_table(
        "./input_emp",
        "INSERT INTO EMP (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO)"
        "VALUES(?,?,?,?,?,?,?,?)",
    )

    # DEPT
    DB.insert_table(
        "./input_dept",
        "INSERT INTO DEPT (DEPTNO, DNAME, LOC) VALUES(?,?,?)",
    )


if __name__ == "__main__":
    main()
