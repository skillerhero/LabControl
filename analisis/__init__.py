from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
db=SQLAlchemy(app)
#improtar las rutas
from analisis.views.auth import auth
from analisis.views.recepcion import recepcion
app.register_blueprint(auth)
app.register_blueprint(recepcion)
with app.app_context():
    db.create_all()