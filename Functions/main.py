from FileCheck import MethodFileCheck
from FileCreate import MethodFileCreate
from FileDelete import MethodFileDelete
from FileRead import MethodFileRead
from FileWrite import MethodFileWrite
from FileDetect import MethodFileDetect

# Llama a la función MethodFileRead
nombre_archivo = "ArchiveNumber.txt"
message = "aposongo"
FilePath1 = 'C:\\Users\\carlo\\Documents\\dev\\Bloky\\Functions\\archivo_ejemplo.txt'

# contenido = MethodFileCheck(nombre_archivo) # Funciona
# contenido = MethodFileCreate(nombre_archivo) # Funciona
# contenido = MethodFileDelete(nombre_archivo) # Funciona
# contenido = MethodFileRead(nombre_archivo) # Funciona
# contenido = MethodFileWrite(nombre_archivo, message) # Funciona
contenido = MethodFileDetect(FilePath1)

print(contenido)
