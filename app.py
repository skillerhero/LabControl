from analisis import app
from flask import redirect, url_for
from flask import session
# Importa el blueprint 'auth' que has definido en auth.py
from analisis.views.auth import auth

# Ruta principal que redirige a la pantalla de login si el usuario no está autenticado
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    # Si el usuario está autenticado, puedes renderizar la página principal aquí
    # ...

if __name__ == '__main__':
    app.run()