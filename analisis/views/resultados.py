from flask import render_template, request, redirect, url_for, Blueprint, session, g
from analisis import db
from datetime import datetime 
from analisis.models.muestra import Muestra
from analisis.models.analisis import Analisis
from analisis.models.resultado import Resultado

resultados = Blueprint('resultados', __name__, url_prefix='/resultados')

@resultados.route('/')
def index():
    resultados = Resultado.query.all()
    return render_template('resultados/index.html', resultados=resultados, segment='resultados')

@resultados.route('/agregar_resultados/<int:mues_id>', methods=['GET', 'POST'])
def agregar_resultados(mues_id):
    # Obtener el objeto Muestra asociado al mues_id
    muestra = Muestra.query.get_or_404(mues_id)
    
    # Obtener el área del usuario actual
    user_area_id = g.user.user_area_id_fk
    
    # Obtener los análisis asociados a la muestra y al área del usuario
    analisis_asociados = []
    if user_area_id is not None:
        analisis_asociados = Analisis.query.join(Resultado, Resultado.resul_ana_id_fk == Analisis.ana_id) \
                                            .filter(Resultado.resul_mues_id_fk == mues_id) \
                                            .filter(Analisis.ana_area_id_fk == user_area_id) \
                                            .filter(Resultado.resul_sta == "O")\
                                            .all()
    else:
        analisis_asociados = []

    # Almacenar los análisis asociados en la sesión
    session['analisis_asociados'] = [analisis.ana_id for analisis in analisis_asociados]
    
    if request.method == 'POST':
        selected_analisis_id = request.form['resul_ana_id']
        print("ID del análisis seleccionado:", selected_analisis_id)
        resultado = Resultado.query.filter_by(resul_ana_id_fk=selected_analisis_id, resul_mues_id_fk=mues_id, resul_sta='O').first()

        if resultado:
            resultado.resul_fecha = datetime.now()  
            resultado.resul_componente = request.form['resul_componente']
            resultado.resul_unidad = request.form['resul_unidad']
            resultado.resul_resultado = request.form['resul_resultado']
            resultado.resul_rango = request.form['resul_rango']
            resultado.resul_fuera_de_rango = request.form.get('resul_fuera_de_rango', '').lower() == 'true'
            resultado.resul_sta = "F"
            db.session.commit()
            print("Resultado modificado con éxito.")
        else:
            print("No se encontró ningún resultado que cumpla con las condiciones.")
    
    return render_template('resultados/agregar_resultados.html', muestra=muestra, lista_de_analisis=analisis_asociados, segment='agregarresultados')


@resultados.route('/editar_resultados/<int:resul_id>', methods=['GET', 'POST'])
def editar_resultados(resul_id):
    resultado = Resultado.query.get_or_404(resul_id)
    muestras = Muestra.query.all()
    lista_de_analisis = Analisis.query.all()
    if request.method == 'POST':
        resultado.resul_fecha = datetime.now()  
        resultado.resul_componente = request.form['resul_componente']
        resultado.resul_unidad = request.form['resul_unidad']
        resultado.resul_resultado = request.form['resul_resultado']
        resultado.resul_rango = request.form['resul_rango']
        resultado.resul_fuera_de_rango = request.form.get('resul_fuera_de_rango', '').lower() == 'true'
        resultado.resul_ana_id = request.form.get('resul_ana_id')
        resultado.resul_mues_id = request.form.get('resul_mues_id')
        db.session.commit()
        return redirect(url_for('resultados.index'))
    
    return render_template('resultados/editar_resultados.html', resultado=resultado, muestras=muestras, lista_de_analisis=lista_de_analisis, segment='editarresult')

@resultados.route('/eliminar_resultados/<int:resul_id>')
def eliminar_resultados(resul_id):
    print('resultados a eliminar: ',resul_id)
    resultado = Resultado.query.get_or_404(resul_id)
    db.session.delete(resultado)
    db.session.commit()
    print('resultado eliminado con éxito')
    return redirect(url_for('resultados.index'))


@resultados.route('/detalle_resultados/<int:resul_id>', methods=['GET', 'POST'])
def detalle_resultados(resul_id):
    resultado = Resultado.query.get_or_404(resul_id)
    if request.method == 'POST':
        resultado.resul_fecha = datetime.now()  
        resultado.resul_componente = request.form['resul_componente']
        resultado.resul_unidad = request.form['resul_unidad']
        resultado.resul_resultado = request.form['resul_resultado']
        resultado.resul_rango = request.form['resul_rango']
        resultado.resul_fuera_de_rango = request.form.get('resul_fuera_de_rango', '').lower() == 'true'
        resultado.resul_ana_id = request.form.get('resul_ana_id')
        resultado.resul_mues_id = request.form.get('resul_mues_id')
        return redirect(url_for('resultados.index'))
    muestras = Muestra.query.all()
    lista_de_analisis = Analisis.query.all()
    return render_template('resultados/detalle_resultados.html', resultado=resultado, segment='detalle_resultados', muestras=muestras, lista_de_analisis=lista_de_analisis)
