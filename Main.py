#### MENÚ ###
#1 - Empezar cuestionario
#2 - Ranking (opcional)
#3 - Salir
#Hay que crear una aplicacion por consola en py en la que se puedan realizar cuestionarios tipo test.
# El usuario responde a las preguntas y al final se corrigen y dan una nota




#Aqui esta el menu inicial
def Menu():
    nombre = PreguntarNombre()
    while True:
        print(
                "···· MENÚ ···· \n"
                "1 - Empezar cuestionario \n"
                "2 - Ranking\n"
                "3 - Gestionar Preguntas (pass: Admin)\n"
                "4 - Salir")
        opcion = input()
        if opcion == "1":
            print(
                "Esto es un cuestionario tipo test, para responder usa la letra que corresponda,"
                " cualquier otro valor contara como no contestada")
            maxPreguntas = int(input("Cuantas preguntas quieres hacer?"))
            contador = 0
            nota=0
            aciertos= 0
            fallos = 0
            omitidas = 0
            while contador<maxPreguntas:
                pregunta = ASKer(preguntas)
                if pregunta==True: aciertos += 1
                elif pregunta== False: fallos +=1
                else: omitidas +=1
                nota += SumarPuntos(pregunta)
                contador+=1
            nota = (nota*10/maxPreguntas)
            nota =round(nota,2)
            print(f"Tan tan tan....... {nombre}\n"
                  f"Has respondido un total de {contador} preguntas, de las cuales: \n"
                  f"Aciertos: {aciertos}\n"
                  f"Fallos: {fallos}\n"
                  f"Omitidas: {omitidas}")
            print(f"Tu nota es de {nota}")
            notaAciertos = [nota,aciertos]
            ranking[nombre]=notaAciertos

        elif opcion == "2":
            rankingOrdenado = dict(sorted(ranking.items(),key=lambda item: item[1], reverse=True))
            print("NOMBRE\t\tNOTA\tACIERTOS")
            for posicion in rankingOrdenado:
                if len(posicion)<3:
                    print(f"{posicion}\t\t\t {rankingOrdenado[posicion][0]} \t\t{rankingOrdenado[posicion][1]}")
                elif len(posicion)>8:
                    print(f"{posicion}\t {rankingOrdenado[posicion][0]} \t\t{rankingOrdenado[posicion][1]}")
                else:
                    print(f"{posicion}\t\t {rankingOrdenado[posicion][0]} \t\t{rankingOrdenado[posicion][1]}")

        elif opcion == "3":
            Login()
        elif opcion == "4":
            break

#Aqui añadimos mas preguntas al test
def AñadirPreguntas(Diccionario):
    while True:
        pregunta = input("Dime la pregunta (0 para salir)")
        if pregunta == "0":
            print(Diccionario)
            break

        respuestas = input("Dime las respuestas separadas por un -").split("-")
        verdadera= input("Cual de las respuestas es la verdadera? (A,B,C,D)")

        verificacion = input("Esta pregunta corresponde a esta respuesta?\n"
                             f"{pregunta}\n"
                             f"{respuestas}\n"
                             f"La correcta es la {verdadera}"
                             " (N para cancelar)")

        if verificacion.lower() != "n":
            verdadera.upper()
            respuestas.append(verdadera)
            Diccionario[pregunta]= respuestas

#Aqui esta el login para añadir preguntas
def Login():
    password = input("Dime la pass")
    if password == "Admin":
        AñadirPreguntas(preguntas)
    else: print("Usuario no valido")
#Si pasa añadimos pregunta, si no vuelve al menu

def PreguntarNombre():
    nombre = input("Hola, esto es un programa que realiza preguntas, como te llamas?")
    return nombre

#Aqui esta el preguntaPreguntas
def ASKer(ListadoDePreguntas):
    import random
    preguntaAleatoria = random.choice(list(ListadoDePreguntas.keys()))
    respuestasConSolucion = ListadoDePreguntas[preguntaAleatoria]
    print(preguntaAleatoria)
    respuestas = respuestasConSolucion[:-1]
    respuesta = input(f"{respuestas}")
    acertada = True
    if respuesta.upper() != respuestasConSolucion[-1] and respuesta.upper() in opciones:
        acertada = False
        print("Respuesta erronea")
    elif respuesta.upper() == respuestasConSolucion[-1]:
        print("Respuesta correcta")
    else:
        acertada = 2
        print("Respuesta omitida")
    return acertada
#Devolvemos verdadero o falso dependiendo de si ha acertado

#Funcion para sumar puntos a la nota
def SumarPuntos(boleano):
    if boleano == True:
        valor =1
    elif boleano == False:
        valor =-(1/3)
    elif boleano == 2:
        valor = 0
    return valor
#Devuelve cuantos puntos suma cada pregunta

#Cositas que son necesarias
preguntas = { #Diccionario preguntas y respuestas
    "Pregunta1": ["Respuesta1", "Respuesta2", "Respuesta3", "Respuesta4", "A"],
    "Pregunta2": ["Respuesta1", "Respuesta2", "Respuesta3", "Respuesta4", "B"],
    "Pregunta3": ["Respuesta1", "Respuesta2", "Respuesta3", "Respuesta4", "C"],
}
opciones = ["A", "B", "C", "D"]
ranking ={"ander":[9.1,10],
          "josune":[10.0,6]}


Menu()
