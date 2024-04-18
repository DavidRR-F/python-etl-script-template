import pytest
from sqlalchemy import create_engine

from script.managers.database import DatabaseManager


@pytest.fixture(scope="module")
def db_manager():
    DATABASE_URL = "sqlite:///:memory:"
    manager = DatabaseManager(DATABASE_URL)
    manager.execute_query(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)"
    )
    yield manager
    manager.execute_query("DROP TABLE users")


def test_insert(db_manager):
    db_manager.insert(
        "INSERT INTO users (name, email) VALUES (:name, :email)",
        name="test",
        email="test",
    )
    assert db_manager.select_first("SELECT * FROM users") == (1, "test", "test")


def test_select_first(db_manager):
    db_manager.insert(
        "INSERT INTO users (name, email) VALUES (:name, :email)",
        name="test2",
        email="test2",
    )
    assert db_manager.select_first("SELECT * FROM users") == (1, "test", "test")


def test_select_all(db_manager):
    assert db_manager.select_all("SELECT * FROM users") == [
        (1, "test", "test"),
        (2, "test2", "test2"),
    ]


def test_select_dataframe(db_manager):
    df = db_manager.select_dataframe("SELECT * FROM users")
    assert df.shape == (2, 3)
