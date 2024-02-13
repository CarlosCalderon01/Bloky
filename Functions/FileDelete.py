import os


def MethodFileDelete(nameFile):
    if os.path.exists(nameFile):
        os.remove(nameFile)
        # print(f'arhivi {nameFile} ha sido borrado.')
    else:
        # print(f'archivo {nameFile} no existe.')
        return
