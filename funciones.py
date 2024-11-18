from conexion import conectar #Importo misql
import datetime #libreria para fechas de python 


def ingresar_alumno():
    conexion = conectar() #llamo a la funcion de mysql
    if conexion:
        cursor = conexion.cursor()
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        documento = input("Documento: ")
        fecha_nacimiento = input("Ingresa la fecha de nacimiento (DIA-MES-AÑO): ")
        try:
         fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d-%m-%Y").strftime("%Y-%m-%d")
         #toma una fecha dd-mm-yyyy la convierte en un objeto de fecha, luego la vuelve a convertir en una cadena de texto forma yyyy-mm-dd
        except ValueError:
                 print("Formato de fecha incorrecto")        
        telefono = input("Teléfono: ")
        domicilio = input("Domicilio: ")

        cursor.execute( #c concursor me vinculo con la bd
            "INSERT INTO alumnos (nombre, apellido, documento, fecha_nacimiento, telefono, domicilio) VALUES (%s, %s, %s, %s, %s, %s)",
            (nombre, apellido, documento, fecha_nacimiento, telefono, domicilio)
        )
        conexion.commit()
        print("Alumno ingresado correctamente.")
        cursor.close()
        conexion.close()

def mostrar_alumnos():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM alumnos")
        alumnos = cursor.fetchall()
        for alumno in alumnos:
            print(alumno)
        cursor.close()
        conexion.close()

def eliminar_alumno():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        id_alumno = input("ID del alumno a eliminar: ")
        cursor.execute("DELETE FROM alumnos WHERE id = %s", (id_alumno,))
        conexion.commit()
        print("Alumno eliminado.")
        cursor.close()
        conexion.close()

def actualizar_alumno():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        id_alumno = input("ID del alumno a actualizar: ")
        nombre = input("Nuevo nombre (o dejar vacío): ")
        apellido = input("Nuevo apellido (o dejar vacío): ")
        documento = input("Nuevo documento (o dejar vacío): ")
        fecha_nacimiento = input("Nueva fecha de nacimiento (YYYY-MM-DD, o dejar vacío): ")
        telefono = input("Nuevo teléfono (o dejar vacío): ")
        domicilio = input("Nuevo domicilio (o dejar vacío): ")

        campos = []
        valores = []

        if nombre:
            campos.append("nombre = %s")
            valores.append(nombre)
        if apellido:
            campos.append("apellido = %s")
            valores.append(apellido)
        if documento:
            campos.append("documento = %s")
            valores.append(documento)
        if fecha_nacimiento:
            campos.append("fecha_nacimiento = %s")
            valores.append(fecha_nacimiento)
        if telefono:
            campos.append("telefono = %s")
            valores.append(telefono)
        if domicilio:
            campos.append("domicilio = %s")
            valores.append(domicilio)

        if campos:
            valores.append(id_alumno)
            cursor.execute(f"UPDATE alumnos SET {', '.join(campos)} WHERE id = %s", valores)
            conexion.commit()
            print("Alumno actualizado correctamente.")
        else:
            print("No se actualizó ningún campo.")

        cursor.close()
        conexion.close()




# CURSOS

def agregar_curso():
  conexion = conectar()
  if conexion:
    cursor = conexion.cursor()    
    nombre = input("Nombre del curso: ")
    descripcion = input("Descripción del curso: ")
    duracion = input("Duración del curso (en semanas): ")

    cursor.execute(
        "INSERT INTO cursos (nombre_curso, descripcion, duracion) VALUES (%s, %s, %s)",
        (nombre, descripcion, duracion)
    )
    conexion.commit()  # Guardar los cambios
    print("Curso agregado con éxito.")


def mostrar_cursos():
  conexion = conectar()
  if conexion:
    cursor = conexion.cursor()    
    cursor.execute("SELECT * FROM cursos")
    cursos = cursor.fetchall()
    
    for curso in cursos:
        print(f"ID: {curso[0]}, Nombre: {curso[1]}, Descripción: {curso[2]}, Duración: {curso[3]} semanas")


#INSCRIBIR 
def inscribir_alumno():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        # consulta para obtener solo ID y nombre de los alumnos
        cursor.execute("SELECT id, nombre FROM alumnos") #ESPECIFICAM ID Y NOMBRE 
        alumnos = cursor.fetchall() #fetchall obtiene todas las filas de la consulta y las guarda en una lista
        if alumnos:
            print("Alumnos disponibles para inscribir:")
            for alumno in alumnos: #recorro la lista creada por fetchall
                print(f"ID: {alumno[0]}, Nombre: {alumno[1]}")
        else:
            print("No hay alumnos registrados.")
            return  # Si no hay alumnos, terminamos la función
   
         #mostrar los cursos disponibles
        cursor.execute("SELECT id, nombre_curso FROM cursos") #ESPECIFICAM ID Y NOMBRE 
        cursos = cursor.fetchall() #fetchall obtiene todas las filas de la consulta y las guarda en una lista

        # Mostrar solo el ID y nombre de los cursos cargados
        if cursos:
            print("Cursos disponibles :")
            for curso in cursos: #recorro la lista creada por fetchall
                print(f"ID: {curso[0]}, Nombre: {curso[1]}")
        else:
            print("No hay cursos registrados.")
            return 
        
        
        
        # Solicitar ID del alumno y curso
        alumno_id = int(input("ID del alumno: "))
        curso_id = int(input("ID del curso: "))
         # Obtener la fecha actual en formato para eviotar errores
        fecha_inscripcion = datetime.date.today()
        # Insertar inscripción en la tabla 'inscripciones'
        cursor.execute(
            "INSERT INTO inscripciones (alumno_id, curso_id, fecha_inscripcion) VALUES (%s, %s, %s)",
            (alumno_id, curso_id, fecha_inscripcion)
        )
        conexion.commit()
        print("Alumno inscripto.")
        
