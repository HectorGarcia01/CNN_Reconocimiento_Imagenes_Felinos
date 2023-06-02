from flask import Blueprint, render_template 

#Creamos la sección para las rutas de predicción
rutas_prediccion = Blueprint('prediccion', __name__)

#Configuramos la ruta para la predicción
@rutas_prediccion.route('/prediccion/felinos')
def prediccion():
    #Renderizamos el template predicción
    return render_template('prediccion.html')