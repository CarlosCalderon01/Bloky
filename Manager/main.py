import os


def cambiar_nombres_carpeta(ruta_carpeta):
    lista_archivos = os.listdir(ruta_carpeta)

    for contador, nombre_archivo in enumerate(lista_archivos, start=1):
        nombre, formato = os.path.splitext(nombre_archivo)

        ruta_antiguo = os.path.join(ruta_carpeta, nombre_archivo)
        nombre_nuevo = f"{formato[1:]}_{contador}{formato}"
        ruta_nuevo = os.path.join(ruta_carpeta, nombre_nuevo)

        os.rename(ruta_antiguo, ruta_nuevo)

        print(f"Renombrado: {nombre_archivo} a {nombre_nuevo}")


ruta_carpeta = "ruta_path"

cambiar_nombres_carpeta(ruta_carpeta)
