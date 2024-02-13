import magic


def MethodFileDetect(FilePath):
    detector = magic.Magic()

    try:
        formato = detector.from_file(FilePath)
        print(f'El formato del archivo {FilePath} es: {formato}')
    except FileNotFoundError:
        print(f'El archivo {FilePath} no fue encontrado.')
    except magic.MagicException as e:
        print(f'Ocurrió un error al detectar el formato: {e}')
