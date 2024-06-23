from app.sql import SQL_Server

# host		IP地址
# user      用户名
# password  密码
# database  数据库名称

host='localhost'
user='postgres'
password='7'
database='hospital'
autocommit=True

def config():
    return SQL_Server(host, user, password, database, autocommit)
        
