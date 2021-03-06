from operator import length_hint
from flask import Flask, render_template, request, redirect, url_for

# Inicializar la aplicacion
app = Flask(__name__, template_folder='templates')

#arreglos
login_User=[]
Ag_Citas=[]


#Ruta para llamara a recuperar contraseña.
@app.route('/Recuperar_Contraseña')
def recuperarCo():
    return render_template('RecuperarC.html')

#Ruta para llamara a la pagina principal.
@app.route('/Inicio')
def principal():
    return render_template('Principal.html')

#Ruta para llamara a la pagina para agendar citas.
@app.route('/Agendar_Cita', methods=['GET','POST'])
def Agendar_Cita():
    if(request.method == "POST"):
        #Instanciamiento de datos de nuestra pagina Citas
        Nombre = request.form['pnombre']          
        Apellido = request.form['papellido'] 
        Dia = request.form['date']
        Email = request.form['email']      
        Trata = request.form['treatment']

        #(Condicional) Si el formulario no tiene ingresado datos no registrara
        if(Nombre == "" or Apellido  == "" or Dia == "" or Email == ""  or Trata == ""):
            return redirect(url_for('Agendar_Cita'))
        else:
            id_pac = len(Ag_Citas) + 1
            Ag_Citas.append({'id_pac' : id_pac,'pnombre': Nombre, 'papellido': Apellido, 'date': Dia, 'email': Email,
            'treatment': Trata})
            print(Ag_Citas)
    return render_template('AgCitas.html', Og_Citas = Ag_Citas)

#Para borrar
@app.route('/borrar', methods=["GET","POST"])
def borrar():   
    if(request.method == "POST"):        
        Ag_Citas.clear()        
    return redirect(url_for('Agendar_Cita'))

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

# Ruta principal para el login.
@app.route('/', methods=['GET','POST'])
def Login():
    #Obtiene los datos del pagina Login por medio del metodo POST
    if(request.method == "POST"):
        Email = request.form['email']  #O  btencion de correo
        Password = request.form['Password']  #Obtencion de contraseña


        #try para evaluar si un correo no se encuentra en la lista
        try:
            if (login_User.index(Email) >= 0):    #obtener el correo
                Indice = login_User.index(Email)
                if(login_User[Indice] == Email and login_User[Indice+1] == Password):   # Compara con el registro
                    return redirect(url_for('principal'))    # Nos envia a la pagina principal o inicio
                else:
                    return redirect(url_for('Login'))
        except:
            return redirect(url_for('Login'))

    return render_template('Login.html')

#Ruta para llamara a registro.
@app.route('/Registro' , methods=['GET','POST'])
def Registro():
    if(request.method == "POST"): #Obtiene los datos por medio del metodo POST
        nombre = request.form['pnombre']
        apellidos = request.form['Apellido']
        email = request.form['Email']         
        password = request.form['password']
        if(nombre == "" or apellidos == "" or email  == "" or password == ""):    #Condicion para direccionar si no hay datos
            return redirect(url_for('Registro'))
        else:
            #Ingresa datos al array
            login_User.append(nombre)
            login_User.append(apellidos)
            login_User.append(email)
            login_User.append(password)
            return redirect(url_for('Login'))
    return render_template('Registro.html')


if __name__ == '__main__':
    app.run(debug=True) # Para ejecutar la aplicacion