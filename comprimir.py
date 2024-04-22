from cryptography.fernet import Fernet
from sqlalchemy_utils import EncryptedType
def generar_y_guardar_clave():
    """
    Genera una clave y la guarda en un archivo
    """
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)

def cargar_clave():
    """
    Carga la clave desde un archivo
    """
    return open("clave.key", "rb").read()


clave = cargar_clave()

fernet = Fernet(clave)

datos = "RAFAEL".encode()

datos_encriptados = fernet.encrypt(datos)
print("Datos encriptados:", datos_encriptados)

datos_desencriptados = fernet.decrypt(str.encode('3mwygAeleI9y+Z9+4luOQg=='))
print("Datos desencriptados:", datos_desencriptados.decode())
