import os


def MethodFileCreate(nameFile):
    with open(nameFile, 'w') as file:
        # file.write('new archivo')
        print("se creo el archivo"+{nameFile})
        return nameFile
