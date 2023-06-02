from flask import request, redirect
from models.usuario import Usuario                              #Cargamos la clase Usuario

#Definimos la función para validar las credenciales del usuario
def validar_credenciales():
    try:
        #Obtenemos los datos del formulario
        correo = request.form['correo']
        password = request.form['password']

        #Buscamos el usuario en la bd por su correo
        usuario = Usuario.query.filter_by(correo=correo).first()

        #Validamos si las contraseñas coinciden
        if usuario and usuario.verificar_contraseña(password):
            #Redireccionamos a la ruta para la predicción
            return redirect('/prediccion/felinos')
        else:
            #Redireccionamos al mismo login
            return redirect('/login')
    except Exception as e:
        #Redireccionamos al mismo login
        return redirect('/login')