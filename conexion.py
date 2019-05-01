import psycopg2
import os


def conection():
    # Conexion de localhost
    dbname = 'workreports'
    user = 'jaredhz'
    host = 'workreports.cm9qevhwerud.eu-central-1.rds.amazonaws.com'
    password = 'asdqwe123'

    
    conection =  psycopg2.connect(f"dbname={dbname}\
                 user={user} host={host} password={password}")

    return conection
