from flask import Blueprint, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression

regresion = Blueprint('regresion', __name__, url_prefix='/regresion')

materiales_a = np.load("materialesA.npy")
materiales_b = np.load("materialesB.npy")
materiales_c = np.load("materialesC.npy")

modelo = LinearRegression()

@regresion.route('/')
def index():
    return render_template('regresion/index.html')

@regresion.route('/predict', methods=['POST'])
def predict():
    dia_semana = int(request.form['dia_semana'])

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
