from flask import Flask, render_template

# Inicializar la aplicacion
app = Flask(__name__, template_folder='templates')

# Ruta principal para el login
@app.route('/')
def login():
    return render_template('Login.html')

@app.route('/Registrarse')
def registro():
    return render_template('Registro.html')

@app.route('/Recuperar_Contraseña')
def recuperarCo():
    return render_template('RecuperarC.html')

@app.route('/Inicio')
def principal():
    return render_template('Principal.html')

@app.route('/Contacto')
def contactos():
    return render_template('Contactos.html')

# Para ejecutar la aplicacion
if __name__ == '__main__':
    app.run(debug=True)