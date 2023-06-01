from db.conexionBD import db #Cargamos la instacia db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)        #Definimos el atributo id como llave primaria
    nombre = db.Column(db.String(30))                   #Definimos el atributo para el nombre del usuario
    apellido = db.Column(db.String(30))                 #Definimos el atributo para el apellido del usuario
    direccion = db.Column(db.String(50))               #Definimos el atributo para la dirección del usuario
    correo = db.Column(db.String(30), unique=True)     #Definimos el atributo para el correo del usuario y la establecemos como unica 
    password = db.Column(db.String(30))                #Definimos el atributo para la contraseña del usuario

    