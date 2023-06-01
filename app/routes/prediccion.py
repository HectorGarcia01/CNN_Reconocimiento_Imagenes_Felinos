from flask import Blueprint #Para poder crear secciones dentro de la aplicación
from flask import render_template #Para renderizar vistas

#Creamos la sección para las rutas de usuarios
rutas_prediccion = Blueprint('prediccion', __name__)

#Configuramos la ruta para la predicción
@rutas_prediccion.route('/prediccion/felinos')
def prediccion():
    #Renderizamos el template predicción
    return render_template('prediccion.html')