import sqlite3


def title(msg: str) -> None:
    size = len(msg) + 6
    print("*" * size)
    print(f"*  {msg}  *")
    print("*" * size)


class DB:
    def __init__(self, db_name: str, table_name: str):
        self.db_name = db_name
        self.table_name = table_name

        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name}(
                id integer primary key autoincrement,
                name text,
                kind text,
                calorie integer
            )"""
        )
        self.conn.commit()

    def insert_table(self, args):
        self.cur.execute(
            f"INSERT INTO {self.table_name}(name, kind, calorie) VALUES (?,?,?)",
            tuple(args),
        )
        self.conn.commit()

    def select_table(self, sql: str):
        for row in self.cur.execute(sql):
            print(row)
        print()


def main():
    db = DB(db_name=":memory:", table_name="ice")

    db.create_table()
    db.insert_table(["locky load", "THE 31", 162])
    db.insert_table(["Nuts To You", "Elegant", 168])
    db.insert_table(["Choped Chocolate", "CHOCOLATE", 175])
    db.insert_table(["Vannila", "Kentackiy", 186])
    db.insert_table(["Baginner", "Washington", 199])

    title("Q1")
    db.select_table(
        """
        SELECT distinct i1.name, i2.name, i1.kind, i1.calorie + i2.calorie
        FROM ice i1, ice i2
        WHERE i1.id != i2.id
        ;
        """
    )

    title("Q2")
    db.select_table(
        """
        SELECT i1.name, i2.name, i1.calorie + i2.calorie AS CAL
        FROM ice i1, ice i2
        WHERE (i1.id != i2.id)
            AND (CAL <= 350)
            AND 'Elegant' IN (i1.kind, i2.kind)
        ORDER BY CAL ASC
        ;
        """
    )

    title("Q3")
    db.select_table(
        """
        SELECT i1.name, i2.name, i3.name, i1.calorie + i2.calorie + i3.calorie AS CAL
        FROM ice i1, ice i2, ice i3
        WHERE (i1.id != i2.id AND i2.id != i3.id AND i3.id != i1.id)
            AND (CAL <= 510)
            AND 'Elegant' IN (i1.kind, i2.kind, i3.kind)
        ORDER BY CAL ASC
        ;
        """
    )


if __name__ == "__main__":
    main()
