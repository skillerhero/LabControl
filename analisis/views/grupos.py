from flask import render_template, request, redirect, url_for, flash
from analisis import db
from flask import render_template, Blueprint
from analisis.models.grupos import Grupo
from analisis.models.analisis import Analisis
from analisis.models.grupos_analisis_rel import GruposAnalisisRel
from math import ceil

grupos = Blueprint('grupos', __name__, url_prefix='/grupos')

@grupos.route('/')
def index():
    grupos_por_pagina = 20
    pagina_actual = request.args.get('pagina', 1, type=int)
    grupos_totales = Grupo.query.count()
    total_paginas = ceil(grupos_totales / grupos_por_pagina)
    inicio = (pagina_actual - 1) * grupos_por_pagina
    fin = inicio + grupos_por_pagina
    grupos_paginados = Grupo.query.slice(inicio, fin).all()
    return render_template('grupos/index.html', grupos=grupos_paginados, segment='index', total_paginas=total_paginas, pagina_actual=pagina_actual)

@grupos.route('/agregar', methods=['GET', 'POST'])
def agregar():
    form_data = request.form if request.method == 'POST' else None
    if request.method == 'POST':
        grupo_nombre = request.form.get('grupo_nombre')
        grupo_costo = request.form.get('grupo_costo')
        grupo_sta = request.form.get('grupo_sta')

        # Verificar si el grupo ya existe en la base de datos
        grupo_existente = Grupo.query.filter_by(grupo_nombre=grupo_nombre).first()
        if grupo_existente:
            flash(f'El grupo "{grupo_nombre}" ya existe.', 'danger')
        else:
            nuevo_grupo = Grupo(grupo_nombre=grupo_nombre, grupo_costo=grupo_costo, grupo_sta=grupo_sta)
            db.session.add(nuevo_grupo)
            db.session.commit()
            grupo = Grupo.query.filter_by(grupo_nombre=grupo_nombre).first()
            analisis = request.form.getlist('analisis[]')
            for ana in analisis:
                nuevo_grupos_analisis_rel = GruposAnalisisRel(gana_grupo_id_fk=grupo.grupo_id,gana_ana_id_fk=ana)
                db.session.add(nuevo_grupos_analisis_rel)
                db.session.commit()
            flash('Grupo creado exitosamente.', 'success')
            return redirect(url_for('grupos.agregar'))
    lista_analisis = Analisis.query.all()
    return render_template('grupos/agregar_grupos.html', segment='agregar', lista_analisis=lista_analisis, form=form_data)

@grupos.route('/editar/<int:grupo_id>', methods=['GET', 'POST'])
def editar(grupo_id):
    grupo = Grupo.query.get_or_404(grupo_id)
    if request.method == 'POST':
        nuevo_nombre = request.form.get('grupo_nombre')
        
        # Verificar si el nuevo nombre ya existe en otro grupo
        if nuevo_nombre != grupo.grupo_nombre:
            grupo_existente = Grupo.query.filter_by(grupo_nombre=nuevo_nombre).first()
            if grupo_existente:
                flash(f'El grupo "{nuevo_nombre}" ya existe.', 'danger')
                return redirect(url_for('grupos.editar', grupo_id=grupo_id))

        grupo.grupo_nombre = nuevo_nombre
        grupo.grupo_costo = request.form.get('grupo_costo')
        grupo.grupo_sta = request.form.get('grupo_sta')
        db.session.commit()
        flash('Grupo editado con éxito.', 'success')
        return redirect(url_for('grupos.editar', grupo_id=grupo_id))
    lista_analisis_select = db.session.query(Analisis).join(GruposAnalisisRel, GruposAnalisisRel.gana_ana_id_fk == Analisis.ana_id).join(Grupo, Grupo.grupo_id == GruposAnalisisRel.gana_grupo_id_fk).filter(Grupo.grupo_id == grupo_id).all()
    lista_analisis = Analisis.query.all()

    return render_template('grupos/editar_grupos.html', grupo=grupo, lista_analisis_select=lista_analisis_select, lista_analisis=lista_analisis, segment='editar')

@grupos.route('/eliminar/<int:grupo_id>')
def eliminar(grupo_id):
    print('Grupo a eliminar:', grupo_id)
    grupo = Grupo.query.get_or_404(grupo_id)
    db.session.delete(grupo)
    db.session.commit()
    print('Grupo eliminado con éxito')
    return redirect(url_for('grupos.index'))
