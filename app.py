from analisis import app
from flask import redirect, url_for
from flask import session


@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    segment = 'index'  # Define el valor de segment

    
    if session.get('user_area_id_fk') == 6 or session.get('user_area_id_fk') == 7:
        return redirect(url_for("home.indexRecepcion")) 
    else:
        return redirect(url_for("home.index"))

if __name__ == '__main__':
    app.run()
