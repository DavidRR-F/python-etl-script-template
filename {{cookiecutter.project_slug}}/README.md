# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

### Example Core Config Usage

1. Define `core/config` variables with .env
```env
db_user="Foo"  
db_pass="Bar"  
db_host="localhost"  
db_name="testdb"
log_file="/var/logs/script.log"
```

2. Create Sql files and run querys

`sql/insert_user.sql`
```sql
insert into users(name, email) 
values(:name, :email)
```

`sql/stats.sql`
```sql
select top(100) *
from q1
left join q2
on q1.term = q2.term
```
`main.py`
```python
from managers import dm, qm

def main():
    dm.insert(qm.insert_user, name="Foo", email="Bar")
    df: pd.Dataframe = dm.select_dataframe(qm.stats)
    
```
