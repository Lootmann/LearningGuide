"""
tests/test_db.py

# NOTE: how to use teardown
"""
import os

from src.db import DB


class TestDB:
    def setup_method(self):
        self.db = DB(db_name="new.db", table_name="news")

    def teardown_method(self):
        os.remove("new.db")

    def test_init_db(self):
        assert self.db.db_name == "new.db"
        assert self.db.table_name == "news"

    def test_insert_urls(self):
        self.db.insert_url("www.w1.org", "1b2c34d")
        self.db.insert_url("www.w2.org", "1b2c34d")
        self.db.insert_url("www.w3.org", "1b2c34d")
        assert self.db.urls == ["www.w1.org", "www.w2.org", "www.w3.org"]

    def test_insert_shorten_urls(self):
        self.db.insert_url("www.w1.org", "1a1a1a")
        self.db.insert_url("www.w2.org", "2b2b2b")
        self.db.insert_url("www.w3.org", "3c3c3c")
        assert self.db.shorten_urls == ["1a1a1a", "2b2b2b", "3c3c3c"]

    def test_find_url(self):
        self.db.insert_url("www.w1.org", "1b2c3d")
        self.db.insert_url("www.w2.org", "1b2c3d")
        assert self.db.find_url("www.w1.org") is True
        assert self.db.find_url("www.w2.org") is True
        assert self.db.find_url("www.w3.org") is False

    def test_find_shorten_url(self):
        self.db.insert_url("www.w1.org", "1b2c3d")
        self.db.insert_url("www.w2.org", "2b3c4d")
        assert self.db.find_shorten_url("1b2c3d") is True
        assert self.db.find_shorten_url("2b3c4d") is True
        assert self.db.find_shorten_url("1a2b3c") is False

    def test_get_shorten_url(self):
        self.db.insert_url("www.w1.org", "1b2c3d")
        self.db.insert_url("www.w2.org", "2b3c4d")
        assert self.db.get_shorten_url("www.w1.org") == "1b2c3d"
        assert self.db.get_shorten_url("www.w2.org") == "2b3c4d"
