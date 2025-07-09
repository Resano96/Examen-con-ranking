from Escritura import imprimir


def leer_entero(mensaje, color= None):
    try :
        imprimir(mensaje,color)
        entero = int(input())
    except:
        raise  ValueError("Te he pedido un numero entero ")

    return entero

def leer_letra(mensaje,color = None):
    if mensaje.length!=1:
        imprimir("Respuesta no valida",color)



def leer_string(mensaje, color = None):
    imprimir(mensaje,color)
    texto = input()
    return texto


