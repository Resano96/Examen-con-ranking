import random

from Cositas_Utiles.Colores import colores_mensajes as c
from Cositas_Utiles.Escritura import imprimir as imp
from Cositas_Utiles.Escritura import imprimirConMarco as impM
from Cositas_Utiles.Lectura import leer_letra, leer_string, leer_entero
import json




#def cargar_datos(ruta):
    #with open(ruta) as contenido:
#        preguntas =json.load(contenido)
#        return preguntas

if __name__=='__main__':
    ruta = 'Cositas_Utiles/preguntas.json'
  #  diccionario =cargar_datos(ruta)



preguntas=[]

for pregunta in diccionario: preguntas.append(pregunta)

def Cuestionario(i, defpreguntas):
    listado_preguntas = defpreguntas
    for j in range(i):
        preguntar(listado_preguntas)



##aqui necesito un numero de preguntas
def preguntar(listado):

    preg= random.choice(listado)
    imp(preg,c["Pregunta"])
#    listado.remove(preg)
    return listado

for i in range (3):

    preguntar(preguntas)
#Cuestionario(3,preguntas)


##def menu():
##    Nombre = preguntar_nombre()
##    while True:
##        impM(
##            "···· MENÚ ···· \n"
##            "1 - Empezar cuestionario \n"
##            "2 - Ranking\n"
##            "3 - Gestionar Preguntas (pass: Admin)\n"
##            "4 - Salir",c["Menu"])
##        leer_letra("Que opcion quieres usar?",c["Input"])
##        switch={
##            1:Cuestionario()
##            2:mostrar_ranking()
##            3:menu_preguntas()
##            4:  break

##        }



def preguntar_nombre():
    imp("Hola, soy un script que hace examenes con ranking",c["Print"])
    nombre = leer_string("Como te llamas?",c["Input"])
    return nombre




preguntar_nombre()
