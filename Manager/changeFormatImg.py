# pip install Pillow
import os
from PIL import Image
import time  # Importar el módulo time

def convertir_y_borrar_con_retraso(ruta_carpeta, retraso_segundos):
    for ruta_principal, carpetas, archivos in os.walk(ruta_carpeta):
        for nombre_archivo in archivos:
            # Verificar si el archivo es una imagen y no es JPEG
            if nombre_archivo.lower().endswith(('.jpg', '.png', '.bmp', '.webp')) and not nombre_archivo.lower().endswith(('.jpeg', '.gif')):
                ruta_archivo = os.path.join(ruta_principal, nombre_archivo)

                try:
                    # Intentar abrir la imagen
                    imagen = Image.open(ruta_archivo)

                    # Obtener el nombre del archivo sin extensión
                    nombre_sin_extension, _ = os.path.splitext(nombre_archivo)

                    # Convertir la imagen al modo RGB
                    imagen = imagen.convert('RGB')

                    # Crear nueva ruta con extensión JPEG
                    nueva_ruta_archivo = os.path.join(ruta_principal, f"{nombre_sin_extension}.jpeg")

                    # Guardar la imagen en formato JPEG
                    imagen.save(nueva_ruta_archivo, "JPEG")
                    
                    # Mostrar mensaje indicando el cambio de formato
                    #print(f"Convertido: {nombre_archivo} a {nombre_sin_extension}.jpeg")

                    # Borrar el archivo original
                    os.remove(ruta_archivo)
                    #print(f"Borrado: {nombre_archivo}")

                except Exception as e:
                    # Imprimir un mensaje si no se puede abrir la imagen
                    print(f"Error al abrir la imagen {nombre_archivo}: {e}")

                # Agregar retraso entre iteraciones
                time.sleep(retraso_segundos)

# Ruta del directorio que contiene las imágenes
ruta_carpeta_imagenes = "D:\\SubCarpetas"

retraso_segundos = 0.2

# Llamar a la función principal con retraso entre iteraciones
convertir_y_borrar_con_retraso(ruta_carpeta_imagenes, retraso_segundos)
