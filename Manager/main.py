import os


def cambiar_nombres_carpeta(ruta_carpeta, nuevo_nombre):
    lista_archivos = os.listdir(ruta_carpeta)

    for nombre_archivo in lista_archivos:
        ruta_antiguo = os.path.join(ruta_carpeta, nombre_archivo)
        nombre_nuevo = nuevo_nombre + '_' + nombre_archivo
        ruta_nuevo = os.path.join(ruta_carpeta, nombre_nuevo)

        os.rename(ruta_antiguo, ruta_nuevo)

        print(f"Renombrado: {nombre_archivo} a {nombre_nuevo}")


ruta_carpeta = "ruta_path"
nuevo_nombre = "newname"


cambiar_nombres_carpeta(ruta_carpeta, nuevo_nombre)
