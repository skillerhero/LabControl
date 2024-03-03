from flask import render_template, request, redirect, url_for
from analisis import db
from flask import render_template,Blueprint
from analisis.models.resultado import Resultado
from datetime import datetime 
from analisis.models.muestra import Muestra
from analisis.models.analisis import Analisis
resultados=Blueprint('resultados',__name__,url_prefix='/resultados')

@resultados.route('/')
def index():
    resultados = Resultado.query.all()
    return render_template('resultados/index.html', resultados=resultados, segment='resultados')

@resultados.route('/agregar_resultados', methods=['GET', 'POST'])
def agregar_resultados():
    muestras=Muestra.query.all()
    lista_de_analisis=Analisis.query.all()
    if request.method == 'POST':
        resul_fecha = datetime.now()  
        resul_componente = request.form.get('resul_componente')
        resul_unidad = request.form.get('resul_unidad')
        resul_resultado = request.form.get('resul_resultado') 
        resul_rango = request.form.get('resul_rango')
        resul_fuera_de_rango = request.form.get('resul_fuera_de_rango', '').lower() == 'true'
        resul_ana_id = request.form.get('resul_ana_id')
        resul_mues_id = request.form.get('resul_mues_id')
        nuevo_resultado = Resultado(resul_fecha=resul_fecha, resul_componente=resul_componente, 
                            resul_unidad=resul_unidad, resul_resultado=resul_resultado,
                            resul_rango=resul_rango, resul_fuera_de_rango=resul_fuera_de_rango,
                            resul_ana_id=resul_ana_id, resul_mues_id=resul_mues_id)

        
        db.session.add(nuevo_resultado)
        db.session.commit()
        print('Resultado agregado con éxito')
        return redirect(url_for('resultados.index'))
    return render_template('resultados/agregar_resultados.html',muestras=muestras,lista_de_analisis=lista_de_analisis, segment='agregarresultados')

@resultados.route('/editar_resultados/<int:resul_id>', methods=['GET', 'POST'])
def editar_resultados(resul_id):
    resultado = Resultado.query.get_or_404(resul_id)
    muestras=Muestra.query.all()
    lista_de_analisis=Analisis.query.all()
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
    print("Muestras editar resultados: ", muestras)
    return render_template('resultados/editar_resultados.html', resultado=resultado,muestras=muestras,lista_de_analisis=lista_de_analisis, segment='editarresult')

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
    muestras=Muestra.query.all()
    lista_de_analisis=Analisis.query.all()
    return render_template('resultados/detalle_resultados.html', resultado=resultado, segment='detalle_resultados',muestras=muestras,lista_de_analisis=lista_de_analisis)

@resultados.route('/detalle_muestra/<int:mues_id>', methods=['GET', 'POST'])
def detalle_muestra(mues_id):
    recepcion = Muestra.query.get_or_404(mues_id)
    if request.method == 'POST':
        recepcion.muestra_folio = request.form['mues_folio']
        print(recepcion.muestra_folio)
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
        return redirect(url_for('analistas.home'))
    return render_template('analistas/detalle_muestra.html', recepcion=recepcion, segment='detalle_muestra')