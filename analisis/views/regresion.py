from flask import Blueprint, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression

regresion = Blueprint('regresion', __name__, url_prefix='/regresion')
modelo = LinearRegression()

@regresion.route('/')
def index():
    return render_template('regresion/index.html')

@regresion.route('/predict', methods=['POST','GET'])
def predict():
    materiales_a = np.load("historico_caja_guantes.npy")
    materiales_b = np.load("historico_jeringas.npy")
    materiales_c = np.load("historico_tubos_recoleccion.npy")

    total_caja_guantes = int(0)
    total_jeringa = int(0)
    total_tubos_recoleccion = int(0)

    caja_guantes = []
    jeringas = []
    tubos_recoleccion = []
    for dia in range(5):
        listInputs=[]
        listOutputs=[]
        x = materiales_a[:,dia]
        valoresAnteriores=3
        for i in range(valoresAnteriores,len(x)):
            entrada=np.reshape(x[i-valoresAnteriores:i],-1)
            listInputs.append(entrada)
            listOutputs.append(x[i])
        listInputs=np.asanyarray(listInputs)
        listOutputs=np.asanyarray(listOutputs).ravel()
        modelo.fit(listInputs,listOutputs)
        prediccion_a = int(modelo.predict([materiales_a[-3:,dia]])[0])
        total_caja_guantes += prediccion_a
        caja_guantes.append(prediccion_a)

        listInputs=[]
        listOutputs=[]
        x = materiales_b[:,dia]
        valoresAnteriores=3
        for i in range(valoresAnteriores,len(x)):
            entrada=np.reshape(x[i-valoresAnteriores:i],-1)
            listInputs.append(entrada)
            listOutputs.append(x[i])
        listInputs=np.asanyarray(listInputs)
        listOutputs=np.asanyarray(listOutputs).ravel()
        modelo.fit(listInputs,listOutputs)
        prediccion_b = int(modelo.predict([materiales_b[-3:,dia]])[0])
        total_jeringa += prediccion_b
        jeringas.append(prediccion_b)

        listInputs=[]
        listOutputs=[]
        x = materiales_c[:,dia]
        valoresAnteriores=3
        for i in range(valoresAnteriores,len(x)):
            entrada=np.reshape(x[i-valoresAnteriores:i],-1)
            listInputs.append(entrada)
            listOutputs.append(x[i])
        listInputs=np.asanyarray(listInputs)
        listOutputs=np.asanyarray(listOutputs).ravel()
        modelo.fit(listInputs,listOutputs)
        prediccion_c = int(modelo.predict([materiales_c[-3:,dia]])[0])
        total_tubos_recoleccion += prediccion_c
        tubos_recoleccion.append(prediccion_c)
    caja_guantes.append(total_caja_guantes)
    jeringas.append(total_jeringa)
    tubos_recoleccion.append(total_tubos_recoleccion)

    print(caja_guantes, jeringas, tubos_recoleccion)

    return render_template('regresion/result.html', caja_guantes=caja_guantes, jeringas=jeringas, tubos_recoleccion=tubos_recoleccion)

@regresion.route('/historico', methods=['GET', 'POST'])
def historico():
    # Cargar los datos
    materiales_a = np.load("historico_caja_guantes.npy")
    materiales_b = np.load("historico_jeringas.npy")
    materiales_c = np.load("historico_tubos_recoleccion.npy")
    
    # Dividir los datos en grupos de 20 filas
    materiales_a_paginados = [materiales_a[i:i+20] for i in range(0, len(materiales_a), 20)]
    materiales_b_paginados = [materiales_b[i:i+20] for i in range(0, len(materiales_b), 20)]
    materiales_c_paginados = [materiales_c[i:i+20] for i in range(0, len(materiales_c), 20)]

    # Organizar los datos paginados en un diccionario
    materiales = {'A': materiales_a_paginados, 'B': materiales_b_paginados, 'C': materiales_c_paginados}

    # Obtener el número total de páginas para la paginación
    total_pages = max([len(materiales[material]) for material in materiales])

    # Obtener el número de página actual
    current_page = request.args.get('pagina', 1, type=int)

    # Pasar los datos a la plantilla
    return render_template('regresion/historico.html', materiales=materiales, total_pages=total_pages, current_page=current_page)

@regresion.route('/editar', methods=['GET', 'POST'])
def editar():
    data = np.load('historico_tubos_recoleccion.npy')
    if request.method == 'POST':
        # Aquí puedes agregar la lógica para manipular los datos
        # Por ejemplo, para agregar una fila:
        if 'add' in request.form:
            new_row = np.array([request.form.get('valor1'), request.form.get('valor2'), request.form.get('valor3'), request.form.get('valor4'), request.form.get('valor5')])
            data = np.vstack([data, new_row])
        # Para eliminar una fila:
        elif 'delete' in request.form:
            row_to_delete = int(request.form.get('fila'))
            data = np.delete(data, row_to_delete, axis=0)
        np.save('historico_tubos_recoleccion.npy', data)
    return render_template('regresion/editar.html', data=data.tolist())