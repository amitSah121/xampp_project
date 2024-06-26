# API Documentation

## Introduction

This api endpoint backend is based on python running on cgi on xampp server at http://103.211.202.111/ .The backend is based on **sqlite3** database. By default all users can be able to use the api with a constant password since password mechanism is not being implemented at a level. The project structure is:

- backend
    - app
        - app.html
        - app_table.html
        - app_fields.html
        - w3.css
        - w3.js
    - main.py
    - funcs.py
    - tests

App Interface
-------
1) The main application can be called from http://103.211.202.111/backend/app/app.html . 
2) The login screen appears, note: default username=guest, password=guest. For guest purpose only usernamep=admin.Login.
2) app.html presents interface to create , delete and view databases
3) after creating and going inside a database say "Test.db", you will be presented with a url http://103.211.202.111/backend/app/app_table.html?database=Test.db
    1) The interface presented gives flexibility in creating, updating and deleting tables with the use of executing command.
    2) CREATE TABLE Table_1 (name, roll) will create a table with fields name and roll both being integer by default.
    3) CREATE TABLE COMPANY(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50), SALARY REAL) is a representation of syntax
4) after creating a table say "Table_1" and and clicking it you will be presented in http://103.211.202.111/backend/app/app_table.html?database=Test&table=Table_1
    1) Its interface also provides a command executer.
    2) It presents with field names and values.


API Introduction
---------------
The format presents the url as http://103.211.202.111/backend/main.py?username=name1&password=password1&func=function_name&oprional_parameter1=parm1&oprional_parameter2=parm2.....

Note: These urls can be directly executed on chrome or any web browser.

1) To read all databases available
    - func = read_database_names
    - no optional parameters
    - http://103.211.202.111/backend/main.py?username=guest&&password=guest&&func=read_database_names
```json
{
  "files": [
    {
      "name": "pebble.db"
    },
    {
      "name": "SAPR.db"
    },
    {
      "name": "Skdas.db"
    },
    {
      "name": "table.db"
    },
    {
      "name": "test.db"
    }
  ]
}
```

```javascript
let cross_origin_properties = {    
    method: 'GET',    
    withCredentials: true,    
    crossorigin: true,    
    mode: 'cors',       
};
let url_prefix = "https://103.211.202.111/backend/main.py?";
let username = "guest";
let password = "guest";
let func = "read_database_names";
fetch(url_prefix+`username=${username}&password=${password}&func=${func}`,cross_origin_properties)
.then(data => data.json())
.then(json => console.log(json));
```
2) To create a database
    - func = create_database
    - optional parameter
        - db_name=databasename
    - http://103.211.202.111/backend/main.py?username=guest&password=guest&func=create_database&db_name=Hello
```json
{
    "status" : "OK"
}

and after executing read_databases

{
  "files": [
    {
      "name": "db_1.db"
    },
    {
      "name": "pebble.db"
    },
    {
      "name": "SAPR.db"
    },
    {
      "name": "Skdas.db"
    },
    {
      "name": "table.db"
    },
    {
      "name": "test.db"
    }
  ]
}
```

```javascript
let cross_origin_properties = {    
    method: 'GET',    
    withCredentials: true,    
    crossorigin: true,    
    mode: 'cors',       
};
let url_prefix = "https://103.211.202.111/backend/main.py?";
let username = "guest";
let password = "guest";
let func = "create_database";
let db_name = "Hello"
fetch(url_prefix+`username=${username}&password=${password}&func=${func}&db_name=${db_name}`,cross_origin_properties)
.then(data => data.json())
.then(json => console.log(json));
```

3) To delete database
    - func = delete_database
    - optional parameter
        - db_name = databasename
    - http://103.211.202.111/backend/main.py?username=guest&password=guest&func=delete_database&db_name=test
```json
after executing read_databases again, removes pebble.db
{
  "files": [
    {
      "name": "db_1.db"
    },
    {
      "name": "SAPR.db"
    },
    {
      "name": "Skdas.db"
    },
    {
      "name": "table.db"
    },
    {
      "name": "test.db"
    }
  ]
}
```
```javascript
let cross_origin_properties = {    
    method: 'GET',    
    withCredentials: true,    
    crossorigin: true,    
    mode: 'cors',       
};
let url_prefix = "https://103.211.202.111/backend/main.py?";
let username = "guest";
let password = "guest";
let func = "delete_database";
let db_name = "Hello"
fetch(url_prefix+`username=${username}&password=${password}&func=${func}&db_name=${db_name}`,cross_origin_properties)
.then(data => data.json())
.then(json => console.log(json));
```

4) To read all tables available in a database
    - func = read_database_table_names
    - optional parameters
        - db_name = databasename
    - http://103.211.202.111/backend/main.py?username=guest&password=guest&func=read_database_table_names&db_name=test
```json
{
  "files": [
    {
      "name": "triple"
    }
  ],
  "db_name": "table",
  "status": "OK"
}
```

