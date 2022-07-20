import sqlite3
from sqlite3 import Error

# base.py
def conexion():
    try:
        conn = sqlite3.connect('../database.db')
        return conn
    except Error:
        print("o rayos! :(")

def tabla_grupos(conn):
    '''
    crear tabla para los grupos de facebook
    :param conn: conexion a la base de datos
    :return: no return
    '''
    print("Creando base de datos para las ventas")
    cursor = conn.cursor()
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS [grupos] (
[prupoId] INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
[NombreGrupo] VARCHAR(50)  NULL,
[UrlGrupo] VARCHAR(50)  NULL,
[TipoGrupo] VARCHAR(50)  NULL,
[VolumenGrupo] VARCHAR(50)  NULL,
[ActividadGrupo] VARCHAR(50)  NULL,
[ActividadEstadistica] FLOAT  NULL
);
    """)
    conn.commit()

