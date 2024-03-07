from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

# Importar las rutas
from analisis.views.auth import auth
from analisis.views.recepcion import recepcion
from analisis.views.home import home
from analisis.views.areas import areas
from analisis.views.analisis import analisis
from analisis.views.resultados import resultados
from analisis.views.grupos import grupos
from analisis.views.regresion import regresion

# Registrar blueprints
app.register_blueprint(auth)
app.register_blueprint(recepcion)
app.register_blueprint(home)
app.register_blueprint(areas)
app.register_blueprint(analisis)
app.register_blueprint(resultados)
app.register_blueprint(grupos) 
app.register_blueprint(regresion) 

with app.app_context():
    db.create_all()
