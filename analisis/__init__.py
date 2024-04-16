from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

#----------------------------------------------------------------------------------------------------------------------------------
import os
import platform
import subprocess
dump_cmd = f"mysqldump --defaults-extra-file=analisis\my.cnf -u admin -h databaserafael.cj2mqqcw6wf0.us-east-2.rds.amazonaws.com analisis > analisis_backup.sql"
dump_cmd2 = f"mysql -u admin -p admin analisis < analisis_backup.sql"
if platform.system() == 'Windows':
    try:
        subprocess.run(dump_cmd, shell=True, check=True)
        subprocess.run(dump_cmd2, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        pass
        print(f"Error al hacer el volcado de la base de datos: {str(e)}")

#----------------------------------------------------------------------------------------------------------------------------------
app = Flask(__name__)
socketio = SocketIO(app=app, cors_allowed_origins='*')
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

# Importar las rutas
from analisis.views.auth import auth
from analisis.views.recepcion import recepcion
from analisis.views.analistas import home
from analisis.views.areas import areas
from analisis.views.analisis import analisis
from analisis.views.resultados import resultados
from analisis.views.grupos import grupos
from analisis.views.regresion import regresion
from analisis.views.mediciones import mediciones

# Registrar blueprints
app.register_blueprint(auth)
app.register_blueprint(recepcion)
app.register_blueprint(home)
app.register_blueprint(areas)
app.register_blueprint(analisis)
app.register_blueprint(resultados)
app.register_blueprint(grupos) 
app.register_blueprint(regresion) 
app.register_blueprint(mediciones) 

with app.app_context():
    db.create_all()
