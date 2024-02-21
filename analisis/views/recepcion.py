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
recepcion=Blueprint('recepcion',__name__,url_prefix='/recepcion')

def get_user(id):
    user=User.query.get_or_404(id)
    return user

@recepcion.route("/")
def index():
    muestras=Muestra.query.all()
    descuentos=Descuento.query.all()
    analisis=Analisis.query.all()
    db.session.commit()
    return render_template('recepcion/home.html',muestras=muestras,descuentos=descuentos,analisis=analisis)

@recepcion.route("/create",methods=['GET','POST'])
#@login_required
def registrarMuestra():
    if request.method=='POST':
        print(request.form)
        mues_folio=request.form.get('folio')
        mues_nombre=request.form.get('nombre')
        mues_apellido_paterno=request.form.get('apellido_paterno')
        mues_apellido_materno=request.form.get('apellido_materno')
        mues_calle=request.form.get('calle')
        mues_num_ext=request.form.get('num_ext')
        mues_num_int=request.form.get('num_int')
        mues_colonia=request.form.get('colonia')
        mues_tel=request.form.get('tel')
        mues_email=request.form.get('email')
        mues_horas_ayuno=request.form.get('horas_ayuno')
        mues_alimentos=request.form.get('alimentos')
        mues_enfermedades=request.form.get('enfermedades')
        mues_medicamentos=request.form.get('medicamentos')
        mues_rubrica=request.form.get('rubrica')
        mues_des_id_fk=request.form.get('descuento')
        analisis=request.form.getlist('analisis[]')
        muestra=Muestra(mues_folio, mues_nombre, mues_apellido_paterno, mues_apellido_materno, mues_calle, mues_num_ext,
         mues_num_int, mues_colonia, mues_tel, mues_email, mues_horas_ayuno, mues_alimentos, mues_enfermedades, mues_medicamentos, mues_rubrica,mues_des_id_fk)
        db.session.add(muestra)
        db.session.flush()
        db.session.refresh(muestra)
        print(muestra)
        for analis in analisis:
            relacion=MuestraAnalisisRel(muestra.mues_id,analis)
            db.session.add(relacion)
        db.session.commit()

    muestras=Muestra.query.all()
    descuentos=Descuento.query.all()
    analisis=Analisis.query.all()
    return render_template('analisis/registroMuestra.html',muestras=muestras,descuentos=descuentos,analisis=analisis)
