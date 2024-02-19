import functools
from flask import render_template,Blueprint
from analisis.models.user import User
from analisis.models.muestra import Muestra
from analisis.models.descuento import Descuento
from analisis.models.analisis import Analisis
from analisis import db
home=Blueprint('home',__name__,url_prefix='/home')

def get_user(id):
    print('id: ', id)
    user=User.query.get_or_404(id)
    return user

@home.route("/")
def index():
    muestras=Muestra.query.all()
    descuentos=Descuento.query.all()
    analisis=Analisis.query.all()
    db.session.commit()
    return render_template('home.html',muestras=muestras,descuentos=descuentos,analisis=analisis)
