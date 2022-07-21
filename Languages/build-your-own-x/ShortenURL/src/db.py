"""
src/db.py

# NOTE: HOW TO USE and HANDLE Dependency Injection
"""
import sqlite3
from typing import List


class DB:
    DB_NAME: str = "urls.db"
    TABLE_NAME: str = "urls"

    def __init__(self, db_name: str = "", table_name: str = ""):
        if db_name != "":
            self.DB_NAME = db_name

        if table_name != "":
            self.TABLE_NAME = table_name

        self.con = sqlite3.connect(self.DB_NAME)
        self.cur = self.con.cursor()

        sql = f"""CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT, shorten_url TEXT)"""

        self.cur.execute(sql)
        self.con.commit()

    def insert_url(self, url: str, shorten_url: str):
        """insert_db
        insert tables
        :param url: str
        :param shorten_url: str
        :return:
        """
        sql = f"""INSERT INTO {self.TABLE_NAME} (url, shorten_url) VALUES (?,?)"""

        self.cur.execute(sql, (url, shorten_url))
        self.con.commit()

    def find_url(self, url: str) -> bool:
        """
        find url from table

        :param url:
        :return: return True when url is found
        """
        sql = f"""SELECT id FROM {self.TABLE_NAME} WHERE url = ?"""
        self.cur.execute(sql, (url,))
        return self.cur.fetchone() is not None

    def find_shorten_url(self, shorten_url: str) -> bool:
        """
        find shorten_url from table

        :param shorten_url:
        :return: return True when shorten_url is found
        """
        sql = f"""SELECT id FROM {self.TABLE_NAME} WHERE shorten_url = ?"""
        self.cur.execute(sql, (shorten_url,))
        return self.cur.fetchone() is not None

    def get_shorten_url(self, url: str) -> str:
        """
        get shorten_url from table
        :param url:
        :return: shorten_url
        """
        sql = f"""SELECT shorten_url FROM {self.TABLE_NAME} WHERE url = ?"""
        self.cur.execute(sql, (url,))
        return self.cur.fetchone()[0]

    @property
    def urls(self) -> List[str]:
        self.cur.execute(f"SELECT * FROM {self.TABLE_NAME}")

        res = []
        for row in self.cur.fetchall():
            res.append(row[1])
        return res

    @property
    def shorten_urls(self) -> List[str]:
        self.cur.execute(f"SELECT * FROM {self.TABLE_NAME}")

        res = []
        for row in self.cur.fetchall():
            res.append(row[2])
        return res

    @property
    def connection(self):
        return self.con

    @property
    def db_name(self) -> str:
        return self.DB_NAME

    @property
    def table_name(self) -> str:
        return self.TABLE_NAME
