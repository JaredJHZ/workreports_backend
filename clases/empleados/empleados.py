import psycopg2
from conexion import conection

class empleados:

    def __init__(self,id,ap_paterno,ap_materno,nombres):
        self.id = id
        self.ap_paterno = ap_paterno
        self.ap_materno = ap_materno
        self.nombres = nombres

    def save(self):
        try:
            self.con = conection()
            self.cursor = self.con.cursor()
            query = f"INSERT INTO empleados.empleados(id, ap_paterno, ap_materno, nombre) VALUES('{self.id}','{self.ap_paterno}','{self.ap_materno}','{self.nombres}' ); "
            self.cursor.execute(query)
            self.con.commit()
            self.con.close()
            print("empleado guardados")
            return True
        except psycopg2.Error as e:
            return (False , e.pgcode, e)

def get_empleado(id):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"SELECT * FROM empleados.empleados WHERE id = '{id}' ;"
        cursor.execute(query)
        data = cursor.fetchone()
        cursor.close()
        con.close()
        id = data[0]
        nombre = data[1]
        ap_paterno = data[2]
        ap_materno = data[3]
        empleado = {
            "id":id,
            "nombre":nombre,
            "ap_paterno":ap_paterno,
            "ap_materno":ap_materno
        }
        return empleado
    except psycopg2.Error as e:
        return (False , e.pgcode, e)
    

def modificar_empleado(id, nombre, ap_paterno, ap_materno):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"UPDATE empleados.empleados SET nombre = '{nombre}', ap_paterno = '{ap_paterno}', ap_materno = '{ap_materno}' WHERE id = '{id}'"
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        return True
    except psycopg2.Error as e:
        return (False , e.pgcode, e)

def eliminar_empleado(id):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"DELETE FROM empleados.empleados WHERE id = '{id}';"
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        return True
    except psycopg2.Error as e:
        return (False , e.pgcode, e)

def get_all():
    try:
        con = conection()
        cursor = con.cursor()
        query = f"SELECT * FROM empleados.empleados;"
        cursor.execute(query)
        data = cursor.fetchall()
        employees = []
        for empleado in data:
            employee = {
                "id":empleado[0],
                "nombre":empleado[1],
                "ap_paterno":empleado[2],
                "ap_materno":empleado[3]
            }
            employees.append(employee)
        con.close()
        cursor.close()
        return employees
    except psycopg2.Error as e:
        return (False , e.pgcode, e)