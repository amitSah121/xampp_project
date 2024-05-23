Methods
- getvalue(str) - for single parameter having single value
- getlist(str) - for same parameter having multiple values
- data["username"] retuns a file
- FieldStorage.getfirst(name, default=None)
- FieldStorage.getlist(name)
- cgi.test()
- cgi.print_environ()
  Format the shell environment in HTML.
- cgi.print_form(form)
  Format a form in HTML.
-cgi.print_directory()
  Format the current directory in HTML.
- cgi.print_environ_usage()
  Print a list of useful (used by CGI) environment variables in HTML.
- theValue = formStorage['PARAM_NAME'].value
  Get a parameter string from the form

- for further information
https://robosparrow.github.io/2020/09/29/python-cgi-parsing-json-requests.html

```python
fileitem = form["userfile"]
  if fileitem.file:
      # It's an uploaded file; count lines
      linecount = 0
      while True:
          line = fileitem.file.readline()
          if not line: break
          linecount = linecount + 1

# examples
<input type="checkbox" name="item" value="1" />
<input type="checkbox" name="item" value="2" />
item = form.getvalue("item")
if isinstance(item, list):
    # The user is requesting more than one item.
else:
    # The user is requesting only one item.


```

```python
curl \
    --request POST \
    --header "Content-Type: application/x-www-form-urlencoded" \
    --header "X-Marvin-Status: depressed" \
    --data 'name=Deep Thought&answer=42' \
    http://raspberrypi.local:9000/hitchhiker/api/ultimate-question.py?test=1
server

#!/usr/bin/env python3

import os
import sys
import json

from urllib.parse import parse_qs

content_len = os.environ.get('CONTENT_LENGTH', '0')
method = os.environ.get('REQUEST_METHOD', '')
query_string = os.environ.get('QUERY_STRING', '')
x_header = os.environ.get('HTTP_X_MARVIN_STATUS', '')

body = sys.stdin.read(int(content_len))
res = json.loads(body)

print('method: ', method)
print('header[X-Marvin-Status]: ', x_header)
print('query: ', query_string)
print('json: ', res)

if not query_string:
    exit()

query = parse_qs(query_string)
print('test: ', query['test'][0])
```

## For sqlite3

- create database
  import sqlite3
  con = sqlite3.connect("tutorial.db")

- connect to database
  con = sqlite3.connect("tutorial.db")
  cur = con.cursor()

- execute a command
  cur.execute("CREATE TABLE movie(title, year, score)")
  res.fetchone()
  res.fetchall()

- execute many commnads
  data = [
      ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
      ("Monty Python's The Meaning of Life", 1983, 7.5),
      ("Monty Python's Life of Brian", 1979, 8.0),
  ]
  cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
  con.commit() # Remember to commit the transaction after executing INSERT.

- reading
  for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

- closing a database
  con.close()

- delete database
  import os
  os.remove(databaseName)


## Apps

note: 103.211.202.111/backend/app.html

### Protocols

1) username
2) password
3) func

e.g. http://103.211.202.111/backend/main.py/username=Hello&&password=12345&&func=read_database_names

#### Funcs available
1) read_database_names
  e.g. username=Hello&&password=12345&&func=read_database_names
2) create_database
  e.g. username=admin&password=12345&func=create_database&db_name=test
3) delete_database
 e.g. username=admin&password=12345&func=delete_database&db_name=test
4) read_database_table_names
 e.g. username=admin&password=12345&func=read_database_table_names&db_name=test
5) execute_command
  e.g. username=admin&password=12345&func=execute_command&db_name=database_name&command=command
6) execute_command_on_table
  e.g. username=admin&password=12345&func=execute_command_on_table&db_name=database_name&table_name=table_name&command=command
7) read_database_table_field_names
  e.g. username=admin&password=12345&func=read_database_table_field_names&db_name=database_name&table_name=table_name

#### References 
1) https://www.sitepoint.com/get-url-parameters-with-javascript/
2) https://www.w3schools.com/w3css/w3css_tables.asp
3) https://www.w3schools.com/w3js/w3js_hide.asp
4) https://docs.python.org/3/library/sqlite3.html
5) https://robosparrow.github.io/2020/09/29/python-cgi-parsing-json-requests.html
