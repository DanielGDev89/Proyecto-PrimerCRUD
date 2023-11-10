import os

CARPETA = 'Contactos/' # carpeta de contactos
EXTENSION = '.txt'     # extension de archivos

class Contacto:                  #estructura de contacto
    def __init__(self, nombre, telefono, profesion):
        self.nombre = nombre
        self.telefono = telefono
        self.profesion = profesion


def app_principal():
    
    crear_directorio()

    mostrar_menu()

    preguntar = True
    while preguntar:
        opcion = input ('Seleccione una opcion: \r\n')
        opcion = int(opcion)

        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contacto()
            preguntar = False
        elif opcion == 4:
            Buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no valida, intente de nuevo')
