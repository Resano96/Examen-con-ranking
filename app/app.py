from flask import Flask, render_template, request, url_for, redirect, session
import json
import os

app = Flask(__name__)
app.secret_key = 'Ander'

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#CONFIG

DATA_DIR = os.path.join(app.root_path, 'data')
PREGUNTAS_PATH = os.path.join(DATA_DIR, 'preguntas.json')
RANKING_PATH   = os.path.join(DATA_DIR, 'ranking.json')

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#CARGAR JSON

def cargar_datos1(ruta):
    with open(ruta, encoding='utf-8') as contenido:
        datos_raw = json.load(contenido)
    listado = []
    for _, valores in datos_raw.items():
        listado.append({
            'nombre': valores[0],
            'nota': int(valores[1]),
            'acertadas': int(valores[2]),
            'falladas': int(valores[3]),
            'no_contestadas': int(valores[4])
        })
    return sorted(listado, key=lambda x: x['nota'], reverse=True)

def cargar_datos2(ruta):
    with open(ruta, encoding='utf-8') as contenido:
        datos_raw = json.load(contenido)
    listado_preguntas = []
    for pregunta, valores in datos_raw.items():
        listado_preguntas.append({
            'pregunta': pregunta,
            'respuestas': valores[:4],
            'correcta': valores[4],
        })
    return listado_preguntas

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#INDEX

@app.route('/')
def index():
    data = {'Titulo': 'Pagina de Preguntas'}
    return render_template('index.html', data=data)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#CONTACTO

@app.route('/contacto')
def contacto():
    data = {'titulo': 'Contacto', 'nombre': 'Ander'}
    return render_template('contacto.html', data=data)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#RANKING

@app.route('/ranking')
def ranking():
    listado_ranking = cargar_datos1(RANKING_PATH)
    data = {
        'Titulo': 'Ranking de Preguntas',
        'ranking': listado_ranking,
        'top_cuanto': len(listado_ranking),
        'top3': listado_ranking[:3]
    }
    return render_template('ranking.html', data=data)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#MOSTRAR PREGUNTAS

@app.route('/preguntas_completas')
def preguntas_completas():
    preguntas = cargar_datos2(PREGUNTAS_PATH)
    data = {'Titulo': 'Listado completo de preguntas', 'preguntas': preguntas}
    return render_template('preguntas2.html', data=data)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#AÑADIR PREGUNTAS

@app.route('/añadir_pregunta', methods=['GET'])
def formulario_nueva_pregunta():
    return render_template('formulario_pregunta.html')

@app.route('/guardar_pregunta', methods=['POST'])
def guardar_nueva_pregunta():
    with open(PREGUNTAS_PATH, 'r', encoding='utf-8') as f:
        preguntas = json.load(f)
    pregunta = request.form['pregunta']
    respuestas = [
        request.form['respuesta0'],
        request.form['respuesta1'],
        request.form['respuesta2'],
        request.form['respuesta3'],
    ]
    correcta = request.form['correcta']
    if pregunta in preguntas:
        return "Esa pregunta ya existe", 400
    preguntas[pregunta] = respuestas + [correcta]
    with open(PREGUNTAS_PATH, 'w', encoding='utf-8') as f:
        json.dump(preguntas, f, indent=4, ensure_ascii=False)
    return redirect(url_for('preguntas_completas'))

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#BORRAR PREGUNTAS

@app.route('/borrar_pregunta', methods=['GET'])
def mostrar_formulario_eliminar():
    preguntas = cargar_datos2(PREGUNTAS_PATH)
    data = {'Titulo': 'Eliminar una pregunta', 'preguntas': preguntas}
    return render_template('eliminar_pregunta.html', data=data)

@app.route('/eliminar_pregunta', methods=['POST'])
def eliminar_pregunta():
    pregunta_a_borrar = request.form['pregunta']
    with open(PREGUNTAS_PATH, 'r', encoding='utf-8') as f:
        preguntas = json.load(f)
    if pregunta_a_borrar in preguntas:
        del preguntas[pregunta_a_borrar]
        with open(PREGUNTAS_PATH, 'w', encoding='utf-8') as f:
            json.dump(preguntas, f, indent=4, ensure_ascii=False)
    return redirect(url_for('preguntas_completas'))

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#PREGUNTAS

@app.route('/test')
def iniciar_cuestionario():
    session.clear()
    preguntas = cargar_datos2(PREGUNTAS_PATH)


    session['preguntas'] = preguntas
    session['index'] = -1
    session['aciertos'] = 0
    session['fallos'] = 0
    session['no_contestadas'] = 0

    return redirect(url_for('mostrar_pregunta'))

@app.route('/pregunta')
def mostrar_pregunta():
    index = session.get('index', -1)
    preguntas = session.get('preguntas', [])

    if index == -1:
        pregunta = {
            'pregunta': "Hola, ¿cómo te llamas?",
            'respuestas': [],
            'correcta': None
        }
        return render_template('pregunta_nombre.html', pregunta=pregunta)

    if index >= len(preguntas):
        return redirect(url_for('mostrar_resultado'))

    pregunta = preguntas[index]
    return render_template('pregunta.html', pregunta=pregunta, index=index)

@app.route('/guardar_nombre', methods=['POST'])
def guardar_nombre():
    usuario = request.form.get('usuario', 'Anónimo')
    session['usuario'] = usuario
    session['index'] = 0
    return redirect(url_for('mostrar_pregunta'))

@app.route('/responder', methods=['POST'])
def responder():
    seleccion = request.form.get('respuesta')
    correcta = request.form.get('correcta')
    if seleccion is None:
        session['no_contestadas'] += 1
    elif seleccion == correcta:
        session['aciertos'] += 1
    else:
        session['fallos'] += 1
    session['index'] += 1
    return redirect(url_for('mostrar_pregunta'))

def actualizar_ranking(usuario, aciertos, total, no_contestadas=0):
    falladas = total - aciertos
    nota = int((aciertos / total) * 10) if total > 0 else 0

    # Intentar leer el ranking actual
    try:
        with open(RANKING_PATH, 'r', encoding='utf-8') as f:
            ranking = json.load(f)
    except FileNotFoundError:
        ranking = {}

    # Crear o actualizar la entrada
    ranking[usuario] = [
        usuario,
        nota,
        aciertos,
        falladas,
        no_contestadas
    ]

    # Guardar otra vez el archivo
    with open(RANKING_PATH, 'w', encoding='utf-8') as f:
        json.dump(ranking, f, indent=4, ensure_ascii=False)

@app.route('/resultado')
def mostrar_resultado():
    total = len(session.get('preguntas', []))
    aciertos = session.get('aciertos', 0)
    fallos = session.get('fallos', 0)
    no_contestadas = session.get('no_contestadas', 0)
    porcentaje = int((aciertos / total) * 100) if total > 0 else 0

    usuario = session.get('usuario', 'Anónimo')
    actualizar_ranking(usuario, aciertos, total, no_contestadas)

    return render_template('resultado.html',
                           total=total,
                           aciertos=aciertos,
                           fallos= fallos,
                           no_contestadas=no_contestadas,
                           porcentaje=porcentaje)

@app.route('/verificar', methods=['POST'])
def verificar():
    seleccion = int(request.form['respuesta'])
    correcta = int(request.form['correcta'])
    acierto = (seleccion == correcta)
    return render_template('resultado.html', acierto=acierto)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#OTROS

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    return "ok"

def pagina_no_encontrada(error):
    return redirect(url_for('index'))

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#MAIN

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)