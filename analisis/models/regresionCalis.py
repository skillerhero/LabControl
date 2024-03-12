from sklearn.linear_model import LinearRegression
import numpy as np


materiales_a = np.load("materialesB.npy")

modelo = LinearRegression()

dia_semana = int(0)
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

print(int(modelo.predict([materiales_a[-3:,dia_semana]])[0]))

