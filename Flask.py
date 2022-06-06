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

# Para ejecutar la aplicacion
if __name__ == '__main__':
    app.run(debug=True)