# -*- coding: utf-8 -*-
import sqlite3
from config import cfg

database = cfg.get('db','').get('db_path','')
# 建立数据库连接
def OpenDb():
    #database = "./resources/database/data.db"
    conn = sqlite3.connect(database)
    # conn.row_factory = sqlite3.Row
    return conn


## 创建表


def create_table(table_name):
    """
    创建一个名为 table_name 的 SQLite 表。
    如果表已存在，则不创建。
    """
    conn = OpenDb()
    cursor = conn.cursor()

    # 检查表是否存在
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
    if cursor.fetchone() is None:
        # 创建表
        cursor.execute(f"""
        CREATE TABLE {table_name} (
            sno INTEGER PRIMARY KEY  NOT NULL,
            name archar(50) NOT NULL,
            gender INTEGER  ,
            birthday char(2) ,
            major varchar(50) NOT NULL,
            password varchar(10),
            userprofile_url varchar(50)
        );
        """)
        conn.commit()
        print(f"Table {table_name} created successfully.")
    else:
        print(f"Table {table_name} already exists.")

    conn.close()


# 获取数据库连接
def GetSql(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    fields = []
    for field in cur.description:
        fields.append(field[0])

    result = cur.fetchall()
    # for item in result:
    #     print(item)
    cur.close()
    return result, fields


# 关闭数据库连接
def CloseDb(conn):
    conn.close()


# 获取数据库连接
def GetSql2(sql):
    conn = OpenDb()
    result, fields = GetSql(conn, sql)
    CloseDb(conn)
    return result, fields


# 改
def UpdateData(data, tablename):
    conn = OpenDb()
    values = []
    cursor = conn.cursor()
    idName1 = list(data)[0]
    idName2 = list(data)[1]
    for v in list(data)[2:]:
        values.append("%s='%s'" % (v, data[v]))
    sql = "update %s set %s where %s='%s' and %s='%s'" % (
    tablename, ",".join(values), idName1, data[idName1], idName2, data[idName2])
    # print (sql)
    cursor.execute(sql)
    conn.commit()
    CloseDb(conn)


# 增
def InsertData(data, tablename):
    conn = OpenDb()
    values = []
    cusor = conn.cursor()
    #print(data)
    fieldNames = list(data)
    #print(fieldNames)
    for v in fieldNames:
        values.append(data[v])
    sql = "insert into  %s (%s) values( %s) " % (tablename, ",".join(fieldNames), ",".join(["?"] * len(fieldNames)))
    # print(sql)
    cusor.execute(sql, values)
    conn.commit()
    CloseDb(conn)


# 删
def DelDataById(id1, id2, value1, value2, tablename):
    conn = OpenDb()
    # values = []
    cursor = conn.cursor()

    sql = "delete from %s  where %s=? and %s=?" % (tablename, id1, id2)
    # print (sql)

    cursor.execute(sql, (value1, value2))
    conn.commit()
    CloseDb(conn)

def alter_table(table_name,database):
    conn = OpenDb(database)
    new_table_name = table_name + '_new'
    cursor = conn.cursor()
    #columns = ', '.join(add_columns.keys())
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{new_table_name}';")
    if cursor.fetchone() is None:
        # 创建表
        cursor.execute(f"""
        CREATE TABLE {new_table_name} (
            sno INTEGER PRIMARY KEY  NOT NULL,
            name archar(50) NOT NULL,
            gender INTEGER  ,
            birthday char(2) ,
            major varchar(50) NOT NULL,
            password varchar(10),
            userprofile_url varchar(50)
        );
        """)
        conn.commit()
        print(f"Table {new_table_name} created successfully.")
    else:
        print(f"Table {new_table_name} already exists.")
        sql = f'DROP TABLE {new_table_name};'
        conn.execute(sql)
        cursor.execute(f"""
        CREATE TABLE {new_table_name} (
            sno INTEGER PRIMARY KEY  NOT NULL,
            name archar(50) NOT NULL,
            gender INTEGER  ,
            birthday char(2) ,
            major varchar(50) NOT NULL,
            password varchar(10),
            userprofile_url varchar(50)
        );
        """)
        conn.commit()
        print(f"Table {new_table_name} created successfully.")

    # 将旧表的数据复制到新表中
    sql = f'INSERT INTO {new_table_name} (sno,name,gender,birthday,major,password,userprofile_url) SELECT sno,name,gender,birthday,major,password,"" FROM {table_name};'
    #print(sql)
    conn.execute(sql)

    # 删除旧表
    sql = f'DROP TABLE {table_name};'
    conn.execute(sql)

    # 将新表重命名为旧表的名字
    sql = f'ALTER TABLE {new_table_name} RENAME TO {table_name};'
    conn.execute(sql)
    conn.commit()
    CloseDb(conn)


def show_table_scheam(db_obj,table_name):
    cursor = db_obj.cursor()

    # 查看特定表的结构
    #table_name = table_name
    cursor.execute(f"PRAGMA table_info({table_name})")

    # 获取表结构信息
    results = cursor.fetchall()
    for row in results:
        print(row)

    # 关闭连接
    db_obj.close()


if __name__ == '__main__':
    database='../resources/database/data.db'
    db=OpenDb(database)
    table_name='student'
    #table_name='teacher'
    #table_name='course'
    #table_name='score'
    #show_table_scheam(db,table_name)
    sqls="select * from student"
    #sqls = "select * from teacher"
    fileds,res=GetSql(db,sqls)
    print(fileds)
    print(res)
    #alter_table(table_name,database)
