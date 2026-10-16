import MySQLdb
from MySQLdb.connections import Connection

DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = ""
DB_NAME = "clinica_db"

class Conexion:
    __instancia = None
    __conexion = None

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super(Conexion, cls).__new__(cls)
        return cls.__instancia

    def __init__(self):
        if self.__conexion is None:
            self.__conexion = MySQLdb.connect(
                host=DB_HOST,
                user=DB_USER,
                passwd=DB_PASS,
                db=DB_NAME
            )

    def obtener_conexion(self) -> Connection:
        return self.__conexion


db1 = Conexion()
conn1 = db1.obtener_conexion()
db2 = Conexion()
conn2 = db2.obtener_conexion()

print(conn1 is conn2)
