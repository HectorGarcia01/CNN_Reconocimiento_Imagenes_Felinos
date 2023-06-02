from main import db #Cargamos la instacia db

class Prediccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)                                #Definimos el atributo id como llave primaria
    porcentaje_leon = db.Column(db.String(20))                                  #Definimos el atributo para la predicción de leon
    porcentaje_gato = db.Column(db.String(20))                                  #Definimos el atributo para el predicción de gato
    porcentaje_tigre = db.Column(db.String(20))                                 #Definimos el atributo para la predicción de tigre
    porcentaje_pantera= db.Column(db.String(20))                                #Definimos el atributo para el predicción de pantera
    imagen_prediccion = db.Column(db.String(100))                               #Definimos el atributo para la imagen de la predicción
    id_usuario_fk = db.Column(db.Integer, db.ForeignKey('usuario.id'))          #Definimos el atributo para el id del usuario con llave foranea

    #Definimos el constructor para pasar los datos a la bd
    def __init__(self, porcentaje_leon, porcentaje_gato, porcentaje_tigre, porcentaje_pantera, imagen_prediccion, id_usuario_fk):
        self.porcentaje_leon = porcentaje_leon                                                        #Asignamos el valor proporcionado al atributo porcentaje_leon
        self.porcentaje_gato = porcentaje_gato                                                        #Asignamos el valor proporcionado al atributo porcentaje_gato
        self.porcentaje_tigre = porcentaje_tigre                                                      #Asignamos el valor proporcionado al atributo porcentaje_tigre
        self.porcentaje_pantera = porcentaje_pantera                                                  #Asignamos el valor proporcionado al atributo porcentaje_pantera
        self.porcentaje_pantera = imagen_prediccion                                                   #Asignamos el valor proporcionado al atributo imagen_prediccion
        self.porcentaje_pantera = id_usuario_fk                                                       #Asignamos el valor proporcionado al atributo id_usuario_fk