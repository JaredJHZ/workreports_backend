import psycopg2
def errorHandling(code, error):
    print(error)
    if code == "23505":
        return "Error, existe un campo en uso!"+"--DETALLE--"+error.pgerror