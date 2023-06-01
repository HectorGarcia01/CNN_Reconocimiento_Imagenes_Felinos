from main import app                #Cargamos el archivo main que posee la configuración de la aplicación
from db.conexionBD import db        #Cargamos la instancia db

#Para que cree todas las tablas que hemos definido en los modelos
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    #Inicializamos el servidor web
    app.run(debug=True)
