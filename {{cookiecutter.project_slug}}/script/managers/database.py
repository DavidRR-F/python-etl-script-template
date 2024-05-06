from ..core import env

from typing import Optional, List, Type, Union
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseManager:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        self.session = sessionmaker(bind=self.engine)

    def _execute_query(self, sql, select=None, **params):
        with self.session() as session:
            result = session.execute(sql, params)
            if select == "FIRST":
                return result.first()
            if select == "ALL":
                return result.fetchall()
            return None

    def execute(self, sql, **params):
        self._execute_query(sql, **params)

    def select_all(
        self, sql, cls: Optional[Type] = None, **params
    ) -> Union[List[object], List[tuple], List[None]]:
        results = self._execute_query(sql, select="ALL", **params)
        if cls:
            return [cls(*result) for result in results]
        return results

    def select_first(
        self, sql, cls: Optional[Type] = None, **params
    ) -> Union[object, tuple, None]:
        result = self._execute_query(sql, select="FIRST", **params)
        if cls:
            return cls(*result) if result else None
        return result

    def select_dataframe(self, sql, **params) -> pd.DataFrame:
        with self.engine.connect() as conn:
            return pd.read_sql(sql, con=conn, params=params)


dm = DatabaseManager(env.db_uri)


dm = DatabaseManager(env.db_uri)
