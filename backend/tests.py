import sqlite3
import os

# con = sqlite3.connect(":memory:")
# p = con.execute("PRAGMA database_list").fetchall()
# print(p)
# con.close()
path = os.getcwd()
dir_list = os.listdir(path)
for file_name in dir_list:
    if ".db" in file_name:
        print(file_name)

# con = sqlite3.connect("table.db")
# con.close()