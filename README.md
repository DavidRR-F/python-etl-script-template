# All in One Python ETL Template

This repository provides a streamlined structure for ETL projects. Leveraging Poetry package manager, it efficiently manages your script directory, integrates Jupyter notebook management, and offers custom commands for kernel creation and new notebook setup. The included query manager class organizes SQL queries into designated files within the SQL directory, making them easily accessible in Python code to streamline your ETL workflow. 

Thanks to [GCBallesteros](https://github.com/GCBallesteros) you can use this template in conjuction with neovim plugins [NotebookNavigator](https://github.com/GCBallesteros/NotebookNavigator.nvim) and [Jupytext](https://github.com/GCBallesteros/jupytext.nvim) to create a all in one python data management workspace. Also check out [Dadbod-UI](https://github.com/kristijanhusak/vim-dadbod-ui) for querying databases through neovim.

![image](https://github.com/DavidRR-F/python-etl-script-template/assets/99210748/b32f61ff-9b99-4ff8-a21d-23e6b3acbe6d)

My [Notebook Neovim Configuration](https://github.com/DavidRR-F/dotfiles/tree/main/.config/nvim/lua/david/plugins/python)

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

### ToDo
- [ ] Airflow Dag Template/Generator

### File Structure

![image](https://github.com/DavidRR-F/python-etl-script-template/assets/99210748/76089428-f22b-4ff7-963c-b9d26c11c1d7)
