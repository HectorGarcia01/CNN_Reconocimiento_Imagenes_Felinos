from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import *
from routes.usuario import rutas_usuario            #Cargamos las rutas del usuario
from routes.prediccion import rutas_prediccion      #Cargamos las rutas de las predicciones

#Creamos una instancia de Flask y definimos la ruta static
app = Flask(__name__)

#Configuramos la bd
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{USUARIO_BD}:{PASSWORD_BD}@{NOMBRE_HOST}/{NOMBRE_BD}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Pasamos la instancia de app a SQLAlchemy
SQLAlchemy(app)

#Agregamos las rutas del usuario a la aplicación
app.register_blueprint(rutas_usuario)

#Agregamos las rutas de las predicciones
app.register_blueprint(rutas_prediccion)
