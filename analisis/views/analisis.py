# Importaciones necesarias
from flask import Flask, render_template, request, redirect, url_for
from analisis import db
from flask import render_template, Blueprint
from analisis.models.analisis import Analisis

analisis = Blueprint('analisis', __name__, url_prefix='/analisis')

@analisis.route('/')
def index():
    analisis_por_pagina = 20
    pagina_actual = request.args.get('pagina', 1, type=int)
    analisis_paginados = Analisis.query.paginate(page=pagina_actual, per_page=analisis_por_pagina)
    return render_template('analisis/index.html', analisis=analisis_paginados)

@analisis.route('/agregar_analisis', methods=['GET', 'POST'])
def agregar_analisis():
    if request.method == 'POST':
        ana_nombre = request.form.get('ana_nombre')
        ana_costo = request.form.get('ana_costo')
        ana_sta = request.form.get('ana_sta')
        ana_area_id_fk = request.form.get('ana_area_id_fk')

        nuevo_analisis = Analisis(ana_nombre=ana_nombre, ana_costo=ana_costo, ana_sta=ana_sta, ana_area_id_fk=ana_area_id_fk)  # Pasar ana_area_id_fk
        db.session.add(nuevo_analisis)
        db.session.commit()
        print('Analisis agregado con éxito')
        return redirect(url_for('analisis.index'))
    return render_template('analisis/agregar_analisis.html', segment='agregar_analisis')

@analisis.route('/editar_analisis/<int:ana_id>', methods=['GET', 'POST'])
def editar_analisis(ana_id):
    analisis = Analisis.query.get_or_404(ana_id)
    if request.method == 'POST':
        analisis.ana_nombre = request.form['ana_nombre']
        analisis.ana_costo = request.form['ana_costo']
        analisis.ana_sta = request.form['ana_sta']
        db.session.commit()
        return redirect(url_for('analisis.index'))
    return render_template('analisis/editar_analisis.html', analisis=analisis, segment='editar_analisis')

@analisis.route('/detalle_analisis/<int:ana_id>', methods=['GET', 'POST'])
def detalle_analisis(ana_id):
    analisis = Analisis.query.get_or_404(ana_id)
    if request.method == 'POST':
        return redirect(url_for('analisis.index'))
    return render_template('analisis/detalle_analisis.html', analisis=analisis, segment='detalle_analisis')

@analisis.route('/eliminar_analisis/<int:ana_id>')
def eliminar_analisis(ana_id):
    print('Analisis a eliminar: ', ana_id)
    analisis = Analisis.query.get_or_404(ana_id)
    db.session.delete(analisis)
    db.session.commit()
    print('Analisis eliminado con éxito')
    return redirect(url_for('analisis.index'))
