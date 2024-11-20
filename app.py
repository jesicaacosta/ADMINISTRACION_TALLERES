from funciones import ingresar_alumno, mostrar_alumnos, eliminar_alumno, actualizar_alumno,inscribir_alumno,agregar_curso, mostrar_cursos


def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1: Ingresar nuevo alumno")
        print("2: Mostrar alumnos")
        print("3: Actualizar alumno")
        print("4: Inscribir alumno existente a un curso")
        print("5. Eliminar alumno del registro")
        print("6: Agregar curso" )
        print("7: Mostrar cursos disponibles")
        print("8 para salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            ingresar_alumno()
        elif opcion == "2":
            mostrar_alumnos()
        elif opcion == "3":
            actualizar_alumno()
        elif opcion == "4":
            inscribir_alumno()
        elif opcion == "5":
            eliminar_alumno()
        elif opcion == "6":
            agregar_curso()
        elif opcion == "7":
            mostrar_cursos()
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")


print("antes del if!")
    
if __name__ == "__main__": 
         #se ejecuta solo si el archivo se ejecuta directamente, no al importarse desde otro archivo.
    menu()
    print("dentro del if")

print("fuera del if")


