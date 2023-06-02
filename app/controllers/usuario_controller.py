from flask import request, redirect
from models.usuario import Usuario                              #Cargamos la clase Usuario
from main import db                                             #Cargamos la instancia db

#Definimmos la función para guardar los datos en la bd
def guardar_usuario():
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
