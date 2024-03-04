from flask import render_template, request, redirect, url_for, Blueprint
from analisis.models.user import User
from analisis.models.muestra import Muestra
from analisis.models.descuento import Descuento
from analisis.models.analisis import Analisis
from analisis.models.resultado import Resultado
from analisis import db
from flask import g

home = Blueprint('home', __name__, url_prefix='/home')

def get_user(id):
    print('id: ', id)
    user = User.query.get_or_404(id)
    return user

@home.route("/")
def index():
    user_id = g.user.user_id
    user_area_id = g.user.user_area_id_fk
    print(user_area_id)
    muestras = []
    if user_area_id is not None:
        muestras = Muestra.query.join(Resultado, Resultado.resul_mues_id_fk == Muestra.mues_id) \
                                .join(Analisis, Analisis.ana_id == Resultado.resul_ana_id_fk) \
                                .filter(Analisis.ana_area_id_fk == user_area_id) \
                                .all()
    else:
        muestras = Muestra.query.all()
    
    descuentos = Descuento.query.all()
    analisis = Analisis.query.all()
    db.session.commit()

    print("muestras index: ", muestras)
    return render_template('analistas/home.html', muestras=muestras, descuentos=descuentos, analisis=analisis, segment='index')

@home.route("/recepcion")
def indexRecepcion():
    muestras = Muestra.query.all()
    descuentos = Descuento.query.all()
    analisis = Analisis.query.all()
    db.session.commit()
    print("muestras recepcion: ", muestras)
    segment = 'recepcion'  # Define el valor de segment
    return render_template('recepcion/home.html', muestras=muestras, descuentos=descuentos, analisis=analisis, segment='indexRecepcion')

@home.route('/detalle_muestra/<int:mues_id>', methods=['GET', 'POST'])
def detalle_muestra(mues_id):
    recepcion = Muestra.query.get_or_404(mues_id)
    user_area_id = g.user.user_area_id_fk
    
    # Obtener los análisis asociados a la muestra y al área del usuario
    analisis_asociados = []
    if user_area_id is not None:
        analisis_asociados = Analisis.query.join(Resultado, Resultado.resul_ana_id_fk == Analisis.ana_id) \
                                            .filter(Resultado.resul_mues_id_fk == mues_id) \
                                            .filter(Analisis.ana_area_id_fk == user_area_id) \
                                            .all()
    else:
        analisis_asociados = []

    if request.method == 'POST':
        recepcion.muestra_folio = request.form['mues_folio']
        print(recepcion.muestra_folio)
        recepcion.muestra_nombre = request.form['mues_nombre']
        recepcion.muestra_apellido_paterno = request.form['mues_apellido_paterno']
        recepcion.muestra_apellido_materno = request.form['mues_apellido_materno']
        recepcion.muestra_telefono = request.form['mues_tel']
        recepcion.muestra_email = request.form['mues_email']
        recepcion.muestra_calle = request.form['mues_calle']
        recepcion.muestra_colonia = request.form['mues_colonia']
        recepcion.muestra_num_ext = request.form['mues_num_ext']
        recepcion.muestra_num_int = request.form['mues_num_int']
        recepcion.muestra_horas_ayuno = request.form['mues_horas_ayuno']
        recepcion.muestra_alimentos = request.form['mues_alimentos']
        recepcion.muestra_enfermedades = request.form['mues_enfermedades']
        recepcion.muestra_medicamentos = request.form['mues_medicamentos']
        recepcion.muestra_rubrica = request.form['mues_rubrica']
        db.session.commit()
        return redirect(url_for('analistas.index'))
    
    return render_template('analistas/detalle_muestra.html', recepcion=recepcion, analisis_asociados=analisis_asociados, segment='detalle_muestra')