```javascript
let cross_origin_properties = {    
    method: 'GET',    
    withCredentials: true,    
    crossorigin: true,    
    mode: 'cors',       
};
let url_prefix = "https://103.211.202.111/backend/main.py?";
let username = "guest";
let password = "guest";
let func = "read_database_table_names";
let db_name = "Hello"
fetch(url_prefix+`username=${username}&password=${password}&func=${func}&db_name=${db_name}`,cross_origin_properties)
.then(data => data.json())
.then(json => console.log(json));
```

5) To read table field names
    - func = read_database_table_field_names
    - optional parameters
        - db_name = databasename
        - table_name = tablename
    - http://103.211.202.111/backend/main.py?username=guest&password=guest&func=read_database_table_field_names&db_name=database_name&table_name=table_name
```json
{
  "db_name": "table",
  "table_name": "triple",
  "values": [
    [2, 3],
    [5, 6]
  ],
  "column_names": [
    {
      "name": "hello"
    },
    {
      "name": "fellow"
    }
  ],
  "status": "OK"
}
```

```javascript
let cross_origin_properties = {    
    method: 'GET',    
    withCredentials: true,    
    crossorigin: true,    
    mode: 'cors',       
};
let url_prefix = "https://103.211.202.111/backend/main.py?";
let username = "guest";
let password = "guest";
let func = "read_database_table_field_names";
let table_name = "sb"
let db_name = "Hello"
fetch(url_prefix+`username=${username}&password=${password}&func=${func}&db_name=${db_name}&table_name=${table_name}`,cross_origin_properties)
.then(data => data.json())
.then(json => console.log(json));
```

6) To execute command on database
    - func = execute_command
    - optional parameters
        - db_name = databasename
    - http://103.211.202.111/backend/main.py?username=guest&password=guest&func=execute_command&db_name=database_name&command=command
    - e.g. select * from table_1 is written as command=select+%2A+from+table_1
    - e.g. http://103.211.202.111/backend/main.py?username=guest&&password=guest&&func=execute_command&db_name=table&command=select+%2A+from+triple
```json
{
  "db_name": "table",
  "status": "[(2, 3), (5, 6)]"
}
```

```javascript
let cross_origin_properties = {    
    method: 'GET',    
    withCredentials: true,    
    crossorigin: true,    
    mode: 'cors',       
};
let url_prefix = "https://103.211.202.111/backend/main.py?";
let username = "guest";
let password = "guest";
let func = "execute_command";
let db_name = "Hello";
let table_name = "sb"; 
let command = "create table sb (start INT, first INT)"
fetch(url_prefix+`username=${username}&password=${password}&func=${func}&db_name=${db_name}&table_name=${table_name}&command=${command}`,cross_origin_properties)
.then(data => data.json())
.then(json => console.log(json));
```

6) To execute command on table
    - func = execute_command_on_table
    - optional parameters
        - db_name = databasename
        - table_name = tablename
    - http://103.211.202.111/backend/main.py?username=guest&password=guest&func=execute_command_on_table&db_name=test&table_name=table_1&command=command
    - e.g. select * from table_1 is written as command=select+%2A+from+table_1
    - e.g. http://103.211.202.111/backend/main.py?username=guest&&password=guest&&func=execute_command_on_table&db_name=table&table_name=triple&command=select+%2A+from+triple
```json
{
  "db_name": "table",
  "status": "[(2, 3), (5, 6)]"
}
```

```javascript
let cross_origin_properties = {    
    method: 'GET',    
    withCredentials: true,    
    crossorigin: true,    
    mode: 'cors',       
};
let url_prefix = "https://103.211.202.111/backend/main.py?";
let username = "guest";
let password = "guest";
let func = "execute_command";
let db_name = "Hello";
let table_name = "sb"; 
let command = "insert into sb (start, first) values (2,3)"
fetch(url_prefix+`username=${username}&password=${password}&func=${func}&db_name=${db_name}&table_name=${table_name}&command=${command}`,cross_origin_properties)
.then(data => data.json())
.then(json => console.log(json));
```
 7) To create new user
  - func = create_register
  - optional_parameter
    - username
    - password
  - http://103.211.202.111/backend/main.py?username=guest&password=guest&func=create_register
  - e.g. http://103.211.202.111/backend/app/app_database.html?username=guest&password=guest

```javascript
let cross_origin_properties = {    
    method: 'GET',    
    withCredentials: true,    
    crossorigin: true,    
    mode: 'cors',       
};
let url_prefix = "https://103.211.202.111/backend/main.py?";
let username = "guest";
let password = "guest";
let func = "create_register";
fetch(url_prefix+`username=${username}&password=${password}&func=${func}`,cross_origin_properties)
.then(data => data.json())
.then(json => console.log(json));
```

Lastly , https://www.url-encode-decode.com/ website can be used to convert "select * from table_1" to "select+%2A+from+table_1"

