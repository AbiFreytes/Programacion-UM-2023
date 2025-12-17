import os
from pathlib import Path

from flask import Flask
from dotenv import load_dotenv

#Importamos nuevas librerias clase 3
from flask_restful import Api #Agrego la clase Api

#Importar SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

#Importar Flask JWT
from flask_jwt_extended import JWTManager

from flask_mail import Mail

#Inicio Restful
api = Api()

#Inicializar SQLAlchemy
db = SQLAlchemy()

#Inicializar JWT
jwt = JWTManager()

#Inicializar mail
mailsender = Mail()

#Metodo que inicializa la app
def create_app():
    #Inicio Flask
    app = Flask(__name__)

    #variables de entorno
    env_path = Path(__file__).resolve().parent / '.env'
    load_dotenv(env_path)

    #Si no existe el archivo de base de datos crearlo (solo válido si se utiliza SQLite)
    database_path = Path(os.getenv('DATABASE_PATH', '')).expanduser()
    database_name = os.getenv('DATABASE_NAME', '')
    database_file = (database_path / database_name).resolve()

    database_file.parent.mkdir(parents=True, exist_ok=True)
    database_file.touch(exist_ok=True)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Url de configuración de base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{database_file.as_posix()}"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_file.as_posix()

    db.init_app(app)

    #Importar directorio de recursos
    import main.resources as resources

    api.add_resource(resources.UsuariosResource, '/usuarios')

    api.add_resource(resources.UsuarioResource, '/usuario/<id>')

    api.add_resource(resources.UsuarioActualResource, '/usuario/actual')

    api.add_resource(resources.UsuariosAlumnosResource, '/alumnos')

    api.add_resource(resources.UsuarioAlumnoResource, '/alumno/<id>')

    api.add_resource(resources.AlumnoByUsuarioResource, '/alumno/usuario/<id_usuario>')

    api.add_resource(resources.UsuarioProfesorResource, '/profesor/<id>')

    api.add_resource(resources.UsuariosProfesoresResource, '/profesores')

    api.add_resource(resources.ProfesoresPublicosResource, '/profesores-publicos')

    api.add_resource(resources.ProfesorByUsuarioResource, '/profesor/usuario/<id_usuario>')

    api.add_resource(resources.PlanificacionesResource, '/planificaciones')

    api.add_resource(resources.PlanificacionResource, '/planificaciones/<id>')

    api.add_resource(resources.PlanificacionesByAlumnoResource, '/planificaciones/alumno/<id_alumno>')

    #Cargar la aplicacion en la API de Flask Restful
    #es para que la aplicacion de flask funcione como API
    api.init_app(app)

    #Cargar clave secreta
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')


    #Cargar tiempo de expiración de los tokens
    expires_raw = os.getenv('JWT_ACCESS_TOKEN_EXPIRES')
    try:
        expires_seconds = int(expires_raw) if expires_raw is not None else 3600
    except ValueError:
        app.logger.warning('JWT_ACCESS_TOKEN_EXPIRES invalid; defaulting to 3600 seconds')
        expires_seconds = 3600
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = expires_seconds

    jwt.init_app(app)

    from main.auth import routes
    #Importar blueprint
    app.register_blueprint(routes.auth)

    #Configuración de mail
    app.config['MAIL_HOSTNAME'] = os.getenv('MAIL_HOSTNAME')
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS')
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['FLASKY_MAIL_SENDER'] = os.getenv('FLASKY_MAIL_SENDER')
    #Inicializar en app
    mailsender.init_app(app)

    #Por ultimo retornamos la aplicacion inicializada
    return app
