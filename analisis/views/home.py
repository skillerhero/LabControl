import functools
from flask import render_template,Blueprint,flash,g,redirect,request,session,url_for
from werkzeug.exceptions import abort
from analisis.models.user import User
from analisis.models.muestra import Muestra
from analisis.models.descuento import Descuento
from analisis.models.analisis import Analisis
from analisis.models.muestra_analisis_rel import MuestraAnalisisRel
from werkzeug.security import check_password_hash,generate_password_hash
from analisis import db
from analisis.views.auth import login_required
home=Blueprint('home',__name__,url_prefix='/home')

def get_user(id):
    user=User.query.get_or_404(id)
    return user

@home.route("/")
def index():
    muestras=Muestra.query.all()
    descuentos=Descuento.query.all()
    analisis=Analisis.query.all()
    db.session.commit()
    return render_template('home.html',muestras=muestras,descuentos=descuentos,analisis=analisis)
