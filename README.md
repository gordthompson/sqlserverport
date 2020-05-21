# sqlserverport

A simple Python module to query the SQL Browser service for the port number of a SQL Server instance. The Linux implementation of Microsoft's "ODBC Driver xx for SQL Server" is (still) unable to resolve instance names, so Windows users can just do

```python
import pyodbc
serverspec = r'myserver\SQLEXPRESS'
conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER={};...'.format(serverspec))
```

but that won't work on Linux. This module lets us do

```python
import pyodbc
from sqlserverport import sqlserverport
servername = 'myserver'
serverspec = '{0},{1}'.format(
    servername,
    sqlserverport.lookup(servername, 'SQLEXPRESS'))
conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER={};...'.format(serverspec))
```

## Installing

```
pip install sqlserverport
```
