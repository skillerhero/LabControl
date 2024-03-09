import functools
from flask import render_template, Blueprint, redirect, request, url_for
from analisis.models.user import User
from analisis.models.muestra import Muestra
from analisis.models.descuento import Descuento
from analisis.models.analisis import Analisis
from analisis.models.grupos import Grupo
from analisis.models.resultado import Resultado
from analisis.models.grupos_analisis_rel import GruposAnalisisRel
from analisis import db
from analisis.views.auth import login_required
from flask import make_response
from weasyprint import HTML

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
    if request.method == 'POST':
        mues_folio = request.form.get('folio')
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
        mues_alimentos = request.form.get('alimentos')
        mues_enfermedades = request.form.get('enfermedades')
        mues_medicamentos = request.form.get('medicamentos')
        mues_rubrica = request.form.get('rubrica')
        mues_des_id_fk = request.form.get('descuento')
        grupos = request.form.getlist('grupo_analisis[]')
        analisis = request.form.getlist('analisis[]')

        muestra = Muestra(mues_folio, mues_nombre, mues_apellido_paterno, mues_apellido_materno, mues_calle, mues_num_ext,
                          mues_num_int, mues_colonia, mues_tel, mues_email, mues_horas_ayuno, mues_alimentos, mues_enfermedades, mues_medicamentos, mues_rubrica, mues_des_id_fk)
        db.session.add(muestra)
        db.session.flush()
        db.session.refresh(muestra)
        # Recorrer los análisis seleccionados y verificar si ya están asociados a la muestra
        for ana in analisis:
            # Verificar si el análisis ya está asociado a la muestra
            if not Resultado.query.filter_by(resul_ana_id_fk=ana, resul_mues_id_fk=muestra.mues_id).first():
                # Si no está asociado, crear una nueva instancia de Resultado y asociarla a la muestra
                resultado_analisis = Resultado(resul_ana_id_fk=ana, resul_mues_id_fk=muestra.mues_id, resul_fecha=None, resul_componente=None, resul_unidad=None, resul_resultado=None, resul_rango=None, resul_fuera_de_rango=None, resul_sta="O")
                db.session.add(resultado_analisis)

        # Recorrer los grupos seleccionados y agregar los análisis asociados a cada grupo
        for grupo_id in grupos:
            analisis_grupo = GruposAnalisisRel.query.filter_by(gana_grupo_id_fk=grupo_id).all()
            for relacion in analisis_grupo:
                # Verificar si el análisis ya está asociado a la muestra
                if not Resultado.query.filter_by(resul_ana_id_fk=relacion.gana_ana_id_fk, resul_mues_id_fk=muestra.mues_id).first():
                    # Si no está asociado, crear una nueva instancia de Resultado y asociarla a la muestra
                    resultado_analisis = Resultado(resul_ana_id_fk=relacion.gana_ana_id_fk, resul_mues_id_fk=muestra.mues_id, resul_fecha=None, resul_componente=None, resul_unidad=None, resul_resultado=None, resul_rango=None, resul_fuera_de_rango=None, resul_sta="O")
                    db.session.add(resultado_analisis)

        # Guardar los cambios en la base de datos
        db.session.commit()

    # Obtener los datos necesarios para mostrar en el formulario
    muestras = Muestra.query.all()
    descuentos = Descuento.query.all()
    analisis = Analisis.query.all()
    grupos = Grupo.query.all()
    return render_template('analisis/registroMuestra.html', muestras=muestras, descuentos=descuentos, analisis=analisis, grupos=grupos, segment="registrarM")

@recepcion.route('/detalle_muestra/<int:mues_id>', methods=['GET', 'POST'])
def detalle_muestra(mues_id):
    recepcion = Muestra.query.get_or_404(mues_id)
    if request.method == 'POST':
        
        return redirect(url_for('recepcion.home'))
    return render_template('recepcion/detalle_muestra.html', recepcion=recepcion, segment='detalle_muestra')


@recepcion.route('/pdf_resultados/<int:mues_id>', methods=['GET', 'POST'])
def pdf_resultados(mues_id):
    muestra = Muestra.query.get_or_404(mues_id)
    resultados = Resultado.query.filter_by(resul_mues_id_fk=mues_id).all()
    for resultado in resultados:
        print(resultado.resul_id)
        print(resultado.resul_ana_id_fk)
        print(resultado.resul_mues_id_fk)
        print(resultado.resul_fecha)
        print(resultado.resul_componente)
        print(resultado.resul_unidad)
        print(resultado.resul_resultado)
        print(resultado.resul_rango)
        print(resultado.resul_fuera_de_rango)
        print(resultado.resul_sta)

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
        return redirect(url_for('recepcion.home'))
    return render_template('recepcion/editar_muestra.html', recepcion=recepcion, segment='editar_muestra')


@recepcion.route('/eliminar_muestra/<int:mues_id>')
def eliminar_muestra(mues_id):
    print('muestra a eliminar: ',mues_id)
    recepcion = Muestra.query.get_or_404(mues_id)
    db.session.delete(recepcion)
    db.session.commit()
    print('muestra eliminado con éxito')
    return redirect(url_for('recepcion.home'))
