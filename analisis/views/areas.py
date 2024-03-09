# Importaciones necesarias
from flask import render_template, request, redirect, url_for, flash
from analisis import db
from flask import render_template, Blueprint
from analisis.models.area import Area
from math import ceil

areas = Blueprint('areas', __name__, url_prefix='/areas')

@areas.route('/')
def index():
    areas_por_pagina = 10
    pagina_actual = request.args.get('pagina', 1, type=int)
    areas_totales = Area.query.count()
    total_paginas = ceil(areas_totales / areas_por_pagina)
    inicio = (pagina_actual - 1) * areas_por_pagina
    fin = inicio + areas_por_pagina
    areas_paginadas = Area.query.slice(inicio, fin).all()
    return render_template('areas/index.html', areas=areas_paginadas, segment='index', total_paginas=total_paginas, pagina_actual=pagina_actual)

#Agregar área
@areas.route('/agregar_area', methods=['GET', 'POST'])
def agregar_area():
    if request.method == 'POST':
        area_nombre = request.form.get('area_nombre')
        area_sta = request.form.get('area_sta')

        # Verificar si el área ya existe en la base de datos
        area_existente = Area.query.filter_by(area_nombre=area_nombre).first()
        if area_existente:
            flash('El área ingresada ya existe.', 'danger')
        else:
            nueva_area = Area(area_nombre=area_nombre, area_sta=area_sta)
            db.session.add(nueva_area)
            db.session.commit()
            flash('Área agregada exitosamente.', 'success')

    return render_template('areas/agregar_area.html', segment='agregar_area')

@areas.route('/editar_area/<int:area_id>', methods=['GET', 'POST'])
def editar_area(area_id):
    area = Area.query.get_or_404(area_id)
    if request.method == 'POST':
        area.area_nombre = request.form['area_nombre']
        area.area_sta = request.form['area_sta']
        db.session.commit()
        return redirect(url_for('areas.index'))
    return render_template('areas/editar_area.html', area=area, segment='editar_area')

@areas.route('/detalle_area/<int:area_id>', methods=['GET', 'POST'])
def detalle_area(area_id):
    area = Area.query.get_or_404(area_id)
    if request.method == 'POST':
        area.area_nombre = request.form['area_nombre']
        area.area_sta = request.form['area_sta']
        db.session.commit()
        return redirect(url_for('areas.index'))
    return render_template('areas/detalle_area.html', area=area, segment='detalle_area')

@areas.route('/eliminar_area/<int:area_id>')
def eliminar_area(area_id):
    print('Área a eliminar: ', area_id)
    area = Area.query.get_or_404(area_id)
    db.session.delete(area)
    db.session.commit()
    print('Área eliminada con éxito')
    return redirect(url_for('areas.index'))
