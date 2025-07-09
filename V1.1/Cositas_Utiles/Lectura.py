from .Escritura import imprimir
from Cositas_Utiles.Colores import colores_mensajes as c


def leer_entero(mensaje, color= None):
    try :
        imprimir(mensaje,color)
        entero = int(input())
    except:
        raise  ValueError("Te he pedido un numero entero ")

    return entero

def leer_letra(mensaje,color = None):
    imprimir(mensaje, color)
    texto = input()
    if len(texto)!=1:
        imprimir("Respuesta no valida",c["Error"])
        pass

    return texto



def leer_string(mensaje, color = None):
    imprimir(mensaje,color)
    texto = input()
    return texto


