from flask import Flask, render_template

#Creamos una instancia de Flask y definimos la ruta static
app = Flask(__name__, static_url_path='/static')

#Configuramos la ruta para el login
@app.route('/login')
def login():
    #Renderizamos el template login
    return render_template('login.html')

#Configuramos la ruta para el registro de usuarios
@app.route('/registro/usuario')
def registro():
    #Renderizamos el template registro
    return render_template('registro.html')

#Configuramos la ruta para la predicción
@app.route('/usuario/prediccion')
def prediccion():
    #Renderizamos el template predicción
    return render_template('prediccion.html')

if __name__ == '__main__':
    #Inicializamos el servidor web
    app.run()
