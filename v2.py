


def Menu():
    nombre = input("Dime tu nombre")
    while True:
        print(
                "···· MENÚ ···· \n"
                "1 - Empezar cuestionario \n"
                "2 - Ranking\n"
                "3 - Gestionar Preguntas (pass: Admin)\n"
                "4 - Salir")
        opcion = input()
        if opcion == "1":
            #Cuestionario
            tema= input("sobre cual de los temas quieres las preguntas?\n"
                        "Tema1\n"
                        "Tema2\n"
                        "Tema3\n")
            if tema == "1"or tema.lower() == "tema1":

                resultado =preguntar_Preguntas(preguntas)
                aciertos_fallos_omitidas = resultado
                #[int, int , int]
                nota =  Calcular_puntos(aciertos_fallos_omitidas)
                #int
                print(f"Tu nota es de {nota}, \n"
                      f"has acertado {aciertos_fallos_omitidas[0]}, \n"
                      f"has fallado {aciertos_fallos_omitidas[1]}, \n"
                      f"has omitido {aciertos_fallos_omitidas[2]}")

            if tema == "2"or tema.lower() == "tema2":
                preguntar_Preguntas(preguntas)

            if tema == "3"or tema.lower() == "tema3":
                preguntar_Preguntas(preguntas)






        if opcion == "2":
            #Ranking
            print("2")
        if opcion == "3":
            #Gestionar preguntas
            print("3")
        if opcion == "4":
            break

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def preguntar_Preguntas(Base_de_preguntas):
    aciertos = 3
    fallos = 3
    omitidas = 0

    for pregunta in Base_de_preguntas:
        preg =print(pregunta)
        resp = print(Base_de_preguntas.get(pregunta))

        preg
        resp
    aciertos_fallos_omitidas= [aciertos, fallos, omitidas]
    return aciertos_fallos_omitidas
    # [int, int, int]
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def Calcular_puntos(Aciertos_fallos_omitidas):
    Aciertos_fallos_omitidas.split(",")
    acertadas = Aciertos_fallos_omitidas[0]
    fallos = Aciertos_fallos_omitidas[1]
    nota = (acertadas*1)+(fallos/3)

    return nota
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


preguntas = { #Diccionario preguntas y respuestas
    "Pregunta1": ["Respuesta1", "Respuesta2", "Respuesta3", "Respuesta4", "A"],
    "Pregunta2": ["Respuesta1", "Respuesta2", "Respuesta3", "Respuesta4", "B"],
    "Pregunta3": ["Respuesta1", "Respuesta2", "Respuesta3", "Respuesta4", "C"],
}