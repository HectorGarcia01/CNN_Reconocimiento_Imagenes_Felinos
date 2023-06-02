from flask import Blueprint, render_template 
from controllers.autenticacion_controller import verificar_sesion_pred           #Cargamos la función verificar_sesion_pred del controlador

#Creamos la sección para las rutas de predicción
rutas_prediccion = Blueprint('prediccion', __name__)

#Configuramos la ruta para la predicción
@rutas_prediccion.route('/prediccion/felinos')
def prediccion():
    #Retornamos la función verificar_sesion_pred
    return verificar_sesion_pred()