from flask import Blueprint, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression

regresion = Blueprint('regresion', __name__, url_prefix='/regresion')
modelo = LinearRegression()

@regresion.route('/')
def index():
    return render_template('regresion/index.html')

@regresion.route('/predict', methods=['POST'])
def predict():
    materiales_a = np.load("materialesA.npy")
    materiales_b = np.load("materialesB.npy")
    materiales_c = np.load("materialesC.npy")

    dia_semana = int(request.form['dia_semana']) -1 

    listInputs=[]
    listOutputs=[]
    x = materiales_a[:,dia_semana]
    valoresAnteriores=3
    for i in range(valoresAnteriores,len(x)):
        entrada=np.reshape(x[i-valoresAnteriores:i],-1)
        listInputs.append(entrada)
        listOutputs.append(x[i])
    listInputs=np.asanyarray(listInputs)
    listOutputs=np.asanyarray(listOutputs).ravel()
    modelo.fit(listInputs,listOutputs)

    prediccion_a = int(modelo.predict([materiales_a[-3:,dia_semana]])[0])


    listInputs=[]
    listOutputs=[]
    x = materiales_b[:,dia_semana]
    valoresAnteriores=3
    for i in range(valoresAnteriores,len(x)):
        entrada=np.reshape(x[i-valoresAnteriores:i],-1)
        listInputs.append(entrada)
        listOutputs.append(x[i])
    listInputs=np.asanyarray(listInputs)
    listOutputs=np.asanyarray(listOutputs).ravel()
    modelo.fit(listInputs,listOutputs)

    prediccion_b = int(modelo.predict([materiales_b[-3:,dia_semana]])[0])

    listInputs=[]
    listOutputs=[]
    x = materiales_c[:,dia_semana]
    valoresAnteriores=3
    for i in range(valoresAnteriores,len(x)):
        entrada=np.reshape(x[i-valoresAnteriores:i],-1)
        listInputs.append(entrada)
        listOutputs.append(x[i])
    listInputs=np.asanyarray(listInputs)
    listOutputs=np.asanyarray(listOutputs).ravel()
    modelo.fit(listInputs,listOutputs)
    prediccion_c = int(modelo.predict([materiales_c[-3:,dia_semana]])[0])
    return render_template('regresion/result.html', prediccion_a=prediccion_a, prediccion_b=prediccion_b, prediccion_c=prediccion_c)

@regresion.route('/historico', methods=['GET', 'POST'])
def historico():
    # Cargar los datos
    materiales_a = np.load("materialesA.npy")
    materiales_b = np.load("materialesB.npy")
    materiales_c = np.load("materialesC.npy")

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
