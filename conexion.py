#MODULO PARA IMPORTAR MYSQL INICIAR SIEMPRE SERVICIOS 

import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  #datos de workbench
            password="root",  
            database="gestion_cursos"
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None
