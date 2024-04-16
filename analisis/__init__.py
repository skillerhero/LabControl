from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

#----------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------OBTENER LA BASE DE DATOS REMOTA
#----------------------------------------------------------------------------------------------------------------------------------
import platform
import subprocess

def obtenerBDRemota():
    dump_cmd = "mysqldump --defaults-extra-file=analisis/my.cnf -u admin -h databaserafael.cj2mqqcw6wf0.us-east-2.rds.amazonaws.com analisis > analisis_backup.sql"
    dump_cmd2 = "mysql --defaults-extra-file=analisis/my2.cnf -u root analisis < analisis_backup.sql"
    if platform.system() == 'Windows':
        try:
            subprocess.run(dump_cmd, shell=True, check=True)
            subprocess.run(dump_cmd2, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            pass
            print(f"Error al hacer el volcado de la base de datos: {str(e)}")

def subirBDLocal():
    dump_cmd = "mysqldump --defaults-extra-file=analisis/my2.cnf -u root analisis > analisis.sql"
    dump_cmd2 = "mysql --defaults-extra-file=analisis/my.cnf -u admin -h databaserafael.cj2mqqcw6wf0.us-east-2.rds.amazonaws.com analisis < analisis.sql"
    if platform.system() == 'Windows':
        try:
            subprocess.run(dump_cmd, shell=True, check=True)
            subprocess.run(dump_cmd2, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error al subir la base de datos: {str(e)}")
#----------------------------------------------------------------------------------------------------------------------------------
import mysql.connector
import time
import threading

def revisar_conexion():
    config = {
        'user': 'admin',
        'password': 'TN#z2bQX94&bd$n',
        'host': 'databaserafael.cj2mqqcw6wf0.us-east-2.rds.amazonaws.com',
        'database': 'analisis',
        'raise_on_warnings': True
    }
    while True:
        try:
            cnx = mysql.connector.connect(**config)
            if cnx.is_connected():
                print("Conexión exitosa.")
                cnx.close()
            else:
                print("No se pudo conectar.")
        except mysql.connector.Error as err:
            print(f"Algo salió mal: {err}")
        time.sleep(60) 
if platform.system() == 'Windows':
    t = threading.Thread(target=revisar_conexion)
    t.start()
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
