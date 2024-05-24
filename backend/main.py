#!"C:/Users/Administrator/AppData/Local/Programs/Python/Python312/python.exe"

import cgi
from funcs import read_database_names
from funcs import create_database
from funcs import delete_database
from funcs import read_database_table_names
from funcs import execute_command
from funcs import execute_command_on_table
from funcs import read_database_table_field_names
from funcs import check_login
from funcs import create_register
# import json
# import sqlite3

# import cgitb
# cgitb.enable()

print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print("Content-Type: application/json; charset=UTF-8\n\n")

## note by default everything will be in json

if __name__ == "__main__":
    data = cgi.FieldStorage()
    function_to_use = data.getfirst("func")
    # if not (username == "admin" and password == "12345"):
    #     print('"err":"incorrect username or password"')
    
    if function_to_use == "read_database_names":
        print(read_database_names(data))
    elif function_to_use == "create_database":
        print(create_database(data)) 
    elif function_to_use == "delete_database":
        print(delete_database(data))
    elif function_to_use == "read_database_table_names":
        print(read_database_table_names(data))
    elif function_to_use == "execute_command":
        print(execute_command(data))
    elif function_to_use == "execute_command_on_table":
        print(execute_command_on_table(data))
    elif function_to_use == "read_database_table_field_names":
        print(read_database_table_field_names(data))
    elif function_to_use == "check_login" :
        print(check_login(data))
    elif function_to_use == "create_register":
        print(create_register(data))
    
    # make = data.getvalue("make")
    # p = {'fello':'hello','hello':10}
    # print(json.dumps(p))
else: print('"err":"called as a module"')