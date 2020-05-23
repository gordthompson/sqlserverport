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
import sqlserverport
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

## Example

```python
# example.py
import sqlserverport

# test data
server_name = "192.168.0.103"
instance_name = "SQLEXPRESS"

try:
    result = r"Instance {0}\{1} is listening on port {2}.".format(
        server_name,
        instance_name,
        sqlserverport.lookup(server_name, instance_name),
    )
except sqlserverport.BrowserError as err:
    result = err.message
except sqlserverport.NoTcpError as err:
    result = err.message

print(result)
```