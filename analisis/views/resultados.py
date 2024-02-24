# Importaciones necesarias
from flask import render_template, request, redirect, url_for
from analisis import db
from flask import render_template,Blueprint
from analisis.models.resultado import Resultado
from datetime import datetime 
resultados=Blueprint('resultados',__name__,url_prefix='/resultados')

@resultados.route('/')
def index():
    resultados = Resultado.query.all()
    return render_template('resultados/index.html', resultados=resultados)

@resultados.route('/agregar_resultados', methods=['GET', 'POST'])
def agregar_resultados():
    if request.method == 'POST':
        resul_fecha = datetime.now()  
        resul_componente = request.form.get('resul_componente')
        resul_unidad = request.form.get('resul_unidad')
        resul_resultado = request.form.get('resul_resultado') 
        resul_rango = request.form.get('resul_rango')
        resul_fuera_de_rango = request.form.get('resul_fuera_de_rango', '').lower() == 'true'

        nuevo_resultado = Resultado(resul_fecha=resul_fecha, resul_componente=resul_componente, 
                                     resul_unidad=resul_unidad, resul_resultado=resul_resultado,
                                     resul_rango=resul_rango, resul_fuera_de_rango=resul_fuera_de_rango)
        
        db.session.add(nuevo_resultado)
        db.session.commit()
        print('Resultado agregado con éxito')
        return redirect(url_for('resultados.index'))
    
    return render_template('resultados/agregar_resultados.html')

@resultados.route('/editar_resultados/<int:resul_id>', methods=['GET', 'POST'])
def editar_resultados(resul_id):
    resultado = Resultado.query.get_or_404(resul_id)
    if request.method == 'POST':
        resultado.resul_fecha = datetime.now()  
        resultado.resul_componente = request.form['resul_componente']
        resultado.resul_unidad = request.form['resul_unidad']
        resultado.resul_resultado = request.form['resul_resultado']
        resultado.resul_rango = request.form['resul_rango']
        resul_fuera_de_rango = request.form.get('resul_fuera_de_rango', '').lower() == 'true'
        
        db.session.commit()
        return redirect(url_for('resultados.index'))
    return render_template('resultados/editar_resultados.html', resultado=resultado)

@resultados.route('/eliminar_resultados/<int:resul_id>')
def eliminar_resultados(resul_id):
    print('resultados a eliminar: ',resul_id)
    resultado = Resultado.query.get_or_404(resul_id)
    db.session.delete(resultado)
    db.session.commit()
    print('resultado eliminado con éxito')
    return redirect(url_for('resultados.index'))