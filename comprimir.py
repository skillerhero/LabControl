from cryptography.fernet import Fernet

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

# Genera y guarda la clave
generar_y_guardar_clave()

# Carga la clave
clave = cargar_clave()

# Instancia un objeto Fernet usando la clave
fernet = Fernet(clave)

# Supón que 'datos' es la información sensible que quieres encriptar
datos = "información sensible".encode()

# Encripta los datos
datos_encriptados = fernet.encrypt(datos)
print("Datos encriptados:", datos_encriptados)

# Desencripta los datos
datos_desencriptados = fernet.decrypt(datos_encriptados)
print("Datos desencriptados:", datos_desencriptados.decode())

