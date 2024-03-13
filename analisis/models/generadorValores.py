import numpy as np

# Define los posibles números de tubos de ensayo que se pueden pedir en un día
tubos_por_dia = np.array([0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# Define las probabilidades asociadas a cada número de tubos de ensayo
# Estas probabilidades se pueden ajustar para reflejar la demanda del laboratorio
probabilidades = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025])
# Asegúrate de que las probabilidades sumen 1
probabilidades = probabilidades / probabilidades.sum()
# Genera los valores aleatorios para una semana (5 días)
valores = np.random.choice(tubos_por_dia, size=(100,5), p=probabilidades)
np.save("historico_tubos_recoleccion",valores)


probabilidades=[]
valores = []
caja_guantes_por_dia = np.array([0, 1, 2])
probabilidades = np.array([0.6, 0.3, 0.1])
probabilidades = probabilidades / probabilidades.sum()
valores = np.random.choice(caja_guantes_por_dia, size=(100,5), p=probabilidades)
np.save("historico_caja_guantes",valores)

probabilidades=[]
valores = []
jeringas_por_dia = np.array([0,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50])
media = 15 
desviacion_estandar = 5 
probabilidades = np.array([np.exp(-(x - media)**2 / (2 * desviacion_estandar**2)) for x in jeringas_por_dia])
probabilidades = probabilidades / probabilidades.sum()
valores = np.random.choice(jeringas_por_dia, size=(100,5), p=probabilidades)
np.save("historico_jeringas",valores)
