from flask import Flask
from config import config
from dotenv import load_dotenv
from flask_cors import CORS


# Cargar variables de entorno
load_dotenv()

#Routes
from routes import horarios

app = Flask(__name__)

CORS(app, resources={"*":{"origins": "http://localhost:3000"}})

def page_not_found(error):
    return "Page not found", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(horarios.main, url_prefix='/api/horarios')
    
    
    # Errores
    app.register_error_handler(404, page_not_found)
    app.run()
