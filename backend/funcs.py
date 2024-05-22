import json
import sqlite3
import os

def read_database_names():
    temp = {}
    temp["files"] = []
    try:
        path = os.getcwd()
        dir_list = os.listdir(path)
        for file_name in dir_list:
            if ".db" in file_name:
                temp["files"].append({"name":file_name})
    except Exception as e:
        temp["status"] = "err"
        temp["err"] = str(e)

    return json.dumps(temp)

def create_database(data):
    temp = {}
    db_name = data.getfirst("db_name")
    if db_name != None:
        try:
            con = sqlite3.connect(db_name+".db")
            con.close()
            temp["status"] = "OK"
        except Exception as e:
            temp["err"] = str(e)
            temp["status"] = "err"
    else:
        temp["status"] = "err"
        temp["err"] = "name not provided"
    return json.dumps(temp)

def delete_database(data):
    temp = {}
    db_name = data.getfirst("db_name")
    try:
        path = os.getcwd()
        dir_list = os.listdir(path)
        for file_name in dir_list:
            if ".db" in file_name:
                if(file_name.split(".")[0] == db_name):
                    os.remove(file_name)
    except Exception as e:
        temp["status"] = "err"
        temp["err"] = str(e)

    return json.dumps(temp)

def read_database_table_names(data):
    temp = {}
    temp["files"] = []
    db_name = data.getfirst("db_name")
    temp["db_name"] = db_name
    if db_name != None:
        try:
            con = sqlite3.connect(db_name+".db")
            sql_query = "SELECT name FROM sqlite_master  WHERE type='table';"
            cursor = con.cursor()
            cursor.execute(sql_query)
            p = cursor.fetchall()
            for items in p:
                temp["files"].append({"name":items[0]})
            temp["status"] = "OK"
        except Exception as e:
            temp["err"] = str(e)
            temp["status"] = "err"
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
    temp["db_name"] = db_name
    if db_name != None:
        try:
            con = sqlite3.connect(db_name+".db")
            sql_query = command
            cursor = con.cursor()
            cursor.execute(sql_query)
            p = cursor.fetchall()
            temp["status"] = str(p)
            con.commit()
        except Exception as e:
            temp["err"] = str(e)
            temp["status"] = "err"
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
    temp["db_name"] = db_name
    if db_name != None and table_name != None and table_name in command:
        try:
            con = sqlite3.connect(db_name+".db")
            sql_query = command
            cursor = con.cursor()
            cursor.execute(sql_query)
            p = cursor.fetchall()
            temp["status"] = str(p)
            con.commit()
        except Exception as e:
            temp["err"] = str(e)
            temp["status"] = "err"
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
    temp["db_name"] = db_name
    temp["table_name"] = table_name
    if db_name != None and table_name != None:
        try:
            con = sqlite3.connect(db_name+".db")
            sql_query = "SELECT * FROM "+table_name
            cursor = con.cursor()
            cursor.execute(sql_query)
            p = cursor.fetchall()
            temp["values"] = p
            temp["column_names"] = list(map(lambda x: {"name":x[0]}, cursor.description))
            temp["status"] = "OK"
        except Exception as e:
            temp["err"] = str(e)
            temp["status"] = "err"
        finally:
            if con != None:
                con.close()
    else:
        temp["status"] = "err"
        temp["err"] = "name not provided"
    return json.dumps(temp)

    