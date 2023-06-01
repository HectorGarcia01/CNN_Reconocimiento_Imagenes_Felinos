from main import app #Cargamos el archivo main que posee la configuración de la aplicación

if __name__ == '__main__':
    #Inicializamos el servidor web
    app.run(debug=True)
