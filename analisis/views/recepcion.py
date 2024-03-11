import random, string
from flask import render_template, Blueprint, redirect, request, url_for
from analisis.models.user import User
from analisis.models.muestra import Muestra
from analisis.models.descuento import Descuento
from analisis.models.analisis import Analisis
from analisis.models.grupos import Grupo
from analisis.models.resultado import Resultado
from analisis.models.grupos_analisis_rel import GruposAnalisisRel
from analisis import db
from flask import g
from analisis.views.analistas import home
from flask import make_response, flash, session
from weasyprint import HTML
from analisis import socketio

recepcion = Blueprint('recepcion', __name__, url_prefix='/recepcion')

def get_user(id):
    user = User.query.get_or_404(id)
    return user

@recepcion.route("/")
def home():
    muestras = Muestra.query.all()
    descuentos = Descuento.query.all()
    analisis = Analisis.query.all()
    grupos = Grupo.query.all()
    db.session.commit()
    return render_template('recepcion/home.html', muestras=muestras, descuentos=descuentos, analisis=analisis, grupos=grupos, segment="home")


@recepcion.route("/create", methods=['GET', 'POST'])
def registrarMuestra():
    muestras = Muestra.query.all()
    descuentos = Descuento.query.all()
    lista_analisis = Analisis.query.all()
    lista_grupos = Grupo.query.all()
    form_data = request.form if request.method == 'POST' else None
    #ESTO ES PARA GENERAR UN FOLIO AUTOMATICO
    if request.method == 'GET':
        while True:
            folio_generado = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
            if not Muestra.query.filter_by(mues_folio=folio_generado).first():
                break
        print(folio_generado)
        return render_template('analisis/registroMuestra.html', muestras=muestras, descuentos=descuentos, analisis=lista_analisis, grupos=lista_grupos, segment="registrarM", form=form_data, folio_generado=folio_generado)

    if request.method == 'POST':
        mues_folio = request.form.get('folio_hidden')
        mues_nombre = request.form.get('nombre')
        mues_apellido_paterno = request.form.get('apellido_paterno')
        mues_apellido_materno = request.form.get('apellido_materno')
        mues_calle = request.form.get('calle')
        mues_num_ext = request.form.get('num_ext')
        mues_num_int = request.form.get('num_int')
        mues_colonia = request.form.get('colonia')
        mues_tel = request.form.get('tel')
        mues_email = request.form.get('email')
        mues_horas_ayuno = request.form.get('horas_ayuno')
        mues_alimentos = request.form.get('alimentos_hidden')
        mues_enfermedades = request.form.get('enfermedades_hidden')
        mues_medicamentos = request.form.get('medicamentos_hidden')
        mues_rubrica = request.form.get('rubrica')
        mues_des_id_fk = request.form.get('descuento')
        mues_edad = request.form.get('edad_hidden')
        mues_fec_nac = request.form.get('fecha_nacimiento')

        grupos = request.form.getlist('grupo_analisis[]')
        analisis = request.form.getlist('analisis[]')

        muestra = Muestra(mues_folio, mues_nombre, mues_apellido_paterno, mues_apellido_materno, mues_calle, mues_num_ext,
                  mues_num_int, mues_colonia, mues_tel, mues_email, mues_horas_ayuno, mues_alimentos, mues_enfermedades, mues_medicamentos, mues_rubrica, mues_des_id_fk, mues_edad, mues_fec_nac)

        db.session.add(muestra)
        db.session.flush()
        db.session.refresh(muestra)

        for ana in analisis:
            if not Resultado.query.filter_by(resul_ana_id_fk=ana, resul_mues_id_fk=muestra.mues_id).first():
                # Si no está asociado, crear una nueva instancia de Resultado y asociarla a la muestra
                resultado_analisis = Resultado(resul_ana_id_fk=ana, resul_mues_id_fk=muestra.mues_id, resul_fecha=None, resul_componente=None, resul_unidad=None, resul_resultado=None, resul_rango=None, resul_fuera_de_rango=None, resul_sta="O")
                db.session.add(resultado_analisis)

        for grupo_id in grupos:
            analisis_grupo = GruposAnalisisRel.query.filter_by(gana_grupo_id_fk=grupo_id).all()
            for relacion in analisis_grupo:
                # Verificar si el análisis ya está asociado a la muestra
                if not Resultado.query.filter_by(resul_ana_id_fk=relacion.gana_ana_id_fk, resul_mues_id_fk=muestra.mues_id).first():
                    # Si no está asociado, crear una nueva instancia de Resultado y asociarla a la muestra
                    resultado_analisis = Resultado(resul_ana_id_fk=relacion.gana_ana_id_fk, resul_mues_id_fk=muestra.mues_id, resul_fecha=None, resul_componente=None, resul_unidad=None, resul_resultado=None, resul_rango=None, resul_fuera_de_rango=None, resul_sta="O")
                    db.session.add(resultado_analisis)
                else:
                    flash('Uno o más análisis ya están asociados con un grupo.', 'error')
                    return render_template('analisis/registroMuestra.html', muestras=muestras, descuentos=descuentos, analisis=lista_analisis, grupos=lista_grupos, segment="registrarM", form=form_data)
        db.session.commit()
        flash('Muestra creada correctamente')
        socketio.emit('notification_update')
        if session.get('user_area_id_fk') == 6 or session.get('user_area_id_fk') == 7:
            return redirect(url_for("recepcion.home"))
        else:
            return redirect(url_for('home.index')) 
    return render_template('analisis/registroMuestra.html', muestras=muestras, descuentos=descuentos, analisis=lista_analisis, grupos=lista_grupos, segment="registrarM",form=form_data)



