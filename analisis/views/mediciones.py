from flask import render_template, request, redirect, url_for
from analisis import db
from flask import render_template, Blueprint
from math import ceil
from analisis.models.mediciones_analisis import MedicionesAnalisis
from analisis.models.analisis import Analisis
mediciones = Blueprint('mediciones', __name__, url_prefix='/mediciones')

@mediciones.route('/')
def index():
    mediciones_por_pagina = 10
    pagina_actual = request.args.get('pagina', 1, type=int)
    mediciones_totales = MedicionesAnalisis.query.count()
    total_paginas = ceil((mediciones_totales / mediciones_totales) if mediciones_totales else 0)
    inicio = (pagina_actual - 1) * mediciones_por_pagina
    fin = inicio + mediciones_por_pagina
    mediciones_paginadas = MedicionesAnalisis.query.slice(inicio, fin).all()
    return render_template('mediciones/index.html', mediciones=mediciones_paginadas, segment='index', total_paginas=total_paginas, pagina_actual=pagina_actual)

@mediciones.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        mediciones_analisis_ana_id_fk = request.form.get('mediciones_analisis_ana_id_fk')
        mediciones_analisis_componente = request.form.get('mediciones_analisis_componente')
        mediciones_analisis_unidad = request.form.get('mediciones_analisis_unidad')
        mediciones_analisis_rango = request.form.get('mediciones_analisis_rango')
        nueva_medicion = MedicionesAnalisis(mediciones_analisis_ana_id_fk=mediciones_analisis_ana_id_fk,
                                             mediciones_analisis_componente=mediciones_analisis_componente,
                                             mediciones_analisis_unidad=mediciones_analisis_unidad,
                                             mediciones_analisis_rango=mediciones_analisis_rango)
        db.session.add(nueva_medicion)
        db.session.commit()
        print('Medición agregada con éxito')
        return redirect(url_for('mediciones.index'))
    lista_analisis = Analisis.query.all()
    return render_template('mediciones/agregar_mediciones.html', segment='agregar',lista_analisis=lista_analisis)

@mediciones.route('/editar/<int:mediciones_analisis_id>', methods=['GET', 'POST'])
def editar(mediciones_analisis_id):
    medicion = MedicionesAnalisis.query.get_or_404(mediciones_analisis_id)
    if request.method == 'POST':
        medicion.mediciones_analisis_ana_id_fk = request.form.get('mediciones_analisis_ana_id_fk')
        medicion.mediciones_analisis_componente = request.form.get('mediciones_analisis_componente')
        medicion.mediciones_analisis_unidad = request.form.get('mediciones_analisis_unidad')
        medicion.mediciones_analisis_rango = request.form.get('mediciones_analisis_rango')
        db.session.commit()
        print('Medición editada con éxito')
        return redirect(url_for('mediciones.index'))
    lista_analisis = Analisis.query.all()
    return render_template('mediciones/editar_mediciones.html', medicion=medicion, segment='editar', lista_analisis=lista_analisis)

@mediciones.route('/eliminar/<int:mediciones_analisis_id>')
def eliminar(mediciones_analisis_id):
    print('Medicion a eliminar:', mediciones_analisis_id)
    medicion = MedicionesAnalisis.query.get_or_404(mediciones_analisis_id)
    db.session.delete(medicion)
    db.session.commit()
    print('Medición eliminada con éxito')
    return redirect(url_for('mediciones.index'))
