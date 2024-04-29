from ..core import env

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


class DatabaseManager:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        self.session = sessionmaker(bind=self.engine)

    def execute(self, sql, **params):
        with self.session() as session:
            with session.begin():
                result = session.execute(text(sql), params)
            return result

    def select_all(self, sql, cls=None, **params):
        result = self.execute_query(sql, **params)
        if cls:
            return [cls(row) for row in result.fetchall()]
        return result.fetchall()

    def select_first(self, sql, clas=None, **params):
        result = self.execute_query(sql, **params)
        if cls:
            return cls(result.fetchone())
        return result.fetchone()

    def select_dataframe(self, sql, **params) -> pd.DataFrame:
        with self.engine.connect() as conn:
            return pd.read_sql(sql, con=conn, params=params)


dm = DatabaseManager(env.db_uri)
