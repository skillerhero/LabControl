from flask import Blueprint, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression

regresion = Blueprint('regresion', __name__, url_prefix='/regresion')

materiales_a = np.array([[100, 150, 200, 250, 300],
                         [110, 160, 210, 260, 310],
                         [120, 170, 220, 270, 320]])

materiales_b = np.array([[80, 120, 160, 200, 240],
                         [85, 125, 165, 205, 245],
                         [90, 130, 170, 210, 250]])

materiales_c = np.array([[50, 75, 100, 125, 150],
                         [55, 80, 105, 130, 155],
                         [60, 85, 110, 135, 160]])

modelo = LinearRegression()

@regresion.route('/')
def index():
    return render_template('regresion/index.html')

@regresion.route('/predict', methods=['POST'])
def predict():
    dia_semana = int(request.form['dia_semana'])

    X = np.array([[1], [2], [3]])

    modelo.fit(X, materiales_a[:, dia_semana-1].reshape(-1, 1))
    prediccion_a = int(modelo.predict([[dia_semana]])[0])

    modelo.fit(X, materiales_b[:, dia_semana-1].reshape(-1, 1))
    prediccion_b = int(modelo.predict([[dia_semana]])[0])

    modelo.fit(X, materiales_c[:, dia_semana-1].reshape(-1, 1))
    prediccion_c = int(modelo.predict([[dia_semana]])[0])

    return render_template('regresion/result.html', prediccion_a=prediccion_a, prediccion_b=prediccion_b, prediccion_c=prediccion_c)
