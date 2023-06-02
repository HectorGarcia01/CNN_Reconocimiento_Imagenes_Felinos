from flask import Blueprint, render_template, redirect, request
from controllers.usuario_controller import guardar_usuario      #Cargamos la función guardar_usuario del controlador

#Creamos la sección para las rutas de usuarios
rutas_usuario = Blueprint('usuario', __name__)

#Configuramos la ruta raíz para redirigir al login
@rutas_usuario.route('/')
def root():
    return redirect('/login')

#Configuramos la ruta para el login
@rutas_usuario.route('/login')
def login():
    #Renderizamos el template login
    return render_template('login.html')

#Configuramos la ruta para el registro de usuarios
@rutas_usuario.route('/registro/usuario')
def registro():
    #Renderizamos el template registro
    return render_template('registro.html')

#Configuramos la ruta para guardar los datos del usuario
@rutas_usuario.route('/registro/nuevo_usuario', methods=['POST'])
def nuevo_usuario():
    return guardar_usuario()