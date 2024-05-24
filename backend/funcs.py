import json
import sqlite3
import os

def read_database_names(data):
    temp = {}
    temp["files"] = []
    username = data.getfirst("username")
    password = data.getfirst("password")
    temp["username"] = username
    temp["password"] = password
    con = None
    temp_1 = check_login_and_return_databases(data)
    try:
        if temp_1["status"] == "OK" and temp_1["username"] == username and temp_1["password"] == password:
            path = os.getcwd()
            dir_list = os.listdir(path)
            for file_name in dir_list:
                if ".db" in file_name:
                    for items in temp_1["database"]:
                        if items+".db" == file_name:
                            temp["files"].append({"name":file_name})
            temp["status"] = "OK"
        else:
            temp["status"] = "login again"
    except Exception as e:
        temp["status"] = str(e)
        temp["err"] = str(e)

    return json.dumps(temp)

def create_database(data):
    temp = {}
    db_name = data.getfirst("db_name")
    username = data.getfirst("username")
    password = data.getfirst("password")
    temp["username"] = username
    temp["password"] = password
    con = None
    temp_1 = check_login_and_return_databases(data)
    if db_name != None:
        try:
            if temp_1["status"] == "OK" and temp_1["username"] == username and temp_1["password"] == password:
                con = sqlite3.connect(db_name+".db")
                con.close()
                con = sqlite3.connect("logins.db")
                cursor = con.cursor()
                cursor.execute('insert into info values ("'+username+'","'+password+'","'+db_name+'")')
                cursor.execute('insert into info values ("admin", "admin","'+db_name+'")')
                con.commit()
                temp["status"] = "OK"
            else:
                temp["status"] = "login again"
        except Exception as e:
            temp["err"] = str(e)
            temp["status"] = str(e)
    else:
        temp["status"] = "err"
        temp["err"] = "name not provided"
    return json.dumps(temp)

def delete_database(data):
    temp = {}
    db_name = data.getfirst("db_name")
    username = data.getfirst("username")
    password = data.getfirst("password")
    temp["username"] = username
    temp["password"] = password
    con = None
    temp_1 = check_login_and_return_databases(data)
    try:
        if temp_1["status"] == "OK" and temp_1["username"] == username and temp_1["password"] == password:
            path = os.getcwd()
            dir_list = os.listdir(path)
            for file_name in dir_list:
                if ".db" in file_name:
                    if(file_name.split(".")[0] == db_name):
                        os.remove(file_name)
                        con = sqlite3.connect("logins.db")
                        cursor = con.cursor()
                        cursor.execute(f'delete from info where username="{username}" and password="{password}" and database_created="{db_name}"')
                        cursor.execute(f'delete from info where username="admin" and password="admin" and database_created="{db_name}"')
                        con.commit()
                        
            temp["status"] = "OK"
        else:
            temp["status"] = "login again"
    except Exception as e:
        temp["status"] = str(e)
        temp["err"] = str(e)

    return json.dumps(temp)

def read_database_table_names(data):
    temp = {}
    temp["files"] = []
    db_name = data.getfirst("db_name")
    username = data.getfirst("username")
    password = data.getfirst("password")
    temp["username"] = username
    temp["password"] = password
    con = None
    temp_1 = check_login_and_return_databases(data)
    temp["db_name"] = db_name
    if db_name != None:
        try:
            if temp_1["status"] == "OK" and temp_1["username"] == username and temp_1["password"] == password:
                con = sqlite3.connect(db_name+".db")
                sql_query = "SELECT name FROM sqlite_master  WHERE type='table';"
                cursor = con.cursor()
                cursor.execute(sql_query)
                p = cursor.fetchall()
                for items in p:
                    temp["files"].append({"name":items[0]})
                temp["status"] = "OK"
            else:
                temp["status"] = "login again"
        except Exception as e:
            temp["err"] = str(e)
            temp["status"] = str(e)
        finally:
            if con != None:
                con.close()
    else:
        temp["status"] = "err"
        temp["err"] = "name not provided"
    return json.dumps(temp)

def execute_command(data):
    temp = {}
    db_name = data.getfirst("db_name")
    command = data.getfirst("command")
    username = data.getfirst("username")
    password = data.getfirst("password")
    temp["username"] = username
    temp["password"] = password
    con = None
    temp_1 = check_login_and_return_databases(data)
    temp["db_name"] = db_name
    if db_name != None:
        try:
            if temp_1["status"] == "OK" and temp_1["username"] == username and temp_1["password"] == password:
                con = sqlite3.connect(db_name+".db")
                sql_query = command
                cursor = con.cursor()
                cursor.execute(sql_query)
                p = cursor.fetchall()
                # temp["status"] = str(p)
                con.commit()
                temp["status"] = "OK"
            else:
                temp["status"] = "login again"
        except Exception as e:
            temp["err"] = str(e)
            temp["status"] = str(e)
        finally:
            if con != None:
                con.close()
    else:
        temp["status"] = "err"
        temp["err"] = "name not provided"
    return json.dumps(temp)

