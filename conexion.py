import psycopg2
import os


def conection():
    # Conexion de localhost
    dbname = 'workreports'
    user = 'jaredhz'
    host = '127.0.0.1'
    password = 'Atleti123@'

    if 'RDS_HOSTNAME' in os.environ:
        dbname = os.environ['RDS_DB_NAME']
        print(dbname)
        user = os.environ['RDS_USERNAME']
        print(user)
        host = os.environ['RDS_HOSTNAME']
        print(host)
        password = os.environ['RDS_PASSWORD']
        print(password)
    
    conection =  psycopg2.connect(f"dbname={dbname}\
                 user={user} host={host} password={password}")

    return conection
