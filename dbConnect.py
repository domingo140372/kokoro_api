#__date__ = 2022-02-01
#!/usr/bin/python3.8
'''
    Cretated by Domingo Utrera 
    Data Base connection to parameters data to connect siigo_api
    these parameters should be changed 
    the database is in postgreSql
'''

import sys
#import psycopg2 as pg
#import pymysql as mys
from config import *

def connect(type_con):
    global connection
    
    if type_con == 'postgres':
        import psycopg2 as db
        user = USER_POSTGRES
        port = PORT_POSTGRES
    
    elif type_con == 'mysql':
        import pymysql as db
        user = USER_MYSQL
        port = PORT_MYSQL 

    config={
        'host': HOST,
        'port': port,
        'database': DATA_BASE,
        'user': user,
        'password': PASSWORD
    }
    try:
        connection = db.connect(** config)
        
    except db.Error as  error:
        connection = None 
        print(error)
        sys.exit(1)
    
    return connection

if __name__ == "__main__":
    connect('mysql')
    print("me conecte bien")