import os


def MethodFileCheck(nameFile):
    if os.path.exists(nameFile):
        print(f'El archivo {nameFile} existe.')
    else:
        print(f'El archivo {nameFile} no existe.')
        return nameFile
