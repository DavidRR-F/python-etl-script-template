import os
from sqlalchemy import text


class QueryManager:
    sql_dir = None
    sql_files = None

    def __init__(self, sql_dir):
        self.sql_dir = sql_dir
        self.sql_files = [
            f
            for f in os.listdir(self.sql_dir)
            if os.path.isfile(os.path.join(self.sql_dir, f)) and ".sql" in f
        ]

    def __getattr__(self, item):
        if item + ".sql" in self.sql_files:
            with open(os.path.join(self.sql_dir, item + ".sql"), "r") as f:
                return text(f.read())
        else:
            raise AttributeError(f"QueryManager cannot find file {str(item)}.sql")


qm = QueryManager(os.path.join(os.path.dirname(os.path.dirname(__file__)), "sql"))
