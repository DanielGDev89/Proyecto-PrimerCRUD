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

def eliminar_contacto():
    nombre = input('Ingrese el nombre del contacto a eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)                     #trata de eliminar el archivo
        print('\r\n Contacto eliminado correctamente')

    except expression as identifier:
        print('El contacto no existe')

    app_principal()

def Buscar_contacto():
    nombre = input('Ingrese el nombre del contacto: \r\n')
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:            #trata de abrir el archivo
            print('\r\n Informacion del contacto: \r\n')
            for linea in contacto:

                print(linea.rstrip())

            print('\r\n')
    
    except IOError:                                                     #si el archivo no existe o da error imprime mensaje
        print('el archivo no existe')

    app_principal()

def mostrar_contacto():
    archivos = os.listdir(CARPETA)          #accedemos a contactos y listamos lo que hay dentro

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]               #validar que solo archivos .txt sean listados
    
    for archivo in archivos_txt:                                        #recorremos y abrimos los archivos
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:                                      #recorrer cada linea del archivo a imprimir
                print(linea.rstrip())                                   # imprimir y eliminar saltos de lineas
        
            print('\r\n')

  

    app_principal()

