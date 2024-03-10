from flask import render_template, request, redirect, url_for, Blueprint, session
from analisis.models.user import User
from analisis.models.muestra import Muestra
from analisis.models.descuento import Descuento
from analisis.models.analisis import Analisis
from analisis.models.resultado import Resultado
from analisis import db
from flask import g
from flask import jsonify

home = Blueprint('home', __name__, url_prefix='/home')

def get_user(id):
    user = User.query.get_or_404(id)
    return user

@home.route("/getMuestras")
def getMuestras():
    muestras = []
    if g.user.user_area_id_fk is not None:
        if session.get('user_area_id_fk') == 6 or session.get('user_area_id_fk') == 7:
            muestras = Muestra.query.join(Resultado, Resultado.resul_mues_id_fk == Muestra.mues_id) \
                        .join(Analisis, Analisis.ana_id == Resultado.resul_ana_id_fk) \
                        .filter(Analisis.ana_area_id_fk == g.user.user_area_id_fk) \
                        .filter(Resultado.resul_sta == 'O')\
                        .all()
        else:
            muestras = Muestra.query.join(Resultado, Resultado.resul_mues_id_fk == Muestra.mues_id) \
                .join(Analisis, Analisis.ana_id == Resultado.resul_ana_id_fk) \
                .filter(Resultado.resul_sta == 'F')\
                .all()

    else:
        muestras = Muestra.query.all()

    muestras_dict = []
    for muestra in muestras:
        muestra_dict = muestra.to_dict()
        muestra_dict['url_detalle'] = url_for('home.detalle_muestra', mues_id=muestra.mues_id)
        muestra_dict['url_resultados'] = url_for('resultados.agregar_resultados', mues_id=muestra.mues_id)
        muestras_dict.append(muestra_dict)

    return jsonify(muestras_dict)


@home.route("/")
def index():
    user_id = g.user.user_id
    user_area_id = g.user.user_area_id_fk
    muestras = []
    if user_area_id is not None:
        muestras = Muestra.query.join(Resultado, Resultado.resul_mues_id_fk == Muestra.mues_id) \
                                .join(Analisis, Analisis.ana_id == Resultado.resul_ana_id_fk) \
                                .filter(Analisis.ana_area_id_fk == user_area_id) \
                                .filter(Resultado.resul_sta == 'O')\
                                .all()
    else:
        muestras = Muestra.query.all()
    
    descuentos = Descuento.query.all()
    analisis = Analisis.query.all()
    db.session.commit()
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

    # Almacenar los análisis asociados en la sesión
    session['analisis_asociados'] = [analisis.ana_id for analisis in analisis_asociados]

    if request.method == 'POST':
        return redirect(url_for('analistas.index'))
    
    return render_template('analistas/detalle_muestra.html', recepcion=recepcion, analisis_asociados=analisis_asociados, segment='detalle_muestra')
