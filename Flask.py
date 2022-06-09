from flask import Flask, render_template

# Inicializar la aplicacion
app = Flask(__name__, template_folder='templates')

# Ruta principal para el login.
@app.route('/')
def login():
    return render_template('Login.html')
#Ruta para llamara a registro.
@app.route('/Registrarse')
def registro():
    return render_template('Registro.html')
#Ruta para llamara a recuperar contraseña.
@app.route('/Recuperar_Contraseña')
def recuperarCo():
    return render_template('RecuperarC.html')
#Ruta para llamara a la pagina principal.
@app.route('/Inicio')
def principal():
    return render_template('Principal.html')
#Ruta para llamara a la pagina para agendar citas.
@app.route('/Agendar_Cita')
def agCita():
    return render_template('AgCitas.html')
#Ruta para llamara a Ortodoncia.
@app.route('/Ortodoncia')
def ortodoncia():
    return render_template('Ortodoncia.html')
#Ruta para llamara a odontopediatria.
@app.route('/Odontopediatria')
def odonto():
    return render_template('Odontopediatria.html')
#Ruta para llamara a contacto.
@app.route('/Contacto')
def contactos():
    return render_template('Contactos.html')
#Ruta para llamara a sobre nosotros o About.
@app.route('/Sobre_Nosotros')
def about():
    return render_template('About.html')


# Para ejecutar la aplicacion
if __name__ == '__main__':
    app.run(debug=True)