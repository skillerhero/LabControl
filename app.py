from analisis import app, socketio
from flask import redirect, url_for,session
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    segment = 'index'
    if session.get('user_area_id_fk') == 6 or session.get('user_area_id_fk') == 7:
        return redirect(url_for("home.indexRecepcion")) 
    else:
        return redirect(url_for("home.index"))

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000)
    app.run()
