# Proyecto de Preguntas y Respuestas con Flask

Este es un proyecto desarrollado en **Python** utilizando el framework **Flask**.  
La aplicación permite realizar tests de preguntas, registrar puntuaciones en un ranking y gestionar (añadir y eliminar) preguntas desde la interfaz.

---

## Funcionalidades

-  Realizar un test de preguntas con opción de dejar respuestas en blanco.  
-  Registro de usuario al iniciar el test.  
-  Ranking con nota, preguntas acertadas, falladas y no contestadas.  
-  Listado completo de preguntas.  
-  Añadir nuevas preguntas desde un formulario.  
-  Eliminar preguntas existentes.  
-  Página de inicio y contacto.  
-  Manejo de errores con página personalizada.

---

## Estructura del proyecto

    ├── app.py # Archivo principal Flask
    ├── /templates # Archivos HTML (Jinja2)
    │ ├── index.html
    │ ├── pregunta.html
    │ ├── pregunta_nombre.html
    │ ├── resultado.html
    │ ├── ranking.html
    │ ├── preguntas2.html
    │ ├── contacto.html
    │ ├── formulario_pregunta.html
    │ ├── eliminar_pregunta.html
    │ └── layout.html
    ├── /data
    │ ├── preguntas.json
    │ ├── ranking.json
    ├── requirements.txt
    ├── README.md
    └── .gitignore

---

## ️ Instalación y uso

### 1. Clonar el repositorio

    git clone <URL-del-repo>
    cd <nombre-del-proyecto>

### 2. Crear entorno virtual (recomendado)

    python -m venv env

### 2.1. Activar el entorno:

Linux/Mac:

    source env/bin/activate

Windows:

    .\env\Scripts\activate

### 3. Instalar dependencias

    pip install -r requirements.txt

### 4. Ejecutar la aplicación

    python app.py

### 5. Abrir la aplicación en el navegador
Cuando ejecutes el comando anterior, Flask mostrará algo como:

    Running on http://127.0.0.1:5000 (Press CTRL+C to quit)

Solo tienes que abrir tu navegador y entrar en http://127.0.0.1:5000.

Desde ahí podrás navegar:

Página principal → /

Iniciar test → /test

Ranking → /ranking

Listado de preguntas → /preguntas_completas

Añadir pregunta → /añadir_pregunta

---

## Tecnologías utilizadas
* Python 3

* Flask

* Jinja2

* HTML / CSS (para las plantillas)

* Archivos JSON como base de datos

---

## Autor

Ander Resano Farelo

Proyecto realizado como práctica para clase utilizando Flask y archivos JSON.