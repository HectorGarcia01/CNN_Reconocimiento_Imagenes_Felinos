from flask import request, redirect, session
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
            #Creamos una sesión con el id del usuario
            session['id_usuario'] = usuario.id

            #Redireccionamos a la ruta para la predicción
            return redirect('/prediccion/felinos')
        else:
            #Redireccionamos al mismo login
            return redirect('/login')
    except Exception as e:
        #Redireccionamos al mismo login
        return redirect('/login')
    
#Definimos una función para verificar la sesión del usuario
def verificar_sesion():
    if not 'id_usuario' in session:
        return redirect('/login')
    
    #Redireccionamos a la ruta para ver el perfil
    return redirect('/usuario/perfil')

#Definimos una función para cerrar la sesión del usuario
def logout_usuario():
    #Borramos la sesión
    session.pop('id_usuario', None)

    #Redireccionamos a la ruta para cerrar sesión
    return redirect('/login')