from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
import platform
import subprocess
import filecmp

DB_USER_REMOTO = 'admin'
DB_PASSWORD_REMOTO = 'TN#z2bQX94&bd$n'
DB_HOST_REMOTO = 'databaserafael.cj2mqqcw6wf0.us-east-2.rds.amazonaws.com'
DB_NAME = 'analisis'
SQLALCHEMY_TRACK_MODIFICATIONS=False
URI_REMOTO = f"mysql+pymysql://{DB_USER_REMOTO}:{DB_PASSWORD_REMOTO}@{DB_HOST_REMOTO}/{DB_NAME}"
DB_USER_LOCAL = 'root'
DB_PASSWORD_LOCAL = 'admin'
DB_HOST_LOCAL = '127.0.0.1'
DB_NAME = 'analisis'
SQLALCHEMY_TRACK_MODIFICATIONS=False
URI_LOCAL = f"mysql+pymysql://{DB_USER_LOCAL}:{DB_PASSWORD_LOCAL}@{DB_HOST_LOCAL}/{DB_NAME}"

app = Flask(__name__)
socketio = SocketIO(app=app, cors_allowed_origins='*')
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'J^8G#2L$k6hP3@F!d*DbT'
app.config['TESTING'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
usando_bd_local = False
try:
    if platform.system() == 'Windows':
        with app.app_context():
            app.config['SQLALCHEMY_DATABASE_URI'] = URI_LOCAL
        usando_bd_local = True
        print("Usando base de datos local")
    else:
        with app.app_context():
            app.config['SQLALCHEMY_DATABASE_URI'] = URI_REMOTO
        print("Usando base de datos remota")
    # cnx = mysql.connector.connect(**config)
    # if cnx.is_connected():
    #     print("Conexión exitosa. Usando la base de datos remota.")
    #     cnx.close()
except:
    print(f"Algo salió mal.")
db = SQLAlchemy(app)

#----------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------OBTENER LA BASE DE DATOS REMOTA
#----------------------------------------------------------------------------------------------------------------------------------
def comparar_archivos(file1, file2):
    return filecmp.cmp(file1, file2)

def obtenerBDRemota():
    dump_cmd = "mysqldump --defaults-extra-file=analisis/my.cnf -u admin -h databaserafael.cj2mqqcw6wf0.us-east-2.rds.amazonaws.com analisis > analisis_backup.sql"
    dump_cmd2 = "mysql --defaults-extra-file=analisis/my2.cnf -u root analisis < analisis_backup.sql"
    if platform.system() == 'Windows':
        try:
            print("Obteniendo bd remota")
            subprocess.run(dump_cmd, shell=True, check=True)
            print("Reemplazando la bd local")
            subprocess.run(dump_cmd2, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error al hacer el volcado de la base de datos: {str(e)}")

def subirBDLocal():
    dump_cmd = "mysqldump --defaults-extra-file=analisis/my2.cnf -u root analisis > analisis.sql"
    dump_cmd2 = "mysql --defaults-extra-file=analisis/my.cnf -u admin -h databaserafael.cj2mqqcw6wf0.us-east-2.rds.amazonaws.com analisis < analisis.sql"
    if platform.system() == 'Windows':
        try:
            print("Obteniendo bd local")
            subprocess.run(dump_cmd, shell=True, check=True)
            print("Reemplazando la bd remota")
            subprocess.run(dump_cmd2, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error al subir la base de datos: {str(e)}")
#----------------------------------------------------------------------------------------------------------------------------------
if platform.system() == 'Windows':
    try:
        config = {
            'user': DB_USER_REMOTO,
            'password': DB_PASSWORD_REMOTO,
            'host': DB_HOST_REMOTO,
            'database': DB_NAME,
            'raise_on_warnings': True
        }
        import mysql.connector
        cnx = mysql.connector.connect(**config)
        if cnx.is_connected():
            print("Conexión exitosa.")
            cnx.close()
            obtenerBDRemota()
    except:
        print('Error al tratar de hacer backup de la bd remota')

# def revisar_conexion():
#     config = {
#         'user': DB_USER_REMOTO,
#         'password': DB_PASSWORD_REMOTO,
#         'host': DB_HOST_REMOTO,
#         'database': DB_NAME,
#         'raise_on_warnings': True
#     }
#     while True:
#         try:
#             cnx = mysql.connector.connect(**config)
#             if cnx.is_connected():
#                 print("Conexión exitosa. Usando la base de datos remota.")
#                 cnx.close()
#                 with app.app_context():
#                     app.config['SQLALCHEMY_DATABASE_URI'] = URI_REMOTO
#                     db.engine.dispose()
#                 obtenerBDRemota()
#             else:
#                 print("No se puede conectar. Usando la base de datos local.")
#                 with app.app_context():
#                     app.config['SQLALCHEMY_DATABASE_URI'] = URI_LOCAL
#                     db.engine.dispose()
#         except mysql.connector.Error as err:
#             print(f"Algo salió mal: {err}. Usando la base de datos local.")
#             with app.app_context():
#                 app.config['SQLALCHEMY_DATABASE_URI'] = URI_LOCAL
#                 db.engine.dispose()
#         time.sleep(60)
#----------------------------------------------------------------------------------------------------------------------------------
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