def execute_command_on_table(data):
    temp = {}
    db_name = data.getfirst("db_name")
    command = data.getfirst("command")
    table_name = data.getfirst("table_name")
    username = data.getfirst("username")
    password = data.getfirst("password")
    temp["username"] = username
    temp["password"] = password
    con = None
    temp_1 = check_login_and_return_databases(data)
    temp["db_name"] = db_name
    if db_name != None and table_name != None and table_name in command:
        try:
            if temp_1["status"] == "OK" and temp_1["username"] == username and temp_1["password"] == password:
                con = sqlite3.connect(db_name+".db")
                sql_query = command
                cursor = con.cursor()
                cursor.execute(sql_query)
                p = cursor.fetchall()
                # temp["status"] = str(p)
                con.commit()
                temp["status"] = "OK"
            else:
                temp["status"] = "login again"
        except Exception as e:
            temp["err"] = str(e)
            temp["status"] = str(e)
        finally:
            if con != None:
                con.close()
    else:
        temp["status"] = "err"
        temp["err"] = "name not provided"
    return json.dumps(temp)


def read_database_table_field_names(data):
    temp = {}
    db_name = data.getfirst("db_name")
    table_name = data.getfirst("table_name")
    username = data.getfirst("username")
    password = data.getfirst("password")
    temp["username"] = username
    temp["password"] = password
    con = None
    temp_1 = check_login_and_return_databases(data)
    temp["db_name"] = db_name
    temp["table_name"] = table_name
    if db_name != None and table_name != None:
        try:
            if temp_1["status"] == "OK" and temp_1["username"] == username and temp_1["password"] == password:
                con = sqlite3.connect(db_name+".db")
                sql_query = "SELECT * FROM "+table_name
                cursor = con.cursor()
                cursor.execute(sql_query)
                p = cursor.fetchall()
                temp["values"] = p
                temp["column_names"] = list(map(lambda x: {"name":x[0]}, cursor.description))
                temp["status"] = "OK"
            else:
                temp["status"] = "login again"
        except Exception as e:
            temp["err"] = str(e)
            temp["status"] = str(e)
        finally:
            if con != None:
                con.close()
    else:
        temp["status"] = "err"
        temp["err"] = "name not provided"
    return json.dumps(temp)

    
def check_login(data):
    temp = {}
    username = data.getfirst("username")
    password = data.getfirst("password")
    temp["username"] = None
    temp["password"] = None
    con = None
    try:
        con = sqlite3.connect("logins.db")
        sql_query = "SELECT * FROM info"
        cursor = con.cursor()
        cursor.execute(sql_query)
        p = cursor.fetchall()
        for items in p:
            uname = items[0]
            pword = items[1]
            if uname == username and pword == password:
                temp["username"] = username
                temp["password"] = password
                break
        if temp["username"] == None:
            temp["status"] = "wrong username or password"
        else:
            temp["status"] = "OK"
    except Exception as e:
        temp["err"] = str(e)
        temp["status"] = str(e)
    finally:
        if con != None:
            con.close()
    return json.dumps(temp)

def check_login_and_return_databases(data):
    temp = {}
    username = data.getfirst("username")
    password = data.getfirst("password")
    temp["username"] = None
    temp["password"] = None
    temp["database"] = []
    con = None
    try:
        con = sqlite3.connect("logins.db")
        sql_query = "SELECT * FROM info"
        cursor = con.cursor()
        cursor.execute(sql_query)
        p = cursor.fetchall()
        for items in p:
            uname = items[0]
            pword = items[1]
            database = items[2]
            if uname == username and pword == password:
                temp["username"] = username
                temp["password"] = password
                temp["database"].append(database)
        if temp["username"] == None:
            temp["status"] = "wrong username or password"
        else:
            temp["status"] = "OK"
    except Exception as e:
        temp["err"] = str(e)
        temp["status"] = str(e)
    finally:
        if con != None:
            con.close()
    return temp

    
def create_register(data):
    temp = {}
    username = data.getfirst("username")
    password = data.getfirst("password")
    temp["username"] = username
    temp["password"] = password
    con = None
    try:
        con = sqlite3.connect("logins.db")
        sql_query = 'Insert Into info (username, password, database_created) values ("'+username+'","'+password+'","__no_databases_yet_created__")'
        cursor = con.cursor()
        cursor.execute(sql_query)
        con.commit()
        temp["status"] = "OK"
    except Exception as e:
        temp["err"] = str(e)
        temp["status"] = str(e)
    finally:
        if con != None:
            con.close()

    return json.dumps(temp)