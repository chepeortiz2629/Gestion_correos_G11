###############################################################
########################## Librerias ##########################
###############################################################

from datetime import datetime
from ast import Return
from tkinter.messagebox import RETRY
from flask import Flask, render_template, url_for, request, redirect, flash

app=Flask(__name__)
app.secret_key='mi clave de secreta'+str(datetime.now)


###############################################################
############## Rutas para recuperar informacion ###############
###############################################################

@app.route('/addregistro', methods=['POST'])
def add_registro():
    datos=request.form
    nom=datos['nombre']
    ape=datos['apellido']
    usu=datos['email']
    p1=datos['pass1']
    p2=datos['pass2']
    
    
 #  p1enc=generate_password_hash(p1)
    if nom=='' and ape=='' and usu=='' and p1=='' and p2=='':
        flash('Datos Imcompletos')
    elif p1!=p2:
        flash("Las Contraseñas no Coinciden")    
    elif len(p1)<8:
        flash('Contraseña no cumple tamaño minimo')
 #   else:
   #     resultado=controlador.insertar_usuarios(nom,ape,usu,p1enc)
    #    if resultado:
 #       flash('Informacion Almacenada')
    else:
        flash('Error en Almacenamiento')

    return redirect(url_for('registro'))
    









###############################################################
################## Rutas de navegacion ########################
###############################################################

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login')
def login():
    #session.clear()
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/verificacion')
def verificar():
    return render_template('verificacion.html')

@app.route('/mensajeria')
def mensajeria():
    return render_template('mensajeria.html')

@app.route('/recuperar')
def recuperar():
    return render_template('recuperar.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')    

@app.route('/restablecer/<usuario>')
@app.route('/restablecer')
def restablecer(usuario=None):
    if usuario==None:
        return render_template('restablecer.html')  
    else:
        return render_template('restablecer.html', datauser=usuario)      

@app.route('/mensajes')
def mensajes():
    return render_template('mensajes.html')   


if __name__=='__main__':
    app.run(debug=True)