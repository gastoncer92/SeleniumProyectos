from conexion import *

def insertar_base_grupo(conn, grupo):
    '''
    Guarda un grupo a la base de datos
    :param conn: conexion a base de datos
    :param grupo: [prupoId,NombreGrupo,UrlGrupo,TipoGrupo,VolumenGrupo,ActividadGrupo,ActividadEstadistica]
    :return: no return
    '''
