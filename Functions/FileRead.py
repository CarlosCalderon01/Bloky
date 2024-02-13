def MethodFileRead(nameFile):
    with open(nameFile, 'r') as file:
        contenido = file.read()
    # print(contenido)
    return contenido
