# Importaciones necesarias
from flask import Flask, render_template, request, redirect, url_for
from analisis import db
from flask import render_template,Blueprint
from analisis.models.grupos import Grupo
grupos = Blueprint('grupos', __name__, url_prefix='/grupos')

@grupos.route('/')
def index():
    grupos = Grupo.query.all()
    return render_template('grupos/index.html', grupos=grupos, segment='index')

@grupos.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        grupo_nombre = request.form.get('grupo_nombre')
        grupo_costo = request.form.get('grupo_costo')
        nuevo_grupo = Grupo(grupo_nombre=grupo_nombre, grupo_costo=grupo_costo)
        db.session.add(nuevo_grupo)
        db.session.commit()
        print('Grupo agregado con éxito')
        return redirect(url_for('grupos.index'))
    return render_template('grupos/agregar.html', segment='agregar')

@grupos.route('/editar/<int:grupo_id>', methods=['GET', 'POST'])
def editar(grupo_id):
    grupo = Grupo.query.get_or_404(grupo_id)
    if request.method == 'POST':
        grupo.grupo_nombre = request.form.get('grupo_nombre')
        grupo.grupo_costo = request.form.get('grupo_costo')
        db.session.commit()
        print('Grupo editado con éxito')
        return redirect(url_for('grupos.index'))
    return render_template('grupos/editar.html', grupo=grupo, segment='editar')

@grupos.route('/eliminar/<int:grupo_id>')
def eliminar(grupo_id):
    print('Grupo a eliminar:', grupo_id)
    grupo = Grupo.query.get_or_404(grupo_id)
    db.session.delete(grupo)
    db.session.commit()
    print('Grupo eliminado con éxito')
    return redirect(url_for('grupos.index'))
