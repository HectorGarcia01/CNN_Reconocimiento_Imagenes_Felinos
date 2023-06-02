from flask import Blueprint, render_template, redirect, request
from models.usuario import Usuario      #Cargamos la clase Usuario
from main import db                     #Cargamos la instancia db

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
    #Obtenemos los datos del formulario
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    direccion = request.form['direccion']
    correo = request.form['correo']
    password = request.form['password']

    #Instanciamos la clase Usuario para crear uno nuevo objeto
    nuevo_usuario = Usuario(nombre, apellido, direccion, correo, password)

    #Guardamos el nuevo usuario
    db.session.add(nuevo_usuario)

    #Finalizamos la conexión para que guarde el nuevo usuario a la bd
    db.session.commit()

    #Redireccionamos a la ruta para el registro de usuario
    return redirect('/registro/usuario')