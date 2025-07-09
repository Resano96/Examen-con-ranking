from colorama import Fore, Style

def imprimir(mensaje, color=None):
    if color != None:
        print(color + mensaje + Style.RESET_ALL)
        return
    print(mensaje)

def imprimirConMarco(mensaje, color=None):


    frases = mensaje.split("\n")
    long_frases = [len(frase) for frase in frases]
    long_max = max(long_frases)
    rayita = "-" * (long_max + 3)
    imprimir(rayita,color)
    for frase in frases:
        long_max= max(long_frases)
        if long_max == len(frase):
            imprimir(f"|{frase} |",color)
        elif ((long_max - len(frase))%2==0):
            espacio = int(((long_max - len(frase))/2))
            imprimir(f"|{" "*espacio}{frase}{" "*espacio} |",color)
        elif ((long_max - len(frase))%2==1):
            long_max = long_max-1
            espacio_adelante = int((long_max - len(frase))/2)
            espacio_detras = int(((long_max - len(frase))/2)+1)
            imprimir(f"|{" "*espacio_adelante}{frase}{" "*espacio_detras} |",color)
        else:
            print("No hay else que valga, o es la mas larga, o la longitud es par o es impar")
    imprimir(rayita,color)
