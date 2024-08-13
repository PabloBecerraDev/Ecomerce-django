import random
import string
import os


def codeGenerator(size = 6, chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def obtener_contenido_variable(nombre_variable):
    try:
        contenido = os.environ[nombre_variable]
        return contenido
    except KeyError:
        return f"La variable de entorno '{nombre_variable}' no esta definida."
    


