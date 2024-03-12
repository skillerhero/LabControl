from flask import render_template, request, redirect, url_for, Blueprint, session, g
from analisis import db
from datetime import datetime 
from analisis.models.muestra import Muestra
from analisis.models.analisis import Analisis
from analisis.models.resultado import Resultado
from analisis.models.mediciones_analisis import MedicionesAnalisis
from analisis import socketio
import json
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
    lista_de_analisis = []
    if user_area_id is not None:
        lista_de_analisis = Analisis.query.join(Resultado, Resultado.resul_ana_id_fk == Analisis.ana_id) \
            .filter(Resultado.resul_mues_id_fk == mues_id) \
            .filter(Analisis.ana_area_id_fk == user_area_id) \
            .filter(Resultado.resul_sta == "O")\
            .all()
    else:
        lista_de_analisis = []

    # Almacenar los análisis asociados en la sesión
    session['analisis_asociados'] = [analisis.ana_id for analisis in lista_de_analisis]
    
    if request.method == 'POST':
        selected_analisis_id = request.form['resul_ana_id']
        mediciones = MedicionesAnalisis.query.filter_by(mediciones_analisis_ana_id_fk=selected_analisis_id).all()
        for medicion in mediciones:
            resultado = Resultado.query.filter_by(resul_ana_id_fk=selected_analisis_id, resul_mues_id_fk=mues_id, resul_sta='O').first()
            if resultado:
                resultado.resul_fecha = datetime.now()  
                resultado.resul_resultado = request.form[f'resul_resultado_{medicion.mediciones_analisis_id}']
                resultado.resul_fuera_de_rango = request.form.get(f'resul_fuera_de_rango_{medicion.mediciones_analisis_id}', '').lower() == 'true'
                resultado.resul_sta = "F"
                db.session.commit()
                socketio.emit('notification_update')
                print("Resultado modificado con éxito.")

        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        # Obtener todos los resultados asociados a la muestra
        resultados_muestra = Resultado.query.filter_by(resul_mues_id_fk=mues_id).all()
        
        # Verificar si todos los resultados de la muestra tienen resul_sta == "F"
        todos_f = all(resultado.resul_sta == "F" for resultado in resultados_muestra)
        print('todos_f :')
        print(todos_f)
        if todos_f:
            # Si todos los resultados tienen resul_sta == "F", actualiza el estado de la muestra
            muestra = Muestra.query.get(mues_id)
            if muestra:
                muestra.mues_sta = "F"
                db.session.commit()
                socketio.emit('notification_update')
                resultados = Resultado.query.all()
                return redirect(url_for('resultados.index', resultados=resultados))
        else:
            print("No se encontró ningún resultado que cumpla con las condiciones.")
        return redirect(url_for('resultados.agregar_resultados', mues_id=mues_id))
    mediciones_por_analisis = {}
    for analisis in lista_de_analisis:
        mediciones_por_analisis[analisis.ana_id] = MedicionesAnalisis.query.filter_by(mediciones_analisis_ana_id_fk=analisis.ana_id).all()

    return render_template('resultados/agregar_resultados.html', mediciones_por_analisis=json.dumps({k: [i.serialize for i in v] for k, v in mediciones_por_analisis.items()}), muestra=muestra, lista_de_analisis=lista_de_analisis,segment='agregarresultados')


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
        socketio.emit('notification_update')
        return redirect(url_for('resultados.index'))
    
    return render_template('resultados/editar_resultados.html', resultado=resultado, muestras=muestras, lista_de_analisis=lista_de_analisis, segment='editarresult')

@resultados.route('/eliminar_resultados/<int:resul_id>')
def eliminar_resultados(resul_id):
    print('resultados a eliminar: ',resul_id)
    resultado = Resultado.query.get_or_404(resul_id)
    db.session.delete(resultado)
    db.session.commit()
    socketio.emit('notification_update')
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