@recepcion.route('/detalle_muestra/<int:mues_id>', methods=['GET', 'POST'])
def detalle_muestra(mues_id):
    recepcion = Muestra.query.get_or_404(mues_id)
    user_area_id = g.user.user_area_id_fk
    
    # Obtener los análisis asociados a la muestra y al área del usuario
    analisis_asociados = []
    if user_area_id is not None:
        analisis_asociados = Analisis.query.join(Resultado, Resultado.resul_ana_id_fk == Analisis.ana_id) \
                                            .filter(Resultado.resul_mues_id_fk == mues_id) \
                                            .all()
    else:
        analisis_asociados = []

    # Almacenar los análisis asociados en la sesión
    session['analisis_asociados'] = [analisis.ana_id for analisis in analisis_asociados]

    if request.method == 'POST':
        return redirect(url_for('analistas.index'))
    return render_template('recepcion/detalle_muestra.html', recepcion=recepcion, analisis_asociados=analisis_asociados, segment='detalle_muestra')


@recepcion.route('/pdf_resultados/<int:mues_id>', methods=['GET', 'POST'])
def pdf_resultados(mues_id):
    muestra = Muestra.query.get_or_404(mues_id)
    resultados = Resultado.query.filter_by(resul_mues_id_fk=mues_id).all()

    rendered_html = render_template('recepcion/pdf_template.html', muestra=muestra, resultados=resultados)

    pdf = HTML(string=rendered_html).write_pdf()

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=resultados.pdf'
    return response


@recepcion.route('/editar_muestra/<int:mues_id>', methods=['GET', 'POST'])
def editar_muestra(mues_id):
    recepcion = Muestra.query.get_or_404(mues_id)
    if request.method == 'POST':
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
        socketio.emit('notification_update')
        return redirect(url_for('recepcion.home'))
    return render_template('recepcion/editar_muestra.html', recepcion=recepcion, segment='editar_muestra')


@recepcion.route('/eliminar_muestra/<int:mues_id>')
def eliminar_muestra(mues_id):
    print('muestra a eliminar: ',mues_id)
    recepcion = Muestra.query.get_or_404(mues_id)
    db.session.delete(recepcion)
    db.session.commit()
    socketio.emit('notification_update')
    print('muestra eliminado con éxito')
    return redirect(url_for('recepcion.home'))
