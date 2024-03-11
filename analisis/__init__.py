from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = 'J^8G#2L$k6hP3@F!d*DbT'
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
