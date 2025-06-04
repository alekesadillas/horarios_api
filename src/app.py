from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import timedelta

from config import config
from dotenv import load_dotenv
from flask_cors import CORS





# Cargar variables de entorno
load_dotenv()

#Routes
from routes import horarios

app = Flask(__name__)

app.secret_key = 'clave_secreta' 
app.permanent_session_lifetime = timedelta(minutes=30) 

CORS(app, resources={"*":{"origins": "http://localhost:5000"}})



# -------- RUTA PRINCIPAL REDIRIGE AL LOGIN --------
@app.route('/')
def home():
    return redirect(url_for('login'))


# -------- LOGIN --------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        if usuario == 'admin' and contrasena == '12345':
            session.permanent = True
            session['usuario'] = usuario
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Usuario o contraseña incorrectos')
    return render_template('login.html')


# -------- DASHBOARD (INDEX) --------
@app.route('/index')
def index():
    if 'usuario' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))


# -------- LOGOUT --------
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))




# -------- API DE HORARIOS (desde horarios.py) --------

def page_not_found(error):
    return "Page not found", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(horarios.main, url_prefix='/api/horarios')
    
    
    # Errores
    app.register_error_handler(404, page_not_found)
    app.run()

