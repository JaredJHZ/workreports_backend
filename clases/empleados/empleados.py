import psycopg2

class empleados:

    def __init__(self,id,ap_paterno,ap_materno,nombres,id_direccion):
        self.id = id
        self.ap_paterno = ap_paterno
        self.ap_materno = ap_materno
        self.nombres = nombres
        self.id_direccion = id_direccion

    def save(self):
        try:
            self.con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
            self.cursor = self.con.cursor()
            query = f"INSERT INTO empleados.empleados(id, ap_paterno, ap_materno, nombre, id_direccion) VALUES('{self.id}','{self.ap_paterno}','{self.ap_materno}','{self.nombres}','{self.id_direccion}' ); "
            self.cursor.execute(query)
            self.con.commit()
            self.con.close()
            print("empleado guardados")
            return True
        except psycopg2.OperationalError as e:
            print('Unable to connect!\n{0}').format(e)
            return False

def get_empleado(id):
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
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
        id_direccion = data[4]
        empleado = {
            "id":id,
            "nombre":nombre,
            "ap_paterno":ap_paterno,
            "ap_materno":ap_materno,
            "id_direccion":id_direccion
        }
        return empleado
    except:
        print("error al obtener empleado")
        return False
    

def modificar_empleado(id, nombre, ap_paterno, ap_materno, id_direccion):
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
        cursor = con.cursor()
        query = f"UPDATE empleados.empleados SET nombre = '{nombre}', ap_paterno = '{ap_paterno}', ap_materno = '{ap_materno}', id_direccion = '{id_direccion}' WHERE id = '{id}'"
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        return True
    except:
        print("error al modificar direccion")
        return False

def eliminar_empleado(id):
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
        cursor = con.cursor()
        query = f"DELETE FROM empleados.empleados WHERE id = '{id}';"
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        return True
    except:
        print("error al eliminar la empleados")
        return False

def get_all():
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
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
                "ap_materno":empleado[3],
                "id_direccion":empleado[4]
            }
            employees.append(employee)
        con.close()
        cursor.close()
        return employees
    except:
        print("error al obtener empleados")
        return False