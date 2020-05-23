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
