import pytest

from script.managers.query import QueryManager


@pytest.fixture
def sql_directory(tmp_path):
    d = tmp_path / "sql"
    d.mkdir()
    (d / "test_query.sql").write_text("SELECT * FROM test_table;")
    return d


def test_init(sql_directory):
    qm = QueryManager(sql_directory)
    assert qm.sql_dir == sql_directory
    assert qm.sql_files == ["test_query.sql"]


def test_getattr(sql_directory):
    qm = QueryManager(sql_directory)
    assert str(qm.test_query) == "SELECT * FROM test_table;"


def test_getattr_error(sql_directory):
    qm = QueryManager(sql_directory)
    with pytest.raises(AttributeError) as excinfo:
        qm.nonexistent
    assert "QueryManager cannot find file nonexistent.sql" in str(excinfo.value)
