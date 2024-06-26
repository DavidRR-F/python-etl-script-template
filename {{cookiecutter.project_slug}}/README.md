# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Example Usage

Define `core/config` variables with .env
```env
db_user="Foo"  
db_pass="Bar"  
db_host="localhost"  
db_name="testdb"
log_file="/var/logs/script.log"
```
## Notebook Managment


Create a Kernel that uses the projects virtualenv
```bash
poetry run create-kernel <kernel-name>
```
Create a new notebook in the notebook directory
```bash
poetry run create-book <notebook-name>
```

## SQL Query Managment

Create a SQL file in the sql directory

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
on q1.clientId = q2.clientId
```
Reference the Query via the Querymanager in Script or Notebook

`main.py`
```python
from managers import dm, qm

def main():
    dm.execute(qm.insert_user, name="Foo", email="Bar")
    df: pd.Dataframe = dm.select_dataframe(qm.stats)
    
```

`notebook.ipynb`

```python
# %%
from script.managers.query import qm 
from script.managers.database import dm 
df = dm.select_dataframe(qm.stats)
df 
# %%
```
