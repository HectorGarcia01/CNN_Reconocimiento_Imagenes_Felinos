from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

#Creamos una instancia de Flask y definimos la ruta static
app = Flask(__name__, static_url_path='/static')

#Cargamos las configuraciones de la bd
app.config.from_pyfile('./config/config.py')

#Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{app.config['DB_USER']}:{app.config['DB_PASSWORD']}@{app.config['DB_HOST']}/{app.config['DB_NAME']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Creamos una instancia de SQLAlchemy
db = SQLAlchemy(app)

#Importamos los modelos
from models.usuario import Usuario
from models.prediccion import Prediccion

#Configuramos la ruta raíz para redirigir al login
@app.route('/')
def root():
    return redirect('/login')

#Configuramos la ruta para el login
@app.route('/login')
def login():
    #Renderizamos el template login
    return render_template('login.html')

#Configuramos la ruta para el registro de usuarios
@app.route('/registro/usuario')
def registro():
    #Renderizamos el template registro
    return render_template('registro.html')

#Configuramos la ruta para la predicción
@app.route('/usuario/prediccion/felinos')
def prediccion():
    #Renderizamos el template predicción
    return render_template('prediccion.html')

if __name__ == '__main__':
    #Inicializamos el servidor web
    app.run()
