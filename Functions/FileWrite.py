def MethodFileWrite(nameFile, message):
    with open(nameFile, 'w') as file:
        result = file.write(message)
        return
