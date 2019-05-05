import psycopg2
import os


def conection():
    # Conexion de localhost
    dbname = 'wr'
    user = 'jaredhz'
    #host = 'workreports.cm9qevhwerud.eu-central-1.rds.amazonaws.com'
    host = '127.0.0.1'
    #password = 'asdqwe123'
    password = 'Atleti123@'

    
    conection =  psycopg2.connect(f"dbname={dbname}\
                 user={user} host={host} password={password}")

    return conection
